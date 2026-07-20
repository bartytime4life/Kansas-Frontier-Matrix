<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-ingest-readme
title: Shared Ingest Boundary
type: readme
version: v0.2
status: draft; repository-grounded
owners:
  - <pipeline-owner>
  - <ingest-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-07-20
policy_label: public-with-ingest-source-admission-and-quarantine-gates
truth_posture: cite-or-abstain
responsibility_root: pipelines/
path: pipelines/ingest/README.md
path_posture: existing-parent-documentation-lane; shared-executable-ingest-authority-permitted; implementation-not-yet-confirmed
evidence_snapshot:
  base_ref: main
  base_commit: 13e1b27bf8cc4fdd4d88305532e69c444c07a4b5
  prior_blob: da14498b6a94c0aa52ebe73d5c4d7056e9f7011e
related:
  - ../README.md
  - ../domains/README.md
  - fauna/README.md
  - ../../docs/architecture/directory-rules.md
  - ../../docs/architecture/domain-placement-law.md
  - ../../pipeline_specs/README.md
  - ../../connectors/README.md
  - ../../contracts/source/README.md
  - ../../schemas/contracts/v1/source/README.md
  - ../../policy/rights/README.md
  - ../../policy/sensitivity/README.md
  - ../../data/registry/sources/README.md
  - ../../data/receipts/ingest/README.md
  - ../../data/proofs/evidence_bundle/README.md
tags:
  - kfm
  - pipelines
  - ingest
  - source-admission
  - raw
  - quarantine
  - receipts
  - evidence
  - fail-closed
notes:
  - "This edition distinguishes a valid responsibility location from a verified executable implementation."
  - "Directory Rules establish pipelines/ as executable HOW and pipeline_specs/ as declarative WHAT."
  - "Domain-owned ingest code belongs under pipelines/domains/<domain>/; pipelines/ingest/<domain>/ requires an explicit compatibility or migration posture."
  - "No shared ingest entrypoint, accepted shared ingest spec, dedicated shared ingest test lane, or dedicated shared ingest fixture lane was confirmed at the pinned snapshot."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `pipelines/ingest/` — shared ingest boundary

> Repository boundary for cross-domain ingest and source-admission logic. The path is valid for shared executable pipeline behavior, but the pinned repository snapshot establishes documentation and a Fauna compatibility child—not a verified shared ingest runtime.

![status](https://img.shields.io/badge/status-draft-blue)
![truth](https://img.shields.io/badge/truth-repository--grounded-2e7d32)
![implementation](https://img.shields.io/badge/implementation-not%20confirmed-6f42c1)
![lifecycle](https://img.shields.io/badge/output-RAW%20or%20QUARANTINE-455a64)
![publication](https://img.shields.io/badge/direct%20publication-denied-d62728)

## At a glance

| Question | Repository-grounded answer | Status |
|---|---|---:|
| Does this path exist? | Yes. This README exists at `pipelines/ingest/README.md`. | **CONFIRMED** |
| Is `pipelines/ingest/` permitted by Directory Rules? | Yes. Directory Rules name `ingest/` as a shared executable sublane under `pipelines/`. | **CONFIRMED doctrine** |
| Is a shared ingest implementation present? | No shared executable entrypoint or helper named by the prior README was found in the bounded exact-path probes. | **UNKNOWN beyond probes; not confirmed** |
| What child was directly confirmed? | `fauna/README.md`, now documented as a compatibility boundary rather than the canonical Fauna implementation home. | **CONFIRMED** |
| Where does domain-owned ingest logic belong? | Under `pipelines/domains/<domain>/`. | **CONFIRMED doctrine** |
| Where do declarative run definitions belong? | Under `pipeline_specs/`, using a repository-accepted domain or shared layout. | **CONFIRMED root split; exact ingest layout UNKNOWN** |
| Can this lane publish? | No. It cannot authorize release or write directly to public surfaces. | **DENY** |

> [!IMPORTANT]
> A valid directory location is not proof that code, contracts, schemas, fixtures, tests, CI coverage, source activation, or runtime behavior exists. This README defines the boundary that future shared ingest work must satisfy; it does not certify that implementation.

## Contents

- [Purpose](#purpose)
- [Placement and ownership](#placement-and-ownership)
- [Observed repository state](#observed-repository-state)
- [Responsibility boundaries](#responsibility-boundaries)
- [Source-edge contract](#source-edge-contract)
- [Lifecycle and trust membrane](#lifecycle-and-trust-membrane)
- [Required admission gates](#required-admission-gates)
- [Identity, time, rights, and sensitivity](#identity-time-rights-and-sensitivity)
- [Receipts, proofs, and finite outcomes](#receipts-proofs-and-finite-outcomes)
- [Implementation admission criteria](#implementation-admission-criteria)
- [Testing and validation](#testing-and-validation)
- [Correction and rollback](#correction-and-rollback)
- [Evidence ledger](#evidence-ledger)
- [Related repository surfaces](#related-repository-surfaces)
- [Open questions](#open-questions)
- [Maintenance](#maintenance)

---

## Purpose

`pipelines/ingest/` is the responsibility boundary for executable ingest behavior that is genuinely reusable across multiple KFM domains.

A future implementation may coordinate common checks such as:

- resolving stable `SourceDescriptor` references;
- verifying staged-payload digests and capture metadata;
- preserving source roles supplied by governed registry records;
- checking explicit rights, citation, cadence, and temporal fields;
- returning a fail-closed admission disposition;
- preparing deterministic receipt fragments;
- routing unresolved material toward governed quarantine handling.

Those capabilities are **PROPOSED responsibilities**, not claims about current files. At the pinned snapshot, the repository did not establish a shared entrypoint, accepted shared-ingest contract, dedicated shared spec, dedicated shared tests, or dedicated shared fixtures.

This lane must never become a convenient place to collapse connectors, domain transformations, policy, proof, storage, and publication into one step.

[Back to top](#top)

---

## Placement and ownership

Directory Rules distinguish:

- `pipelines/` — executable pipeline logic: **how** governed work runs;
- `pipeline_specs/` — declarative configuration: **what** should run;
- `connectors/` — source-specific retrieval and admission at the source edge;
- `pipelines/domains/<domain>/` — domain-owned executable processing;
- `data/` — lifecycle data, receipts, proofs, and registry artifacts;
- `release/` — release decisions, correction, withdrawal, and rollback authority.

### Shared versus domain-owned placement

Code belongs in this lane only when all of the following are true:

1. its primary responsibility is ingest or source admission;
2. it is used by more than one domain without embedding one domain's semantics;
3. it does not fetch from one named upstream source;
4. it does not define object meaning, machine shape, or policy;
5. its writer and side-effect boundaries are explicit;
6. it returns inspectable, finite, fail-closed results;
7. the same responsibility is not already owned by a shared package or validator.

Domain-specific ingest belongs under `pipelines/domains/<domain>/`. Source-specific retrieval belongs under `connectors/<source_id>/`. A domain child under `pipelines/ingest/<domain>/` must be treated as **CONFLICTED** unless an accepted ADR, compatibility note, or migration plan explains the exception.

The confirmed `fauna/README.md` child follows that compatibility posture. It does not establish a general pattern for adding more domain children here.

### Authority limit

This README may document placement and required behavior. It cannot:

- accept an ADR;
- activate a source;
- define a `SourceDescriptor`;
- create schema or policy authority;
- approve rights or sensitivity;
- establish EvidenceBundle closure;
- approve lifecycle promotion;
- authorize release or publication.

[Back to top](#top)

---

## Observed repository state

The following observations are bounded to `main@13e1b27bf8cc4fdd4d88305532e69c444c07a4b5`.

### Confirmed surfaces

| Surface | Observation | Status |
|---|---|---:|
| `pipelines/ingest/README.md` | Existing target; prior blob `da14498b...`. | **CONFIRMED** |
| `pipelines/ingest/fauna/README.md` | Existing compatibility-boundary README; blob `11220d55...`. | **CONFIRMED** |
| `pipelines/README.md` | Parent executable-pipeline responsibility documentation exists. | **CONFIRMED** |
| `pipelines/domains/README.md` | Domain pipeline responsibility documentation exists. | **CONFIRMED** |
| `pipeline_specs/README.md` | Declarative specification root documentation exists. | **CONFIRMED** |
| Source contract/schema roots | `contracts/source/README.md` and `schemas/contracts/v1/source/README.md` exist. | **CONFIRMED files** |
| Registry and lifecycle roots | Source registry, RAW, WORK, QUARANTINE, PROCESSED, receipt, and proof READMEs exist. | **CONFIRMED files** |

File presence establishes a repository surface, not operational readiness.

### Exact-path probes that did not resolve

The prior README presented the following as a recommended implementation shape. Exact reads at the pinned snapshot returned `NOT_FOUND`:

~~~text
pipelines/ingest/INGEST_SHARED_CONTRACT.md
pipelines/ingest/run_dry_fixture.py
pipelines/ingest/validate_source_descriptor.py
pipelines/ingest/validate_source_intake.py
pipelines/ingest/validate_payload_integrity.py
pipelines/ingest/validate_rights_citation.py
pipelines/ingest/preserve_source_role.py
pipelines/ingest/admit_raw_capture.py
pipelines/ingest/route_quarantine_reason.py
pipelines/ingest/emit_ingest_receipt.py
pipeline_specs/ingest/README.md
tests/pipelines/ingest/README.md
fixtures/ingest/README.md
~~~

These results prove only bounded absence at the named paths. They do not prove that equivalent behavior is absent everywhere in the repository.

### Current maturity statement

| Claim | Outcome |
|---|---:|
| This is a documented shared-ingest responsibility boundary. | **CONFIRMED** |
| Shared ingest executables are implemented here. | **UNKNOWN / not confirmed** |
| A shared ingest command is accepted and runnable. | **UNKNOWN / no command documented** |
| Shared ingest specs, fixtures, and tests have accepted dedicated homes. | **UNKNOWN** |
| Any live source is activated through this lane. | **UNKNOWN; do not infer** |
| This lane can release or publish. | **DENY** |

[Back to top](#top)

---

## Responsibility boundaries

| Responsibility | Owning home | Relationship to this lane |
|---|---|---|
| Source-specific retrieval, authentication, paging, and upstream API behavior | `connectors/<source_id>/` | Caller or upstream producer; not owned here. |
| Cross-domain admission helpers | `pipelines/ingest/` | Permitted future responsibility when evidence-backed. |
| Domain-specific ingest and transformation | `pipelines/domains/<domain>/` | Canonical domain execution home. |
| Declarative run configuration | `pipeline_specs/` | Read-only input to an executor; exact shared-ingest layout unresolved. |
| Source identity and activation state | `data/registry/sources/` | Governed input; this lane must not mutate it implicitly. |
| Object meaning | `contracts/` | Referenced authority; not duplicated here. |
| Machine shape | `schemas/contracts/v1/` | Referenced authority; not duplicated here. |
| Rights, sensitivity, and release admissibility | `policy/` | Decision authority remains outside executable helpers. |
| RAW, WORK, QUARANTINE, and PROCESSED artifacts | `data/<phase>/` | Governed lifecycle homes; never stored beside code. |
| Process receipts | `data/receipts/` | Process memory, not proof or approval. |
| EvidenceBundle and proof closure | `data/proofs/` | Separate evidence authority. |
| Promotion, release, correction, and rollback decisions | `release/` | Separate decision authority. |
| Public API, map, UI, exports, and AI answers | governed released surfaces | No direct path from this lane. |

### Anti-collapse rules

The following equivalences are forbidden:

~~~text
connector success       != ingest admission
ingest admission        != normalization
RAW capture             != processed record
receipt present         != evidence closure
schema valid            != source authoritative
hash valid              != rights approved
source role recorded    != source role accepted forever
pipeline success        != release approval
generated summary       != evidence
file move               != lifecycle promotion
~~~

[Back to top](#top)

---

## Source-edge contract

Any future shared ingest component must operate as a bounded helper invoked by an identified connector, domain pipeline, fixture harness, or other approved caller. It must not silently become the owner of every source-edge responsibility.

### Minimum caller inputs

The exact schema is **UNKNOWN** until repository contracts and schemas establish it. At minimum, a caller should be able to supply or reference:

- caller identity and authorized scope;
- stable source and `SourceDescriptor` references;
- source role and activation state;
- staged payload or immutable payload reference;
- expected and observed digest metadata;
- retrieval and source-vintage timestamps;
- media type, size, and capture context;
- rights, terms, attribution, and citation posture;
- domain and intended lifecycle disposition;
- sensitivity and required-review references;
- run identifier and idempotency context.

Missing or contradictory fields must produce an explicit non-admission result. They must not be guessed from filenames, display labels, endpoint names, or generated prose.

### Writer boundary

Directory Rules require connector outputs to land in governed RAW or QUARANTINE homes with source descriptors, checksums, and ingest receipts. This README does not decide whether a future shared helper writes those artifacts or returns an admission decision to the connector.

Until an accepted contract resolves that question:

- the caller retains responsibility for authorized writes;
- a shared helper should prefer pure validation and deterministic result construction;
- no helper may write to WORK, PROCESSED, CATALOG, TRIPLET, PUBLISHED, or release homes as an ingest shortcut;
- partial failures must not leave an unlabeled or apparently admitted artifact.

[Back to top](#top)

---

## Lifecycle and trust membrane

~~~mermaid
flowchart TD
    A["SourceDescriptor + staged payload"] --> B["Bounded ingest checks"]
    B --> C{"Admission gates close?"}
    C -->|Yes| D["Governed RAW capture"]
    C -->|No| E["Hold, deny, error, or QUARANTINE"]
    D --> F["Domain pipeline handoff"]
    F --> G["WORK / QUARANTINE"]
    G --> H["PROCESSED candidate"]
    H --> I["Catalog / triplet and release gates"]
    I --> J["PUBLISHED public-safe artifact"]
~~~

The diagram shows responsibility transitions, not a verified running workflow.

The canonical lifecycle remains:

~~~text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
~~~

Promotion is a governed state transition, not a file move. Shared ingest may participate at the source edge only. It does not own later promotion gates.

### Public boundary

Public clients, MapLibre surfaces, governed API responses, exports, search indexes, graph projections, and AI systems must not read this directory or internal lifecycle stores as public truth.

No ingest helper may:

- expose RAW, WORK, or QUARANTINE records to a public client;
- produce a public layer or API payload;
- mark an artifact released;
- bypass EvidenceBundle, policy, review, manifest, correction, or rollback requirements;
- treat a successful source fetch as permission to publish.

[Back to top](#top)

---

## Required admission gates

The exact executable contract remains **PROPOSED**. Any implementation admitted here must demonstrate the following responsibilities or explicitly delegate them to a verified authority.

| Gate | Minimum check | Fail-closed behavior |
|---|---|---|
| Caller scope | Caller, domain, run, and permitted side effects are explicit. | Refuse execution or return error. |
| Source identity | Stable source and `SourceDescriptor` references resolve. | Hold or quarantine. |
| Activation | Source activation state permits the requested mode. | Deny live use; fixture-only if authorized. |
| Source role | Role comes from governed source metadata and is preserved. | Abstain, deny, or quarantine on ambiguity. |
| Payload integrity | Digest, size, media type, manifest, and capture metadata agree. | Reject or quarantine; no partial admission. |
| Rights and citation | Terms, attribution, citation, and intended-use posture are explicit. | Quarantine or deny when unresolved. |
| Time | Retrieval, source-vintage, observation, processing, and valid-time meanings remain distinct. | Hold on missing or contradictory material time. |
| Sensitivity | Restricted fields and exact harmful geometry are identified before later use. | Deny, restrict, generalize under policy, or quarantine. |
| Schema/contract refs | Referenced shapes and meanings are versioned and resolvable. | Do not invent replacement fields. |
| Idempotency | Repeated input does not create ambiguous duplicate admissions. | Return a stable existing result or explicit conflict. |
| Receipt | Inputs, versions, decisions, hashes, failures, and outputs are recordable. | Treat missing process memory as incomplete. |
| Side effects | Writer targets are allowlisted and limited to the caller's approved RAW/QUARANTINE scope. | Abort before write. |
| No direct publication | No catalog, release, API, UI, map, or PUBLISHED write occurs. | Deny. |

An implementation must test negative paths, not just the happy path.

[Back to top](#top)

---

## Identity, time, rights, and sensitivity

### Identity

- Stable IDs must come from governed contracts, registries, or deterministic rules.
- A display name, URL, taxon label, filename, or map feature ID is not automatically a stable source or record identity.
- Deduplication must preserve provenance and must not silently merge distinct source roles.
- The implementation must record the versions of contracts, schemas, policy, and descriptors used.

### Time

Ingest must not collapse:

- source publication time;
- retrieval time;
- observation or event time;
- valid time;
- processing time;
- catalog time;
- release time.

Unknown or source-ambiguous time semantics must remain labeled and must not be promoted into a precise claim.

### Rights and source roles

Rights and source role are independent:

- an official source may still impose restrictive terms;
- a public license does not make every claim authoritative;
- an aggregator must not be relabeled as a primary observation source;
- a payload digest proves byte identity, not permission or truth.

Unknown rights block public release and may block admission depending on the governing policy and intended use.

### Sensitivity

Rare species, archaeology, living-person data, DNA/genomic material, private-property detail, cultural or sacred context, critical infrastructure, and other exact-harm information fail closed.

Ingest must preserve restricted source detail only in approved internal homes. Redaction, generalization, aggregation, delay, or withholding for public use occurs under policy and must leave receipts. Style-only hiding is not an acceptable sensitive-data transform.

[Back to top](#top)

---

## Receipts, proofs, and finite outcomes

### Receipts are process memory

An ingest receipt may record:

- caller and run identity;
- source and descriptor references;
- input and output digests;
- timestamps and tool versions;
- checks performed;
- explicit disposition and reason codes;
- RAW or QUARANTINE references;
- failures, retry posture, and correction lineage.

It does not prove source truth, rights approval, EvidenceBundle closure, release approval, or public safety by itself.

### Proof remains separate

EvidenceBundle and proof artifacts belong under `data/proofs/`. Ingest may preserve evidence references, but it must not generate a claim that its own receipt is sufficient evidence.

### Finite outcomes

The repository did not establish an accepted shared-ingest outcome enum at the pinned snapshot. The final vocabulary and machine shape are therefore **UNKNOWN**.

Any future contract must nevertheless:

- use a finite, documented set of outcomes;
- distinguish successful RAW admission from quarantine, hold, denial, and execution error;
- include stable reason codes;
- make partial or unknown state explicit;
- prohibit default-allow behavior;
- define retry and idempotency semantics.

This README intentionally does not invent canonical enum values.

[Back to top](#top)

---

## Implementation admission criteria

Do not add trust-bearing code here until a change provides or references all applicable items below.

### Required with the first executable slice

- [ ] A named shared responsibility used by at least two domain lanes.
- [ ] An accepted entrypoint and invocation contract.
- [ ] Versioned object meaning and machine shape, or explicit references to existing authorities.
- [ ] A resolved writer boundary for RAW and QUARANTINE.
- [ ] Synthetic, public-safe, no-network fixtures.
- [ ] Valid, invalid, restricted, ambiguous-rights, missing-role, digest-mismatch, and retry cases.
- [ ] Deterministic output and receipt expectations.
- [ ] Tests for no WORK/PROCESSED/CATALOG/PUBLISHED shortcut.
- [ ] Tests for no direct public or release side effects.
- [ ] Source, rights, sensitivity, evidence, pipeline, and security review as applicable.
- [ ] CI wiring with explicit permissions and no publication credentials.
- [ ] Correction, rollback, and disable instructions.
- [ ] Updated README maturity and evidence ledger.

### Placement recheck

Before adding a helper, compare it with:

- `packages/` for broadly reusable library behavior;
- `tools/validators/` for reusable validation authority;
- `connectors/` for source-specific behavior;
- `pipelines/domains/<domain>/` for domain-owned behavior;
- `pipeline_specs/` for declarative configuration.

Do not create a parallel implementation merely because this README names a possible responsibility.

[Back to top](#top)

---

## Testing and validation

### Current execution status

There is no verified shared-ingest quickstart command in this directory. Do not document a runnable command until its entrypoint, dependencies, fixtures, side effects, and expected outputs are present and tested.

### Repository-level checks

The repository currently defines:

~~~bash
make validate
make boundary-guards
~~~

These commands are repository-wide checks. They are not a shared-ingest runtime and do not prove all gates in this README.

At the pinned snapshot:

- `make validate` delegates to schema and contract test surfaces;
- `make boundary-guards` includes a connector/pipeline non-publisher boundary test;
- the documentation link-check workflow is an explicit readiness hold and does not actually validate README links;
- no dedicated `tests/pipelines/ingest/README.md` or `fixtures/ingest/README.md` was confirmed.

### Minimum future test matrix

| Family | Required cases |
|---|---|
| Source identity | resolved descriptor; missing descriptor; wrong source; inactive source |
| Integrity | matching digest; mismatch; missing manifest; size/media-type conflict |
| Rights/citation | allowed; restricted; unknown; missing attribution |
| Source role | preserved role; unknown role; prohibited role escalation |
| Time | complete fields; ambiguous source-vintage; contradictory event/retrieval time |
| Sensitivity | public-safe; generalized-only; restricted; exact-harm geometry |
| Lifecycle | RAW admission; QUARANTINE; no direct WORK/PROCESSED/PUBLISHED write |
| Idempotency | replay; duplicate run ID; same payload with changed descriptor |
| Failure | validation error; policy unavailable; interrupted write; receipt failure |
| Security | path traversal; unsafe archive; hostile metadata; secret leakage |

### Documentation validation for this README

Reviewers should verify:

1. exactly one H1;
2. one complete KFM metadata wrapper;
3. balanced fenced blocks;
4. valid relative links;
5. no proposed file presented as implemented;
6. no command presented as an ingest quickstart;
7. no receipt, proof, or release authority collapse;
8. rendered Mermaid readability.

[Back to top](#top)

---

## Correction and rollback

### Documentation correction

If repository evidence changes:

1. pin the new evidence snapshot;
2. update the observed-state table;
3. move claims between **CONFIRMED**, **PROPOSED**, **CONFLICTED**, and **UNKNOWN**;
4. preserve the former statement in the changelog when materially significant;
5. record unresolved structural conflict in the drift register or an ADR when required.

### Implementation rollback

A future ingest implementation must define:

- how to disable the entrypoint;
- how to stop new writes without deleting history;
- how incomplete RAW or QUARANTINE artifacts are labeled;
- how receipts preserve the failed attempt;
- how retries avoid duplicate admissions;
- how downstream consumers are notified;
- how a bad implementation is reverted without rewriting prior source captures.

Release rollback remains under `release/`. Removing or reverting ingest code is not equivalent to withdrawing a published artifact.

[Back to top](#top)

---

## Evidence ledger

| Evidence | What it supports | Truth posture |
|---|---|---:|
| `docs/architecture/directory-rules.md` | Responsibility-root rules; `pipelines/` versus `pipeline_specs/`; shared `ingest/` lane; lifecycle and Domain Placement Law. | **CONFIRMED live file; document status review** |
| Supplied Directory Rules PDF | Same placement and lifecycle doctrine, including connector RAW/QUARANTINE outputs. | **CONFIRMED supplied source** |
| Supplied Pipeline Living Implementation Manual v0.3 | Fail-closed, receipt-emitting, fixture-first pipeline design; source role, rights, sensitivity, and finite outcomes. | **CONFIRMED supplied doctrine; implementation proposals remain proposed** |
| Supplied Unified Implementation Architecture Build Manual | Trust membrane, no raw public path, source-ledger-first, no autopublish, correction and rollback posture. | **CONFIRMED supplied doctrine** |
| `main@13e1b27b...` exact file reads | Target, parent/domain/spec roots, Fauna child, source contract/schema, registry, lifecycle, receipt, and proof documentation. | **CONFIRMED bounded repository evidence** |
| Exact probes listed above | Named proposed shared helpers and dedicated spec/test/fixture README paths did not resolve. | **CONFIRMED bounded absence** |
| `Makefile` and relevant PR workflows | Repository-level validation commands and workflow permission/readiness posture. | **CONFIRMED files; runtime results not implied** |

Evidence limits:

- no runtime ingest execution was performed;
- no live connector was invoked;
- no source payload, restricted record, or credential was accessed;
- no complete recursive inventory was available through the bounded connector reads;
- no branch-protection settings or deployment environment were inspected;
- no human review or release decision is implied.

[Back to top](#top)

---

## Related repository surfaces

| Surface | Relationship |
|---|---|
| [`../README.md`](../README.md) | Parent executable-pipeline boundary. |
| [`../domains/README.md`](../domains/README.md) | Canonical parent for domain-owned pipeline execution. |
| [`fauna/README.md`](fauna/README.md) | Confirmed compatibility child; not a precedent for new domain children. |
| [`../../docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md) | Live placement doctrine and lifecycle boundaries. |
| [`../../docs/architecture/domain-placement-law.md`](../../docs/architecture/domain-placement-law.md) | Domain responsibility placement guidance. |
| [`../../pipeline_specs/README.md`](../../pipeline_specs/README.md) | Declarative pipeline configuration root. |
| [`../../connectors/README.md`](../../connectors/README.md) | Source-specific fetch and source-edge responsibility. |
| [`../../contracts/source/README.md`](../../contracts/source/README.md) | Source object meaning and contract boundary. |
| [`../../schemas/contracts/v1/source/README.md`](../../schemas/contracts/v1/source/README.md) | Versioned source machine-shape boundary. |
| [`../../policy/rights/README.md`](../../policy/rights/README.md) | Rights admissibility responsibility. |
| [`../../policy/sensitivity/README.md`](../../policy/sensitivity/README.md) | Sensitivity policy responsibility. |
| [`../../data/registry/sources/README.md`](../../data/registry/sources/README.md) | Source registry and descriptor authority. |
| [`../../data/receipts/ingest/README.md`](../../data/receipts/ingest/README.md) | Ingest process-memory lane. |
| [`../../data/proofs/evidence_bundle/README.md`](../../data/proofs/evidence_bundle/README.md) | Separate EvidenceBundle proof authority. |
| [`../../docs/standards/RUN_RECEIPT.md`](../../docs/standards/RUN_RECEIPT.md) | Repository run-receipt standard. |

[Back to top](#top)

---

## Open questions

| ID | Question | Status |
|---|---|---:|
| `PIPE-INGEST-001` | Which concrete responsibility is shared by two or more domain ingest lanes and should be implemented here first? | **UNKNOWN** |
| `PIPE-INGEST-002` | Should shared ingest write RAW/QUARANTINE or return a deterministic disposition to connector/domain callers? | **NEEDS ADR or accepted contract review** |
| `PIPE-INGEST-003` | Which existing contract and schema define source-intake and ingest-disposition records? | **NEEDS VERIFICATION** |
| `PIPE-INGEST-004` | What finite outcome and reason-code vocabulary is accepted for ingest? | **UNKNOWN** |
| `PIPE-INGEST-005` | Does a shared declarative spec belong at `pipeline_specs/ingest/` or elsewhere under the existing spec root? | **UNKNOWN** |
| `PIPE-INGEST-006` | What are the accepted dedicated test and fixture homes for shared ingest? | **UNKNOWN** |
| `PIPE-INGEST-007` | Which receipt subtype and schema record shared ingest without creating a parallel receipt authority? | **NEEDS VERIFICATION** |
| `PIPE-INGEST-008` | Which CI check will prove shared admission, idempotency, quarantine, and no-publish behavior? | **UNKNOWN** |
| `PIPE-INGEST-009` | Which owners replace the metadata placeholders and review the first trust-bearing implementation? | **UNKNOWN** |
| `PIPE-INGEST-010` | Is the Fauna compatibility child temporary, and what migration event removes it? | **CONFLICTED / NEEDS DECISION** |

[Back to top](#top)

---

## Maintenance

Re-review this README when:

- a shared ingest executable is added;
- an accepted ingest contract, schema, or outcome vocabulary appears;
- `pipeline_specs/` accepts a shared-ingest layout;
- dedicated fixtures, tests, or CI wiring appear;
- connector writer responsibility changes;
- a new domain child is proposed under this directory;
- receipt placement or naming is resolved;
- Directory Rules or Domain Placement Law changes;
- a source, rights, sensitivity, public, release, correction, or rollback boundary changes.

### Last reviewed

- Date: 2026-07-20
- Evidence snapshot: `main@13e1b27bf8cc4fdd4d88305532e69c444c07a4b5`
- Prior target blob: `da14498b6a94c0aa52ebe73d5c4d7056e9f7011e`
- Runtime execution: **NOT RUN**
- Shared ingest implementation: **NOT CONFIRMED**
- Human approval: **PENDING**

### Changelog

| Version | Date | Change |
|---|---|---|
| `v0.2` | 2026-07-20 | Regrounded the README in live repository evidence; distinguished valid placement from implementation; removed speculative tree-as-implementation guidance; recorded exact-path absences; clarified domain placement, caller/writer boundaries, evidence limits, validation, correction, and rollback. |
| `v0.1` | 2026-06-13 | Established the initial shared-ingest documentation contract. |

---

KFM rule: shared ingest may help decide whether source-bound material is eligible for governed RAW admission or must fail closed. It cannot turn a source fetch, hash, receipt, schema pass, or generated summary into evidence, processed truth, release approval, or public truth.

[Back to top](#top)
