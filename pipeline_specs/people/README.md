<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-people-readme
title: pipeline_specs/people/ — People Pipeline Specification Compatibility Alias
type: readme
version: v0.2
status: draft; repository-grounded; compatibility-alias; readme-only; no-active-alias-specification-established
owners: OWNER_TBD — Pipeline-spec steward · People/DNA/Land domain steward · Living-person privacy steward · Consent and revocation steward · DNA/genomic steward · Land-records steward · Evidence steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-13
updated: 2026-07-17
supersedes: v0.1
policy_label: restricted-doctrine; people; genealogy; dna; genomic; consent; revocation; land-ownership; living-person-sensitive; private-person-parcel-deny-default; declarative-only; compatibility-alias; no-secrets; no-live-activation; no-public-path; no-publication; release-gated
current_path: pipeline_specs/people/README.md
truth_posture: CONFIRMED current target file, parent pipeline-spec root contract, canonical People/DNA/Land companion lane, five inert canonical stage YAML stubs, README-only checked alias inventory, executable alias boundary, Directory Rules placement conflict, proposed schema-home ADR, CODEOWNERS route, and TODO-only People/DNA/Land workflow / PROPOSED alias contract, future machine validation, deterministic canonical binding, finite state model, source-role and rights gates, assertion boundaries, living-person classification, consent/revocation/retention requirements, DNA/genomic restrictions, title boundaries, finite outcomes, validation matrix, correction, deactivation, and rollback behavior / UNKNOWN accepted alias ADR, canonical pipeline-spec schema, parser, registry, loader, scheduler, alias activation semantics, source activation, active alias profiles, substantive alias fixtures/tests, validator wiring, receipt emission, branch-protection enforcement, release integration, and production use / NEEDS VERIFICATION owners, exhaustive recursive directory inventory, accepted people versus people-dna-land migration decision, exact source-role enum, consent authority, living-person determination, DNA tokenization and retention controls, title-interest rules, correction propagation, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: "dc30140567828b45d54426b0e55055ef8d83b5a7"
  prior_blob: 205ff71859698f66b0f0243e3ed7c62c2d0ca78c
  authoring_prompt_sha256: b061d3d8b153af8083cd1f62f447b389c396b5a882e590328ede7c3e3ff25e85
  confirmed_alias_files:
    - pipeline_specs/people/README.md
  checked_absent_alias_paths:
    - pipeline_specs/people/ingest.yaml
    - pipeline_specs/people/assertions.yaml
    - pipeline_specs/people/validate.yaml
    - pipeline_specs/people/watchers.yaml
    - pipeline_specs/people/rollback.yaml
    - tests/pipeline_specs/people/README.md
    - fixtures/pipeline_specs/people/README.md
  confirmed_canonical_companion_files:
    - pipeline_specs/people-dna-land/README.md
    - pipeline_specs/people-dna-land/ingest.yaml
    - pipeline_specs/people-dna-land/normalize.yaml
    - pipeline_specs/people-dna-land/validate.yaml
    - pipeline_specs/people-dna-land/catalog.yaml
    - pipeline_specs/people-dna-land/publish.yaml
  canonical_stage_posture: "all five checked canonical YAML files contain stages: []"
  workflow_posture: .github/workflows/domain-people-dna-land.yml exists as a pull_request/main-push TODO-only echo scaffold
related:
  - ../README.md
  - ../people-dna-land/README.md
  - ../../pipelines/domains/people/README.md
  - ../../pipelines/domains/people-dna-land/README.md
  - ../../docs/architecture/directory-rules.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/domains/people-dna-land/CANONICAL_PATHS.md
  - ../../docs/domains/people-dna-land/people.md
  - ../../.github/workflows/domain-people-dna-land.yml
  - ../../data/receipts/generated/README.md
  - ../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, pipeline-specs, people, people-dna-land, compatibility-alias, assertion-first, genealogy, living-person, privacy, consent, revocation, dna-boundary, land-title-boundary, evidence, receipts, governance, no-parallel-authority]
notes:
  - "v0.2 replaces planning-heavy alias-file proposals with a commit-pinned account of the current README-only alias lane and its inert canonical companion scaffolds."
  - "The governing domain segment is people-dna-land under the current path register; people remains a compatibility alias unless an accepted ADR and migration record change that boundary."
  - "File presence, valid YAML, a workflow conclusion, or an alias reference does not establish activation, source admission, consent, evidence closure, policy approval, release approval, or publication."
  - "Living-person identifiers, DNA/genomic material, raw kit/vendor identifiers, exact sensitive locations, private person-parcel joins, unresolved title claims, and unclear-rights sources fail closed by default."
  - "This revision changes documentation and generated process provenance only. It does not create or activate pipeline specs, schemas, policies, sources, fixtures, tests, executable logic, lifecycle objects, receipts, proofs, releases, or public surfaces."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People Pipeline Specification Compatibility Alias

`pipeline_specs/people/`

> **One-line purpose.** Preserve `pipeline_specs/people/` as a documented compatibility alias for narrowly scoped People declarations while keeping all pipeline-spec authority, sensitive-domain controls, activation, execution, evidence, policy, and release decisions subordinate to the governed People / Genealogy / DNA / Land lane.

![status](https://img.shields.io/badge/status-repository--grounded%20draft-orange)
![version](https://img.shields.io/badge/version-v0.2-informational)
![inventory](https://img.shields.io/badge/alias%20inventory-README--only-lightgrey)
![authority](https://img.shields.io/badge/authority-compatibility%20alias-critical)
![canonical](https://img.shields.io/badge/canonical%20segment-people--dna--land-6a1b9a)
![sensitivity](https://img.shields.io/badge/sensitivity-deny%20by%20default-critical)
![activation](https://img.shields.io/badge/active%20alias%20specs-none%20established-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> [!IMPORTANT]
> **Repository evidence snapshot:** `main@dc30140567828b45d54426b0e55055ef8d83b5a7`. The checked alias lane contains this README and no checked YAML profile. The governing sibling lane contains `README.md` plus `ingest.yaml`, `normalize.yaml`, `validate.yaml`, `catalog.yaml`, and `publish.yaml`; each checked YAML file currently has `stages: []`. These facts establish scaffold presence only. They do not establish an accepted schema, active spec, executable consumer, admitted source, consent decision, evidence closure, release readiness, or publication.

> [!CAUTION]
> A shorter path is not a lighter governance path. A Person Assertion is not a canonical person. A Relationship Hypothesis is not a confirmed relationship. DNA evidence is not public kinship truth. A consent reference is not perpetual authorization. An assessor record is not title truth. Parcel geometry is not title-boundary proof. A successful check is not an `EvidenceBundle`, `PolicyDecision`, `ReleaseManifest`, correction, or rollback.

> [!WARNING]
> Do not place real living-person identifiers, raw DNA or genomic material, kit or vendor identifiers, private person-to-parcel joins, exact sensitive locations, unredacted restricted instruments, credentials, secrets, or unreleased lifecycle data in this directory, examples, fixtures, logs, screenshots, issues, or pull-request bodies.

## Quick navigation

- [Purpose and audience](#purpose-and-audience)
- [Authority and repository fit](#authority-and-repository-fit)
- [Current inspected inventory](#current-inspected-inventory)
- [Bounded context and ubiquitous language](#bounded-context-and-ubiquitous-language)
- [Owned responsibility and explicit non-ownership](#owned-responsibility-and-explicit-non-ownership)
- [Interfaces and trust membrane](#interfaces-and-trust-membrane)
- [Sources, rights, consent, privacy, and sensitivity](#sources-rights-consent-privacy-and-sensitivity)
- [Identity, assertion, and temporal semantics](#identity-assertion-and-temporal-semantics)
- [Lifecycle and finite outcomes](#lifecycle-and-finite-outcomes)
- [Future alias specification contract](#future-alias-specification-contract)
- [Directory and sublane discipline](#directory-and-sublane-discipline)
- [Inputs, outputs, and dependencies](#inputs-outputs-and-dependencies)
- [Validation, fixtures, and workflow maturity](#validation-fixtures-and-workflow-maturity)
- [Watchers, dry runs, and no-op discipline](#watchers-dry-runs-and-no-op-discipline)
- [Evidence, receipts, release, correction, and rollback](#evidence-receipts-release-correction-and-rollback)
- [Review and change discipline](#review-and-change-discipline)
- [Definition of done](#definition-of-done)
- [Open verification register](#open-verification-register)
- [Evidence ledger](#evidence-ledger)

---

## Purpose and audience

`pipeline_specs/people/` is a compatibility boundary inside the canonical `pipeline_specs/` responsibility root.

Its safe purpose is narrow:

- explain why the `people` segment exists beside `people-dna-land`;
- prevent the alias from becoming a second source of pipeline-spec authority;
- define the minimum governance burden for any future alias artifact;
- point maintainers to the governing People / Genealogy / DNA / Land specification and executable lanes;
- preserve assertion-first, consent-aware, privacy-safe, DNA-safe, title-safe, evidence-bound, and reversible behavior;
- record current repository evidence and unresolved decisions without upgrading plans into implementation facts.

This README is for pipeline-spec maintainers, People/DNA/Land domain stewards, privacy and consent reviewers, DNA/genomic and land-record reviewers, source and rights stewards, evidence and policy reviewers, validation and release maintainers, CI maintainers, and coding agents.

It does **not** create a new bounded context, machine schema, parser, registry, active profile, source admission, pipeline implementation, lifecycle transition, policy decision, release decision, or public interface.

[Back to top](#top)

---

## Authority and repository fit

### Responsibility split

```text
pipeline_specs/  = declarative run intent: WHAT may run and under which gates
pipelines/       = executable behavior: HOW processing occurs
connectors/      = source retrieval and admission support; never publication
contracts/       = semantic meaning
schemas/         = machine-checkable shape
policy/          = admissibility, rights, consent, privacy, sensitivity, and release obligations
tests/fixtures/  = enforceability proof and controlled synthetic or redacted examples
data/            = lifecycle state, registries, consent/revocation state, receipts, proofs, catalogs, triplets, and published artifacts
release/         = release, correction, withdrawal, supersession, and rollback authority
apps/            = governed serving surfaces; never direct consumers of alias specs or internal stores
```

Directory Rules place declarative pipeline configuration under `pipeline_specs/` and executable behavior under `pipelines/`. Domain names appear as segments inside responsibility roots, not as repository roots.

### Alias relationship

| Surface | Current role | Status |
|---|---|---|
| [`pipeline_specs/README.md`](../README.md) | Root contract for declarative pipeline configuration. | **CONFIRMED** |
| [`pipeline_specs/people-dna-land/README.md`](../people-dna-land/README.md) | Governing whole-domain People / Genealogy / DNA / Land specification boundary. | **CONFIRMED file / draft authority boundary** |
| `pipeline_specs/people/README.md` | Compatibility alias documentation; no checked active alias profile. | **CONFIRMED file / README-only checked inventory** |
| [`pipelines/domains/people-dna-land/README.md`](../../pipelines/domains/people-dna-land/README.md) | Governing whole-domain executable pipeline boundary. | **CONFIRMED file** |
| [`pipelines/domains/people/README.md`](../../pipelines/domains/people/README.md) | Executable compatibility alias; subordinate to the whole-domain lane. | **CONFIRMED file / compatibility boundary** |
| [`CANONICAL_PATHS.md`](../../docs/domains/people-dna-land/CANONICAL_PATHS.md) | Current domain path register; uses `people-dna-land` as the domain segment and records alternate `people` naming as conflict. | **CONFIRMED file / draft path register** |
| Accepted alias ADR | Decision authorizing independent alias specs or migration. | **UNKNOWN / not found by bounded search** |

> [!IMPORTANT]
> Until an accepted ADR, path map, migration record, compatibility contract, and rollback plan say otherwise, `people-dna-land` is the governing segment and `people` remains an alias. This README must not be cited as authority to duplicate schemas, contracts, policies, source registries, lifecycle stores, receipts, proofs, releases, or public routes.

### Directory Rules conflict

Two live Directory Rules artifacts were inspected:

- [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md);
- [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md).

They share the placement doctrine relevant here: `pipeline_specs/` owns declarative configuration and a domain is a segment inside a responsibility root. Their own canonical-document placement remains an unresolved repository conflict. This revision does not resolve that conflict or create a third copy.

[Back to top](#top)

---

## Current inspected inventory

### Alias lane

The bounded repository search and direct-path probes found:

```text
pipeline_specs/people/
└── README.md    # CONFIRMED
```

The following checked paths were absent at the evidence snapshot:

```text
pipeline_specs/people/ingest.yaml
pipeline_specs/people/assertions.yaml
pipeline_specs/people/validate.yaml
pipeline_specs/people/watchers.yaml
pipeline_specs/people/rollback.yaml
tests/pipeline_specs/people/README.md
fixtures/pipeline_specs/people/README.md
```

**Interpretation:** no active alias specification, fixture suite, or alias-specific validation surface was established by the checked paths. This is a bounded finding, not proof that every imaginable nested path was exhaustively enumerated.

### Governing companion lane

The checked sibling lane contains:

```text
pipeline_specs/people-dna-land/
├── README.md
├── ingest.yaml
├── normalize.yaml
├── validate.yaml
├── catalog.yaml
└── publish.yaml
```

Each checked YAML file currently contains a name, `version: 1`, and `stages: []`.

**Interpretation:** these are inert scaffolds. A filename, YAML parse, empty stage list, merge, workflow conclusion, or future schedule does not activate a source or pipeline and does not satisfy evidence, policy, consent, validation, release, correction, or rollback gates.

### Workflow evidence

[`domain-people-dna-land.yml`](../../.github/workflows/domain-people-dna-land.yml) currently runs on pull requests and pushes to `main`, but its three jobs only echo TODO messages. It has no checked alias-specific validation command and no evidence that branch protection requires its job names.

[Back to top](#top)

---

## Bounded context and ubiquitous language

The governing bounded context is **People / Genealogy / DNA / Land Ownership**. The `people` alias may describe only a carefully bounded People sublane and inherits the whole context's definitions and controls.

| Term | Meaning preserved by this alias |
|---|---|
| `Person Assertion` | An evidence-bound claim about a person; not a canonical identity or public fact. |
| `Person Identity Candidate` | A proposed grouping or match requiring review; not `PersonCanonical`. |
| `PersonCanonical` | A reviewed identity state whose exact promotion and release rules remain governed outside this alias. |
| `NameAssertion` | An asserted name with source, time, and evidence; not identity proof by itself. |
| `LifeEvent` | An asserted event such as birth, death, marriage, residence, or migration, with distinct temporal fields and source support. |
| `RelationshipAssertion` | An evidence-bound asserted relationship. |
| `RelationshipHypothesis` | A candidate inference that must not be presented as confirmed. |
| `FamilyGroup` | A review grouping of assertions; not automatic kinship truth. |
| `DNA Match Evidence` | Restricted observation evidence; not a confirmed relationship and never public merely because it is referenced. |
| `ConsentGrant` | Purpose-, scope-, subject-, time-, and data-bound authorization; not perpetual or unrestricted permission. |
| `RevocationReceipt` | Auditable evidence that a revocation was received and handled; exact canonical shape is **NEEDS VERIFICATION**. |
| `LandInstrument` | A deed, title, mortgage, lien, easement, lease, probate, or related instrument carrying source-specific legal weight. |
| `Assessor Record` | Administrative or tax evidence; not title truth. |
| `Parcel Version` | A versioned spatial representation; not title-boundary proof. |
| `Ownership Assertion` | A source- and time-scoped claim about an interest; not a final legal determination. |
| `EvidenceRef` / `EvidenceBundle` | A reference and resolved evidence package required where claims depend on evidence. |
| `ReleaseManifest` | Release-state record owned outside this directory; spec text cannot substitute for it. |

The exact field names, enums, identity rules, and machine schemas remain subordinate to accepted contracts and schemas. This README defines maintenance boundaries, not canonical object shape.

[Back to top](#top)

---

## Owned responsibility and explicit non-ownership

### What this alias README owns

This README may:

- explain the compatibility status of `pipeline_specs/people/`;
- describe what a future alias profile would have to reference and preserve;
- record checked repository evidence and verification gaps;
- require a deterministic link to the governing `people-dna-land` profile or registry entry;
- require explicit source, rights, consent, privacy, evidence, policy, review, receipt, release, correction, and rollback gates;
- define contributor and reviewer checks that prevent parallel authority.

### What the directory may contain now

The only currently supported content is compatibility documentation.

A future non-README alias artifact is **PROPOSED** and should not be added until an accepted decision establishes:

1. why the alias is required;
2. which canonical spec identity it aliases;
3. which parser and registry recognize it;
4. how duplicate or conflicting profiles are rejected;
5. how activation, suspension, supersession, and deactivation work;
6. where tests and fixtures live;
7. how rollback removes the alias without changing canonical behavior.

### What this directory does not own

| Do not place or decide here | Owning responsibility |
|---|---|
| Executable pipeline code | `pipelines/`, primarily the governing `people-dna-land` lane |
| Source clients and retrieval logic | `connectors/` |
| Source admission or source authority | source registry, policy, review, and connector admission surfaces |
| Object meaning | `contracts/` |
| Machine shape | `schemas/`, with current proposed schema-home direction under `schemas/contracts/v1/` |
| Privacy, consent, DNA, rights, sensitivity, retention, or release policy | `policy/` and authorized review processes |
| Production or lifecycle data | the correct phase under `data/` |
| Consent or revocation state | accepted governed state under `data/` and policy-owned controls |
| Receipts and proofs | `data/receipts/` and `data/proofs/` |
| Catalog or triplet truth | governed catalog/triplet lanes under `data/` |
| Release, correction, withdrawal, or rollback decisions | `release/` |
| Public API, map, UI, export, or AI code | governed application and package roots |
| Living-person, DNA, title, or legal determinations | authorized evidence, policy, review, and legal/steward processes outside this alias |

[Back to top](#top)

---

## Interfaces and trust membrane

### Internal interfaces

A future alias artifact may reference, but must not replace:

- an accepted canonical People/DNA/Land pipeline-spec identity;
- one verified executable consumer under `pipelines/`;
- admitted `SourceDescriptor` identifiers;
- semantic contracts and machine schemas;
- policy bundle or decision references;
- deterministic fixtures and expected outcomes;
- receipt and proof requirements;
- release-candidate, correction, and rollback requirements.

The alias must not be a hidden fallback. Consumers should reject an alias artifact when its canonical target, version, digest, owner, state, or compatibility relationship cannot be resolved.

### Public interfaces

There is no public interface to `pipeline_specs/people/`.

Public clients must not:

- read this directory as data;
- infer that a person, relationship, DNA match, ownership interest, or parcel claim is true from a spec;
- bypass the governed API;
- read RAW, WORK, QUARANTINE, candidate, canonical, consent, or internal stores;
- receive unreleased fields or geometry;
- receive generated language without evidence, policy, review, citation, release, stale-state, and correction handling.

Any public-safe People derivative must be produced through the governing lifecycle and released through governed interfaces. This README is not an activation endpoint, source registry, policy service, evidence resolver, or release API.

[Back to top](#top)

---

## Sources, rights, consent, privacy, and sensitivity

### Source-role anti-collapse

A future alias spec must reference source descriptors by stable identifier and preserve source role. Exact canonical source-role enum values remain **NEEDS VERIFICATION**.

At minimum, processing must distinguish:

- authoritative or primary evidence from corroborating evidence;
- contextual sources from claim-supporting sources;
- administrative records from legal/title evidence;
- modeled or generated candidates from observations;
- restricted sources from public-safe sources;
- source availability from permitted use;
- citation availability from redistribution rights.

Disallowed shortcuts:

```text
source listed in spec -> source admitted
source accessible -> source permitted for use
obituary or tree overlay -> canonical identity
DNA match -> confirmed relationship
assessor record -> title truth
parcel geometry -> title boundary
successful retrieval -> current or complete evidence
```

### Living-person privacy

Living-person status and uncertainty are policy-significant. A future profile must fail closed when living/deceased classification cannot be established strongly enough for the requested purpose and release tier.

The spec must not carry real personal data. It may carry identifiers for approved policies, source descriptors, schemas, or fixtures, but not the sensitive subject records themselves.

### Consent and revocation

Where consent applies, a future profile must require checks for:

- authorized subject or authority;
- allowed purpose and audience;
- data categories and operations covered;
- geographic and temporal scope;
- effective, expiry, and retention dates;
- downstream use and disclosure limits;
- revocation status at use, recompile, export, and release time;
- deletion, withdrawal, or correction obligations;
- an auditable consent/revocation decision or receipt reference.

A cached consent result must not override a later revocation.

### DNA and genomic material

Raw sequences, segments, kit identifiers, vendor identifiers, match lists, triangulation details, and derived relationship outputs do not belong in this directory or public examples.

A future alias profile that touches DNA-derived evidence must remain subordinate to the restricted whole-domain lane and require:

- purpose-limited and consent-aware use;
- tokenized or indirect references;
- retention and deletion controls;
- no public raw or row-level output;
- no conversion of probabilistic evidence into confirmed kinship;
- policy and specialist review before any derivative exposure.

### Land and title

Land-related context must preserve:

```text
assessor or tax record != title truth
parcel geometry != legal title boundary
recorded instrument != complete current ownership without chain and time review
person-parcel join != public ownership truth
```

Private joins, unresolved interests, exact sensitive locations, and ambiguous rights fail closed.

[Back to top](#top)

---

## Identity, assertion, and temporal semantics

### Identity

A future alias spec should have deterministic identity derived from an accepted canonical spec identity and version, not from filename alone.

It should bind, at minimum:

- canonical target spec or profile identifier;
- alias identifier;
- schema and contract versions;
- content or spec digest;
- owner and review state;
- compatibility and supersession state;
- executable consumer identifier;
- source descriptor set and policy profile set.

The exact digest and canonicalization rules remain **NEEDS VERIFICATION** until an accepted contract or ADR defines them.

### Assertion state

A future profile must preserve distinct states such as:

```text
asserted
candidate
reviewed
canonical or accepted for a bounded purpose
restricted
released public-safe derivative
superseded
withdrawn
```

This list is conceptual, not a canonical enum. No transition may be inferred from alias presence or pipeline success alone.

### Time

Where material, a future profile must keep these times distinct:

- event or observation time;
- valid time;
- source publication or record time;
- source vintage;
- retrieval time;
- processing time;
- review time;
- consent effective, expiry, and revocation time;
- release time;
- correction, supersession, withdrawal, and rollback time.

A missing or stale time dimension must produce a bounded negative outcome rather than a current-tense claim.

[Back to top](#top)

---

## Lifecycle and finite outcomes

The governing lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare intended inputs, outputs, prerequisites, and blockers. It does not perform promotion merely by existing.

### Stage obligations

| Stage | Alias-related obligation |
|---|---|
| Pre-RAW / admission edge | Resolve source descriptor, role, rights, sensitivity, access, citation, and permitted use before intake. |
| RAW | Preserve immutable source payload or reference and retrieval provenance outside this directory. |
| WORK | Normalize assertions, identity candidates, time, consent references, and rights posture without upgrading claims. |
| QUARANTINE | Hold malformed, ambiguous, restricted, revoked, unsupported, or policy-blocked material with a reason. |
| PROCESSED | Emit validated, evidence-linked, still-governed records and receipts; not public truth. |
| CATALOG / TRIPLET | Emit governed projections only after evidence and catalog closure; graph edges remain projections. |
| PUBLISHED | Require policy, review, release manifest, public-safe transform, correction path, and rollback target. |

### Finite outcomes

Exact canonical enums remain **NEEDS VERIFICATION**. A safe implementation must nevertheless terminate explicitly rather than guess. Expected outcome families include:

| Outcome family | Meaning |
|---|---|
| Candidate success | Produce a bounded candidate or processed output for the next governed gate; never imply publication. |
| `NO_OP` | No material, eligible, or newly supported change; emit an auditable no-op result where required. |
| `HOLD` / `QUARANTINE` | More evidence, rights, consent, sensitivity, identity, temporal, or review work is required. |
| `ABSTAIN` | The requested claim or transform cannot be supported strongly enough. |
| `DENY` | Policy, consent, rights, sensitivity, access, or release posture forbids the action. |
| `ERROR` | Operational or contract failure; do not silently downgrade to allow. |

A watcher, parser, workflow, pipeline, model, or alias resolver must not convert `HOLD`, `ABSTAIN`, `DENY`, or `ERROR` into success.

[Back to top](#top)

---

## Future alias specification contract

No accepted alias machine schema or active profile was verified. The following is a **PROPOSED review contract**, not canonical YAML.

A future alias artifact should be rejected unless it can resolve all of these:

| Contract area | Minimum requirement |
|---|---|
| Identity | Stable alias ID, accepted canonical target ID, version, digest, owner, state, and lineage. |
| Authority | Explicit statement that the alias has no independent semantic, schema, policy, source, evidence, or release authority. |
| Consumer | One verified executable consumer and supported version range. |
| Sources | Admitted source descriptor references, source roles, rights, citation, access, and freshness requirements. |
| Scope | Named People sublane and explicit exclusion of whole-domain DNA or land authority unless separately approved. |
| Assertions | Distinct asserted, candidate, reviewed, canonical, restricted, and released-derivative states. |
| Privacy | Living-person classification and fail-closed uncertainty behavior. |
| Consent | Purpose, scope, expiry, revocation, retention, and deletion obligations where applicable. |
| DNA | Restricted reference-only posture, no raw data in spec, and no public kinship inference. |
| Land | Instrument/source role, temporal interest, assessor/title separation, and parcel/title-boundary separation. |
| Time | Observation/event, valid, source-vintage, retrieval, processing, review, consent, release, and correction times. |
| Lifecycle | Allowed input/output phases, quarantine routes, and promotion prerequisites. |
| Evidence | `EvidenceRef` resolution requirements and citation behavior. |
| Policy/review | Named policy profiles, required reviewers, and finite deny/abstain/hold behavior. |
| Receipts | Run, transform, validation, consent/revocation, redaction, review, no-op, and release-readiness receipt requirements as applicable. |
| Fixtures/tests | Synthetic or irreversibly redacted valid, invalid, denied, abstain, stale, revoked, and conflict cases. |
| Release | No direct publication; required candidate, manifest, correction, withdrawal, and rollback references. |
| Deactivation | Deterministic disable, supersession, and rollback behavior if the canonical target changes or disappears. |

Illustrative relationship only:

```yaml
#PROPOSED concept — not a canonical schema or active configuration.
alias:
  segment: people
  canonical_segment: people-dna-land
  canonical_spec_ref: <accepted-spec-id>
  canonical_spec_digest: <accepted-digest>
  independent_authority: false
state: draft
activation:
  allowed: false
  reason: no-accepted-alias-contract
```

Do not copy this snippet into an active configuration until a canonical schema, parser, registry, tests, and accepted migration decision exist.

[Back to top](#top)

---

## Directory and sublane discipline

### Current directory map

```text
pipeline_specs/
├── README.md
├── people-dna-land/
│   ├── README.md
│   ├── ingest.yaml
│   ├── normalize.yaml
│   ├── validate.yaml
│   ├── catalog.yaml
│   └── publish.yaml
└── people/
    └── README.md
```

### Rules for future alias content

- Do not duplicate the five canonical stage scaffold files under `people/`.
- Do not create alias-local contracts, schemas, policies, source registries, fixtures, tests, receipts, proofs, catalogs, releases, or lifecycle stores.
- Do not create a child directory merely to mirror a canonical People/DNA/Land sublane.
- Do not add an alias YAML file until an accepted decision defines its canonical target, machine shape, validation, registry, consumer, compatibility period, and rollback.
- Prefer updating the governing `people-dna-land` lane when the requested behavior applies to the whole bounded context.
- If a narrow People-only profile is justified, its canonical ownership must be explicit and it must remain unable to bypass DNA, consent, privacy, land-title, evidence, policy, and release controls.
- Any migration must preserve history, old-to-new mapping, deprecation period, consumer compatibility, and reversal instructions.

### No parallel authority

A future alias must never become a second home for:

```text
canonical spec identity
machine schema
object meaning
policy bundle
source admission
consent or revocation state
evidence bundle
receipt or proof
catalog or triplet truth
release manifest
public API or UI route
```

[Back to top](#top)

---

## Inputs, outputs, and dependencies

### Inputs a future alias may reference

| Input class | Required posture |
|---|---|
| Canonical spec reference | Must resolve to the accepted People/DNA/Land profile and digest. |
| Source descriptors | Stable identifiers; admission, rights, and role resolved elsewhere. |
| Contracts and schemas | Canonical versions from their responsibility roots. |
| Policy profiles | Privacy, consent, DNA, rights, sensitivity, retention, and release rules. |
| Fixtures | Synthetic or irreversibly redacted; no real sensitive records. |
| Lifecycle references | Stable references to governed inputs; never embedded RAW/WORK/QUARANTINE data. |
| Review and state records | Explicit, auditable, and separate from generation. |

### Outputs

This directory emits no runtime output.

A future alias profile may describe expected outputs, but execution must place them under the correct responsibility roots:

- lifecycle records under `data/`;
- validation and run receipts under accepted receipt homes;
- evidence proofs under `data/proofs/`;
- catalog/triplet projections under governed data lanes;
- release candidates and decisions under `release/`;
- public-safe artifacts under governed published lanes;
- public responses through governed APIs.

### Dependencies

A future implementation depends on:

- an accepted canonical People/DNA/Land spec contract and schema;
- an alias or compatibility ADR/path decision;
- a parser and registry that reject ambiguity;
- a verified executable consumer;
- source descriptors and source-role policy;
- privacy, consent, DNA, rights, sensitivity, retention, and release policy;
- deterministic validation and fixtures;
- receipt, evidence, catalog, release, correction, and rollback support.

None of those dependencies is established merely by this README.

[Back to top](#top)

---

## Validation, fixtures, and workflow maturity

### Current state

| Validation surface | Current finding | Status |
|---|---|---|
| Alias README | Present and revised in place. | **CONFIRMED** |
| Alias YAML profiles | None established by checked paths. | **CONFIRMED bounded search/probes** |
| Alias fixture README | Checked path absent. | **CONFIRMED path probe** |
| Alias test README | Checked path absent. | **CONFIRMED path probe** |
| Canonical stage YAMLs | Five files present; each has `stages: []`. | **CONFIRMED** |
| Canonical spec schema | Not established by this review. | **UNKNOWN / NEEDS VERIFICATION** |
| Alias parser/registry/loader | Not established by this review. | **UNKNOWN** |
| People/DNA/Land workflow | TODO-only echo scaffold. | **CONFIRMED file / no enforcement** |
| Branch protection and required checks | Repository settings not inspected. | **UNKNOWN / NEEDS VERIFICATION** |

### Minimum future test matrix

A future alias implementation requires deterministic tests for:

1. canonical target resolution;
2. alias/canonical digest and version compatibility;
3. duplicate and conflicting profile rejection;
4. missing or inactive canonical target rejection;
5. source descriptor and source-role resolution;
6. living-person deny-by-default behavior;
7. consent expiry and revocation at use time;
8. DNA reference-only and no-public-output boundaries;
9. assertion/candidate/reviewed/canonical state separation;
10. assessor/title and parcel/title-boundary separation;
11. temporal completeness and stale-state behavior;
12. quarantine, hold, abstain, deny, error, and no-op outcomes;
13. no runtime output written beside a spec;
14. no direct public client access;
15. required receipt, evidence, release, correction, and rollback references;
16. deactivation and migration rollback.

Tests and fixtures belong under the repository's accepted canonical test and fixture lanes. Their exact alias path remains **NEEDS VERIFICATION** until the alias decision is accepted.

### Documentation-only validation

A README revision should verify:

- one H1;
- unique section headings and working internal navigation;
- balanced code fences;
- valid repository-relative links;
- no trailing whitespace and a final newline;
- no secrets, personal records, DNA material, private land joins, or exact sensitive locations;
- no claim that a TODO workflow or empty YAML scaffold enforces behavior;
- a generated work receipt with a recomputable artifact hash.

[Back to top](#top)

---

## Watchers, dry runs, and no-op discipline

No alias watcher spec was found at the checked path.

A future watcher or scheduled alias profile must:

- observe or propose; never publish;
- run against admitted source descriptors and explicit source roles;
- distinguish source availability from material change;
- preserve issue, valid, source-vintage, retrieval, and processing times;
- emit `NO_OP` when no eligible material change exists;
- quarantine or hold ambiguous, restricted, revoked, stale, malformed, or unsupported material;
- avoid secrets and live sensitive records in logs;
- use bounded retries and idempotency;
- emit candidate receipts and review signals;
- require separate validation, evidence, policy, review, release, correction, and rollback before publication;
- include a kill switch and deterministic deactivation path.

A schedule is not freshness proof. A successful watcher is not source admission, evidence closure, or release approval.

[Back to top](#top)

---

## Evidence, receipts, release, correction, and rollback

### Evidence

A future alias profile may require `EvidenceRef` and `EvidenceBundle` closure. It cannot generate authority merely by naming those objects.

Where a consequential People claim is produced, the downstream governed flow must preserve:

- source identity and role;
- spatial and temporal scope;
- assertion and identity state;
- rights, privacy, consent, DNA, land-title, and sensitivity posture;
- validation and review state;
- evidence resolution and citation;
- release and stale state;
- correction, supersession, withdrawal, and rollback lineage.

### Receipts

Expected receipt families are **PROPOSED until canonical vocabulary is verified**. Depending on the profile, requirements may include:

- source retrieval or intake receipt;
- transform and validation receipt;
- no-op or quarantine receipt;
- consent decision and revocation receipt;
- redaction or aggregation receipt;
- evidence-resolution or citation-validation record;
- review or release-readiness receipt;
- correction, withdrawal, or rollback execution receipt.

A generated work receipt for this README is process provenance only. It is not evidence that the domain behavior is implemented.

### Release and publication

This alias cannot:

- approve a release;
- write to `PUBLISHED`;
- expose a public route;
- convert a candidate into a canonical claim;
- treat merge as publication.

Any releasable derivative requires an authorized release path with policy and review decisions, release manifest, public-safe transform evidence, correction path, and rollback target.

### Correction and rollback

For this README, rollback is a Git revert restoring the prior blob.

For a future alias implementation, rollback must also address:

- alias deactivation;
- registry and loader state;
- canonical target compatibility;
- emitted candidates and receipts;
- catalog/triplet projections;
- released derivatives and caches;
- correction or withdrawal notices;
- revocation and deletion obligations;
- replay or rebuild targets.

[Back to top](#top)

---

## Review and change discipline

A change to this alias lane should use the smallest reversible scope.

Before adding any non-README file:

1. re-read both live Directory Rules artifacts and the drift register;
2. inspect current ADR status and the People/DNA/Land canonical path register;
3. search active branches and pull requests for overlapping work;
4. pin the base commit and current target blob;
5. define the canonical target, parser, registry, consumer, tests, fixtures, and rollback;
6. complete privacy, consent, DNA, land-title, rights, sensitivity, evidence, and release review;
7. record whether an ADR or migration note is required;
8. keep generation, validation, human approval, merge, release, and publication as separate states.

### Review burden

At minimum, review should include:

- `pipeline_specs/` owner;
- People/DNA/Land domain owner;
- privacy and consent reviewer;
- DNA/genomic reviewer when DNA-derived evidence is in scope;
- land-record/title reviewer when ownership or parcel context is in scope;
- evidence, policy, validation, and release reviewers as material;
- docs reviewer for README accuracy.

`CODEOWNERS` routing is not proof that these substantive reviews occurred.

[Back to top](#top)

---

## Definition of done

This README revision is complete when:

- the alias is clearly subordinate to `people-dna-land`;
- current repository inventory is separated from proposals;
- the five canonical YAML scaffolds are described accurately as inert;
- absent checked alias specs, tests, and fixtures are not presented as implemented;
- strong existing assertion, living-person, consent, DNA, assessor/title, parcel/title-boundary, evidence, release, correction, and rollback controls are preserved;
- the `pipeline_specs/` versus `pipelines/` split remains explicit;
- no new path, schema, policy, source, runtime behavior, or release authority is invented;
- repository-relative links and Markdown structure validate;
- workflow maturity and branch-protection uncertainty remain visible;
- rollback is a bounded revert;
- an AI-generated provenance receipt accompanies the change;
- the draft pull request lists acceptance outcomes and unresolved verification items.

A future alias specification is not done until an accepted decision authorizes it and its canonical binding, schema validation, parser/registry behavior, deterministic fixtures, negative tests, executable consumer, sensitive-domain controls, receipts, evidence, release, correction, deactivation, and rollback have been demonstrated.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-PEOPLE-001` | Should the alias remain README-only, become an accepted People sublane, or be retired in favor of `people-dna-land`? | **NEEDS VERIFICATION / ADR** |
| `PIPE-SPEC-PEOPLE-002` | Which contract and machine schema define canonical pipeline specs and alias relationships? | **UNKNOWN / NEEDS VERIFICATION** |
| `PIPE-SPEC-PEOPLE-003` | Which parser, registry, loader, or scheduler consumes pipeline specs? | **UNKNOWN** |
| `PIPE-SPEC-PEOPLE-004` | Which state vocabulary governs draft, review, activation, suspension, supersession, and retirement? | **NEEDS VERIFICATION** |
| `PIPE-SPEC-PEOPLE-005` | Which exact source-role enum and source-admission decision model are canonical? | **NEEDS VERIFICATION** |
| `PIPE-SPEC-PEOPLE-006` | Which authority determines living-person status and uncertainty for each release purpose? | **NEEDS VERIFICATION** |
| `PIPE-SPEC-PEOPLE-007` | Which consent, expiry, revocation, retention, deletion, and downstream-use objects are canonical and enforced? | **NEEDS VERIFICATION** |
| `PIPE-SPEC-PEOPLE-008` | Which DNA tokenization, aggregation, retention, and no-public-output controls are implemented? | **UNKNOWN / NEEDS VERIFICATION** |
| `PIPE-SPEC-PEOPLE-009` | Which legal/title review model governs instruments, interests, assessor records, parcel versions, and ownership assertions? | **NEEDS VERIFICATION** |
| `PIPE-SPEC-PEOPLE-010` | Where should alias-specific tests and fixtures live if an alias is accepted? | **NEEDS VERIFICATION / placement review** |
| `PIPE-SPEC-PEOPLE-011` | Which receipt vocabulary and evidence-resolution flow are canonical for People specs? | **NEEDS VERIFICATION** |
| `PIPE-SPEC-PEOPLE-012` | Which CI job validates People/DNA/Land specs, and is it required by branch protection? | **UNKNOWN** |
| `PIPE-SPEC-PEOPLE-013` | How are corrections, revocations, withdrawals, published derivatives, caches, and graph projections propagated and rolled back? | **NEEDS VERIFICATION** |
| `PIPE-SPEC-PEOPLE-014` | Which Directory Rules copy is canonical? | **CONFLICTED / ADR-class** |
| `PIPE-SPEC-PEOPLE-015` | Is the bounded README-only alias inventory exhaustive across the complete tree and all refs? | **NEEDS VERIFICATION** |

[Back to top](#top)

---

## Evidence ledger

| Evidence | What it supports | Boundary |
|---|---|---|
| [`pipeline_specs/README.md`](../README.md) | Root distinction between declarative specs and executable pipelines; alias listed as compatibility lane. | Draft root contract, not runtime proof. |
| [`pipeline_specs/people-dna-land/README.md`](../people-dna-land/README.md) | Governing whole-domain lane, mixed scaffold inventory, sensitivity and anti-collapse controls. | Draft documentation; active implementation remains bounded. |
| Canonical stage YAMLs in `../people-dna-land/` | Five checked files exist and each has `stages: []`. | Presence and contents only; not activation or enforcement. |
| [`pipelines/domains/people/README.md`](../../pipelines/domains/people/README.md) | Executable alias remains subordinate to the whole-domain lane. | Documentation boundary, not executable proof. |
| [`CANONICAL_PATHS.md`](../../docs/domains/people-dna-land/CANONICAL_PATHS.md) | Current path register uses `people-dna-land` and surfaces `people` naming conflict. | Draft path register; some repository presence claims remain bounded. |
| [`people.md`](../../docs/domains/people-dna-land/people.md) | Assertion-first language, domain object families, deny-default sensitivity, assessor/title and parcel/title separation. | Doctrine/domain documentation, not record-level evidence. |
| [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md) and [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) | Responsibility-root placement and the live duplicate-placement conflict. | This revision does not resolve canonical-document placement. |
| [`ADR-0001`](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Proposed machine-schema home and contract/schema/policy separation. | ADR status is `proposed`, not accepted. |
| [`DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) | Existing repository drift record and conflict-handling posture. | No new drift entry is created by this path-preserving README edit. |
| [`domain-people-dna-land.yml`](../../.github/workflows/domain-people-dna-land.yml) | Pull-request/main trigger and TODO-only echo jobs. | Does not prove enforcement or required-check status. |
| [`data/receipts/generated/README.md`](../../data/receipts/generated/README.md) | Generated work receipt responsibility and non-authority boundary. | Receipt is provenance, not approval or proof. |
| [`generated_receipt.schema.json`](../../schemas/contracts/v1/receipts/generated_receipt.schema.json) | Machine shape for the accompanying generated receipt. | Schema conformance does not prove factual correctness or human approval. |

---

## Maintainer note

Keep `pipeline_specs/people/` README-only until an accepted decision proves that an alias artifact is necessary and safe. Prefer the governing `people-dna-land` lane for whole-context work. Never use the alias to weaken living-person, consent, DNA, land-title, evidence, policy, review, release, correction, or rollback controls.

[Back to top](#top)
