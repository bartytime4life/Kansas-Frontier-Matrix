<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-triplets-readme
title: pipelines/triplets/ - Shared Triplet Projection Pipeline Boundary
type: readme; directory-readme; executable-lane-contract; graph-projection-boundary
version: v0.2
status: draft; repository-grounded; placeholder-only-executable; no-active-shared-triplet-pipeline-established
owners: OWNER_TBD - Pipeline steward · Graph steward · Domain stewards · Catalog steward · Evidence steward · Policy steward · Receipt steward · Release steward · Security reviewer · Docs steward
created: 2026-06-13
updated: 2026-07-22
policy_label: public-documentation; executable-boundary; graph-derived-not-truth; cite-or-abstain; sensitive-joins-fail-closed; no-direct-publication
current_path: pipelines/triplets/README.md
owning_root: pipelines/
responsibility: shared executable triplet and graph-projection logic, if and when implemented; not declarative specification, semantic contract, machine schema, policy, canonical data, graph authority, evidence, proof, release decision, or public-serving authority
truth_posture: CONFIRMED target README and one-line placeholder main.py, thirteen individually opened one-line domain triplets.py placeholders, canonical plural data/triplets lane, singular and root catalog compatibility lanes, README-only direct pipeline-test boundary, missing checked shared triplet spec/test/fixture paths, absent triplet-specific Make target, and placeholder graph-delta/export READMEs at the pinned snapshot / PROPOSED shared projection interface, accepted predicate and edge contracts, deterministic identity rules, receipt binding, fixture corpus, tests, CI, and domain-adapter protocol / UNKNOWN complete history, branch-local or external consumers, generated files, ignored files, graph-store integrations, deployed runtime behavior, current workflow conclusions, and release use / NEEDS VERIFICATION owners, accepted object families, canonical vocabularies, schema and receipt homes, active spec placement, migration decisions, and implementation graduation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: b9d152106796fd2ec07f9ef3ea0c99125d01d1a6
  prior_blob: 098c7e7d631a9a3642b106adf85f291600472114
  inspection_method: commit-pinned GitHub connector reads and bounded repository code search; supplied PDF extraction plus visual inspection for placement and lifecycle doctrine
related:
  - ../README.md
  - main.py
  - ../domains/README.md
  - ../domains/hydrology/triplets/README.md
  - ../../pipeline_specs/README.md
  - ../../tests/pipelines/README.md
  - ../../data/triplets/README.md
  - ../../data/triplets/graph_deltas/README.md
  - ../../data/triplets/exports/README.md
  - ../../data/triplet/README.md
  - ../../catalog/triplet/README.md
  - ../../data/receipts/generated/README.md
  - ../../docs/architecture/directory-rules.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/doctrine/derived-stays-derived.md
  - ../../docs/architecture/identity-and-spec-hash.md
  - ../../docs/standards/RUN_RECEIPT.md
  - ../../.github/workflows/README.md
tags: [kfm, pipelines, triplets, graph-projection, relationship-projection, derived-data, evidence-ref, provenance, deterministic-identity, receipts, correction, rollback, no-publication]
notes:
  - "v0.2 preserves the v0.1 anti-collapse, lifecycle, evidence, policy, receipt, correction, rollback, and no-direct-publication obligations while replacing a proposed implementation tree and pseudo-schema with a commit-pinned current-state boundary."
  - "The shared executable at pipelines/triplets/main.py is a single comment identifying a greenfield placeholder; it defines no import, function, class, command, input, output, receipt, or failure contract."
  - "Thirteen sampled domain triplets.py modules were individually opened and are also one-line greenfield placeholders; the separate Hydrology triplets README is documentation, not executable proof."
  - "No shared pipeline_specs/triplets README, tests/pipelines/triplets README, fixtures/triplets README, or sampled agriculture/hydrology triplets.yaml was present at the checked paths."
  - "This documentation-only revision does not activate a source, parser, pipeline, predicate, graph store, catalog write, receipt emitter, release path, API, UI, map, export, deployment, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `pipelines/triplets/` - Shared Triplet Projection Pipeline Boundary

> Repository-grounded boundary for shared executable relationship-projection logic. The lane is correctly placed under `pipelines/`, but its inspected Python entrypoint is still a one-line greenfield placeholder. No active shared triplet pipeline is established by the current files.

![status](https://img.shields.io/badge/status-draft-yellow)
![implementation](https://img.shields.io/badge/implementation-placeholder-lightgrey)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![truth](https://img.shields.io/badge/triplet%20%E2%89%A0%20canonical%20truth-d62728)
![publication](https://img.shields.io/badge/direct%20publication-denied-d62728)

> [!IMPORTANT]
> A triplet or graph edge is a derived relationship projection. It is not a canonical record, `EvidenceBundle`, policy decision, review approval, catalog closure, release decision, or public claim. Shape-valid, deterministic, or internally consistent graph output still requires evidence, policy, review, release, correction, and rollback closure before public use.

> [!WARNING]
> Do not treat [`main.py`](main.py), the proposed tree in the prior README, a domain README, a green workflow, or a successful merge as evidence that shared triplet execution exists. At the pinned snapshot, the shared entrypoint and sampled domain modules are placeholders.

**Quick navigation:** [Purpose](#purpose) · [Status](#status-and-evidence-boundary) · [Authority](#authority-boundary) · [Current state](#confirmed-current-state) · [Placement](#placement-and-repository-fit) · [Lifecycle](#lifecycle-and-trust-boundary) · [Projection contract](#projection-contract-before-implementation) · [Identity](#identity-provenance-and-evidence) · [Outcomes](#finite-outcomes-and-failure-behavior) · [Tests](#tests-fixtures-receipts-and-ci) · [Security](#security-rights-and-sensitive-relationships) · [Release](#review-release-correction-and-rollback) · [No loss](#no-loss-preservation) · [Done](#definition-of-done) · [Open](#open-verification-backlog) · [Evidence](#evidence-ledger)

---

## Purpose

`pipelines/triplets/` is reserved for executable logic that is genuinely shared across domain lanes and projects governed, evidence-bound relationships into triplet or graph-delta candidates.

If implemented, this lane may provide reusable mechanics for:

- deterministic relationship or edge identity;
- subject, predicate, and object normalization after their owning domains establish meaning;
- provenance, source-role, time-kind, review-state, and evidence-reference propagation;
- duplicate, conflict, supersession, and invalidation detection;
- candidate graph-delta construction;
- no-network fixture execution;
- deterministic receipt-candidate emission; and
- bounded adapters used by more than one domain pipeline.

It does not own the meaning of a subject, predicate, or object. It does not decide whether a relationship is admissible, true, safe, reviewed, released, or public.

### Audience

This README is for pipeline maintainers, domain stewards, graph and catalog reviewers, contract/schema maintainers, evidence and receipt reviewers, policy and sensitivity reviewers, release stewards, CI maintainers, and agents deciding where future triplet work belongs.

### Non-goals of this revision

This revision does not:

- implement or activate triplet projection;
- define an edge, graph-delta, predicate, or receipt schema;
- select a graph database, RDF profile, serialization, or query language;
- create a declarative triplet specification;
- add fixtures, tests, validators, workflows, or Make targets;
- move, rename, retire, or populate a data or compatibility lane;
- change canonical records, lifecycle data, catalog records, evidence, policy, release objects, or public artifacts; or
- resolve open governance decisions through documentation alone.

[Back to top](#top)

---

## Status and evidence boundary

### Safe conclusion

The directory is an accepted executable-logic location in repository doctrine, but its current shared implementation is a placeholder. The README defines the boundary that a future implementation must satisfy; it does not certify that the behavior exists.

| Surface | Evidence at `main@b9d15210` | Status |
|---|---|---|
| This README | Existing v0.1 governance draft. | **CONFIRMED** |
| [`main.py`](main.py) | One comment: `triplets stage - greenfield placeholder`. | **CONFIRMED placeholder** |
| Shared functions, classes, imports, CLI, or package API | None in the opened 42-byte entrypoint. | **NOT ESTABLISHED** |
| Domain `triplets.py` modules | Thirteen individually opened modules contain only one greenfield-placeholder comment. | **CONFIRMED placeholders** |
| Domain triplet documentation | [`pipelines/domains/hydrology/triplets/README.md`](../domains/hydrology/triplets/README.md) exists. | **CONFIRMED documentation; execution not proved** |
| Shared declarative triplet lane | `pipeline_specs/triplets/README.md` returned not found; bounded search found no such lane. | **NOT FOUND AT CHECKED PATH** |
| Sample domain triplet specs | `pipeline_specs/{agriculture,hydrology}/triplets.yaml` returned not found. | **NOT FOUND AT CHECKED PATHS** |
| Dedicated shared tests | `tests/pipelines/triplets/README.md` returned not found. | **NOT FOUND AT CHECKED PATH** |
| Dedicated shared fixtures | `fixtures/triplets/README.md` returned not found. | **NOT FOUND AT CHECKED PATH** |
| Parent pipeline test boundary | [`tests/pipelines/README.md`](../../tests/pipelines/README.md) is README-only at its own bounded snapshot. | **CONFIRMED documentation** |
| Triplet-specific Make target | No `triplet` token occurs in the inspected root `Makefile`. | **NOT ESTABLISHED** |
| Triplet-specific CI | No dedicated command or workflow was established by the bounded reads and search. | **UNKNOWN / NEEDS VERIFICATION** |
| Canonical data lane | [`data/triplets/README.md`](../../data/triplets/README.md) exists and declares relationship-projection authority under `data/`. | **CONFIRMED documentation** |
| Graph-delta and export sublanes | Their READMEs exist and each says `Greenfield stub.` | **CONFIRMED placeholders** |
| Runtime, deployed consumer, graph store, or release use | Not established by source inspection. | **UNKNOWN** |

### Truth labels

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Verified from commit-pinned repository content, supplied doctrine, or generated validation output. |
| **PROPOSED** | A future interface, rule, path, or implementation obligation not established as active. |
| **UNKNOWN** | Available evidence does not establish the claim strongly enough. |
| **NEEDS VERIFICATION** | A specific repository, governance, test, runtime, or release check remains open. |

Bounded absence is not historical or global absence. Branch-local files, ignored or generated artifacts, external systems, unindexed content, and later commits were not exhaustively inspected.

[Back to top](#top)

---

## Authority boundary

`pipelines/triplets/` may eventually own shared executable projection mechanics only.

| Concern | Owning responsibility | This lane's role |
|---|---|---|
| Executable shared projection logic | `pipelines/triplets/` | Own only after code, interface, tests, and receipts exist. |
| Domain-specific relationship meaning and execution | Domain contracts and `pipelines/domains/<domain>/` | Consume shared mechanics without transferring domain authority. |
| Declarative run intent | [`pipeline_specs/`](../../pipeline_specs/README.md) | Read an accepted spec; do not embed parallel configuration authority. |
| Semantic meaning and invariants | `contracts/` | Implement accepted meaning; do not redefine it in code or this README. |
| Machine-checkable shape | `schemas/` | Validate against accepted schemas; do not invent them here. |
| Admissibility, rights, sensitivity, access | `policy/` | Enforce resolved decisions and fail closed; do not decide policy here. |
| Lifecycle graph materialization | [`data/triplets/`](../../data/triplets/README.md) | Emit candidates only through an accepted writer and state transition. |
| Catalog closure | `data/catalog/` plus catalog/release governance | Provide references or candidates; do not declare closure. |
| Evidence and proof | `data/proofs/` and accepted evidence contracts | Preserve references; never fabricate or replace support. |
| Process receipts | `data/receipts/` | Emit through accepted schemas and writers; receipts remain process memory. |
| Release, correction, withdrawal, rollback | `release/` | Provide a reviewable handoff; never approve or publish. |
| Public API, UI, map, search, or export | Governed applications and released artifacts | No direct consumer access to this source lane or unreleased outputs. |

### Anti-collapse rules

The following equivalences are always invalid:

```text
triplet projection == canonical record
graph edge == EvidenceBundle
relationship candidate == confirmed fact
predicate allowlist == policy approval
schema-valid edge == evidence closure
deterministic edge ID == correct relationship
graph-delta receipt == proof pack
pipeline completion == catalog closure
catalog closure == release approval
merge or green CI == KFM publication
generated graph summary == evidence
```

Triplet output remains derived even when it is useful, deterministic, signed, indexed, queried, rendered, or released.

[Back to top](#top)

---

## Confirmed current state

### Shared lane

The checked shared implementation surface is:

```text
pipelines/triplets/
├── README.md    # this boundary document
└── main.py      # one-line greenfield placeholder
```

The entrypoint contains no executable statement, import, function, class, command parser, data model, input reader, output writer, receipt emitter, policy call, evidence resolver, or failure behavior.

### Sampled domain lane

Thirteen direct domain modules were individually opened at the pinned commit:

```text
pipelines/domains/{agriculture,archaeology,atmosphere,fauna,flora,geology,
habitat,hazards,hydrology,people-dna-land,roads-rail-trade,soil,
settlements-infrastructure}/triplets.py
```

Each is a one-line greenfield placeholder. Their presence establishes planned naming only. It does not establish domain projection behavior, shared-helper consumption, spec binding, schema validation, receipt emission, graph storage, or CI coverage.

### Adjacent data and compatibility surfaces

The canonical plural lifecycle lane is [`data/triplets/`](../../data/triplets/README.md). Its direct [`graph_deltas/`](../../data/triplets/graph_deltas/README.md) and [`exports/`](../../data/triplets/exports/README.md) READMEs remain greenfield stubs.

Two other paths require anti-drift handling:

- [`data/triplet/`](../../data/triplet/README.md) declares itself a singular compatibility lane and routes new lifecycle data to `data/triplets/`.
- [`catalog/triplet/`](../../catalog/triplet/README.md) declares itself a root-level compatibility redirect, not a graph, catalog, receipt, proof, or publication authority.

This README does not change or independently validate their retention decisions.

[Back to top](#top)

---

## Placement and repository fit

The supplied Directory Rules and both live repository editions assign:

```text
pipelines/       executable pipeline logic - HOW a governed stage runs
pipeline_specs/  declarative pipeline configuration - WHAT should run
data/triplets/   graph-compatible relationship projections - lifecycle data
tests/           executable behavior proof
fixtures/        controlled examples, synthetic/public-safe by default
release/         promotion, correction, withdrawal, and rollback decisions
```

That makes the existing `pipelines/triplets/` placement appropriate for shared executable projection mechanics. It does not make every cross-domain graph concern appropriate here.

### Admission test

A future file belongs here only when all are true:

1. its primary responsibility is executable triplet or graph-projection logic;
2. at least two accepted domain consumers need the same mechanics, or an accepted architecture decision establishes shared ownership;
3. subject, predicate, object, evidence, source-role, time, and policy semantics remain owned elsewhere;
4. it reads accepted declarative configuration rather than becoming a hidden spec store;
5. it writes only through accepted candidate, receipt, report, or lifecycle interfaces;
6. it cannot publish, approve release, or silently mutate prior released meaning;
7. tests and fixtures can prove deterministic positive and negative behavior; and
8. correction, supersession, invalidation, and rollback effects are explicit.

If behavior belongs to one domain, keep it in that domain's pipeline lane. If it is a reusable library independent of pipeline orchestration, evaluate `packages/`. If it validates machine shape, place it under the accepted validator responsibility. If it stores data or a governance decision, route it to that authority root.

### Files that do not belong here

- declarative YAML or JSON run profiles;
- predicate or edge semantic contracts;
- JSON Schema, SHACL, JSON-LD context, RDF vocabulary, or ontology authority;
- policy rules, sensitivity classifications, rights decisions, or access grants;
- raw, work, quarantine, processed, catalog, triplet, or published data;
- EvidenceBundles, ProofPacks, review records, or release manifests;
- fixtures, tests, generated reports, or workflow definitions;
- graph database state, indexes, backups, or exports;
- API, UI, MapLibre, search, Focus Mode, or AI-serving code; and
- secrets, source credentials, restricted payloads, or exact sensitive locations.

No ADR is required for this in-place documentation clarification. An ADR or accepted migration decision is required before changing a canonical root, creating parallel authority, changing lifecycle semantics, or promoting a compatibility path.

[Back to top](#top)

---

## Lifecycle and trust boundary

Shared triplet work must preserve:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

The slash in `CATALOG / TRIPLET` represents paired closure and graph-projection concerns, not permission to build edges from arbitrary internal material.

| Stage concern | Permitted role for a future shared triplet runner | Forbidden shortcut |
|---|---|---|
| Input admission | Accept pinned references from an authorized domain/catalog caller. | Fetch sources or read arbitrary RAW/WORK material. |
| Candidate build | Derive relationship candidates from accepted records and resolved context. | Promote generated or inferred relationships to canonical truth. |
| Validation | Return explicit validation, conflict, and blocker results. | Treat shape or syntax success as evidence or policy closure. |
| Materialization | Hand candidate graph deltas to an accepted lifecycle writer. | Write directly to public or released aliases. |
| Review | Preserve review state and required reviewer classes. | Self-approve or collapse author and release authority. |
| Release | Supply immutable inputs, outputs, digests, and rollback references. | Create release approval or publish from the shared runner. |
| Correction | Emit invalidation/supersession candidates and affected references. | Delete or silently overwrite prior released meaning. |

Normal public clients must use governed interfaces and released, policy-filtered artifacts. They must not read this source directory, candidate graph stores, internal graph indexes, or unreleased triplet outputs directly.

[Back to top](#top)

---

## Projection contract before implementation

The v0.1 README included an illustrative YAML receipt. No adopted triplet projection schema or active shared interface was verified, so v0.2 does not preserve that example as a pseudo-contract.

Before code graduates beyond the placeholder, an accepted contract must define at least these semantic obligations:

| Concern | Required decision | Why it matters |
|---|---|---|
| Runner identity | Stable pipeline/component ID and version. | Reproducibility and ownership. |
| Caller scope | Owning domain, source lane, catalog handoff, and authorization. | Prevent ownerless cross-domain edges. |
| Input contract | Allowed lifecycle states, reference types, hashes, and schema versions. | Prevent raw or ambiguous input laundering. |
| Relationship contract | Subject, predicate, object, qualifiers, direction, and assertion class. | Prevent ambiguous meaning. |
| Predicate authority | Vocabulary/profile identity and compatibility rules. | Prevent locally invented predicates. |
| Identity | Deterministic edge ID inputs, canonicalization, collision handling, and versioning. | Safe replay and deduplication. |
| Evidence | `EvidenceRef` handling, resolution obligation, bundle linkage, and abstention behavior. | Cite-or-abstain compliance. |
| Provenance | Source IDs and roles, transforms, agents, tools, run refs, and derivation lineage. | Auditability. |
| Time | Observation, valid, retrieval, processing, release, correction, and other accepted time kinds. | Avoid temporal collapse. |
| Policy | Rights, sensitivity, sovereignty, access, redaction/generalization, and decision refs. | Fail-closed handling. |
| Review | Candidate, reviewed, rejected, superseded, and released states without inventing approval. | Separation of duties. |
| Outputs | Candidate edge, graph delta, validation report, receipt, and affected-reference shapes. | Controlled handoff. |
| Failures | Finite outcome and reason-code vocabulary. | No silent success. |
| Replay | Spec/code/input/tool digests and deterministic or bounded-variance rules. | Reproducibility. |
| Correction | Supersession, invalidation, withdrawal, and downstream impact links. | No hidden rewrite. |
| Rollback | Last-known-good code/spec/data set and release-aware rollback target. | Reversibility. |

The semantic contract belongs under `contracts/`; its machine shape belongs under `schemas/`; admissibility belongs under `policy/`; declarative run intent belongs under `pipeline_specs/`. This lane implements those decisions after they are accepted.

### Consumer contract

A domain adapter must not call shared mechanics anonymously. It should provide an accepted caller identity, domain ownership, pinned spec/profile references, input references and digests, policy/evidence state, and requested output class. The shared runner must return a bounded result and must not infer missing authority from the caller's filesystem location.

[Back to top](#top)

---

## Identity, provenance, and evidence

Deterministic identity is necessary but insufficient.

A future edge identity design must establish:

- which normalized fields enter the identity calculation;
- whether qualifiers, time bounds, assertion class, source role, evidence scope, and graph version affect identity;
- canonicalization and digest algorithms;
- collision and algorithm-version behavior;
- stable domain/entity identifiers versus edge/version identifiers;
- duplicate and semantically conflicting edge handling; and
- correction and supersession linkage.

Do not copy an illustrative hash format from documentation into production without an accepted contract and compatibility review. [`identity-and-spec-hash.md`](../../docs/architecture/identity-and-spec-hash.md) contains architecture guidance, but it also marks important paths and decisions as proposed.

### Evidence discipline

- Preserve source roles; do not collapse primary, corroborating, contextual, and restricted sources.
- Preserve `EvidenceRef` as a reference; do not relabel it as an `EvidenceBundle`.
- Resolve claim-bearing relationships to accepted evidence support or return an explicit negative outcome.
- Record whether an edge is observed, asserted by a source, modeled, inferred, aggregated, generalized, or otherwise derived.
- Keep confidence, uncertainty, review state, and release state distinct.
- Invalidate downstream derivatives when supporting evidence, policy, identity, time, or source-role state changes.

### Receipt discipline

The lifecycle doctrine names a `GraphBuildReceipt`, while [`RUN_RECEIPT.md`](../../docs/standards/RUN_RECEIPT.md) documents a broader receipt direction and unresolved schema drift. The exact accepted receipt family, fields, schema path, and emitter for this lane remain **NEEDS VERIFICATION**.

A receipt records process memory. It does not prove that an edge is true, policy-allowed, reviewed, released, or safe to expose.

[Back to top](#top)

---

## Finite outcomes and failure behavior

The future runner must not return an unqualified success. The accepted enum and reason-code schema remain open, but behavior must distinguish at least:

- a candidate that is ready for the next named review gate;
- abstention because evidence or scope is insufficient;
- denial because policy, rights, sensitivity, or access forbids the operation;
- hold/quarantine because review, identity, schema, provenance, time, or ownership is unresolved;
- error because execution or integrity failed; and
- no-op because pinned inputs produce no material graph delta.

Until a contract freezes exact names, these are behavioral classes, not a normative enum.

### Fail-closed conditions

A future implementation must refuse or hold when any required item is missing or inconsistent, including:

- caller or domain ownership;
- accepted predicate profile;
- stable subject or object identity;
- allowed input lifecycle state;
- required evidence support;
- source identity or source role;
- rights, sensitivity, sovereignty, or policy decision;
- material time fields or freshness state;
- spec, code, input, tool, or output digest;
- duplicate/conflict/supersession evaluation;
- review state;
- receipt write or integrity check;
- correction/invalidation linkage; or
- release-aware rollback target when the output can affect released material.

Partial output must remain non-public, identifiable, and recoverable. A retry must not duplicate edges or obscure the first failure.

[Back to top](#top)

---

## Tests, fixtures, receipts, and CI

### Current boundary

The checked `tests/pipelines/` direct lane is documented but not an established executable suite, and the root `Makefile` has no triplet-specific target. No dedicated shared triplet fixture lane, test lane, active spec, or CI command was established by this inspection.

### Graduation proof burden

Before `main.py` becomes active, the implementation needs deterministic positive and negative coverage for:

- one valid public-safe relationship candidate;
- missing caller ownership;
- unknown predicate or incompatible predicate version;
- unstable subject/object identity and digest collision handling;
- unresolved `EvidenceRef` or mismatched `EvidenceBundle` support;
- missing or collapsed source role;
- observation/model/inference class collapse;
- temporal-field collapse or stale support;
- duplicate, contradictory, superseded, or withdrawn edge;
- unknown rights or policy state;
- exact archaeology, rare-species, living-person, genomic, private-land, cultural, or infrastructure relationship exposure;
- redaction/generalization transform linkage;
- direct write to `data/published/` or a public service;
- catalog/release authority impersonation;
- receipt write failure or hash mismatch;
- deterministic replay and repeated-run no-op;
- cancellation and partial-output cleanup;
- correction-driven invalidation; and
- rollback to the last known-good code/spec/input combination.

Default fixtures should be synthetic, minimal, no-network, and public-safe. Tests must not turn fixtures into evidence or duplicate production semantics inside the test harness.

### CI boundary

A future workflow should call a repository-owned command and fail visibly on negative controls. It must not embed a second implementation in YAML, upload sensitive graph material, use workflow success as release approval, or write directly to published authority.

The current [workflow inventory](../../.github/workflows/README.md) reports broad repository checks and many greenfield stubs. Current run conclusions, branch-protection coupling, and triplet-specific enforcement remain **UNKNOWN**.

### README-only validation

This documentation revision should prove:

- one H1 and one closed KFM Meta Block;
- balanced fenced blocks and valid unique anchors;
- repository-relative links resolve at the pinned or proposed head;
- current implementation claims match exact opened files;
- no pseudo-schema or invented accepted object family remains;
- no loss of the v0.1 anti-collapse, lifecycle, evidence, policy, receipt, correction, rollback, and no-publication boundaries;
- no secrets, restricted payloads, or sensitive locations; and
- a valid generated-work receipt with the README content hash.

[Back to top](#top)

---

## Security, rights, and sensitive relationships

Graph joins can expose more than their inputs. A harmless-looking edge may reveal identity, location, association, ownership, access, vulnerability, or sensitive group membership.

High-risk relationship classes include:

- living people, families, land ownership, addresses, and contact or movement patterns;
- DNA, genomic, kinship, health, consent, or re-identification relationships;
- archaeology, burial, sacred, cultural, tribal, or repatriation-sensitive locations and associations;
- rare species, nesting, denning, migration, collection, or exact habitat relationships;
- critical infrastructure, facility dependencies, access routes, vulnerabilities, and operational state;
- private-land access, easements, occupancy, disputes, and inferred ownership;
- source-restricted identifiers, URLs, joins, and redistribution-limited fields; and
- combinations that create a sensitive inference absent from each individual source.

Required posture:

- deny or hold unknown rights, consent, sovereignty, sensitivity, or policy state;
- preserve restricted and public-safe graph views as separate release products;
- generalize, aggregate, redact, delay, or deny before public materialization;
- record each transform and reason in accepted receipts;
- keep exact sensitive values out of logs, CI artifacts, receipts, PR text, and test fixtures;
- treat a relationship's sensitivity as potentially higher than either endpoint's sensitivity; and
- re-evaluate downstream graph products after correction, policy change, or source withdrawal.

This README contains no sensitive payload and changes no access boundary.

[Back to top](#top)

---

## Review, release, correction, and rollback

### Review burden

Future executable changes require review from the owners of the responsibilities actually affected: pipeline, domain semantics, graph/predicate vocabulary, schema/contract, evidence, source roles, identity, policy/sensitivity, receipts, tests/CI, release, and documentation.

[`.github/CODEOWNERS`](../../.github/CODEOWNERS) routes `pipelines/` and trust-bearing roots to `@bartytime4life` at the pinned snapshot. That routing does not prove an independent stewardship assignment, policy approval, evidence closure, or release approval.

### Release boundary

The safe conceptual flow is:

```text
accepted processed or catalog-scoped input
  -> domain-owned relationship request
  -> shared projection mechanics
  -> candidate edge / graph delta + validation + receipt
  -> evidence, policy, identity, and domain review
  -> catalog / graph closure
  -> release candidate and governed release decision
  -> public-safe released graph artifact
  -> governed API / UI / map / export
```

A branch, commit, pull request, merge, successful workflow, graph receipt, catalog entry, or valid edge is not KFM publication.

### Correction and supersession

A correction must preserve:

- the prior edge or immutable reference;
- the corrected or superseding edge;
- reason and effective time;
- affected subject, object, predicate, evidence, source, policy, catalog, release, API, map, search, and export references;
- prior and new digests;
- reviewer and release decision references; and
- rebuild, invalidation, withdrawal, and rollback status.

Do not silently rewrite a released graph.

### Rollback

For this README-only change, rollback is a normal Git revert that restores prior README blob `098c7e7d631a9a3642b106adf85f291600472114`, removes the paired generated receipt introduced by the change, and repeats the same documentation and receipt checks. No pipeline, data, graph, release, or public artifact rollback is required because none is changed.

For future executable work, rollback must pin the last-known-good code, spec, schema, policy bundle, fixtures, dependencies, input set, output set, and release references. It must preserve failed-run and correction history.

[Back to top](#top)

---

## No-loss preservation

The v0.1 README contained strong governance material. This revision preserves its substantive obligations while correcting its implementation posture.

| v0.1 material | v0.2 disposition |
|---|---|
| Shared executable projection purpose | **Retained**, explicitly conditional on implementation graduation. |
| `pipelines/` versus `pipeline_specs/` split | **Retained and grounded** in current Directory Rules and root READMEs. |
| Triplet anti-collapse rules | **Retained and expanded.** |
| Domain-specific logic remains in domain lanes | **Retained**, with thirteen placeholder modules identified. |
| Evidence, source-role, identity, time, provenance, review, and policy gates | **Retained and strengthened.** |
| No direct catalog closure or publication | **Retained and made explicit across lifecycle and consumer boundaries.** |
| Proposed helper file tree | **Removed as current-shape implication**; replaced by the verified two-file shared surface and graduation criteria. |
| Illustrative YAML projection receipt | **Removed as pseudo-schema** because no accepted shared triplet or receipt contract was verified. |
| Proposed tests and fixtures | **Retained as proof obligations**, not claimed paths. |
| Correction, invalidation, supersession, and rollback | **Retained and expanded.** |
| Six open questions | **Retained and expanded** into a repository-grounded verification backlog. |

The document ID and creation date remain unchanged.

[Back to top](#top)

---

## Definition of done

### Documentation acceptance

This README revision is complete when:

- [x] the existing file is revised in place without creating a parallel authority;
- [x] current shared and domain placeholder code is distinguished from future design;
- [x] canonical plural data and compatibility lanes are identified accurately;
- [x] executable, declarative, semantic, machine-shape, policy, data, evidence, receipt, release, and public-serving responsibilities remain separate;
- [x] anti-collapse, lifecycle, source-role, evidence, identity, time, review, security, correction, rollback, and no-publication controls remain visible;
- [x] the proposed helper tree and illustrative receipt are no longer presented as implementation or schema;
- [x] bounded absence claims are labeled and do not imply exhaustive historical absence;
- [x] rollback is limited to documentation and its generated receipt; and
- [x] no runtime, data, release, or public behavior is claimed from this documentation change.

### Implementation graduation

The shared triplet lane is not implementation-complete until repository evidence establishes:

- an accepted shared-use case and at least two real consumers, or an accepted architecture decision;
- semantic contracts for relationship and predicate meaning;
- machine schemas and compatibility/versioning rules;
- stable executable API or CLI and declared side effects;
- accepted declarative spec placement and active profiles;
- deterministic identity/canonicalization and collision behavior;
- public-safe valid and invalid fixtures;
- dedicated positive, negative, no-network, replay, idempotency, correction, and rollback tests;
- evidence, source-role, time, rights, sensitivity, policy, and review gates;
- deterministic receipts with accepted schema and writer;
- controlled candidate output and lifecycle handoff;
- no-direct-publish and no-authority-impersonation tests;
- command-bearing CI with observed results;
- downstream invalidation and correction propagation; and
- safe disable and rollback procedures.

[Back to top](#top)

---

## Open verification backlog

| ID | Question | Evidence needed to close | Status |
|---|---|---|---|
| `TRIPPIPE-001` | Is a shared triplet runner required, or should all projection remain domain-owned? | Consumer inventory, duplication analysis, package/pipeline boundary review, accepted decision. | **NEEDS VERIFICATION** |
| `TRIPPIPE-002` | What command or API should replace the placeholder `main.py`? | Accepted interface contract, implementation, CLI help/API docs, tests, run receipt. | **UNKNOWN** |
| `TRIPPIPE-003` | Where should shared declarative triplet profiles live? | `pipeline_specs/` inventory, placement review, accepted profile and loader. | **NEEDS VERIFICATION** |
| `TRIPPIPE-004` | Which semantic contract owns subject-predicate-object relationships and qualifiers? | Accepted contract and domain-steward review. | **UNKNOWN** |
| `TRIPPIPE-005` | Which machine schema/profile governs edges and graph deltas? | Accepted schema, version policy, fixtures, validator, tests. | **UNKNOWN** |
| `TRIPPIPE-006` | Which predicate vocabularies are allowed and who governs them? | Vocabulary registry, compatibility rules, review ownership. | **NEEDS VERIFICATION** |
| `TRIPPIPE-007` | Which deterministic edge-ID and canonicalization rules are accepted? | Identity contract, algorithm decision, collision fixtures, replay tests. | **NEEDS VERIFICATION** |
| `TRIPPIPE-008` | Is `GraphBuildReceipt` canonical, an alias, or a proposed lifecycle name? | Receipt contract/schema registry and accepted ADR or compatibility decision. | **NEEDS VERIFICATION** |
| `TRIPPIPE-009` | What finite outcome and reason-code vocabulary applies? | Contract, schema, negative fixtures, consumer tests. | **UNKNOWN** |
| `TRIPPIPE-010` | Which checked domain modules will consume shared logic first? | Non-placeholder implementation and integration tests. | **UNKNOWN** |
| `TRIPPIPE-011` | Where do candidate graph deltas live before release, and which writer owns them? | Data-lane contract, schema, writer implementation, receipt, release handoff. | **NEEDS VERIFICATION** |
| `TRIPPIPE-012` | Which shared tests, fixtures, and CI job enforce the lane? | Executable suite, public-safe fixtures, Make/CLI target, command-bearing workflow and observed run. | **UNKNOWN** |
| `TRIPPIPE-013` | Are any graph stores, APIs, searches, maps, exports, or external consumers already bound to placeholder paths? | Complete code/config/history and deployment inventory. | **UNKNOWN** |
| `TRIPPIPE-014` | How are sensitive cross-domain joins classified and transformed? | Policy bundle, relationship sensitivity rules, redaction/generalization contracts and tests. | **NEEDS VERIFICATION** |
| `TRIPPIPE-015` | How do corrections invalidate graph, catalog, search, map, export, and AI derivatives? | Dependency graph, correction contract, invalidation runner, rollback drill. | **UNKNOWN** |
| `TRIPPIPE-016` | Which owners provide pipeline, domain, evidence, policy, graph, receipt, and release review? | Verified stewardship assignments and repository review controls. | **NEEDS VERIFICATION** |
| `TRIPPIPE-017` | Should the singular `data/triplet/` and root `catalog/triplet/` compatibility paths be retained or retired? | Reference inventory, accepted migration plan, deprecation window, rollback. | **NEEDS VERIFICATION / ADR** |
| `TRIPPIPE-018` | Which of the two Directory Rules editions is the canonical document home? | Accepted authority/supersession decision and reference migration. | **NEEDS VERIFICATION / ADR** |

Open items belong in the appropriate contract, schema, policy, ADR, drift register, issue, test, or implementation work. This README must not silently close them.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Observation supported | Status |
|---|---|---|
| `pipelines/triplets/README.md@b9d15210` | Prior v0.1 boundary, anti-collapse rules, proposed tree, pseudo-receipt, tests, and open questions. | **CONFIRMED** |
| [`main.py@b9d15210`](main.py) | Shared entrypoint is a 42-byte one-line greenfield placeholder. | **CONFIRMED** |
| Thirteen `pipelines/domains/*/triplets.py@b9d15210` reads | Sampled domain modules are one-line greenfield placeholders. | **CONFIRMED bounded inventory** |
| [`pipelines/README.md`](../README.md) | `pipelines/` owns executable logic and documents this lane as shared projection support. | **CONFIRMED documentation** |
| [`pipeline_specs/README.md`](../../pipeline_specs/README.md) | Declarative root is placeholder-heavy and no active root spec system is established. | **CONFIRMED documentation** |
| Checked shared/spec/test/fixture paths | Shared triplet spec/test/fixture READMEs and sampled domain triplet YAML files returned not found. | **CONFIRMED bounded absence** |
| [`tests/pipelines/README.md`](../../tests/pipelines/README.md) | Direct pipeline test lane is README-only at its bounded snapshot; default test target excludes it. | **CONFIRMED documentation** |
| [`data/triplets/README.md`](../../data/triplets/README.md) | Canonical plural lifecycle lane for relationship projections; projections are not canonical truth. | **CONFIRMED documentation** |
| [`graph_deltas/README.md`](../../data/triplets/graph_deltas/README.md) and [`exports/README.md`](../../data/triplets/exports/README.md) | Each remains a greenfield stub. | **CONFIRMED** |
| [`data/triplet/README.md`](../../data/triplet/README.md) and [`catalog/triplet/README.md`](../../catalog/triplet/README.md) | Singular data and root catalog paths declare compatibility/redirect roles. | **CONFIRMED documentation** |
| [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md) and [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) | Executable/declarative split, lifecycle/data placement, no-parallel-authority rule; document-home conflict remains open. | **CONFIRMED files / authority conflict unresolved** |
| [`lifecycle-law.md`](../../docs/doctrine/lifecycle-law.md) | `CATALOG / TRIPLET` is paired closure/projection; lifecycle names `GraphBuildReceipt`; unreleased triplets are non-public. | **CONFIRMED doctrine; implementation not implied** |
| Supplied Directory Rules PDF, Pipeline Living Implementation Manual v0.3, Implementation Reference, and Greenfield Plan | Placement, derivative-not-truth, governed-interface, lifecycle, and no-direct-publication doctrine. | **CONFIRMED supplied evidence; current runtime not implied** |
| Root `Makefile@b9d15210` and [workflow inventory](../../.github/workflows/README.md) | No triplet-specific Make target established; current triplet-specific CI and run conclusions remain unverified. | **CONFIRMED bounded source inspection / runtime UNKNOWN** |
| [`CONTRIBUTING.md`](../../CONTRIBUTING.md), [generated receipt lane](../../data/receipts/generated/README.md), and generated-receipt schema | AI-authored documentation requires a generated receipt and pending human review. | **CONFIRMED** |

### Evidence limitations

- The inspection used connector reads and bounded code search, not a complete mounted checkout or full Git history.
- Exact branch-protection settings, required checks, current workflow conclusions, deployed services, external graph stores, and downstream consumers were not established.
- Supplied doctrine and planning artifacts guide architecture; they do not prove repository implementation.
- Search results and 404 checks support bounded statements only.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Date | **2026-07-22** |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Base ref | `main` |
| Pinned evidence commit | `b9d152106796fd2ec07f9ef3ea0c99125d01d1a6` |
| Target path | `pipelines/triplets/README.md` |
| Change type | Documentation-only, full in-place no-loss revision |
| Shared triplet execution | **NOT RUN - inspected entrypoint is a placeholder** |
| Repository-native triplet tests | **NOT RUN - no dedicated suite or command established** |
| Human review | **Pending** |
| Release/publication impact | **None; documentation and provenance only** |

Re-review this README when shared or domain triplet code, specs, contracts, schemas, predicates, identities, policies, fixtures, tests, receipts, graph storage, workflows, correction behavior, release integration, or public consumers change.

[Back to top](#top)
