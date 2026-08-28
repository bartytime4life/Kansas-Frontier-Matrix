<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0012-connector-outputs-to-data-raw-or-data-quarantine-only
title: "ADR-0012 — Connector outputs MUST land in data/raw/ or data/quarantine/ only"
type: adr
adr_id: ADR-0012
version: v1.4
status: draft
owners:
  - "NEEDS VERIFICATION — architecture decision owner"
  - "NEEDS VERIFICATION — connector and source-admission steward"
  - "NEEDS VERIFICATION — data lifecycle steward"
  - "NEEDS VERIFICATION — rights and sensitivity steward"
  - "NEEDS VERIFICATION — receipt and validation steward"
  - "NEEDS VERIFICATION — affected domain stewards"
owner_status: "CODEOWNERS provides repository review routing, but accepted stewardship, decision quorum, required-review rules, source-owner approval, and independent release controls were not verified"
reviewers_required:
  - Architecture steward
  - Docs steward
  - Connector and source-admission steward
  - Data lifecycle steward
  - Rights and sensitivity steward
  - Contracts and schemas stewards
  - Receipt and validation steward
  - Security reviewer
  - At least one affected domain steward
created: 2026-05-11
updated: 2026-08-13
policy_label: public
truth_posture: cite-or-abstain
owning_root: docs/
responsibility: "Record the proposed connector output boundary, distinguish payload landing from process memory, and reconcile bounded enforcement evidence without granting source, lifecycle, release, or publication authority."
responsibility_root: docs/
current_path: docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
supersedes: []
superseded_by: []
evidence_snapshot:
  snapshot_status: current_v1.4_repository_evidence
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 52a6c7b55fc473c813bde6ec413bcda81259e809
  target_prior_blob: 2cf9e082d403a5e4294ed0b845e58edc687f0c8b
  adr_index_blob: 938c5894c36b99e14810918e2c550ab0e92d53b1
  adr_0029_blob: 3ba5f902ffe20a65a259cb0a7dab07f1725d204b
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  connectors_readme_blob: a28336f6c15e0234241a7844e5683a52c2fd5024
  raw_readme_blob: 46dd82857f5e881452f39580ffa73bfc9a43b7c8
  quarantine_readme_blob: 9b375d795d96b15c06e51ef54770a023cd14454c
  ingest_pipeline_readme_blob: 47e484ed891d5b830f6cb30d20829610824f33ab
  connector_gate_workflow_blob: dd3fd47b44ed5151aaa4ce72032a069f4b848190
  non_publisher_test_blob: 3e1217f7c461b42caba7c74a9add39a8ceddc354
  connector_gate_readme_blob: 18b1b0561c9eb7bbcc3bd62bcd6e4ee357dabb2c
  connector_output_scanner_blob: 5b6b69545159e63e672e7c08dc41b519dd265617
  connectors_core_pyproject_blob: ea94c0b24f50a68f3d59becbb34625c42298d7d9
  connectors_core_primitives_blob: a817a1beea6d1e8344e5942db335b17284eebd4a
  connectors_core_transport_blob: a518421e06b0896b814f3bec27dc0d41f68dfa46
  connectors_core_source_adapter_blob: 5ae0390bf9998775ac249ad1e2804bca82ed3180
  connectors_core_artifact_handoff_blob: b8bcd4d17d982372b3a5f2dd98ef684e1ae72ec0
  connectors_core_artifact_handoff_test_blob: 2c247fd110cb8ec67e76a94076b13bab10863749
  source_registry_readme_blob: 2821e9681273bff6b430920d0a45312c5643ba33
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  source_descriptor_schema_blob: 582e70b834278c3c6ca9a8b31efbe0989c96f0bc
  ingest_receipt_contract_blob: 8e76dc10aa23de967501bd32479f83788339a39b
  ingest_receipt_schema_blob: 4e9707bec7da63049c5043562c9470564b77184f
  ingest_receipt_validator_blob: 6596685b04b7889355bf66ae6b25f1f83bacccaf
  ingest_receipt_test_blob: c80a81ac87fb4df7bacb6bbc9d0bd55c12addfde
  source_artifact_contract_blob: 9f5e2f082fa2a3aaf94c1e9d879b0a0baa797639
  source_artifact_schema_blob: f451ccbcd7543896cffb98e6abbca23f61432fa3
  source_artifact_validator_blob: 3d047c1277ba25e627f97c31c8b5d8a81b54c06c
  source_artifact_workflow_blob: 986e76bfe70829957ea6926985cb8bc61626ad0e
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md
  - docs/adr/ADR-0017-source-descriptor-admission-process.md
  - docs/adr/ADR-0021-quarantine-has-structured-exit-paths.md
  - docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - connectors/README.md
  - data/raw/README.md
  - data/quarantine/README.md
  - data/registry/sources/README.md
  - data/receipts/README.md
  - pipelines/ingest/README.md
  - contracts/source/ingest_receipt.md
  - contracts/source/source_artifact.md
  - schemas/contracts/v1/source/ingest_receipt.schema.json
  - schemas/contracts/v1/source/source_artifact.schema.json
  - schemas/contracts/v1/source/source_descriptor.schema.json
  - packages/connectors-core/README.md
  - packages/connectors-core/src/connectors_core/source_adapter.py
  - packages/connectors-core/src/connectors_core/artifact_handoff.py
  - tools/validators/connector_gate/README.md
  - tools/validators/connector_gate/output_paths.py
  - tools/validators/validate_ingest_receipt.py
  - tools/validators/validate_source_artifact.py
  - tests/packages/connectors_core/README.md
  - tests/policy/test_pipeline_connector_non_publisher.py
  - tests/validators/test_validate_ingest_receipt.py
  - .github/workflows/connector-gate.yml
  - .github/workflows/source-artifact-validation.yml
tags: [kfm, adr, governance, connectors, source-admission, pre-raw, raw, quarantine, receipts, non-publisher, trust-membrane, lifecycle, fail-closed]
notes:
  - "v1.4 reconciles the proposed decision with current connector-core, SourceArtifact, IngestReceipt, static-path, and workflow evidence. It changes documentation only and does not accept ADR-0012, activate a source, run a connector, admit payloads, migrate files, or publish anything."
  - "The canonical ADR index uniquely assigns ADR-0012 to this exact path."
  - "Accepted ADR-0029 governs top-level placement through the adopted Directory Rules bytes; it does not accept ADR-0012 or grant connector runtime authority."
  - "Connector payload captures remain limited to RAW or QUARANTINE; receipt candidates are a separate process-memory output through a governed append-only receipt sink."
  - "SourceDescriptor is an admitted registry input, not a per-run connector-owned authority record. A connector may reference or propose a descriptor but must not silently write registry authority during a source run."
  - "Current CI runs bounded static path checks, connector-core primitives, injected transport, SourceAdapter and SourceArtifact handoff tests, plus the IngestReceipt validator prerequisite; actual connector-run receipt presence and persistence remain an explicit hold."
  - "The internal connectors-core package provides no concrete live transport, stable public export, arbitrary storage interface, source activation, evidence, policy, release, or publication authority."
  - "The connector-versus-shared-ingest writer handoff remains implementation-level NEEDS VERIFICATION; this ADR governs allowable effects regardless of which reviewed component performs the final write."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0012 — Connector outputs MUST land in `data/raw/` or `data/quarantine/` only

> **Proposed decision.** Source payloads captured by a connector may enter KFM only through a governed **RAW** or **QUARANTINE** handoff. Connector receipt candidates are separate process-memory outputs and may be persisted only through the governed receipt surface. Connectors do not own normalization, canonical records, registries, evidence, catalogs, graph projections, release decisions, publication, or public serving.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![ADR ID: confirmed](https://img.shields.io/badge/ADR--0012-confirmed-0969da?style=flat-square)](#current-repository-evidence)
[![Payload routes: RAW | QUARANTINE](https://img.shields.io/badge/payload%20routes-RAW%20%7C%20QUARANTINE-1f6feb?style=flat-square)](#decision)
[![Receipts: separate](https://img.shields.io/badge/receipts-separate%20process%20memory-8250df?style=flat-square)](#receipt-and-registry-boundaries)
[![Connector gate: partial](https://img.shields.io/badge/connector%20gate-partial-f59e0b?style=flat-square)](#current-enforcement-maturity)
[![Connector-run receipt: hold](https://img.shields.io/badge/connector--run%20receipt-WORKFLOW__HOLD-b42318?style=flat-square)](#current-enforcement-maturity)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#allowed-and-forbidden-effects)

> [!IMPORTANT]
> **Identity is confirmed; acceptance is not.** [`docs/adr/INDEX.md`](./INDEX.md) uniquely assigns `ADR-0012` to this exact file. Its source metadata is `draft`, which normalizes conservatively to effective status `proposed`. Editing, merging, or linking this ADR does not accept the decision.

<!-- callout-separator -->

> [!CAUTION]
> **A connector success is not source admission, evidence closure, or release.** A successful request, valid `SourceDescriptor` shape, checksum, RAW path, receipt, or passing static test proves only its bounded fact. Rights, sensitivity, source role, review, evidence, later lifecycle transitions, and release remain separate gates.

<!-- callout-separator -->

> [!WARNING]
> **The current repository is only partially enforcing this boundary.** The connector workflow combines a bounded static path suite with no-network tests for internal connector primitives, injected transport, `SourceAdapter`, retrieval-to-`SourceArtifact` handoff, and the repository-owned `IngestReceipt` validator. The static suite parses selected Python, shell, and YAML sinks and retains a legacy connector/pipeline publication-target canary. These checks do not prove complete dynamic, external, URI, sink, language, or source-family coverage; a concrete live transport; governed persistence; runtime confinement; connector-emitted receipt presence; source admission; release; or publication safety.

**Quick navigation:** [Status](#status) · [Evidence](#evidence-boundary) · [Context](#context) · [Decision](#decision) · [Rules](#normative-rules) · [Flow](#boundary-and-state-flow) · [Targets](#allowed-and-forbidden-effects) · [Paths](#path-and-identity-contract) · [Receipts](#receipt-and-registry-boundaries) · [Evidence snapshot](#current-repository-evidence) · [Maturity](#current-enforcement-maturity) · [Validation](#validation-and-enforcement-target) · [Consequences](#consequences) · [Alternatives](#alternatives-considered) · [Migration](#migration-and-graduation-plan) · [Acceptance](#acceptance-gates) · [Risks](#risk-ledger) · [Rollback](#rollback-and-supersession) · [Verification](#verification-checklist) · [References](#references)

---

<a id="status"></a>

## Status

| Field | Current value |
| --- | --- |
| **ADR ID** | `ADR-0012` — unique and confirmed in [`INDEX.md`](./INDEX.md) |
| **Tracked path** | `docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md` |
| **Source metadata** | `draft` |
| **Effective decision status** | `proposed` |
| **Decision class** | Source-edge lifecycle boundary and anti-publication invariant |
| **Current implementation posture** | Root boundaries documented; bounded static path checks; internal no-network connector primitives, injected transport, `SourceAdapter`, and `SourceArtifact` handoff; executable `IngestReceipt` validation; connector-run receipt persistence and runtime confinement held |
| **Implementation effect of this revision** | Documentation and evidence reconciliation only; no connector, validator, contract, schema, lifecycle object, source activation, release, or publication behavior changes |
| **Publication effect** | None |
| **Supersedes / superseded by** | None / none |

### Decision acceptance versus enforcement graduation

Two states remain separate:

1. **ADR acceptance** would approve this numbered source-edge boundary.
2. **Enforcement graduation** requires accepted source/activation semantics, a restricted write interface, deterministic fixtures, complete static and runtime checks, receipt validation, CI, correction, and rollback evidence.

An accepted ADR without enforcement is doctrine. A passing test without an accepted decision is bounded implementation evidence. Neither state alone proves source admission or public safety.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence Boundary

The v1.4 evidence snapshot pins current repository bytes at `main@52a6c7b55fc473c813bde6ec413bcda81259e809`. It preserves the historical v1.2/v1.3 lineage while replacing stale implementation claims with current inspected source, tests, validators, and workflows. Accepted ADR-0029 and its adopted Directory Rules bytes govern placement; ADR-0012 itself remains proposed.

| Evidence level | What is established | What is not established |
| --- | --- | --- |
| **Directory and lifecycle doctrine** | `connectors/` owns source-specific fetch/admission; `data/` owns lifecycle state; connectors are non-publishers | Full executable enforcement |
| **ADR inventory** | Exact ADR ID, filename, source metadata, and effective proposed status | Acceptance |
| **Root documentation** | Connector, RAW, QUARANTINE, registry, receipt, and ingest boundaries are documented | Exhaustive payload inventory or runtime conformance |
| **Contracts and schemas** | Fielded proposed `SourceDescriptor` and `IngestReceipt` shapes exist | Accepted authority, activation, or universal wiring |
| **Workflow and test source** | `connector-gate` runs bounded static path checks, connector-core no-network suites, and the `IngestReceipt` validator prerequisite | Dynamic effects, complete target coverage, connector-run receipt persistence, or source correctness |
| **Source-edge implementation** | Internal `connectors-core` primitives, injected transport, `SourceAdapter`, and retrieval-to-`SourceArtifact` handoff exist with deterministic tests | Concrete live transport, arbitrary persistence, source-specific adoption, or operational maturity |
| **Runtime and operations** | No admissible evidence reviewed here proves live connector runs, active sources, emitted receipts, deployment, or public use | Production maturity |

### Truth labels

| Label | Use in this ADR |
| --- | --- |
| **CONFIRMED** | Verified from current repository bytes, tests, workflows, or governing doctrine. |
| **PROPOSED** | Decision, path role, interface, migration, field, or future enforcement not accepted and proven. |
| **UNKNOWN** | Evidence is insufficient to support a stronger statement. |
| **NEEDS VERIFICATION** | A concrete check exists but is not closed. |
| **CONFLICTED** | Current repository sources assign incompatible names, paths, or writer responsibilities. |
| **HOLD** | A workflow or readiness gate intentionally refuses to claim the capability is implemented. |

[Back to top](#top)

---

<a id="context"></a>

## Context

KFM's lifecycle invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Connectors operate at the source edge. They may observe external state, retrieve or inspect source-native material, preserve source-head and integrity facts, and present a bounded capture candidate to the governed ingest boundary. They do not decide what becomes normalized truth, evidence, catalog state, a graph assertion, a release, a map layer, an API response, or an AI answer.

The source edge is unusually sensitive because connector material has not yet passed through the complete KFM chain:

- accepted source and activation review;
- record-level admission;
- normalization and semantic validation;
- rights and sensitivity policy;
- evidence assembly and citation validation;
- catalog and graph closure;
- accountable review and promotion;
- release, correction, withdrawal, and rollback.

A connector that can write directly to a later phase collapses those gates into transport code. A connector that can create or edit a source registry entry during a run can manufacture its own authority. A connector that can create release, proof, catalog, or public objects becomes a publisher by side effect.

### Drift patterns this ADR prevents

| Anti-pattern | Failure |
| --- | --- |
| **Connector publishes** | Connector or source-specific pipeline writes directly to `data/published/`, `release/`, or a public surface. |
| **Connector canonicalizes** | Source-specific fetch code writes normalized/canonical records into `data/work/` or `data/processed/`. |
| **Connector catalogs** | Fetch code emits STAC, DCAT, PROV, CatalogMatrix, or graph/triplet records as authoritative lifecycle outputs. |
| **Connector self-admits** | Connector run creates or edits its own authoritative `SourceDescriptor`, activation state, rights decision, or source-authority register entry. |
| **Receipt as exception tunnel** | A receipt output path becomes a general route for payloads, proofs, or release-shaped objects. |
| **Lifecycle skip** | RAW or QUARANTINE material reaches PUBLISHED without the governed transitions and their evidence. |
| **Hidden dynamic path** | Runtime string construction evades static forbidden-path tests. |
| **Admin upload bypass** | Restricted uploads land directly in WORK, PROCESSED, catalog, proofs, or published state. |

### In scope

- allowed direct connector effects;
- RAW and QUARANTINE payload landing;
- receipt and registry boundaries;
- source-native preservation;
- no-op, denial, hold, rate-limit, partial, and error outcomes;
- static and runtime enforcement requirements;
- migration and rollback posture.

### Out of scope

- field-level contract/schema revisions;
- final `SourceDescriptor` schema-home or singular/plural migration;
- final activation-state vocabulary;
- source-specific endpoint or rights approval;
- the exact module that owns filesystem persistence;
- normalization or downstream pipeline design;
- quarantine exit semantics beyond coordination with ADR-0021;
- release, public API, UI, map, and AI implementation.

[Back to top](#top)

---

<a id="decision"></a>

## Decision

**Once accepted, this ADR establishes the following rule:**

> A connector may cause source payload material to be persisted only in `data/raw/` or `data/quarantine/` through a governed, restricted sink. Receipt candidates are separate process-memory outputs and may be persisted only through the governed receipt surface. The connector has no authority to choose, write, mutate, or delete any later lifecycle, registry, proof, catalog, release, published, or public-client state.

### Core effect model

| Effect family | Allowed? | Required posture |
| --- | ---: | --- |
| RAW capture candidate | Yes | Source-native, immutable, descriptor/activation resolved, digest-pinned |
| QUARANTINE capture candidate | Yes | Fail-closed hold with structured reason and reviewer route |
| Ingest/connector receipt candidate | Yes, separately | Append-only receipt sink; no payload bytes; process memory only |
| No-op / deny / hold / rate-limit / error result | Yes | Finite safe result; no false success or payload promotion |
| Registry mutation | No | Steward-reviewed registry workflow only |
| WORK / PROCESSED write | No | Downstream pipeline responsibility |
| Catalog / triplet / proof write | No | Owning catalog/graph/proof stages only |
| Release / published write | No | Release and publication authority only |
| Public API/UI/map/export/AI write or response | No | Governed downstream interfaces only |

### Writer ownership is implementation-specific; effects are not

Current repository documentation records a producer/writer handoff conflict between connector-owned RAW/QUARANTINE writes and a possible shared ingest writer. This ADR does not settle that module boundary.

Either reviewed implementation profile may conform:

1. **Restricted connector sink:** connector receives injected `write_raw`, `write_quarantine`, and receipt-candidate interfaces that physically persist only allowed effects.
2. **Orchestrator-owned persistence:** connector returns an immutable candidate bundle; a governed ingest orchestrator validates and persists it to RAW, QUARANTINE, and receipts.

In both profiles:

- source-specific code cannot name arbitrary repository paths;
- the allowed sink set is closed;
- payload and receipt families remain separate;
- later lifecycle and public effects are impossible from the connector interface;
- the persisted result and receipt must identify the actual writer and connector.

### One landing disposition per payload-bearing run

A payload-bearing `run_id` must have one lifecycle landing disposition:

- **RAW** when immediate capture prerequisites pass; or
- **QUARANTINE** when any prerequisite is unresolved, partial, conflicted, invalid, unsafe, or unclassifiable.

A `PARTIAL` ingest outcome defaults to QUARANTINE. Partitioning one external invocation into separately landed child captures is allowed only when each child is assigned an independent stable `run_id`, digest set, receipt, and disposition. One `run_id` must not split payload bytes between RAW and QUARANTINE.

A connector invocation may produce no lifecycle payload when the result is no-op, deny, hold, rate-limited, or error. That outcome still requires bounded process memory when repository policy requires a receipt.

[Back to top](#top)

---

<a id="normative-rules"></a>

## Normative Rules

Conformance language uses RFC 2119-style **MUST**, **MUST NOT**, **SHOULD**, and **MAY**. While this ADR remains proposed, these are proposed acceptance rules; Directory Rules remain the governing source-edge authority.

### MUST

1. Connector source payloads **MUST** land only under one of:

   ```text
   data/raw/<domain>/<source_id>/<run_id>/
   data/quarantine/<domain>/<reason>/<run_id>/
   ```

2. Every payload-bearing run **MUST** choose exactly one landing disposition.
3. The connector **MUST** receive or resolve a current source identity and activation context before live capture, except for an explicitly bounded metadata-only probe that cannot persist source payloads.
4. The persisted capture **MUST** preserve:
   - source identity and source-native identifiers;
   - connector identity and version/ref;
   - operation/request identity;
   - source head or documented not-applicable reason;
   - retrieval and observed times;
   - byte count and content digests;
   - media/package metadata required for replay;
   - landing disposition and safe reason state.
5. Captured payload bytes **MUST** remain source-native except for transport-preserving handling such as chunk assembly, archive preservation, or decompression explicitly described by the source profile and receipt.
6. Every capture **MUST** bind to an `IngestReceipt` candidate or accepted successor receipt family.
7. A quarantine landing **MUST** carry a structured hold reason or resolvable quarantine-case reference.
8. Writes **MUST** be append-only and collision-safe. Replays, corrections, and source refreshes create new records or supersession links rather than silently editing prior capture.
9. Unknown or unclassifiable path, rights, sensitivity, source identity, schema, integrity, or source-head state **MUST** fail closed to QUARANTINE, HOLD, DENY, or ERROR as applicable.
10. Restricted admin/local uploads **MUST** traverse the same source-admission boundary. Operator privilege does not grant a later lifecycle shortcut.

### MUST NOT

A connector or connector-owned runtime **MUST NOT**:

1. write payloads to `data/pre_raw/`, `data/work/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/proofs/`, `data/registry/`, `data/published/`, `data/rollback/`, `release/`, or any other repository target outside the allowed RAW, QUARANTINE, and receipt roots;
2. create authoritative `SourceDescriptor`, source-activation, rights, sensitivity, registry, policy, review, or release records during a capture run;
3. normalize source fields into canonical fields;
4. join records across source files into a KFM domain object;
5. infer claims, source authority, public safety, or release readiness;
6. emit STAC, DCAT, PROV, CatalogMatrix, EvidenceBundle, ProofPack, LayerManifest, ReleaseManifest, PromotionDecision, RollbackCard, or CorrectionNotice as authoritative outputs;
7. mutate or delete existing lifecycle, receipt, registry, proof, catalog, or release records;
8. write code, configuration, contracts, schemas, policy, tests, fixtures, documentation, or workflow files as a side effect of source execution;
9. serve or return source payloads directly to normal public API, UI, MapLibre, Focus Mode, export, search, graph, vector-index, or AI surfaces;
10. hide a partial, denied, held, rate-limited, or failed operation behind `SUCCESS`;
11. store credentials, tokens, secrets, protected URLs, private review notes, or sensitive source values in receipt/public reason strings;
12. use a central receipt path as a payload or general artifact sink.

### SHOULD

A connector **SHOULD**:

- be deterministic and no-network by default in tests;
- accept injected transport, clock, filesystem/sink, sleeper, and randomness dependencies;
- enforce request, byte, record, page, retry, deadline, and cancellation limits;
- preserve ETag, Last-Modified, version, revision, source checksum, or another source-head signal;
- report pagination/truncation/completeness state;
- use stable safe reason-code families;
- emit bounded diagnostics that do not disclose protected material;
- support replay without duplicating prior capture identity;
- distinguish source facts from KFM policy decisions;
- preserve correction and supersession references.

[Back to top](#top)

---

<a id="boundary-and-state-flow"></a>

## Boundary and State Flow

```mermaid
flowchart LR
    EXT["External source or supplied input"]
    ACT["Resolved SourceDescriptor + activation/review context"]
    CONN["Source-specific connector"]
    SINK{"Restricted governed sink"}
    RAW["data/raw/<domain>/<source_id>/<run_id>/"]
    QUAR["data/quarantine/<domain>/<reason>/<run_id>/"]
    REC["data/receipts/ingest/<run_id>/ or accepted receipt home"]
    PIPE["pipelines/ or governed ingest transition"]
    LATER["WORK -> PROCESSED -> CATALOG/TRIPLET -> RELEASE -> PUBLISHED"]
    PUB["Governed API / approved static delivery / UI / MapLibre / AI"]

    EXT --> CONN
    ACT --> CONN
    CONN --> SINK
    SINK -->|capture passed immediate prerequisites| RAW
    SINK -->|held, partial, unsafe, unresolved, invalid| QUAR
    SINK -->|process memory only| REC
    RAW --> PIPE
    QUAR -->|structured exit only| PIPE
    PIPE --> LATER
    LATER --> PUB

    CONN -. forbidden .-> LATER
    CONN -. forbidden .-> PUB
```

The sink edge may be implemented inside a connector runtime or a shared ingest orchestrator. The authority boundary is the same: connector-controlled effects end at RAW, QUARANTINE, and receipt process memory.

### Finite source-edge outcomes

| Outcome class | Meaning | Payload effect |
| --- | --- | --- |
| `RAW_CANDIDATE` | Capture completed and immediate source-edge prerequisites passed | One immutable RAW landing |
| `QUARANTINE_CANDIDATE` | Capture exists but a hold condition applies | One immutable QUARANTINE landing |
| `NO_CHANGE` | Source-head observation indicates no new capture is needed | No payload; receipt/no-op record as required |
| `DENY` | Source/action is not permitted | No payload except a governed minimal denial/attempt receipt where allowed |
| `HOLD` / `REVIEW_REQUIRED` | Prerequisite or review is unresolved before capture | No payload, or QUARANTINE only when preserved material is policy-allowed |
| `RATE_LIMITED` / `RETRYABLE` | Bounded retry may be allowed | No false success; partial state disposed safely |
| `ERROR` | Operation or governance machinery failed | No false RAW success; cleanup/replay instructions recorded safely |

This vocabulary is an operational profile, not a new canonical enum. Exact machine terms remain **PROPOSED / NEEDS VERIFICATION** and must align with accepted contracts.

[Back to top](#top)

---

<a id="allowed-and-forbidden-effects"></a>

## Allowed and Forbidden Effects

| Surface | Connector effect | Boundary |
| --- | ---: | --- |
| `data/raw/` | **Allowed through governed sink** | Source capture only; no normalization or public access |
| `data/quarantine/` | **Allowed through governed sink** | Held capture and local hold sidecars only |
| `data/receipts/` | **Allowed for receipt candidate through governed writer** | Process memory only; no payload bytes or proof/release implication |
| `data/registry/` | **Read only** | Registry/steward workflow owns authoritative records |
| `data/work/` | **Forbidden** | Normalization/candidate transformation |
| `data/processed/` | **Forbidden** | Validated domain objects |
| `data/catalog/` | **Forbidden** | STAC/DCAT/PROV/domain catalog stage |
| `data/triplets/` | **Forbidden** | Graph/relationship projection |
| `data/proofs/` | **Forbidden** | Evidence/proof support |
| `data/published/` | **Forbidden** | Released public-safe carriers |
| `data/rollback/` | **Forbidden** | Rollback data-plane records |
| `release/` | **Forbidden** | Release-governance decisions and manifests |
| `contracts/`, `schemas/`, `policy/` | **Read only / forbidden mutation** | Meaning, shape, and admissibility authorities |
| `docs/`, `tests/`, `fixtures/`, `.github/` | **Forbidden runtime mutation** | Source runs do not edit the repository |
| public apps and delivery surfaces | **Forbidden direct access or serving** | Governed downstream interfaces only |

> [!NOTE]
> A connector may generate an in-memory or temporary candidate object for its caller. Temporary execution state must be bounded, cleaned up, non-authoritative, and incapable of bypassing the governed sink.

[Back to top](#top)

---

<a id="path-and-identity-contract"></a>

## Path and Identity Contract

### RAW target pattern

```text
data/raw/
└── <domain>/
    └── <source_id>/
        └── <run_id>/
            ├── capture_manifest.json      # PROPOSED local sidecar
            ├── source_head.json           # PROPOSED local observation
            ├── checksums.sha256
            ├── receipt_ref.json           # pointer, not receipt authority
            └── payload/
```

### QUARANTINE target pattern

```text
data/quarantine/
└── <domain>/
    └── <reason>/
        └── <run_id>/
            ├── capture_manifest.json
            ├── source_head.json
            ├── checksums.sha256
            ├── receipt_ref.json
            ├── quarantine_case_ref.json   # or accepted structured hold record
            └── payload/
```

The exact sidecar filenames are **PROPOSED**. The required semantics are:

- payload and payload-local capture metadata remain together;
- authoritative source, receipt, policy, proof, and release records stay in their owning homes;
- pointers are stable and resolvable;
- duplication does not create parallel authority.

### Identifier responsibilities

| Identifier | Responsibility |
| --- | --- |
| `source_id` | Resolves the admitted source identity; connector does not mint authority by successful fetch |
| `run_id` | Identifies one connector/ingest attempt and one payload landing disposition |
| `receipt_id` | Identifies the authoritative process-memory record |
| source-head identity | ETag, Last-Modified, upstream version/revision, manifest digest, or accepted alternative |
| payload digest | Pins every persisted payload object |
| supersession/correction ref | Connects refreshes or corrections without mutation |

`run_id` grammar remains governed by ADR-0013 or an accepted successor. This ADR requires stable uniqueness, collision safety, traceability, and replay semantics without selecting a final format.

### Quarantine reasons

The repository already documents broad hold classes. The following route families remain **PROPOSED** pending a controlled vocabulary:

- `source_identity`
- `activation`
- `rights`
- `sensitivity`
- `schema_drift`
- `integrity`
- `geometry_precision`
- `partial_capture`
- `completeness`
- `rate_limit`
- `unclassified`

Reason strings exposed outside reviewer surfaces must be safe and must not reveal protected content, credentials, private endpoints, precise sensitive locations, or security details.

[Back to top](#top)

---

<a id="receipt-and-registry-boundaries"></a>

## Receipt and Registry Boundaries

### SourceDescriptor

A `SourceDescriptor` is source identity and treatment authority. Current repository evidence places descriptor instances under the source registry and gives connectors read access to admitted records.

Therefore:

- a connector run **MUST resolve** a descriptor or accepted activation context before live capture;
- a connector **MUST NOT create or update** the authoritative registry record as a side effect;
- connector preflight MAY emit a **candidate proposal** for steward review outside the live capture path;
- a RAW/QUARANTINE folder SHOULD carry a stable descriptor reference and descriptor version/digest, not an independently editable authoritative descriptor copy;
- an optional frozen snapshot is a non-authoritative audit sidecar unless an accepted contract explicitly promotes it.

The current singular `SourceDescriptor` schema is fielded and closed but declares the plural schema path as canonical, while the source-authority machine register is empty. That is a repository conflict, not permission to pick a new authority in this ADR.

### IngestReceipt

The current proposed `IngestReceipt` schema requires:

- `id`;
- `source_id`;
- `run_id`;
- `started_at`;
- `finished_at`;
- `outcome: SUCCESS | PARTIAL | FAIL`;
- `bytes_in`;
- one or more SHA-256 digests;
- no additional properties.

The contract defines it as source-capture process memory, not source truth, evidence closure, policy permission, release approval, or public access.

This ADR therefore proposes:

1. authoritative receipt persistence under `data/receipts/ingest/` or the accepted receipt-family equivalent;
2. an append-only governed receipt writer;
3. a run-local `receipt_ref` pointer rather than a second editable authority copy;
4. a future receipt/profile extension or companion record for:
   - landing disposition;
   - source-head identity;
   - connector identity/version;
   - capture manifest ref;
   - quarantine case ref;
   - completeness/truncation state;
   - correction/supersession refs.

Those fields are **PROPOSED** and require coordinated contract, schema, fixture, validator, and migration review.

### Capture manifest

A payload-local capture manifest is operational metadata, not a release manifest. It may enumerate:

- relative payload paths;
- byte counts;
- media/archive types;
- SHA-256 digests;
- upstream/source-native identifiers;
- source-head observation;
- receipt and descriptor refs;
- landing disposition.

It must not carry policy approval, evidence closure, release state, or public permission.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current Repository Evidence

| Surface | CONFIRMED current state | Safe conclusion |
| --- | --- | --- |
| [`INDEX.md`](./INDEX.md) | ADR-0012 is uniquely tracked; source metadata `draft`, effective status `proposed` | Identity resolved; decision not accepted |
| [ADR-0029](./ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules](../doctrine/directory-rules.md) | ADR-0029 is accepted and adopts the pinned Directory Rules bytes as top-level placement authority | Placement is authoritative; this proposed connector decision is not thereby accepted |
| [`connectors/README.md`](../../connectors/README.md) | v0.7 inventory records 104 direct connector directories, the RAW/QUARANTINE payload boundary, separate receipt candidates, and mixed implementation maturity | Root boundary exists; inventory does not prove every connector's runtime effects |
| [`data/raw/README.md`](../../data/raw/README.md) | RAW no-public-path root with many documented domain lanes | Path/readme evidence, not payload or source-admission proof |
| [`data/quarantine/README.md`](../../data/quarantine/README.md) | Fail-closed hold root with documented domain lanes and exit burdens | Quarantine semantics documented; automation incomplete |
| [`data/registry/sources/README.md`](../../data/registry/sources/README.md) | SourceDescriptor authority surface documented; specific implementation bundle remains proposed | Connector does not own registry authority |
| Source authority register | Register is proposed and contains no entries at the inspected snapshot | No active source inventory or connector authorization is established by that register |
| [`pipelines/ingest/README.md`](../../pipelines/ingest/README.md) | Direct lane is documentation-only; connector/shared-ingest writer handoff conflicted | Do not infer shared ingest runtime |
| [`connector-gate.yml`](../../.github/workflows/connector-gate.yml) | Runs bounded static path checks; deterministic no-network connector-core, injected-transport, `SourceAdapter`, and artifact-handoff tests; and focused `IngestReceipt` validator polarity, while a second job records an explicit connector-run receipt hold | Multiple prerequisites are executable; connector-run receipt presence and governed persistence are not |
| [`output_paths.py`](../../tools/validators/connector_gate/output_paths.py) and [`test_pipeline_connector_non_publisher.py`](../../tests/policy/test_pipeline_connector_non_publisher.py) | Scan selected Python, shell, and YAML connector targets, fail closed for selected unresolved targets, deny symlink sources, require a nonempty source inventory, and preserve the legacy connector/pipeline publication-target canary | Bounded repository-source analysis does not prove complete dynamic/external/URI coverage, every language or sink, indirect effects, or runtime confinement |
| [`packages/connectors-core`](../../packages/connectors-core/README.md) | Internal `0.0.1` no-network package supplies deterministic primitives and caller-injected transport; it has no stable root export or concrete live transport | Bounded source-edge code exists without storage, source, lifecycle, release, or publication authority |
| [`SourceAdapter`](../../packages/connectors-core/src/connectors_core/source_adapter.py) and [`artifact_handoff.py`](../../packages/connectors-core/src/connectors_core/artifact_handoff.py) | Define a source adapter boundary and transform exact successful retrieval bytes into a proposed `SourceArtifact` candidate under deterministic tests | Candidate construction is not source admission, persistence, lifecycle promotion, or a live connector run |
| `SourceArtifact` contract/schema/validator/workflow | Proposed exact-byte artifact surfaces and validator wiring exist | Valid shape does not authorize a source, choose RAW versus QUARANTINE, persist bytes, or release anything |
| `SourceDescriptor` schema | Fielded, closed, status proposed; singular/plural path metadata conflicted | Machine-shape candidate, not accepted activation |
| [`IngestReceipt` contract](../../contracts/source/ingest_receipt.md), schema, validator, and tests | Proposed closed shape has a repository validator, valid/invalid fixtures, aggregate-profile registration, and focused CI prerequisite checks | No connector-emitted receipt instance, run correspondence, accepted writer, or governed persistence is established |
| Live runs and operations | Not established | No claims about active sources, emitted payloads, production consumers, or public delivery |

### Material corrections from v1.3

- The connector-core package is no longer placeholder-only: bounded no-network primitives, injected transport, `SourceAdapter`, and exact-byte artifact handoff now exist and are tested.
- The connector workflow now combines the static path suite with connector-core tests and a focused `IngestReceipt` validator prerequisite.
- The repository-owned `IngestReceipt` validator and polarity fixtures exist; the current hold is connector-run receipt presence, correspondence, accepted writing, and persistence.
- Proposed `SourceArtifact` contract, schema, validator, and workflow surfaces now exist.
- Static enforcement has deepened, including selected fail-closed unresolved-target handling and symlink-source denial, but remains bounded repository-source analysis rather than runtime confinement.
- Receipt output is a separate allowed family; payload bytes remain RAW/QUARANTINE only.
- The shared connector-versus-ingest writer is unresolved and must not be invented by documentation.
- Accepted ADR-0029 settles top-level placement authority; it does not change ADR-0012 from `draft` / effective `proposed`, activate a source, or grant publication authority.

[Back to top](#top)

---

<a id="current-enforcement-maturity"></a>

## Current Enforcement Maturity

| Level | State | Current result |
| --- | --- | --- |
| **M0 — doctrine stated** | Directory Rules and root READMEs state non-publisher boundary | **CONFIRMED** |
| **M1 — ADR proposed** | Numbered decision under review | **CURRENT** |
| **M2 — bounded static guard** | Selected connector repository targets and legacy connector/pipeline lexical publication-target contexts are tested with deterministic positive/negative cases | **PARTIAL / CONFIRMED** |
| **M3 — no-network source-edge boundary** | Internal primitives, caller-injected transport, `SourceAdapter`, and exact-byte `SourceArtifact` handoff are deterministically tested | **BOUNDED / CONFIRMED** |
| **M4 — full static path coverage** | All forbidden roots, languages, configuration forms, wrappers, and indirect writes checked | **HOLD** |
| **M5 — restricted sink and persistence** | Connector cannot express arbitrary storage or later lifecycle/public effects; accepted writer persists only governed candidates | **NOT ESTABLISHED** |
| **M6 — artifact and receipt validation** | `SourceArtifact` and `IngestReceipt` validators and polarity fixtures exist; connector-run receipt presence, correspondence, and persistence do not | **PARTIAL / WORKFLOW_HOLD** |
| **M7 — activation/rights/sensitivity binding** | Connector run resolves accepted source decision and obligations | **NOT ESTABLISHED** |
| **M8 — runtime side-effect proof** | Tests observe actual writes, mutation denial, cleanup, replay, and sink confinement | **NOT ESTABLISHED** |
| **M9 — required-check and operational evidence** | Required rules, representative active connectors, retained runs, and drift monitoring demonstrate enforcement | **NEEDS VERIFICATION / UNKNOWN** |

A green M2, M3, or M6 prerequisite must not be described as later enforcement maturity, source admission, or publication safety.

[Back to top](#top)

---

<a id="validation-and-enforcement-target"></a>

## Validation and Enforcement Target

### Static guard

The current test denies recognized connector repository writes outside:

```text
data/raw/
data/quarantine/
data/receipts/
```

The bounded implementation uses Python AST analysis, deterministic literal/path-composition resolution, traversal checks, selected shell destinations, and selected YAML command/output keys. Selected recognized unresolved targets and commands fail closed, and inline positive/negative canaries plus a nonempty path-filtered connector source inventory prevent a vacuous pass. That inventory excludes path components named `test`, `tests`, `fixture`, `fixtures`, `example`, or `examples`. This remains a repository-path subset, not full DIR-PLACE-003 runtime enforcement.

M4 remains held. Further coverage must address every language and configuration form used by active connectors, wrapper and indirect writes, destination symlinks and filesystem indirection, subprocess variation, object stores, databases, network-side persistence, and repository-root resolution. Static scanning remains defense in depth, not runtime proof or receipt-correspondence validation.

### No-network source-edge prerequisites

The internal connector-core package now supplies a bounded, deterministic source-edge seam:

- `core.py` provides pure connector primitives without storage or network authority;
- the transport facade accepts caller-injected transport and provides no concrete live network client;
- `SourceAdapter` defines the adapter protocol and value objects without activating a source;
- `artifact_handoff.py` converts exact bytes from a successful retrieval into a proposed `SourceArtifact` candidate without persisting it or advancing lifecycle state;
- the `SourceArtifact` validator checks the proposed exact-byte contract surface; and
- the `IngestReceipt` validator checks the proposed receipt shape and local bindings exercised by its fixtures and focused workflow prerequisite.

These are useful implementation prerequisites. They do not establish a source-specific run, accepted source admission, RAW/QUARANTINE disposition, governed storage, connector-emitted receipt correspondence, or any downstream/public effect.

### Restricted sink tests

A future sink contract should prove:

- only RAW, QUARANTINE, and receipt-candidate methods exist;
- arbitrary path strings are rejected;
- traversal and symlink escape fail closed;
- one run has one landing disposition;
- payload hashes cover every persisted object;
- receipt ref matches source/run/digests;
- prior runs cannot be mutated;
- partial writes are cleaned, held, or quarantined;
- concurrent retries remain collision-safe;
- sensitive diagnostics are redacted.

### Minimum deterministic fixture matrix

| Fixture | Expected result |
| --- | --- |
| Valid RAW capture | RAW candidate + receipt candidate |
| Rights unresolved | QUARANTINE or pre-capture HOLD |
| Sensitivity unresolved | QUARANTINE or pre-capture HOLD |
| Partial capture | QUARANTINE + `PARTIAL` receipt |
| No source change | No payload + no-op receipt |
| Rate limited | No false success; bounded retry result |
| Connector writes WORK | DENY |
| Connector writes PROCESSED | DENY |
| Connector writes CATALOG | DENY |
| Connector writes TRIPLETS | DENY |
| Connector writes PROOFS | DENY |
| Connector writes PUBLISHED | DENY |
| Connector writes RELEASE | DENY |
| Connector mutates registry | DENY |
| Connector mutates prior RAW | DENY |
| Missing or mismatched digest | DENY / QUARANTINE |
| Missing receipt | DENY / HOLD |
| Split RAW and QUARANTINE for one run | DENY |
| Dynamic traversal/symlink escape | DENY |
| Validator unavailable | ERROR |
| Protected detail in reason/log | DENY or redacted failure |

### Report boundary

A mature connector gate report should include:

- validator/profile identity and digest;
- connector/source/run IDs;
- operation and source-head identity;
- requested and actual effect set;
- landing path and classification;
- receipt and capture-manifest refs;
- forbidden effects;
- digest and byte coverage;
- mutation/traversal findings;
- finite decision and safe reason codes;
- policy/activation dependency refs;
- correction/rollback implications.

The report validates a bounded run. It does not admit a source, prove claims, approve policy, or release data.

[Back to top](#top)

---

## Consequences

### Positive

- Connectors cannot silently become normalization, proof, catalog, release, or public-serving systems.
- RAW and QUARANTINE remain auditable first lifecycle states.
- Receipt process memory is preserved without becoming a payload exception tunnel.
- Source registry authority stays separate from source execution.
- Partial, unsafe, or ambiguous captures fail closed.
- Connector implementations can vary while sharing one effect contract.
- Downstream pipelines receive digest-pinned, source-role-visible capture units.
- Static and runtime enforcement can be built against a precise target.

### Costs and tradeoffs

- Existing fetch-and-normalize implementations may need separation.
- A restricted sink and orchestrator contract add implementation work.
- Receipt and capture-manifest profiles need coordinated schema/fixture/validator changes.
- Exactly-one landing disposition is stricter than convenience-oriented partial persistence.
- Active source onboarding requires more review and fixture work.
- Complete enforcement must handle multiple languages, dynamic paths, archives, retries, and partial failures.
- Registry and schema naming conflicts remain separate governance work.

### Neutral consequences

- This ADR does not decide which component physically writes the files.
- A high-authority upstream source still passes the same source-edge lifecycle boundary.
- QUARANTINE is a correct governed outcome, not an implementation failure.
- RAW capture does not imply downstream retention, truth, or publication.

[Back to top](#top)

---

## Alternatives Considered

| Alternative | Disposition | Reason |
| --- | --- | --- |
| Allow connectors to write WORK | Rejected | Collapses fetch/admission with normalization |
| Allow trusted sources to write PROCESSED | Rejected | Source authority does not replace validation, policy, or lifecycle gates |
| Allow direct catalog emission | Rejected | Catalog closure is downstream and cannot be source transport authority |
| Allow connector-owned registry updates | Rejected | Connector would manufacture its own source authority |
| Store authoritative receipt beside RAW only | Rejected | Creates receipt authority inside payload lane; canonical receipt family remains separate |
| Allow split RAW/QUARANTINE per run | Rejected by default | Weakens atomic replay and correction; use independent child runs |
| Add `data/staging/` | Rejected in this ADR | Adds a lifecycle phase and requires a separate decision |
| Rely only on code review | Rejected | Cannot provide deterministic or runtime enforcement |
| Require shared ingest pipeline to be sole writer now | Deferred | Current lane is documentation-only; implementation evidence is insufficient |
| Require connector to be sole writer now | Deferred | Effect boundary is decidable without selecting module ownership |
| Allow direct public streaming for ephemeral feeds | Rejected | Normal public path still requires governed interfaces and release/safety state |
| Treat receipt success as admission | Rejected | Receipt is process memory, not authority |

[Back to top](#top)

---

<a id="migration-and-graduation-plan"></a>

## Migration and Graduation Plan

This document performs no migration. Follow-on work should use the smallest reversible sequence.

### Wave 0 — inventory and claim

1. Enumerate active connector implementations, languages, declared outputs, runtime callers, and tests.
2. Inventory direct and dynamic write effects across `connectors/`, source-specific pipelines, worker code, and upload paths.
3. Inventory source descriptors, activation records, receipt instances, and registry references.
4. Record current violations in the drift register without moving bytes.
5. Claim exact paths before implementation to avoid concurrent repairs.

### Wave 1 — semantic handoff contract

1. Reconcile ADR-0012 with ADR-0017 and ADR-0021.
2. Choose the connector/orchestrator writer profile.
3. Define capture candidate, landing disposition, receipt ref, and quarantine-case semantics.
4. Decide whether `IngestReceipt` is extended or paired with a companion capture record.
5. Resolve source schema singular/plural authority separately through ADR-0001-compatible migration.

### Wave 2 — deterministic fixtures and validators

1. Add public-safe valid/invalid fixtures for every outcome and forbidden effect.
2. Retain the repository-owned `IngestReceipt` validator prerequisite and add deterministic connector-run instances that prove receipt presence, correspondence, and governed persistence.
3. Expand static non-publisher coverage.
4. Add restricted sink unit and integration tests.
5. Keep all tests no-network by default.

### Wave 3 — advisory runtime integration

1. Introduce restricted sink/orchestrator interfaces without moving existing output behavior silently.
2. Run advisory comparisons against current connectors.
3. Emit mismatch reports and migration candidates.
4. Preserve existing paths until each source family has a rollback-tested migration.

### Wave 4 — source-family migrations

For each source family:

1. split fetch/admit from normalization and downstream processing;
2. bind current descriptor and activation context;
3. route payload to one RAW or QUARANTINE run;
4. emit/persist the receipt through the accepted writer;
5. repair references and consumers;
6. add correction/replay tests;
7. retain a reversible compatibility window where needed.

### Wave 5 — fail-closed CI

1. Enable complete path/effect checks for migrated connectors.
2. Promote the receipt job from explicit hold only after actual connector-run presence, correspondence, and governed-persistence cases pass.
3. Verify required-check compatibility and ownership.
4. Keep unmigrated families visible as scoped holds rather than blanket exceptions.

### Wave 6 — operational verification

1. Retain safe run evidence and metrics.
2. Confirm no direct later-stage/public effects.
3. Exercise correction, replay, quarantine, and source retirement.
4. Monitor drift and expiration of compatibility paths.
5. Close the migration only after downstream references and rollback are verified.

### Migration receipt minimum

Every source-family migration should record:

- migration ID and source family;
- prior and new writer paths;
- affected connectors and consumers;
- prior and new receipt/capture identities;
- digest equivalence or intentional transformation;
- tests and workflow evidence;
- compatibility window and expiry;
- rollback target;
- correction/public impact;
- reviewer and decision refs.

[Back to top](#top)

---

<a id="acceptance-gates"></a>

## Acceptance Gates

ADR acceptance and enforcement graduation should require review of these gates.

| Gate | Requirement |
| --- | --- |
| **A1 — identity** | ADR, filename, index row, status, and owners/review burden are coherent |
| **A2 — boundary** | Payload versus receipt versus registry effects are unambiguous |
| **A3 — source admission** | ADR-0017 coordination defines required descriptor/activation context |
| **A4 — quarantine** | ADR-0021 coordination defines held state and structured exit refs |
| **A5 — writer profile** | Connector/orchestrator effect ownership is selected or intentionally deferred with implementable interface |
| **A6 — path profile** | RAW/QUARANTINE patterns and one-disposition rule are accepted |
| **A7 — receipt semantics** | Ingest receipt/capture companion fields and canonical home are resolved |
| **A8 — registry authority** | Connector cannot mutate authoritative source records |
| **A9 — static enforcement** | Every relevant forbidden path/language/config form is covered |
| **A10 — runtime enforcement** | Restricted sink, traversal, mutation, partial-write, retry, and concurrency tests pass |
| **A11 — fixtures** | Valid, invalid, denied, held, partial, no-op, retry, and error cases are deterministic and safe |
| **A12 — policy/security** | Rights, sensitivity, credentials, resource limits, and diagnostic redaction fail closed |
| **A13 — correction/replay** | Refresh, supersession, correction, and replay preserve prior identity |
| **A14 — public boundary** | Public clients cannot invoke connectors or read RAW/QUARANTINE/receipt state directly |
| **A15 — CI/review** | Required checks, ownership, and exception process are verified |
| **A16 — migration/rollback** | Current violations are inventoried with reversible per-family plans |
| **A17 — evidence** | One representative source family demonstrates the complete source-edge boundary without claiming release |

No gate is satisfied merely because this ADR, a README, schema, workflow, pull request, or merge exists.

[Back to top](#top)

---

<a id="risk-ledger"></a>

## Risk Ledger

| Risk | Current posture | Control |
| --- | --- | --- |
| Static test misses dynamic writes | CONFIRMED risk | Restricted sink + runtime side-effect tests |
| Receipt path becomes payload tunnel | Open | Typed/closed receipt writer and payload-size/content denial |
| Connector self-registers source | Open | Registry write denial and activation dependency |
| Partial capture silently marked success | Open | `PARTIAL` semantics, QUARANTINE default, receipt polarity tests |
| One run splits RAW/QUARANTINE | Open | Atomic disposition validator |
| Archive extraction changes source meaning | Open | Preserve source package; record transport handling |
| Symlink/path traversal escapes root | Open | Canonical path resolution and escape tests |
| Admin upload bypass | Open | Treat uploads as source-admission operations |
| Rights/sensitivity checked after capture only | Open | Preflight HOLD/DENY plus QUARANTINE when preservation is allowed |
| Secrets leak into receipts/logs | Open | Safe diagnostics and secret-pattern tests |
| Connector gate README/workflow drift | CONFIRMED documentation drift | Reconcile docs with current command-bearing workflow |
| Singular/plural source-schema authority | CONFIRMED conflict | Separate ADR-0001-compatible migration |
| Source authority register empty | CONFIRMED gap | Do not infer active source inventory |
| Shared ingest lane becomes shadow authority | Open | Named consumers, accepted handoff contract, no convenience centralization |
| Later pipeline writes public directly | Outside connector scope but material | Separate pipeline/release gates and non-publisher tests |
| Repository-side automation merges draft PRs | NEEDS VERIFICATION operational risk | Do not treat merge as ADR acceptance or review evidence |

[Back to top](#top)

---

<a id="rollback-and-supersession"></a>

## Rollback and Supersession

### Documentation rollback

Before merge, close the draft PR and abandon the scoped branch.

After merge, restore the immediate v1.3 preimage:

```text
2cf9e082d403a5e4294ed0b845e58edc687f0c8b
```

or use a focused reviewed revert of this batch. Historical v1.2 blob `c7b1027dc9d25ff6bf886a7a2e2162f8fb2516be` and v1.1 blob `e323ce42e82bdf93252fa0bd68bd86e3b7eedebf` remain lineage evidence, not immediate rollback targets.

### Decision rollback

If ADR-0012 is rejected:

1. retain the file with `status: rejected`;
2. keep Directory Rules enforcement in force;
3. remove only ADR-specific acceptance messaging;
4. do not weaken existing static protections.

If superseded:

1. retain this record;
2. set `status: superseded`;
3. link the accepted successor in both directions;
4. update the index in the same reviewed change;
5. preserve migration and rollback evidence.

### Implementation rollback

Every connector, sink, validator, workflow, schema, receipt, or migration follow-on must identify its own rollback.

Rollback may include:

- restore prior connector/orchestrator writer;
- re-enable a bounded read-only compatibility pointer;
- revert a source-family migration;
- return a gate to advisory mode when a validator defect is demonstrated;
- quarantine newly emitted material;
- invalidate or supersede incorrect receipts;
- correct affected downstream references;
- retain drift entries until remediation is verified.

Do not force-push or delete prior capture, receipt, review, or correction history.

[Back to top](#top)

---

<a id="verification-checklist"></a>

## Verification Checklist

- [x] ADR ID and tracked path confirmed.
- [x] Source metadata `draft` and effective `proposed` status confirmed.
- [x] Current connector, RAW, QUARANTINE, registry, receipt, ingest, workflow, test, and validator documentation inspected.
- [x] Current bounded static enforcement identified.
- [x] Internal connector primitives, injected transport, `SourceAdapter`, and exact-byte artifact handoff inspected.
- [x] `SourceArtifact` and `IngestReceipt` validators and focused workflow prerequisites inspected.
- [x] Current connector-run receipt presence and persistence hold identified.
- [x] `SourceDescriptor` and `IngestReceipt` shapes inspected.
- [x] SourceDescriptor registry authority separated from connector run output.
- [x] Receipt output separated from payload landing.
- [x] Shared connector/ingest writer conflict surfaced rather than silently resolved.
- [x] Existing decision, consequences, alternatives, migration intent, reviewer checklist, and rollback posture preserved.
- [ ] Confirm active connector inventory recursively.
- [ ] Confirm source authority/activation records and accepted vocabulary.
- [ ] Confirm writer ownership and restricted sink contract.
- [ ] Confirm central ingest receipt persistence and consumers.
- [ ] Confirm complete static and runtime forbidden-effect coverage.
- [ ] Confirm quarantine-case record shape and reason vocabulary.
- [ ] Confirm source-schema singular/plural migration.
- [ ] Confirm connector-run receipt presence, correspondence, and governed-persistence fixtures and CI polarity.
- [ ] Confirm required reviews, rulesets, and exception process.
- [ ] Confirm one representative source-edge proof without live-network PR dependency.
- [ ] Confirm implementation and rollback plans before accepting the ADR.

[Back to top](#top)

---

## No-Loss and Change Ledger

| Earlier element | v1.4 disposition |
| --- | --- |
| Connector non-publisher purpose | Preserved and strengthened |
| RAW / QUARANTINE-only payload rule | Preserved |
| Lifecycle invariant | Preserved |
| Exactly-one landing per run | Preserved with partial-run clarification |
| SourceDescriptor / checksum / IngestReceipt traceability | Preserved; authority homes corrected |
| Central receipt exception | Preserved as governed separate receipt output |
| Forbidden write targets | Preserved and expanded |
| Boundary diagram | Rebuilt from current evidence |
| Path patterns and quarantine reasons | Preserved; sidecar authority narrowed |
| `connector_gate` expectations | Preserved; current multi-prerequisite, partial implementation documented |
| Placeholder-only connector-core claim | Replaced with bounded no-network primitives, injected transport, adapter, handoff, and their explicit authority limits |
| `SourceArtifact` surfaces | Added as proposed exact-byte candidate/validation evidence without persistence or admission claims |
| Missing `IngestReceipt` validator claim | Replaced with the current validator and fixtures; connector-run presence, correspondence, and persistence remain held |
| Consequences and alternatives | Preserved and modernized |
| Migration and advisory-to-fail-closed sequence | Preserved and expanded |
| Rollback and supersession | Preserved with exact prior blob |
| Open questions | Replaced stale unknowns with current gaps |
| Stale ADR-0001 link | Corrected to tracked filename |
| “Repo unmounted / paths proposed” posture | Replaced with commit-pinned evidence |
| Accepted placement versus proposed connector decision | Made explicit: ADR-0029 governs top-level placement; ADR-0012 remains `draft` / effective `proposed` |
| Decision/publication status | Unchanged: `draft` / effective `proposed`; no publication |

[Back to top](#top)

---

<a id="references"></a>

## References

### Repository evidence

- [ADR index](./INDEX.md)
- [Accepted Directory Governance ADR](./ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules](../doctrine/directory-rules.md)
- [Connectors root](../../connectors/README.md)
- [RAW root](../../data/raw/README.md)
- [QUARANTINE root](../../data/quarantine/README.md)
- [Source registry](../../data/registry/sources/README.md)
- [Receipt root](../../data/receipts/README.md)
- [Shared ingest boundary](../../pipelines/ingest/README.md)
- [Connector gate workflow](../../.github/workflows/connector-gate.yml)
- [Bounded connector scanner and legacy connector/pipeline lexical publication-target test](../../tests/policy/test_pipeline_connector_non_publisher.py)
- [Connector-gate validator lane](../../tools/validators/connector_gate/README.md)
- [Connector output-path scanner](../../tools/validators/connector_gate/output_paths.py)
- [Internal connector-core boundary](../../packages/connectors-core/README.md)
- [`SourceAdapter` implementation](../../packages/connectors-core/src/connectors_core/source_adapter.py)
- [Exact-byte artifact handoff](../../packages/connectors-core/src/connectors_core/artifact_handoff.py)
- [Connector-core test inventory](../../tests/packages/connectors_core/README.md)
- [IngestReceipt contract](../../contracts/source/ingest_receipt.md)
- [IngestReceipt schema](../../schemas/contracts/v1/source/ingest_receipt.schema.json)
- [IngestReceipt validator](../../tools/validators/validate_ingest_receipt.py)
- [IngestReceipt validator tests](../../tests/validators/test_validate_ingest_receipt.py)
- [SourceArtifact contract](../../contracts/source/source_artifact.md)
- [SourceArtifact schema](../../schemas/contracts/v1/source/source_artifact.schema.json)
- [SourceArtifact validator](../../tools/validators/validate_source_artifact.py)
- [SourceArtifact workflow](../../.github/workflows/source-artifact-validation.yml)
- [SourceDescriptor schema](../../schemas/contracts/v1/source/source_descriptor.schema.json)
- [Source Descriptor Admission ADR](./ADR-0017-source-descriptor-admission-process.md)
- [Quarantine Exit ADR](./ADR-0021-quarantine-has-structured-exit-paths.md)
- [Public Client Boundary ADR](./ADR-0025-public-client-never-reads-canonical-internal-stores.md)
- [Artifact-family separation ADR](./ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)

### Doctrine and planning lineage

The supplied KFM corpus consistently treats connectors and watchers as non-publishers, RAW/QUARANTINE as the source-edge landing, receipts as process memory, public clients as governed-interface consumers, and promotion as a governed state transition. Those materials support the decision rationale but do not replace current repository evidence for implementation maturity.

---

## Change Log

| Version | Date | Change |
| --- | --- | --- |
| `v1.4` | 2026-08-13 | Reconciled accepted placement authority with this still-proposed connector decision; replaced stale connector-core and receipt-validator claims with current no-network primitives, injected transport, `SourceAdapter`, exact-byte `SourceArtifact` handoff, validators, fixtures, and workflow evidence; distinguished prerequisite checks from connector-run receipt presence, governed persistence, runtime confinement, source admission, and publication; changed documentation only. |
| `v1.3` | 2026-07-29 | Recorded the bounded connector repository-path scanner, deterministic policy cases, two-part workflow canary, and explicit limits without accepting this proposed ADR or changing publication authority. |
| `v1.2` | 2026-07-23 | Same-path repository-grounded modernization: confirmed ADR identity; pinned current root, schema, contract, workflow, test, and validator evidence; separated payload landing, receipt persistence, and registry authority; surfaced connector/orchestrator writer conflict; documented partial static enforcement and receipt hold; added complete maturity, acceptance, fixture, migration, risk, and rollback models; preserved `draft` / effective `proposed` status. |
| `v1.1` | 2026-05-15 | Tightened draft-versus-authority language, receipt placement, validator expectations, migration, and acceptance checks. |
| `v1` | 2026-05-11 | Initial connector RAW/QUARANTINE-only decision. |

---

**Last updated:** 2026-08-13 · **Source metadata:** `draft` · **Effective decision status:** `proposed` · **Current enforcement:** bounded static and no-network source-edge prerequisites + connector-run receipt `WORKFLOW_HOLD` · **Publication:** none · **Path:** `docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md` · [Back to top](#top)
