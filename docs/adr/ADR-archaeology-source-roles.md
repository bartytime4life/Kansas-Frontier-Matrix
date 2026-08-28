<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr-candidate/archaeology-source-roles
title: "ADR Candidate — Archaeology Source Roles Bind to the Shared SourceDescriptor Vocabulary"
type: adr
version: v0.2
status: proposed
effective_decision_status: not-assigned
owners:
  - "NEEDS VERIFICATION — architecture decision owner"
  - "NEEDS VERIFICATION — archaeology domain steward"
  - "NEEDS VERIFICATION — source steward"
  - "NEEDS VERIFICATION — evidence and provenance steward"
  - "NEEDS VERIFICATION — rights, cultural, sovereignty, and sensitivity reviewers"
  - "NEEDS VERIFICATION — contract, schema, policy, validation, API/UI, release, correction, and rollback stewards"
owner_status: "CODEOWNERS routing and accepted decision ownership were not verified as equivalent to domain, cultural, sovereignty, rights, policy, release, or independent-review authority"
created: 2026-05-20
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
owning_root: docs/
responsibility: "Record the proposed Archaeology binding to KFM's shared source-role vocabulary, the domain-specific anti-collapse crosswalk, and the gates required before that binding may be treated as accepted or operational."
current_path: docs/adr/ADR-archaeology-source-roles.md
source_scaffold_origin: "docs/domains/archaeology/SOURCE_REGISTRY.md"
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 9d924c665073263f2cbf376d2bf29e7b9f252b06
  target_prior_blob: 2036c72e3780eb360c9ec3423497153fceb2b3db
  target_origin_commit: fa728424d5fee66571bf6a23881faf64e108353a
  adr_index_blob: 938c5894c36b99e14810918e2c550ab0e92d53b1
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  archaeology_source_registry_blob: 7f905f43196eda6a063e65964f8054af0c12be10
  archaeology_sources_blob: bffee469f7d503ea829f49e6465ac4b2ae1e48fc
  shared_source_roles_doc_blob: c528d517503aca2952164b45701246c5abae751c
  source_descriptor_contract_blob: b57ae5ccc042c1423b75c168438800384c9b6713
  source_descriptor_schema_blob: 582e70b834278c3c6ca9a8b31efbe0989c96f0bc
  source_role_use_contract_blob: 6bc07a551511cc8fca8024625cf962e15f77eed0
  source_role_use_schema_blob: e9c5b9f90dd3a77a6f1164b56571fa9d697ef193
  source_role_validator_core_blob: 84c67aa4be17fa2cd5848b556162dfe53698f2e7
  source_role_validator_rules_blob: aa94f33d5e91b10f8b17a2ea88e4c337c45a23bc
  source_role_validator_implementation_blob: 1c1ac6bee24dc819695b53d67a00f08c35cc99ee
  source_role_validator_test_blob: 580c698e53b5144a0f6061d3f5fbc30942485156
  transition_contract_blob: 8da34b5bcf95f0b7319f2fa6a30104a63bc7dac3
  transition_schema_blob: 48c8dfded26ba54840c47c4c6b08a434ffea83ff
  archaeology_role_registry_blob: 21c6b6f818d554b2e46748c1a05fa3bb80673e57
  archaeology_fixture_readme_blob: 34ac7b1f8592fd4bdc3ac6685f8819d215163afa
  archaeology_fixture_placeholder_blob: 0426d335679bda5ebe34a6e18230f5a8f1f9b8d1
  archaeology_validator_blob: 0c6d634ea7298c8a75b68b33265b4aea90371b58
  archaeology_test_blob: e56380f712b1151e61daa15705535ca56986a55d
inspection_boundary: >
  Current-session GitHub reads of the exact target, canonical ADR inventory,
  accepted Directory Rules adoption record and adopted bytes, archaeology source
  documents, shared SourceDescriptor contract/schema, source-role use contract,
  executable no-network source-role validator and tests, transition-assessment
  contract/schema, archaeology registry placeholder, synthetic fixture lane,
  domain validator/test placeholders, target history, open pull requests, and
  active branches. No real archaeology source, restricted repository, cultural
  authority system, rights agreement, source endpoint, connector, lifecycle
  payload, EvidenceBundle resolver, policy evaluator, release environment,
  public client, or deployed runtime was exercised.
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - docs/adr/ADR-0017-source-descriptor-admission-process.md
  - docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - docs/adr/ADR-0024-steward-separation-of-duties-for-release.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/adr/ADR-archaeology-exact-location-policy.md
  - docs/doctrine/directory-rules.md
  - docs/sources/source-roles.md
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - docs/domains/archaeology/SOURCE_REGISTRY.md
  - docs/domains/archaeology/SOURCES.md
  - docs/domains/archaeology/SENSITIVITY.md
  - docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - contracts/source/source_descriptor.md
  - contracts/source/source_role_use_request.md
  - contracts/source/source_role_transition_assessment.md
  - schemas/contracts/v1/source/source_descriptor.schema.json
  - schemas/contracts/v1/source/source_role_use_request.schema.json
  - schemas/contracts/v1/source/source_role_transition_assessment.schema.json
  - data/registry/sources/archaeology/source_roles.yaml
  - fixtures/domains/archaeology/synthetic_source_descriptor/README.md
  - tools/validators/source_role/IMPLEMENTATION.md
  - tools/validators/source_role/source_role_core.py
  - tools/validators/source_role/source_role_rules.py
  - tools/validators/source_role/validate_source_role.py
  - tools/validators/domains/archaeology/validate_source_descriptor.py
  - tests/validators/test_validate_source_role.py
  - tests/source/test_source_role_transition_assessment.py
  - tests/domains/archaeology/test_source_descriptor.py
tags: [kfm, adr, archaeology, source-role, source-descriptor, anti-collapse, evidence, rights, sensitivity, sovereignty, candidate, modeled, aggregate, synthetic, validation]
notes:
  - "This remains an unassigned PROPOSED scaffold and ADR candidate. It does not reserve a number, accept a decision, or change the canonical ADR index."
  - "The proposed decision binds Archaeology to a shared source-role vocabulary rather than creating a parallel domain enum."
  - "The current shared SourceDescriptor schema and source-role validator are implementation evidence with PROPOSED authority, not accepted vocabulary authority."
  - "The seven Archaeology role terms and the uppercase transition-assessment terms are retained as lineage and compatibility inputs pending a reviewed crosswalk."
  - "Exact-location exposure, sovereignty, consent, rights, sensitivity, release, and publication remain separate decisions."
  - "This one-file update creates no source authority, source activation, evidence, policy, review approval, release, deployment, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR Candidate — Archaeology Source Roles Bind to the Shared SourceDescriptor Vocabulary

> **Proposed decision.** Archaeology should use the shared KFM
> `SourceDescriptor.source_role` vocabulary and shared anti-collapse machinery,
> with an explicit archaeology profile that maps domain concepts such as
> observed, regulatory, modeled, aggregate, administrative, candidate, and
> synthetic into the shared machine vocabulary. Archaeology must not create a
> second source-role authority, infer a role from prose or publisher reputation,
> or allow lifecycle promotion, map rendering, AI generation, or public release
> to upgrade source authority.

[![decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![identity: unassigned](https://img.shields.io/badge/ADR-unassigned-6e7781?style=flat-square)](#status)
[![shared validator: fixture first](https://img.shields.io/badge/shared%20validator-fixture--first-0969da?style=flat-square)](#current-implementation-maturity)
[![archaeology profile: hold](https://img.shields.io/badge/archaeology%20profile-HOLD-b42318?style=flat-square)](#conflict-and-hold-register)
[![exact location: separate](https://img.shields.io/badge/exact%20location-separate%20decision-8250df?style=flat-square)](#authority-and-sensitivity-boundary)
[![publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-publication-boundary)

> [!CAUTION]
> **This is an unassigned PROPOSED scaffold and ADR candidate.**
> [`docs/adr/INDEX.md`](./INDEX.md) classifies this file as a slug-only,
> `not-assigned` scaffold. This revision does not claim an ADR number, reserve a
> number, accept the proposed decision, or prove that the Archaeology lane
> enforces it.

> [!IMPORTANT]
> **Current implementation is not accepted vocabulary authority.** The shared
> `SourceDescriptor` schema currently exposes a 16-token lowercase
> `source_role` enum, and the executable shared validator reads that enum
> directly. Archaeology documents describe a seven-term domain grammar, while a
> separate transition-assessment schema uses seven uppercase terms. Those are
> material, inspectable facts; selecting how they relate is the decision under
> consideration, not a fact already settled by file presence.

> [!WARNING]
> **Source role is not public-release permission.** A source can be authoritative
> for a narrow administrative, regulatory, observational, or stewardship claim
> and still be denied from public use because of rights, consent, sovereignty,
> cultural sensitivity, exact-location risk, review state, or release state.
> This candidate does not weaken the Archaeology exact-location or cultural
> review boundary.

**Quick navigation:** [Status](#status) · [Evidence boundary](#evidence-boundary) · [Context](#context) · [Decision](#proposed-decision) · [Shared vocabulary](#current-shared-machine-vocabulary) · [Crosswalk](#archaeology-domain-crosswalk) · [Source families](#source-family-application) · [Transitions](#role-assignment-correction-and-transition) · [Sensitivity](#authority-and-sensitivity-boundary) · [Implementation](#current-implementation-maturity) · [Conflicts](#conflict-and-hold-register) · [Convergence](#implementation-and-convergence-plan) · [Acceptance](#validation-and-acceptance-gates) · [Consequences](#consequences) · [Alternatives](#alternatives-considered) · [Rollback](#rollback-correction-and-supersession) · [Open questions](#open-questions) · [References](#references) · [No-loss ledger](#appendix-a--no-loss-reconciliation-ledger)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **ADR identity** | `not-assigned` — slug-only scaffold; no repository-wide number |
| **Tracked path** | `docs/adr/ADR-archaeology-source-roles.md` |
| **Source metadata** | `proposed` |
| **Effective decision status** | `not-assigned`; non-binding |
| **Decision class** | Domain binding to shared source-role vocabulary and anti-collapse semantics |
| **Directory authority** | Accepted ADR-0029 adopts Directory Rules v2; `docs/adr/` owns the human architectural decision record |
| **Primary evidence checkpoint** | `main@9d924c665073263f2cbf376d2bf29e7b9f252b06` |
| **Current shared implementation** | Rich `SourceDescriptor` schema plus fixture-first source-role validator and tests |
| **Current Archaeology implementation** | Extensive draft prose; machine role registry, domain fixture, domain validator, and domain test remain placeholders |
| **Current decision authority** | Not established |
| **Effect of this revision** | Documentation only |
| **Publication effect** | None |
| **Supersedes / superseded by** | None / none |

### Number assignment, acceptance, implementation, and release are separate

Four transitions must remain visible:

1. **Number assignment** would give this candidate a collision-free repository-wide
   `ADR-NNNN` identity and update the canonical index.
2. **Decision acceptance** would approve the Archaeology-to-shared-vocabulary
   binding and its anti-collapse rules.
3. **Implementation graduation** would require a reviewed mapping profile,
   schema/contract consistency, deterministic fixtures, validators, policy
   bindings, domain consumers, and correction behavior.
4. **Governed release** would apply those controls to a specific source,
   evidence packet, derived artifact, public API payload, map layer, export, or
   AI answer.

A commit, pull request, merge, schema-valid payload, validator `PASS`, green
workflow, or accepted ADR cannot collapse those transitions.

### Directory Rules basis

This is a same-path modernization of an existing tracked decision scaffold.
Accepted Directory Rules place the human decision record under `docs/adr/`.
They keep the connected responsibilities separate:

| Responsibility | Owning surface |
|---|---|
| Human architectural decision | `docs/adr/` |
| Cross-domain source-role guidance | `docs/sources/` |
| Archaeology source-family and admission guidance | `docs/domains/archaeology/` |
| SourceDescriptor meaning | `contracts/source/` |
| Machine-checkable source shape and vocabularies | `schemas/contracts/v1/source/` |
| Source-role use and transition validation | `tools/validators/source_role/` |
| Synthetic examples and executable proof | `fixtures/` and `tests/` |
| Source registry instances | `data/registry/sources/` |
| Rights, sensitivity, access, and release decisions | `policy/` and `release/` |
| Evidence and process memory | `data/proofs/` and `data/receipts/` |
| Public delivery | Governed API and released public-safe artifacts |

No responsibility root, lifecycle phase, schema home, policy home, registry
home, proof home, receipt home, or release home changes in this revision.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence boundary

This candidate is reconciled to current repository evidence at
`main@9d924c665073263f2cbf376d2bf29e7b9f252b06`. It does not rely on the
older scaffold's generic instruction to “fill in” the file, and it does not
convert the draft Archaeology packet into implementation proof.

### Truth labels

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Verified from current repository bytes, tests, validators, accepted Directory Rules, or target history |
| **PROPOSED** | Decision, mapping, owner assignment, migration, or implementation not accepted and proven |
| **UNKNOWN** | Evidence is insufficient to support a stronger statement |
| **NEEDS VERIFICATION** | A concrete repository, reviewer, policy, runtime, source, or release check remains |
| **CONFLICTED** | Current writable or normative-looking surfaces use incompatible role names or semantics |
| **HOLD** | A fail-closed implementation or acceptance blocker remains |

### Current repository evidence

| Surface | CONFIRMED finding | Limit |
|---|---|---|
| This target | Created as a generated 15-line scaffold in commit `fa728424…`; no later substantive revision was present at the checkpoint | File presence did not create a decision |
| [`INDEX.md`](./INDEX.md) | Lists this file among 12 unassigned scaffolds as `not-assigned` | Inventory does not accept it |
| ADR-0029 and Directory Rules | ADR-0029 is accepted and pins the Directory Rules bytes used for placement | Placement authority does not accept source-role semantics |
| [`SOURCE_REGISTRY.md`](../domains/archaeology/SOURCE_REGISTRY.md) | Defines source role as fixed at admission and describes seven Archaeology terms | It is draft prose, contains older repo-depth assumptions, and does not match the current machine enum |
| [`SOURCES.md`](../domains/archaeology/SOURCES.md) | Defines eight source families and repeats the seven-term anti-collapse model | It is draft doctrine/lineage and contains stale proposed-path statements |
| [`source-roles.md`](../sources/source-roles.md) | Provides broad human source-role families and role-to-claim guidance | Its prose vocabulary is not identical to the active schema enum |
| [`source_descriptor.md`](../../contracts/source/source_descriptor.md) | Defines the rich shared `SourceDescriptor` meaning and separates role from authority, rights, sensitivity, review, and release | Contract status remains draft/PROPOSED |
| `source_descriptor.schema.json` | Requires `source_role`, `authority_rank`, `admissibility_limits`, rights, sensitivity, review, release, and lifecycle fields; exposes a 16-token role enum | Schema authority remains PROPOSED; historical path metadata remains in the file |
| Shared source-role validator | Executable no-network validator reads the schema vocabulary, checks role/rank and claim compatibility, rejects AI inference and role laundering, and emits finite outcomes | Profile is explicitly `PROPOSED_INACTIVE`; it creates no authority or publication |
| Shared validator tests | Fourteen fixture cases and deterministic CLI/shim tests exist | Tests prove only the bounded fixture profile |
| Transition assessment | Separate contract/schema uses seven uppercase roles and checks passthrough, aggregation, modeling, synthesis, generalization, and lifecycle promotion | Its `source_role` naming collides conceptually with the 16-token SourceDescriptor vocabulary |
| Archaeology role registry YAML | File exists at `data/registry/sources/archaeology/source_roles.yaml` | It is only a PROPOSED placeholder with no mapping rows |
| Archaeology fixture lane | README accurately labels the synthetic source-descriptor lane placeholder-only | The lone `shpo_like.json` is not SourceDescriptor-shaped |
| Archaeology validator/test | Domain validator raises `NotImplementedError`; domain test is docstring-only | No domain-specific executable proof |
| Exact-location sibling ADR | Separate slug-only scaffold exists | Exact-location policy remains unassigned and must not be silently decided here |
| ADR-0017 | Proposed source-admission ADR separates descriptor shape, activation, watcher intake, record admission, promotion, and release | It does not decide the Archaeology role crosswalk |

### What was not exercised

- no real SHPO, NRHP, field-survey, excavation, collection, laboratory,
  historical, oral-history, or cultural-knowledge source;
- no source endpoint, credential, access agreement, MOU, rights grant, consent
  token, revocation service, or cultural authority system;
- no admitted Archaeology `SourceDescriptor` or populated source-role registry;
- no connector, watcher, RAW/QUARANTINE write, or source activation decision;
- no archaeology policy evaluator or exact-location transform;
- no EvidenceBundle resolution, public API, MapLibre layer, export, Focus Mode
  answer, release manifest, correction propagation, or rollback drill.

[Back to top](#top)

---

<a id="context"></a>

## Context

Archaeology has unusually high consequences when source identity and source
role are collapsed. A regulatory listing can be mistaken for a field
observation. A collection accession can be mistaken for evidence of an object's
original location. A LiDAR anomaly can be presented as a confirmed site. A
county-level density product can be drilled into as per-place truth. A 3D
reconstruction can be presented as observed reality. A public listing can be
treated as permission to reproduce exact coordinates.

KFM already has the pieces needed to prevent those failures, but they are not
yet one coherent authority:

1. The shared `SourceDescriptor` machine schema defines 16 lowercase
   `source_role` values and separate `authority_rank`, `source_type`,
   `admissibility_limits`, rights, sensitivity, review, release, and lifecycle
   axes.
2. The shared source-role use validator reads that machine vocabulary and
   enforces role/rank compatibility, claim-role compatibility, public-surface
   restrictions, AI-inference denial, and role-change lineage.
3. Archaeology source documents use a seven-term domain grammar:
   `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`,
   `candidate`, and `synthetic`.
4. The cross-domain `SourceRoleTransitionAssessment` uses uppercase versions of
   those seven terms as input and output transition classes.
5. The human cross-domain source-role guide uses a broader descriptive
   vocabulary such as primary evidence, context, regulatory context,
   observation, model product, historical source, generated derivative, and
   restricted source.
6. The Archaeology machine mapping file, domain fixture, domain validator, and
   domain test remain placeholders.

Each surface is useful. The risk is treating all of them as interchangeable.
That would create parallel vocabulary authority and allow different consumers
to make different claims from the same source.

### Decision drivers

- **One machine vocabulary:** a source descriptor must have one reviewable role
  vocabulary, not a global enum plus a domain-local enum with ambiguous
  equivalence.
- **Bounded-context clarity:** Archaeology needs domain language without
  redefining the shared source contract.
- **Role-to-claim compatibility:** a source's admissible use depends on the
  claim, not only on publisher reputation or file origin.
- **No role laundering:** promotion, aggregation, modeling, generalization,
  synthesis, map styling, AI explanation, and publication must not upgrade
  authority.
- **Candidate humility:** remote-sensing and predictive signals remain
  candidates until distinct evidence and review support a different claim.
- **Rights and sovereignty independence:** evidentiary role does not override
  rights, consent, cultural authority, exact-location controls, or public
  release.
- **Deterministic enforcement:** positive and negative cases should be
  replayable without network access.
- **Correction and rollback:** a role correction must preserve the prior
  descriptor and downstream lineage.

### Scope

This decision applies to Archaeology source descriptors, source-role mapping,
record- and claim-use checks, source-role propagation, transformations,
catalog/triplet projections, EvidenceBundles, governed API payloads, MapLibre
layers, exports, search, Story Nodes, Focus Mode, AI responses, corrections,
withdrawals, and rollback.

### Out of scope

This candidate does not:

- assign an ADR number or accept itself;
- accept the shared 16-token vocabulary as repository-wide authority;
- replace ADR-0017's source-admission process;
- decide exact-location thresholds, cultural review, sovereignty, consent,
  rights, embargo, or access policy;
- activate any real source or connector;
- define Archaeology object-family schemas;
- approve a source, claim, EvidenceBundle, map layer, AI answer, release, or
  publication;
- migrate or delete any existing role vocabulary, contract, schema, registry,
  fixture, validator, test, policy, or source document;
- establish that a public listing's coordinates are safe to expose;
- treat a model, candidate, aggregate, synthetic representation, map, or
  generated explanation as observed reality.

[Back to top](#top)

---

<a id="proposed-decision"></a>

## Proposed decision

> [!IMPORTANT]
> **PROPOSED:** Archaeology SHALL bind to the shared
> `SourceDescriptor.source_role` vocabulary selected by KFM's cross-domain
> source authority. It SHALL express Archaeology-specific distinctions through
> a reviewed crosswalk, source type, authority rank, admissibility limits,
> claim-role compatibility, secondary roles, evidence, rights, sensitivity, and
> review/release state. It SHALL NOT introduce another writable
> `SourceDescriptor.source_role` enum.

If accepted, the following rules apply.

### 1. Shared vocabulary, domain profile

The shared SourceDescriptor contract/schema owns the machine role vocabulary.
Archaeology owns a domain profile that explains how its source families and
domain terms map into that shared vocabulary.

The domain profile may be stricter than the shared baseline. It may not add a
new machine role token, weaken a shared deny condition, or turn a semantic alias
into canonical machine shape without a reviewed vocabulary change.

### 2. Source role is only one axis

Every use must preserve, at minimum:

- source identity and descriptor version;
- source type;
- one primary shared source role;
- optional shared secondary source roles;
- authority rank and authority notes;
- allowed and prohibited claim roles;
- rights, attribution, redistribution, and access posture;
- sensitivity, sovereignty, consent, and exact-location posture;
- temporal and source-head state;
- evidence, policy, review, release, correction, and rollback references when
  required.

No single `source_role` value can stand in for those dimensions.

### 3. Role is assigned through governed admission

A source role must originate from the admitted SourceDescriptor or an accepted
correction/supersession record. It must not be guessed from:

- a source title, file path, publisher reputation, public availability, or URL;
- a map style, layer name, popup label, graph edge, or catalog category;
- a language model, generated summary, embedding, or retrieval ranking;
- a lifecycle directory, successful connector run, schema pass, or green CI
  result.

Unknown, contradictory, unsupported, or AI-inferred role is fail-closed.

### 4. Promotion does not upgrade role

RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED changes
lifecycle state, not source authority. Promotion cannot convert:

- `candidate_signal` into `observation` or `occurrence_evidence`;
- `model_context` into `observation`;
- `aggregator` or an aggregate output into per-place truth;
- `historical_context` or `corroborating_context` into
  `authoritative_for_claim`;
- `derived_public_product` into source evidence;
- `fixture_only` into any real-source role.

### 5. Candidate confirmation creates new governed lineage

A LiDAR, imagery, geophysics, predictive, or documentary candidate does not
become a site because it is reviewed, mapped, promoted, or published.

When distinct ground evidence supports a site or observation claim:

1. preserve the candidate source and candidate object;
2. admit the new observational or occurrence-supporting source posture
   separately;
3. create the domain assertion with its own evidence and review lineage;
4. connect candidate and confirmed records through explicit relation,
   correction, or supersession semantics appropriate to the object family;
5. preserve the candidate's original role in history.

### 6. Transformations preserve lineage and add support type

Aggregation, modeling, synthesis, and generalization may create a new derived
artifact or support character. They do not rewrite the underlying source role.

- Aggregation requires an aggregation receipt and cannot support per-place
  claims.
- Modeling requires model identity, inputs, method/version, uncertainty, and a
  model-run receipt.
- Synthesis or reconstruction requires a representation receipt and a reality
  boundary note.
- Generalization requires a transform/redaction receipt where sensitivity or
  public exposure is material.
- Every output preserves the distinct set of input source roles.

### 7. Public use is claim-bounded and fail-closed

A public API, map, export, story, search result, or AI answer may use a source
only when:

- the requested claim role is admitted by the descriptor;
- rights, sensitivity, consent, and access posture allow the exposure;
- required evidence, policy, review, and release references resolve;
- source role and limitations remain visible;
- candidate, modeled, aggregate, synthetic, historical, regulatory, legal, and
  derived status are not hidden or upgraded;
- correction and rollback paths exist where the public consequence requires
  them.

### 8. Exact location remains a separate decision

Source role never authorizes exact Archaeology location exposure. Exact
coordinates, burial or sacred contexts, private-land geometry, collection
security, looting risk, oral history, and sovereignty-sensitive material remain
subject to the separate exact-location and sensitivity decision family.

### 9. AI remains interpretive

AI may summarize a resolved source-role use assessment. It may not assign,
upgrade, reconcile, or waive source role; infer permission; confirm a site; or
replace evidence, cultural review, policy, release, correction, or rollback.

### 10. Finite validation outcomes remain non-authoritative

The current shared source-role use profile returns:

| Outcome | Meaning in the validator lane | Non-effect |
|---|---|---|
| `PASS` | Declared descriptor snapshot and use request are internally compatible under the fixture profile | No authority, evidence, activation, review, release, or publication |
| `RESTRICT` | Internal/steward use may proceed only under restrictions | No public permission |
| `ABSTAIN` | Role or confidence cannot support the requested primary claim | No inferred claim |
| `HOLD` | A reviewed role change, policy/review gap, or release dependency remains | No lifecycle or authority transition |
| `DENY` | Role inference, laundering, incompatible claim use, or unsafe exposure is blocked | No fallback allow |
| `ERROR` | Shape, identity, canonicalization, or tool input is invalid | No partial result |

A public runtime may expose a narrower final envelope vocabulary, but it must
not discard the underlying reason codes or convert a validator result into
release authority.

[Back to top](#top)

---

<a id="current-shared-machine-vocabulary"></a>

## Current shared machine vocabulary

The current executable validator loads the following values from
`schemas/contracts/v1/source/source_descriptor.schema.json`.

> [!CAUTION]
> These tokens are **CONFIRMED current implementation**, not an accepted
> repository-wide vocabulary decision. This candidate proposes that Archaeology
> bind to the selected shared vocabulary; it does not independently accept that
> vocabulary.

| Current token | Archaeology-safe interpretation |
|---|---|
| `authoritative_for_claim` | Source is authoritative only for the specifically admitted claim role and scope |
| `regulatory_context` | Official regulatory designation, finding, or status context; not physical observation |
| `legal_context` | Legal instrument or authority for the exact legal claim and jurisdiction; not occurrence or location permission |
| `observation` | Time/place/method-bounded observation; not automatically a confirmed site or public-safe point |
| `occurrence_evidence` | Evidence supporting occurrence within admitted scope; still subject to review and sensitivity |
| `aggregator` | Compiler/index/redistributor; does not inherit original-source authority |
| `operational_context` | Source health, notice, or operational context; not domain truth |
| `remote_sensing_observation` | Sensor-derived observation/detection with acquisition, resolution, processing, and quality metadata |
| `model_context` | Modeled, calibrated, interpolated, predicted, or reconstructed support; not direct observation |
| `candidate_signal` | Unconfirmed lead or anomaly; cannot be represented as a site |
| `historical_context` | Historical record or interpretation with temporal/provenance bounds |
| `corroborating_context` | Supports or checks a claim but cannot carry it alone |
| `derived_public_product` | Released derivative carrier; not source truth or EvidenceBundle |
| `steward_review_source` | Source or authority used for steward/cultural review; does not itself grant public release |
| `citation_source` | Supports attribution or citation context; not automatic claim authority |
| `fixture_only` | Synthetic test support only; never a real source or public evidence |

The schema also keeps `source_type`, `authority_rank`, `claim_role`, sensitivity,
rights, review state, release state, and admissibility limits separate. That
separation is load-bearing for Archaeology.

[Back to top](#top)

---

<a id="archaeology-domain-crosswalk"></a>

## Archaeology domain crosswalk

The seven terms in the current Archaeology documents remain useful as
ubiquitous language for domain review. They should become a compatibility and
explanation layer, not a second machine enum.

| Archaeology term | Shared SourceDescriptor mapping candidates | Required distinction | Forbidden shortcut |
|---|---|---|---|
| `observed` | `observation`; `occurrence_evidence`; narrowly `authoritative_for_claim` | State whether the source records a direct observation, an occurrence-supporting record, or an authority for a bounded claim | Treating any “observed” record as a confirmed, public-safe site |
| `regulatory` | `regulatory_context`; sometimes `legal_context` | Separate regulatory listing/status from legal authority and from physical occurrence | Treating a designation or listing as field observation or disclosure permission |
| `modeled` | `model_context`; `remote_sensing_observation` for sensor-native detection; `candidate_signal` for an unverified interpretation | Separate sensor observation, model output, calibrated result, prediction, and candidate inference | Relabeling modeled or remote-sensing output as direct observation |
| `aggregate` | `aggregator` for an external compiler; `derived_public_product` for a KFM aggregate carrier; claim roles limited to summary/map context | Preserve aggregation unit, method, source mix, uncertainty, and receipt | Drilling aggregate cells into per-site truth |
| `administrative` | `authoritative_for_claim` only for a narrow administrative claim; `citation_source`; `steward_review_source`; sometimes `regulatory_context` | State the exact administrative, custody, accession, permit, inventory, or review claim | Treating accession, inventory, or permit metadata as physical occurrence, title, or legal status |
| `candidate` | `candidate_signal` | Preserve candidate disposition, evidence gap, and no-site framing | Promotion or review silently turning a candidate into a site |
| `synthetic` | `derived_public_product`; `model_context`; `fixture_only` for tests, plus source type and reality-boundary support | Distinguish reconstruction, generated visualization, AI summary, synthetic fixture, and modeled scene | Presenting a reconstruction or generated narrative as observed reality |

### Historical and contextual material

The earlier Archaeology packet identified a generic `context` role as an open
question. The current shared schema already provides more bounded alternatives:

- `historical_context`;
- `corroborating_context`;
- `citation_source`;
- `regulatory_context`;
- `legal_context`;
- `operational_context`;
- `steward_review_source`.

This candidate therefore proposes **not** adding a generic Archaeology
`context` token. The domain profile should select the narrowest shared token and
state the permitted claim role.

### Crosswalk is not equivalence

The table is many-to-many by design. A source family can contain records with
different roles, and one source can support different claims under different
admissibility limits. The implementation must not reduce the crosswalk to a
single unconditional map such as `observed -> observation` for every record.

[Back to top](#top)

---

<a id="source-family-application"></a>

## Source-family application

Archaeology's eight documented source families need claim-bounded defaults, not
blanket role labels.

| Source family | Likely primary shared roles | Required anti-collapse posture |
|---|---|---|
| State site inventory / SHPO-like system | `steward_review_source`, `citation_source`, `authoritative_for_claim` for narrow inventory status; record-level `observation` or `occurrence_evidence` only when supported | Inventory presence is not automatic field observation, legal status, or permission to expose coordinates |
| Public NRHP-like listings | `regulatory_context`; possibly `legal_context` for the exact legal/designation claim | Public listing metadata does not make exact coordinates public-safe in KFM |
| Field survey forms | `observation`, `occurrence_evidence`, `steward_review_source` | Survey coverage, negative survey, field observation, and site conclusion remain distinct |
| Excavation and provenience packets | `observation`, `occurrence_evidence`; narrow `authoritative_for_claim` for documented provenience | Excavation documentation does not waive burial, sovereignty, collection, or exact-location controls |
| Artifact, collection, and repository records | `authoritative_for_claim` for accession/custody; `citation_source`; `steward_review_source`; historical/corroborating roles as applicable | Repository custody or accession does not prove original find location or context |
| Laboratory reports | `observation` for source-native measurement; `model_context` for calibration or modeled interpretation; `corroborating_context` | Raw measurement and calibrated/model-derived result remain distinct |
| Historic maps, plats, land records, and newspapers | `historical_context`, `corroborating_context`, `citation_source`; `legal_context` only for qualifying legal records and claims | Georeferenced or historical depiction does not become present-day observation or exact site truth |
| Oral history and cultural knowledge | `steward_review_source`, `historical_context`, `citation_source`, or `corroborating_context` only under consent and authority | No automated public use, role inference, or disclosure from mere possession or transcription |

A descriptor may use `secondary_source_roles`, but every downstream use must
still pass role-to-claim compatibility and rights/sensitivity/review/release
gates.

[Back to top](#top)

---

<a id="role-assignment-correction-and-transition"></a>

## Role assignment, correction, and transition

### Assignment

Role assignment occurs through governed source admission. The descriptor must
bind source identity, descriptor version, role origin, authority rank,
admissibility limits, and review lineage.

### Correction

A mistaken role is corrected through a new descriptor version or accepted
correction/supersession mechanism. The prior descriptor remains inspectable.
Downstream catalogs, EvidenceBundles, derived products, API payloads, maps,
exports, and AI indexes must be invalidated or corrected where the old role
affected interpretation.

### Transformation

Transformation creates a new output characterization without laundering source
authority.

| Operation | Required output posture | Required support |
|---|---|---|
| Passthrough | Preserve source role and lineage | Input EvidenceBundle linkage where claims depend on evidence |
| Generalize | Preserve source role; add transform/public-safety lineage | Transform or redaction receipt when material |
| Aggregate | Output is an aggregate/derived carrier; inputs remain distinct | Aggregation receipt and aggregation unit |
| Model | Output is modeled context | Model-run receipt, inputs, version, uncertainty |
| Synthesize | Output is synthetic/derived | Representation receipt and reality boundary note |
| Promote lifecycle | Role unchanged | Promotion evidence; candidate inputs remain candidates |

### Transition-assessment naming conflict

The current `SourceRoleTransitionAssessment` uses uppercase
`OBSERVED | REGULATORY | MODELED | AGGREGATE | ADMINISTRATIVE | CANDIDATE |
SYNTHETIC` values in a field also named `source_role`.

That profile supplies valuable anti-collapse proof, but its terms are not
one-to-one values of `SourceDescriptor.source_role`. Before acceptance, KFM
must choose one of these bounded treatments:

1. rename the transition field to a distinct concept such as
   `support_character`, `transition_class`, or `output_character`;
2. retain the field with an explicit, versioned adapter to the shared
   SourceDescriptor vocabulary;
3. revise the shared vocabulary through a separate reviewed cross-domain
   decision.

Directly treating the uppercase seven-term schema as a second
SourceDescriptor role authority is **DENY**.

[Back to top](#top)

---

<a id="authority-and-sensitivity-boundary"></a>

## Authority and sensitivity boundary

Source role answers: **What relationship may this source have to a claim?**

It does not answer:

- may KFM access or copy the source;
- may KFM redistribute source content;
- may a record enter RAW, PROCESSED, CATALOG, or PUBLISHED;
- is a site, burial, sacred place, collection, oral history, or private-land
  location safe to expose;
- has a cultural, tribal, rights-holder, sensitivity, or release reviewer
  approved use;
- is the evidence sufficient;
- is the source current;
- may AI summarize or display it;
- may a map, export, screenshot, story, or API reveal it.

### Independent gates

| Gate | Required question |
|---|---|
| Source identity | Is the source and descriptor version resolved? |
| Role and authority | What shared role, authority rank, and claim limits apply? |
| Rights and access | What terms, attribution, redistribution, access, and consent obligations apply? |
| Sensitivity and sovereignty | What exact-location, cultural, burial, private-land, collection-security, tribal, or revocation controls apply? |
| Evidence | Can the claim resolve to appropriate EvidenceRefs/EvidenceBundles? |
| Review | Which source, domain, cultural, rights, sensitivity, and release reviews are required and recorded? |
| Release | Is there a governed release state, public-safe transform, correction path, and rollback target? |
| Delivery | Does every API, map, export, search, and AI surface preserve the result without side-channel leakage? |

### Exact-location sibling decision

[`ADR-archaeology-exact-location-policy.md`](./ADR-archaeology-exact-location-policy.md)
remains a separate unassigned scaffold. This candidate may depend on a future
accepted exact-location decision, but it does not preempt it. Until the
sensitivity and exact-location authority is accepted and enforced, exact
Archaeology location exposure remains fail-closed.

[Back to top](#top)

---

<a id="authority-and-publication-boundary"></a>

## Authority and publication boundary

This ADR candidate records a proposed semantic and architectural decision only.

It does not:

- create or mutate a SourceDescriptor;
- populate `source_roles.yaml`;
- assign a source role;
- admit or activate a source;
- issue a RightsDecision, SensitivityDecision, CulturalReview, StewardReview,
  PolicyDecision, or SourceActivationDecision;
- create evidence, receipts, proofs, catalogs, release manifests, corrections,
  or rollback cards;
- authorize connector access, lifecycle writes, public API delivery, map
  rendering, AI use, release, deployment, or publication.

Even after acceptance, implementation and release remain separately governed.

[Back to top](#top)

---

<a id="alternatives-considered"></a>

## Alternatives considered

### Option A — Shared SourceDescriptor vocabulary with an Archaeology profile

**Selected.** Preserve one machine vocabulary and validator family while making
Archaeology's domain language, source families, candidate boundary, cultural
review, and sensitivity requirements explicit through a reviewed crosswalk and
stricter domain rules.

### Option B — Keep the seven Archaeology terms as a domain-local machine enum

**Rejected.** This creates parallel role authority, forces adapters at every
shared consumer, and permits silent divergence between source admission,
evidence, policy, catalog, API, map, and AI surfaces.

### Option C — Make the uppercase transition-assessment enum the
SourceDescriptor enum

**Rejected.** The transition profile describes output/transition character and
does not cover the current SourceDescriptor roles, claim compatibility, or
authority-rank semantics. Treating it as the source enum would erase useful
distinctions such as historical, corroborating, citation, steward-review,
remote-sensing, and fixture-only roles.

### Option D — Use no Archaeology-specific profile

**Rejected.** The shared schema cannot, by itself, explain the Archaeology
source families, candidate-not-site rule, laboratory measurement/calibration
split, collection-provenience boundary, oral-history authority, or public
exact-location risk.

### Option E — Infer roles dynamically in connectors or AI

**Rejected.** Role inference by runtime, file path, source reputation, or model
language is unauditable and already denied by the shared validator.

### Option F — Treat role as a quality or confidence score

**Rejected.** Role, authority rank, evidence sufficiency, confidence, rights,
sensitivity, review, and release are different axes. A single score would hide
the reason a claim is allowed, restricted, abstained, held, or denied.

[Back to top](#top)

---

<a id="consequences"></a>

## Consequences

### Positive

- One shared machine vocabulary can serve source admission, EvidenceBundles,
  policy, catalog, governed API, maps, exports, and AI.
- Archaeology retains useful domain language without creating another authority
  surface.
- Candidate, modeled, aggregate, synthetic, regulatory, legal, administrative,
  historical, and observed material remain distinguishable.
- Current shared validators and fixtures can be reused instead of cloned.
- Role changes become versioned, reviewable, correctable, and reversible.
- Exact-location and cultural controls remain independent and fail-closed.
- Public surfaces can expose bounded role badges and limitations without
  exposing restricted source material.

### Costs and tradeoffs

- The seven-term Archaeology prose cannot be copied directly into
  `SourceDescriptor.source_role`.
- Existing Archaeology documents require a careful crosswalk and stale-claim
  correction rather than mechanical terminology replacement.
- Some source families need record-level or claim-level role selection; one
  descriptor-wide label may be insufficient.
- The transition-assessment profile needs naming or adapter clarification.
- Administrative and cultural-authority mappings require domain and steward
  review.
- Public API/UI payloads need more than a role string: authority rank,
  admissibility, rights, sensitivity, evidence, review, release, and correction
  state remain load-bearing.

### Risks if implemented poorly

- A simplistic crosswalk could upgrade administrative or regulatory records
  into occurrence evidence.
- A remote-sensing detection could be mapped to `observation` when it should be
  `remote_sensing_observation` or `candidate_signal`.
- A source family could be assigned one role even though record types inside it
  require different roles.
- An accepted role could be mistaken for permission to expose exact location.
- A derived layer or 3D scene could drop role lineage and appear authoritative.
- Role correction could mutate history rather than issue a new descriptor and
  correction lineage.
- A client could hide restrictions in styling while leaking them through
  labels, URLs, exports, search, screenshots, or AI prose.

[Back to top](#top)

---

<a id="current-implementation-maturity"></a>

## Current implementation maturity

| Capability | Current result | Interpretation |
|---|---|---|
| Target identity and path | **CONFIRMED** | Existing slug-only scaffold at the indexed path |
| ADR number and acceptance | **NOT MET** | `not-assigned`; no decision authority |
| Accepted Directory Rules placement | **CONFIRMED** | Same-path human decision record is correctly placed |
| Shared SourceDescriptor contract | **CONFIRMED file / PROPOSED authority** | Rich semantic contract exists |
| Shared SourceDescriptor schema | **CONFIRMED implemented / PROPOSED authority** | Closed shape and 16-token role enum exist |
| Shared source-role use contract/schema | **CONFIRMED** | Bounded use packet exists |
| Shared role-use validator | **CONFIRMED fixture-first implementation** | No-network finite outcomes and anti-collapse checks exist |
| Shared validator tests | **CONFIRMED** | Fourteen cases plus deterministic CLI/shim tests |
| Transition assessment | **CONFIRMED fixture-first implementation** | Seven uppercase transition classes; naming conflict remains |
| Archaeology source documents | **CONFIRMED extensive draft prose** | Valuable lineage, but vocabulary and repo-state claims require reconciliation |
| Archaeology role registry | **FAIL / placeholder** | No machine crosswalk rows |
| Archaeology valid fixture | **FAIL / absent** | Existing JSON is inventory metadata, not SourceDescriptor shape |
| Archaeology domain validator | **FAIL / placeholder** | Raises `NotImplementedError` |
| Archaeology domain test | **FAIL / placeholder** | Docstring only |
| Archaeology policy evaluator | **UNKNOWN** | No exact role-use evaluation was exercised |
| Source activation and registry use | **UNKNOWN / not exercised** | No real source or connector was used |
| API, MapLibre, export, search, AI binding | **UNKNOWN** | No public consumer behavior was exercised |
| Correction, withdrawal, rollback | **UNKNOWN** | No domain role-correction drill was exercised |
| Release or publication | **NONE** | This revision has no release effect |

The shared validator is materially ahead of the domain-specific Archaeology
fixture lane. That is evidence for reuse, not evidence that the Archaeology
profile is complete.

[Back to top](#top)

---

<a id="conflict-and-hold-register"></a>

## Conflict and hold register

| ID | Conflict or hold | Current posture | Closure requirement |
|---|---|---|---|
| `ARCH-ROLE-01` | Seven lowercase Archaeology terms vs 16 lowercase SourceDescriptor tokens | **CONFLICTED / HOLD** | Reviewed many-to-many crosswalk and claim examples |
| `ARCH-ROLE-02` | Seven uppercase transition classes share the name `source_role` | **CONFLICTED / HOLD** | Rename, adapter, or separate cross-domain vocabulary decision |
| `ARCH-ROLE-03` | Human `source-roles.md` uses broader prose families than the schema | **CONFLICTED / HOLD** | Publish human-to-machine crosswalk without creating a second enum |
| `ARCH-ROLE-04` | Archaeology `source_roles.yaml` is placeholder-only | **FAIL / HOLD** | Define its role as a mapping/profile projection and validate it |
| `ARCH-ROLE-05` | Archaeology synthetic fixture is not SourceDescriptor-shaped | **FAIL / HOLD** | Add public-safe valid and negative fixtures tied to named consumers |
| `ARCH-ROLE-06` | Archaeology domain validator and test are placeholders | **FAIL / HOLD** | Delegate to shared validator and assert domain-specific failures |
| `ARCH-ROLE-07` | `administrative` has no direct shared SourceDescriptor token | **NEEDS VERIFICATION** | Decide claim-bounded mapping with source and archaeology stewards |
| `ARCH-ROLE-08` | Generic `context` was open in older Archaeology prose | **NARROWED / HOLD** | Use bounded shared context tokens unless review proves a gap |
| `ARCH-ROLE-09` | Exact-location and source-role decisions are easy to collapse | **DENY collapse** | Separate accepted decisions, policy, transforms, fixtures, and UI tests |
| `ARCH-ROLE-10` | Role may vary by record or claim inside one source family | **NEEDS VERIFICATION** | Define descriptor, record, and use-request granularity |
| `ARCH-ROLE-11` | Current shared schema authority remains proposed | **HOLD for acceptance** | Cross-domain owner review and compatible migration plan |
| `ARCH-ROLE-12` | Public consumer and correction propagation are unverified | **UNKNOWN / HOLD** | API/UI/AI tests plus correction/rollback dry run |

No hold may be hidden by changing wording, suppressing a badge, or treating a
green shared fixture suite as domain acceptance.

[Back to top](#top)

---

<a id="implementation-and-convergence-plan"></a>

## Implementation and convergence plan

This one-file revision performs none of the following steps. If the decision is
numbered and accepted, use the smallest dependency-closed sequence.

### Phase 0 — Assign and review the decision

1. Check the ADR index, open pull requests, and active branches for a
   collision-free number.
2. Rename the file and H1 together only in the reviewed assignment change.
3. Update `INDEX.md` in the same change.
4. Name decision owners and affected reviewers, including source,
   Archaeology, evidence, cultural/sovereignty, rights/sensitivity, schema,
   policy, validation, public-surface, correction, and release roles.
5. Keep the decision `proposed` until explicit disposition.

### Phase 1 — Freeze vocabulary authority

1. Pin the shared SourceDescriptor contract, schema, and source-role use profile
   under review.
2. Decide whether the 16-token schema vocabulary is accepted, amended, or
   superseded.
3. Define the relationship between human source-role families, shared machine
   tokens, and transition/output characters.
4. Record compatibility and deprecation rules; do not mass-rewrite first.

### Phase 2 — Create the Archaeology mapping profile

1. Convert the seven-term Archaeology grammar into a documented many-to-many
   mapping.
2. State per-source-family and per-claim defaults.
3. Resolve the `administrative` mapping and record/descriptor granularity.
4. Make `data/registry/sources/archaeology/source_roles.yaml` a generated or
   reviewed projection only if that responsibility is confirmed; do not let it
   become a second vocabulary authority.
5. Add stable mapping identifiers and versioning.

### Phase 3 — Replace placeholders with deterministic proof

1. Add synthetic, public-safe SourceDescriptor fixtures covering the eight
   source families.
2. Add negative cases for candidate-as-site, regulatory-as-observation,
   accession-as-provenience, aggregate-as-per-place, modeled-as-observed,
   synthetic-as-reality, AI-inferred role, and rights/sensitivity bypass.
3. Replace the Archaeology domain validator with a thin adapter to the shared
   validator plus domain mapping checks.
4. Replace the docstring-only domain test with executable assertions.
5. Preserve no-network execution and deterministic output.

### Phase 4 — Reconcile transition semantics

1. Rename or adapt the transition-assessment seven-term `source_role` field.
2. Preserve existing fixtures through an explicit compatibility window.
3. Prove that lifecycle promotion does not alter role.
4. Prove aggregation, modeling, synthesis, and generalization add receipts and
   preserve input-role lineage.

### Phase 5 — Bind policy and public consumers

1. Add or update fail-closed policy for role-to-claim compatibility.
2. Verify exact-location, cultural, sovereignty, rights, consent, and release
   checks remain independent.
3. Bind source role, authority rank, limitations, evidence, review, release,
   stale, and correction state through governed API payloads.
4. Add MapLibre/Evidence Drawer, export, search, and AI tests for role badges,
   candidate labels, aggregate limits, model/synthetic disclosures, and
   side-channel resistance.

### Phase 6 — Prove correction and rollback

1. Run a role-correction dry run from an incorrect descriptor through
   correction/supersession, catalog, public payload, cache/index invalidation,
   map/UI, export, and AI retrieval.
2. Verify the prior state remains auditable.
3. Verify rollback restores the last valid released state without restoring
   the incorrect role as current.
4. Record review and release separation appropriate to Archaeology sensitivity.

At every phase, a passing implementation remains a candidate until the
applicable review, policy, evidence, release, correction, and rollback gates
close.

[Back to top](#top)

---

<a id="validation-and-acceptance-gates"></a>

## Validation and acceptance gates

### Acceptance matrix

| Gate | Current result | Acceptance requirement |
|---|---|---|
| Same-path candidate and index classification | **PASS / CONFIRMED** | Preserve `not-assigned` until reviewed numbering |
| Decision owners and reviewers | **FAIL / unassigned** | Name accountable roles and record review |
| Shared vocabulary authority | **HOLD** | Accept or amend one cross-domain SourceDescriptor vocabulary |
| Archaeology seven-term crosswalk | **HOLD** | Versioned, many-to-many, claim-bounded mapping |
| Transition-assessment vocabulary | **HOLD** | Distinct name or accepted adapter |
| SourceDescriptor contract/schema parity | **PARTIAL** | Resolve accepted authority and historical metadata/path drift |
| Archaeology role registry | **FAIL / placeholder** | Validated profile/projection with one owner and no parallel authority |
| Synthetic valid fixtures | **FAIL / absent** | Public-safe, schema-valid examples for representative families |
| Negative anti-collapse fixtures | **FAIL / absent** | Candidate, model, aggregate, regulatory, administrative, historical, synthetic, AI, rights, and sensitivity cases |
| Shared role-use validator | **PASS for fixture profile** | Preserve deterministic no-network behavior and reason codes |
| Archaeology adapter/test | **FAIL / placeholder** | Executable domain mapping and anti-collapse assertions |
| Policy binding | **UNKNOWN** | Evaluated fail-closed role-to-claim policy with rights/sensitivity independence |
| API/UI/AI propagation | **UNKNOWN** | Public payload and client tests preserve role and limitations |
| Correction/rollback proof | **UNKNOWN** | At least one end-to-end dry run |
| Human acceptance review | **PENDING** | Explicit disposition recorded with required reviewers |

### Representative tests

| Family | Positive case | Negative case | Expected result |
|---|---|---|---|
| Field observation | Survey observation used for a bounded observation claim with evidence and review | Survey record treated as exact public site without release controls | `PASS` internally or `DENY` public exposure |
| Regulatory listing | Listing supports regulatory-status context | Listing used as physical occurrence or coordinate-release permission | `DENY` |
| Remote sensing | Sensor detection remains `remote_sensing_observation` or candidate context | Detection presented as confirmed site | `DENY` |
| Candidate | Candidate remains labeled, bounded, and non-authoritative | Candidate promoted into a site through lifecycle movement | `DENY` |
| Aggregate | County/H3 summary used only at admitted scale | Aggregate drilled into per-place truth | `DENY` |
| Collection record | Accession supports custody/administrative claim | Accession used as provenience or occurrence proof | `DENY` or `ABSTAIN` |
| Laboratory result | Measurement and calibrated/model result remain separate | Calibrated date represented as raw measurement | `DENY` |
| Historic source | Historical record supports bounded historical/corroborating context | Historical depiction represented as current observed location | `DENY` or `ABSTAIN` |
| Synthetic representation | Reconstruction carries receipt and reality boundary note | Scene or AI summary presented as observation | `DENY` |
| Role correction | New descriptor/version and lineage are present | In-place mutation with no correction/supersession | `DENY` |
| Rights/sensitivity | Strong role plus approved public-safe transform and release | Strong role used to bypass rights or exact-location policy | `DENY` |
| AI behavior | AI reports the admitted role and limitations from governed input | AI infers or upgrades role | `DENY` |

### Repository-native commands

ADR inventory coherence:

```bash
python tools/validators/validate_adr_index.py
python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers
```

Shared source-role use profile:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m pytest -q tests/validators/test_validate_source_role.py

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/source_role/validate_source_role.py --fixtures

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/sources/validate_source_role.py --fixtures
```

Transition profile:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m pytest -q tests/source/test_source_role_transition_assessment.py
```

Passing these checks proves only the checked inventory or fixture profile. It
does not number or accept this candidate, assign a real source role, approve
rights/sensitivity, activate a source, create evidence, or authorize release.

### Validation required for this documentation-only revision

- complete Markdown parses under the repository's GFM-compatible tooling;
- metadata block parses as YAML;
- fenced blocks are balanced;
- no duplicate generated heading slugs;
- no tabs or trailing whitespace;
- target remains discoverable as a scaffold by the current ADR-index validator;
- only the requested path changes;
- branch is based on the pinned current main;
- hosted checks are reported separately from local/static validation.

[Back to top](#top)

---

<a id="rollback-correction-and-supersession"></a>

## Rollback, correction, and supersession

### While unassigned and proposed

Rollback is a normal revert of the one-file modernization commit. The filename,
scaffold identity, and index row remain unchanged, so no path or index migration
is required.

### If later numbered and accepted

- do not rewrite the accepted decision into the opposite rule;
- use a successor ADR for a material vocabulary or authority reversal;
- maintain reciprocal supersession links;
- preserve prior role mappings and descriptor versions;
- issue correction/supersession records for role changes;
- invalidate affected catalogs, public payloads, caches, tiles, search indexes,
  exports, stories, screenshots under KFM control, and AI retrieval indexes;
- retain the deny-by-default posture while a role, rights, sensitivity, policy,
  or release defect is investigated;
- restore the last known valid released state through the governed rollback
  process.

### Rollback target for implementation work

Every implementation phase must identify:

1. the last valid shared vocabulary/profile version;
2. the last valid Archaeology mapping version;
3. affected descriptor and derived-artifact identities;
4. public consumers and caches requiring invalidation;
5. a reversible compatibility window;
6. the correction notice and rollback reference.

[Back to top](#top)

---

<a id="open-questions"></a>

## Open questions

1. Which collision-free numeric ADR ID should be assigned after rechecking the
   current index, open pull requests, and active branches?
2. Which owners and reviewers have authority to accept the shared vocabulary
   binding and the Archaeology profile?
3. Is the current 16-token SourceDescriptor enum the intended shared vocabulary,
   or should a successor vocabulary be reviewed first?
4. Should the seven uppercase transition terms be renamed
   `support_character`, `transition_class`, or another distinct concept?
5. What is the accepted many-to-many mapping for `administrative`, especially
   inventory, accession, custody, permit, and registration claims?
6. At what granularity is role assigned: source descriptor, source subresource,
   record, EvidenceRef, or use request?
7. When a source contains multiple record types, should it use
   `secondary_source_roles`, split descriptors, or record-level role bindings?
8. Which source families require `steward_review_source` versus
   `citation_source` versus `authoritative_for_claim`?
9. How should oral history and cultural knowledge represent rights-holder
   authority without implying public citation or release permission?
10. How should the exact-location sibling ADR and this role decision reference
    each other without collapsing source authority into exposure policy?
11. What accepted reason codes and public-safe explanations should the
    Archaeology adapter expose?
12. Should `data/registry/sources/archaeology/source_roles.yaml` be handwritten,
    generated from a reviewed source, or replaced by a versioned profile object?
13. Which API/DTO carries role, authority rank, claim compatibility, evidence,
    review, release, and correction state to clients?
14. Which public surfaces must show role badges, and which restricted reason
    details must remain internal?
15. What correction and rollback drill is sufficient before the first real
    Archaeology source or public-safe derivative is admitted?

[Back to top](#top)

---

<a id="references"></a>

## References

### Governing and inventory

- [ADR operating contract](./README.md)
- [Canonical ADR index](./INDEX.md)
- [Accepted ADR-0029 — Directory Governance Standard v2](./ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules](../doctrine/directory-rules.md)

### Related decisions

- [ADR-0010 — Deny-by-default sensitive domains](./ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md)
- [ADR-0017 — Source Descriptor Admission Process](./ADR-0017-source-descriptor-admission-process.md)
- [ADR-0020 — Abstain Is a First-Class Decision](./ADR-0020-abstain-is-a-first-class-decision.md)
- [ADR-0024 — Steward Separation of Duties for Release](./ADR-0024-steward-separation-of-duties-for-release.md)
- [Archaeology exact-location candidate](./ADR-archaeology-exact-location-policy.md)

### Source and Archaeology guidance

- [Shared source-role guide](../sources/source-roles.md)
- [SourceDescriptor standard](../sources/SOURCE_DESCRIPTOR_STANDARD.md)
- [Archaeology Source Registry human guide](../domains/archaeology/SOURCE_REGISTRY.md)
- [Archaeology source-family catalogue](../domains/archaeology/SOURCES.md)
- [Archaeology sensitivity](../domains/archaeology/SENSITIVITY.md)
- [Archaeology publication and policy](../domains/archaeology/PUBLICATION_AND_POLICY.md)

### Contracts and schemas

- [SourceDescriptor contract](../../contracts/source/source_descriptor.md)
- [Source-role use request contract](../../contracts/source/source_role_use_request.md)
- [Source-role transition assessment contract](../../contracts/source/source_role_transition_assessment.md)
- [SourceDescriptor schema](../../schemas/contracts/v1/source/source_descriptor.schema.json)
- [Source-role use request schema](../../schemas/contracts/v1/source/source_role_use_request.schema.json)
- [Source-role transition assessment schema](../../schemas/contracts/v1/source/source_role_transition_assessment.schema.json)

### Validation and fixtures

- [Shared source-role implementation note](../../tools/validators/source_role/IMPLEMENTATION.md)
- [Shared source-role validator](../../tools/validators/source_role/validate_source_role.py)
- [Shared source-role rules](../../tools/validators/source_role/source_role_rules.py)
- [Shared source-role tests](../../tests/validators/test_validate_source_role.py)
- [Transition-assessment tests](../../tests/source/test_source_role_transition_assessment.py)
- [Archaeology synthetic fixture lane](../../fixtures/domains/archaeology/synthetic_source_descriptor/README.md)
- [Archaeology domain validator placeholder](../../tools/validators/domains/archaeology/validate_source_descriptor.py)
- [Archaeology domain test placeholder](../../tests/domains/archaeology/test_source_descriptor.py)
- [Archaeology source-role registry placeholder](../../data/registry/sources/archaeology/source_roles.yaml)

[Back to top](#top)

---

<a id="appendix-a--no-loss-reconciliation-ledger"></a>

## Appendix A — No-loss reconciliation ledger

| Prior scaffold element | Disposition | Result |
|---|---|---|
| Title identifying an Archaeology source-role ADR | **PRESERVED + clarified** | H1 now states the proposed shared-vocabulary binding |
| `Status: PROPOSED scaffold` | **PRESERVED exactly in meaning and discovery token** | Candidate remains unassigned and non-binding |
| Source relationship to `SOURCE_REGISTRY.md` | **PRESERVED + expanded** | Metadata and references retain the original source |
| Referenced path | **PRESERVED** | Same file path; no sibling replacement |
| Instruction to add authoritative content, owners, validation, and cross-links | **IMPLEMENTED as bounded candidate content** | Owners remain NEEDS VERIFICATION; evidence and gates are explicit |
| Separation of schemas, policy, fixtures, and release decisions | **PRESERVED + strengthened** | Responsibility table follows accepted Directory Rules |
| Warning not to treat scaffold as canonical truth | **PRESERVED + strengthened** | Numbering, acceptance, implementation, and release are separate |
| Original source-documents list | **PRESERVED + expanded** | Current shared contracts, schemas, validators, tests, and related ADRs are linked |
| Generic notes | **PRESERVED + made operational** | Anti-collapse, validation, rollback, and non-effects are explicit |

No original governance-significant instruction was silently removed. The
generic generated wording was replaced by repository-grounded decision content.

---

## Change history

| Date | Change | Status |
|---|---|---|
| 2026-05-20 | Generated the initial planned-file scaffold from the Archaeology docs inventory. | `PROPOSED scaffold` |
| 2026-08-14 | Replaced the generic scaffold body in place with a repository-grounded ADR candidate; preserved unassigned/index posture; reconciled shared and domain vocabularies, current validator evidence, conflicts, acceptance gates, convergence, correction, rollback, and no-loss history. | `PROPOSED / not-assigned` |
