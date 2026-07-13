<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-manual-curation-readme
title: connectors/manual_curation/ — Manual Curation Greenfield Process-Helper and Steward-Gate Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Source steward · Review-workflow steward · Architecture steward · Rights reviewer · Sensitivity reviewer · Policy steward · Validation steward · Test steward · Fixture steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; connector-boundary; greenfield-package; manual-curation; process-not-source; steward-gate; source-admission; rights-fail-closed; sensitivity-fail-closed; quarantine-aware; no-network-default; no-activation; no-publication
current_path: connectors/manual_curation/README.md
truth_posture: CONFIRMED repository-present 0.0.0 process-helper scaffold with merged v0.2 source-layout, package-boundary, and test-boundary READMEs, one manual_curation package namespace, empty initializer, comment-only fetch/admit modules, four-field nonconforming local descriptor, README-only named test lane, absent conventional named tests, empty source-authority register, SourceDescriptor schema-path conflict, stub source/rights/sensitivity policy surfaces, and TODO-only connector workflows / CONFLICTED whether a cross-source manual-curation methodology belongs permanently under the source-specific connectors responsibility root and whether a process-not-source package should carry descriptor.yaml / PROPOSED fail-closed process-helper contract, steward-gate responsibilities, caller-owned candidate outcomes, finite local dispositions, and smallest safe implementation sequence / UNKNOWN differently named modules or tests, package buildability, imports, executable behavior, accepted DTOs, fixture routing, workflow integration, substantive CI, deployment, activation, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: b2db8a4f84754c111b28d756cbaac145fa0fcd84
  prior_blob: 3d39acf027befb3899147873832ca3fe06bf744e
related:
  - ../README.md
  - ./pyproject.toml
  - ./src/README.md
  - ./src/manual_curation/README.md
  - ./src/manual_curation/__init__.py
  - ./src/manual_curation/fetch.py
  - ./src/manual_curation/admit.py
  - ./src/manual_curation/descriptor.yaml
  - ./tests/README.md
  - ../../CONTRIBUTING.md
  - ../../.github/CODEOWNERS
  - ../../.github/workflows/connector-gate.yml
  - ../../.github/workflows/source-descriptor-validate.yml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../docs/sources/catalog/manual_curation/README.md
  - ../../docs/sources/catalog/manual_curation/steward-curation-workflow.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../control_plane/source_authority_register.yaml
  - ../../data/registry/sources/README.md
  - ../../policy/source/README.md
  - ../../policy/rights/README.md
  - ../../policy/sensitivity/README.md
  - ../../tests/README.md
  - ../../tests/fixtures/README.md
  - ../../fixtures/README.md
  - ../../release/
tags: [kfm, connectors, manual-curation, manual_curation, process-helper, steward-review, source-admission, descriptor, source-role, rights, sensitivity, policy, validation, evidence, raw, quarantine, no-network, no-publication, governance]
notes:
  - "Direct reads at the pinned base confirm project kfm-connector-manual_curation version 0.0.0, one manual_curation package namespace, an empty __init__.py, comment-only fetch.py and admit.py, and a four-field descriptor.yaml placeholder."
  - "The merged source-layout, package, and test-boundary READMEs are v0.2 and record the same greenfield scaffold, nonconforming descriptor, process-not-source placement conflict, caller-owned candidate boundary, no-network posture, and no-publication posture."
  - "Exact probes recorded by the merged test boundary returned Not Found for tests/conftest.py, test_fetch.py, test_admit.py, test_descriptor.py, test_review_routing.py, and tests/fixtures/README.md. Differently named files remain UNKNOWN."
  - "The manual-curation workflow documentation states that manual curation is a methodology applied to sources, not an upstream publisher or source family, and that it does not own a SourceDescriptor."
  - "The package-local descriptor leaves role and rights unresolved and asserts sensitivity_floor: public. It is not a conforming SourceDescriptor, source identity, activation decision, rights decision, sensitivity clearance, review approval, or release authorization."
  - "The machine source-authority register has entries: []; the populated singular SourceDescriptor schema declares a permissive plural schema canonical; source/rights/sensitivity policy surfaces are stubs; connector workflows run TODO echo steps."
  - "Only this Markdown file is changed. No path, package code, metadata, dependency, descriptor, registry record, policy, schema, contract, fixture, executable test, workflow, source material, credential, lifecycle artifact, evidence object, catalog record, release object, route, or public artifact is created or changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Manual Curation Greenfield Process-Helper and Steward-Gate Boundary

> Repository-grounded boundary for `connectors/manual_curation/`. The folder contains a non-operational `0.0.0` Python scaffold whose name suggests a connector, while the governing workflow documentation defines manual curation as a steward process applied **to** sources—not an upstream publisher or source family.

**Document lifecycle:** `draft v0.2`  
**Current component maturity:** `CONFIRMED` greenfield scaffold; no supported curation runtime exists  
**Owner:** `OWNER_TBD`  
**Authority:** process-helper documentation only; no source, contract, schema, policy, review, lifecycle, evidence, catalog, release, or publication authority  
**Default posture:** process-not-source · steward-gated · no network by default · caller-owned candidates only · unresolved material fails closed · no activation · no publication

> [!IMPORTANT]
> The repository currently provides package metadata with only a name and `0.0.0` version, an empty initializer, comment-only fetch and admission modules, a nonconforming local descriptor, and documentation-only tests. A folder, README, placeholder YAML file, pull request, merge, or green TODO-only workflow is not implementation evidence.

> [!CAUTION]
> `manual_curation` must not be normalized into a source merely because it lives under `connectors/` or contains `descriptor.yaml`. Manual curation operates on the identity, rights, sensitivity, source role, evidence, review, lifecycle, correction, and rollback state of another source. It does not publish source material of its own.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Current state](#current-repository-state) · [Placement](#repository-fit-and-process-ownership-tension) · [Methodology](#relationship-to-the-steward-methodology) · [What belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs-and-input-status) · [Identity](#identity-version-and-idempotency) · [Descriptor](#descriptor-registry-and-activation-boundary) · [Roles](#source-role-review-and-separation-of-duties) · [Rights](#rights-sensitivity-consent-sovereignty-and-access) · [Evidence](#evidence-provenance-and-claim-boundary) · [Outcomes](#proposed-local-dispositions) · [Failure contract](#failure-contract) · [Lifecycle](#lifecycle-catalog-release-and-publication-boundary) · [Side effects](#orchestration-persistence-and-side-effects) · [Security](#security-privacy-and-observability) · [Child contracts](#child-boundary-documents) · [Tests](#tests-fixtures-and-ci) · [Validation](#validation) · [Package](#package-configuration-dependencies-and-imports) · [Review](#review-burden) · [Implementation sequence](#smallest-safe-implementation-sequence) · [Definition of done](#definition-of-done) · [Evidence basis](#evidence-basis) · [Open decisions](#open-decisions-and-adr-triggers) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/manual_curation/` is the current repository location for a proposed helper package that may support a steward-led curation pass without replacing the steward, the governed workflow, or the authority roots the workflow invokes.

A retained helper may eventually:

- assemble a reviewable packet from explicit source, artifact, descriptor, evidence, and prior-review references;
- preserve supplied assertions separately from verified findings;
- preserve the distinction between source identity, curation-run identity, artifact identity, review identity, lifecycle state, and release state;
- validate presence and status of required references without deciding their authority;
- normalize bounded, non-authoritative workflow inputs into an accepted process contract;
- return caller-owned review, hold, quarantine, deny, abstain, conflict, no-op, error, or RAW-candidate results;
- preserve rights, sensitivity, consent, sovereignty, access, source-role, evidence, correction, supersession, withdrawal, and rollback uncertainty;
- record deterministic reason codes and remediation requirements;
- support replayable, redacted, auditable execution after contracts and tests exist;
- stop before lifecycle persistence, catalog closure, release, or publication.

The folder must not become a universal connector, source family, source registry, review authority, policy engine, workflow database, lifecycle writer, EvidenceBundle builder, catalog service, release controller, public API, AI truth source, or administrative bypass.

Manual curation protects the trust membrane only when it walks material through independently owned gates. A helper that collapses those gates into a single convenient function would defeat the purpose of the workflow.

[Back to top](#top)

---

## Authority level

**Greenfield process-helper scaffold. No independent governance authority.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Current path | **CONFIRMED** | `connectors/manual_curation/` and the named scaffold files exist at the pinned base. |
| Responsibility root | **CONFLICTED / NEEDS VERIFICATION** | Directory Rules assign source-specific admission mechanics to `connectors/`, while manual curation is a cross-source methodology and workflow rather than an upstream source. |
| Distribution | **CONFIRMED PLACEHOLDER** | `pyproject.toml` declares `kfm-connector-manual_curation` version `0.0.0` only. |
| Package namespace | **CONFIRMED** | One `src/manual_curation/` namespace exists at the named paths. |
| Current implementation | **GREENFIELD PLACEHOLDER** | `__init__.py` is empty; `fetch.py` and `admit.py` contain comments only. |
| Package-local descriptor | **NONCONFORMING / DENY FOR AUTHORITY USE** | Four minimal fields cannot establish a source, source identity, rights, sensitivity, review, activation, or release. |
| Executable tests | **NOT FOUND AT NAMED PROBES / OTHERWISE UNKNOWN** | The test lane is README-only at the conventional paths recorded by the merged v0.2 test boundary. |
| Stable fixtures | **NOT ESTABLISHED** | Fixture-home doctrine exists; no manual-curation child fixture lane or payload inventory is verified. |
| Source authority | **NOT ESTABLISHED** | The machine source-authority register is `PROPOSED` with `entries: []`. |
| Schema authority | **CONFLICTED** | The populated singular SourceDescriptor schema declares an empty plural scaffold canonical. |
| Policy enforcement | **STUB ONLY** | Source, rights, and sensitivity policy README surfaces do not establish executable package-specific enforcement. |
| Connector CI | **TODO-ONLY** | Named connector and descriptor workflows execute placeholder echo steps. |
| Curation workflow | **DOCUMENTED / NOT IMPLEMENTED HERE** | The steward methodology and workflow are documented, but exact accepted runtime contracts, queues, routes, and integrations are not verified. |
| Source activation | **DENIED / NOT VERIFIED** | This package cannot create or approve an activation decision. |
| Catalog closure | **DENIED / NOT VERIFIED** | No local success result can close a catalog record or establish evidence closure. |
| Public release | **NONE** | This component cannot approve or emit public output. |

Path presence grants a bounded implementation responsibility. It does not grant source status, policy authority, review authority, evidence closure, lifecycle control, or publication power.

[Back to top](#top)

---

## Current repository state

### Bounded snapshot

Direct reads at base commit `b2db8a4f84754c111b28d756cbaac145fa0fcd84` support this named surface:

```text
connectors/manual_curation/
├── README.md                              # this parent boundary; v0.1 before revision
├── pyproject.toml                         # kfm-connector-manual_curation, version 0.0.0
├── src/
│   ├── README.md                          # source-layout and process-ownership boundary v0.2
│   └── manual_curation/
│       ├── README.md                      # package and steward-gate boundary v0.2
│       ├── __init__.py                    # empty
│       ├── fetch.py                       # comment-only placeholder
│       ├── admit.py                       # comment-only placeholder
│       └── descriptor.yaml                # four-field placeholder
└── tests/
    └── README.md                          # negative-first test boundary v0.2
```

The merged test boundary records exact `Not Found` results for:

```text
connectors/manual_curation/tests/conftest.py
connectors/manual_curation/tests/test_fetch.py
connectors/manual_curation/tests/test_admit.py
connectors/manual_curation/tests/test_descriptor.py
connectors/manual_curation/tests/test_review_routing.py
connectors/manual_curation/tests/fixtures/README.md
```

These are bounded absence statements. They do not prove that no differently named, generated, ignored, unindexed, or later-added file exists.

### Current maturity table

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| Parent README | v0.1 before this revision | Stale generic boundary; did not reflect the exact scaffold or process-not-source conflict. |
| `pyproject.toml` | Project name and `0.0.0` only | Build backend, Python support, dependencies, package discovery, commands, and installability are unknown. |
| `src/README.md` | v0.2 source-layout contract | Records the real tree and placement tension; does not implement anything. |
| Package README | v0.2 package/steward-gate contract | Defines future behavior constraints; does not create behavior. |
| `__init__.py` | Empty | No public package API or initialization behavior. |
| `fetch.py` | Comment-only | No fetch, candidate assembly, hashing, source-head observation, retry, staging, or adapter behavior. |
| `admit.py` | Comment-only | No validation, policy call, review routing, disposition, receipt, activation, or lifecycle handoff. |
| `descriptor.yaml` | `name: manual_curation`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public` | Invalid as source authority, activation, rights clearance, sensitivity clearance, review evidence, or release evidence. |
| Test README | v0.2 negative-first proof contract | No runner, collection, coverage, pass rate, or executable proof follows. |
| Workflows | TODO echo steps | A green execution proves only that placeholder steps ran. |

There is no supported quickstart. No supported install, import API, command, configuration contract, workflow adapter, runner, or lifecycle integration was verified.

[Back to top](#top)

---

## Repository fit and process-ownership tension

Directory Rules place files by responsibility, not by topic or convenience. `connectors/` owns source-specific discovery, retrieval, preservation, packaging, integrity, parsing, and admission mechanics. The manual-curation documentation describes a cross-source steward workflow that acts on material from publishers, uploads, archives, watchers, connectors, corrections, and quarantine queues.

Those facts create a real architectural tension:

- **CONFIRMED:** the current helper scaffold lives under `connectors/manual_curation/`.
- **CONFIRMED:** manual curation is not an upstream publisher or source family.
- **PROPOSED:** the package may remain here if its responsibility is narrowed to source-admission helper mechanics subordinate to the steward workflow.
- **UNKNOWN:** whether this is the correct permanent home for cross-source curation orchestration or shared review utilities.
- **NEEDS VERIFICATION:** the accepted DTOs, orchestration owner, queue owner, review-system integration, and migration posture.

This README does not select a replacement path. Naming a new canonical path without repository and ADR evidence would create parallel authority or speculative structure.

| Responsibility | Owning surface | Relationship to this folder |
|---|---|---|
| Source-specific capture and admission mechanics | `connectors/<source>/` | Manual-curation helpers may consume explicit candidates; they do not replace the source connector. |
| Steward methodology and ordered workflow | `docs/sources/catalog/manual_curation/` and accepted methodology docs | Governs process intent; this package does not redefine it. |
| Object meaning | `contracts/` | Package consumes accepted contracts; local classes do not become canonical meaning. |
| Machine shape | `schemas/` | Package validates accepted objects; local dicts, models, YAML, or snapshots do not become schema authority. |
| Source identity and activation | Accepted registry and control-plane surfaces | Package resolves reviewed references; it cannot activate a source or itself. |
| Rights, sensitivity, consent, sovereignty, access, and release policy | `policy/` and reviewed governance records | Package preserves facts and decisions; it cannot clear risk. |
| Connector-local behavior proof | `connectors/manual_curation/tests/` while package remains here | Proves narrow package mechanics only. |
| Cross-system trust-spine proof | Root `tests/` | Proves lifecycle, policy, evidence, catalog, release, correction, rollback, and public-path enforcement. |
| Unit-test-scoped fixtures | `tests/fixtures/` under an accepted child lane | Not selected by this README. |
| Cross-cutting reusable fixtures | Root `fixtures/` under an accepted child lane | Not owned by the connector. |
| Lifecycle state and persistence | `data/` through governed orchestration | Package may return candidates; it cannot select or mutate a sink. |
| Evidence closure and proof | Accepted evidence/proof roots and contracts | Packet assembly or checksum calculation does not create an EvidenceBundle or proof closure. |
| Catalog closure | Catalog responsibility roots and review gates | A local success result cannot close STAC, DCAT, PROV, triplet, or domain records. |
| Release, correction, withdrawal, supersession, and rollback | `release/` and governed lifecycle records | Package may preserve references; it cannot decide or execute release. |
| Public API, UI, AI, map, or graph behavior | Governed application surfaces | Public clients must never import this package or consume unresolved candidates. |

### Placement rule for future changes

Do not move, mirror, alias, or duplicate this package merely to make the tree look cleaner.

Any permanent placement change should include:

1. a verified responsibility owner;
2. an accepted contract boundary;
3. consumers and dependency-direction analysis;
4. import and compatibility analysis;
5. source-descriptor and registry impact analysis;
6. test and fixture migration;
7. workflow and CI migration;
8. docs and cross-reference updates;
9. a drift-register entry and ADR or migration note where required;
10. a reviewed rollback plan.

Until then, the smallest reversible posture is to keep the current path, expose the conflict, and deny authority by default.

[Back to top](#top)

---

## Relationship to the steward methodology

The human-facing manual-curation methodology and the operational workflow outrank this implementation-boundary README on process meaning.

They establish several essential distinctions:

- manual curation is a steward-led methodology, not a source family;
- the workflow is applied to the source being curated;
- the workflow does not own a `SourceDescriptor` for itself;
- source role is assigned deliberately and cannot be inferred from convenience;
- rights and sensitivity are resolved before public release;
- EvidenceBundle outranks generated language;
- AI and watchers may assist, but may not approve;
- catalog closure and release require downstream records and independent gates;
- promotion is a governed state transition, not a file move.

The package, if retained, is a subordinate implementation detail. It may help perform deterministic, bounded mechanics within a curation pass. It may not collapse the methodology into a single function, replace the steward, author policy, decide review, or mint authority.

### Documentation-to-implementation relationship

| Documentation statement | Package obligation | Package prohibition |
|---|---|---|
| Source role cannot be convenience-inferred. | Require an explicit reviewed role or preserve unresolved state. | Do not default or upgrade the role. |
| Rights and sensitivity fail closed. | Preserve status, basis, reviewer, and unresolved reasons. | Do not infer clearance from file presence, metadata, or a local YAML value. |
| EvidenceBundle outranks summaries. | Preserve EvidenceRef values and resolution status. | Do not label packet assembly, model output, or citations as EvidenceBundle closure. |
| AI and watchers are advisory. | Mark generated or watcher-derived fields as assertions or recommendations. | Do not convert them into approval or truth. |
| Catalog closure is gated. | Preserve downstream prerequisites and missing-gate reasons. | Do not emit `catalog_closed`, `published`, or equivalent authority states. |
| Correction and rollback remain visible. | Preserve supplied correction, supersession, withdrawal, and rollback references. | Do not silently overwrite or erase prior state. |

### Methodology drift rule

If code, local tests, or this README conflict with accepted methodology, contracts, schemas, policy, or release rules:

1. fail closed;
2. identify the conflicting authorities;
3. preserve the input and current state without destructive mutation;
4. route for architecture or steward review;
5. add drift tracking when appropriate;
6. do not choose the more permissive interpretation by convenience.

[Back to top](#top)

---

## What belongs here

While the component remains under `connectors/manual_curation/`, accepted content is limited to narrow process-helper mechanics and their local documentation.

Potential future responsibilities include:

- package metadata for one installable `manual_curation` namespace;
- side-effect-free types or adapters for accepted external contracts;
- deterministic candidate-packet assembly from caller-supplied references;
- explicit assertion-versus-finding tagging;
- content or reference digest helpers when defined by accepted contracts;
- presence, format, and cross-reference checks against accepted schemas;
- source-role preservation checks;
- rights, sensitivity, consent, sovereignty, access, and review-state preservation;
- evidence-reference preservation and resolution-status reporting;
- validation-defect and conflict summaries;
- bounded reason-code mapping;
- correction, supersession, withdrawal, and rollback-reference preservation;
- caller-owned process outcome construction;
- redacted, deterministic observability fields;
- connector-local tests for retained package mechanics;
- documentation that accurately reflects implementation and authority limits.

Any such mechanics must remain subordinate to accepted contracts and externally owned decisions.

### Local code may answer

- Is the caller-supplied object structurally readable?
- Are required references present?
- Are expected identifiers syntactically valid under an accepted schema?
- Are two supplied references inconsistent?
- Is a local transform deterministic?
- Which required gate references are missing?
- Which explicit unresolved statuses were supplied?
- What bounded, caller-owned outcome candidate follows from an accepted contract and supplied decisions?

### Local code may not answer

- Is this source authoritative?
- Is the source activated?
- Are the rights sufficient?
- Is the sensitivity class safe for publication?
- Is consent valid?
- Is a sovereignty or cultural-governance requirement satisfied?
- Does the evidence prove the claim?
- Is catalog closure complete?
- Is release approved?
- Should a public client display the result?

Those are governance or downstream system questions.

[Back to top](#top)

---

## What does not belong here

Do not place or implement the following under `connectors/manual_curation/`:

- a source-family definition for `manual_curation`;
- a canonical `SourceDescriptor` for the manual-curation process;
- source registry authority;
- activation decisions;
- canonical contracts or schemas;
- policy rules or policy decisions;
- rights, consent, sovereignty, sensitivity, or public-release approvals;
- reviewer identities, queues, or approval databases unless an accepted owning architecture explicitly places an adapter here;
- canonical EvidenceBundles, proofs, receipts, catalog records, release manifests, corrections, withdrawals, supersessions, or rollback cards;
- direct lifecycle persistence;
- direct writes to RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, receipt, registry, or release roots;
- bulk source payloads, sensitive records, production exports, or real credentials;
- a second fixture registry or shared fixture authority;
- public API routes, UI components, map layers, tiles, graph projections, search indexes, or AI answer paths;
- generated language treated as truth, review, or approval;
- administrative shortcuts that bypass normal policy and review;
- hidden network calls or filesystem mutation during import;
- speculative modules, commands, or folders created only because this README names a future concern.

### Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Treating `manual_curation` as the source being described | Collapses process identity into source identity. |
| Accepting `descriptor.yaml` because the file exists | File presence is not schema conformance, registry admission, policy review, or activation. |
| Defaulting unresolved rights to open | Converts uncertainty into publication authority. |
| Treating `sensitivity_floor: public` as clearance | A package-local placeholder cannot decide sensitivity or release. |
| Letting a steward note become EvidenceBundle closure | Narrative and proof are different object families. |
| Letting a successful helper call write lifecycle state | Collapses computation, orchestration, review, and promotion. |
| Treating passing connector-local tests as trust-spine proof | Local unit tests cannot replace cross-system policy, evidence, catalog, and release tests. |
| Logging full source material or review packets | Can expose protected content, identities, coordinates, credentials, or proprietary data. |
| Creating a new workflow root without ADR/migration evidence | Produces parallel authority and path drift. |

[Back to top](#top)

---

## Inputs and input status

No accepted runtime input contract was verified. The following is a **PROPOSED** boundary for future design, not a current DTO or API.

A helper should consume explicit, immutable or version-pinned references wherever practical. Inputs should distinguish assertions, observations, accepted decisions, and unresolved state.

### Proposed input classes

| Input class | Example content | Required posture |
|---|---|---|
| Source reference | Source ID, descriptor reference, descriptor version | Must refer to the source being curated, never to `manual_curation` as a source by default. |
| Artifact reference | URI, content digest, media type, size, source-head observation | Reference and digest are not truth or rights clearance. |
| Curation-run context | Run ID, parent run, request ID, requested operation | Distinct from source and artifact identity. |
| Assertions | Claimed title, rights, role, sensitivity, provenance, dates | Keep explicitly unverified until supported. |
| Existing findings | Parser output, validator output, watcher signal, prior defect | Preserve producer, method, version, time, and status. |
| Review references | Review request, reviewer role, prior review state | The package may preserve; it must not impersonate the reviewer. |
| Policy references | Policy decision ID, version, scope, result | Must come from the policy authority. |
| Evidence references | EvidenceRef values and resolution status | Must not be converted into EvidenceBundle closure locally. |
| Lifecycle references | Current state, requested transition, receipt references | Informational unless governed orchestration authorizes and performs a transition. |
| Correction/rollback references | Correction notice, supersession, withdrawal, rollback target | Preserve without silently changing prior state. |
| Operation authorization | Actor, scope, purpose, expiration, authorization reference | Needed before consequential external side effects; exact contract is unverified. |

### Assertion classes

A future accepted contract should distinguish at least:

- `SUPPLIED_ASSERTION` — stated by an uploader, source, steward, file, or caller;
- `OBSERVED_FINDING` — deterministically observed by a named tool and version;
- `VERIFIED_FACT` — supported by accepted evidence and review outside this package;
- `POLICY_DECISION` — returned by the policy authority;
- `REVIEW_DECISION` — returned by an authorized reviewer workflow;
- `UNRESOLVED` — missing, disputed, stale, inconsistent, or insufficiently supported;
- `NOT_APPLICABLE` — explicitly not relevant, with a reason.

These labels are **PROPOSED local semantics** until accepted in contracts. The package must not silently infer them from Python types, truthiness, field presence, or naming conventions.

### Input acceptance rule

A helper should fail closed or return a non-authoritative unresolved outcome when:

- source identity is missing or ambiguous;
- descriptor identity or version is missing when required;
- content identity is missing for byte-bearing material;
- rights, sensitivity, consent, sovereignty, access, or review state is unknown and material;
- evidence references are malformed, stale, unresolved, or inconsistent;
- required policy or review decisions are absent;
- a requested transition would skip a lifecycle gate;
- caller authorization is missing or outside scope;
- inputs disagree and no accepted conflict policy resolves them;
- the requested action exceeds package authority.

[Back to top](#top)

---

## Identity, version, and idempotency

Manual curation touches several identities that must not collapse.

| Identity | Meaning | Must remain distinct from |
|---|---|---|
| Source ID | The governed upstream source being curated | Process package, curation run, artifact, review, release |
| Descriptor ID/version | The source-admission governance profile | Source payload, package-local placeholder YAML, activation decision |
| Artifact ID/content digest | A particular byte or object identity | Source identity, claim truth, rights clearance |
| Curation run ID | One invocation or review pass | Source ID, reviewer identity, lifecycle state |
| Review request/decision ID | A review workflow object | Curation run result, policy decision, activation |
| Policy decision ID | A policy authority result | Local validation or steward note |
| EvidenceRef/EvidenceBundle ID | Evidence pointer or resolved bundle | Citation string, summary, receipt, catalog closure |
| Lifecycle transition/receipt ID | A governed state-change event or record | Local function return |
| Catalog record ID/version | Catalog closure object | Source descriptor, helper packet, release |
| Release ID/version | Governed public-release decision | Build, test, packet, review, or catalog state |
| Correction/withdrawal/rollback ID | Reversal or supersession record | Deletion, overwrite, or informal note |

### Deterministic identity

Where accepted contracts permit, future helper behavior should prefer:

- stable caller-supplied IDs;
- canonical serialization before hashing;
- explicit algorithm and version labels;
- content digests for immutable artifacts;
- descriptor versions independent of source versions;
- operation keys derived from source, descriptor, artifact, requested action, and contract version;
- no timestamps or random values inside semantic identities unless the contract explicitly requires them.

### Idempotency

Repeated execution with equivalent accepted inputs should return an equivalent semantic result and should not create repeated external side effects.

A future implementation should distinguish:

- **pure calculation idempotency** — same inputs, same result;
- **submission idempotency** — the same caller-owned request is not submitted twice;
- **transition idempotency** — governed orchestration does not apply the same state transition twice;
- **review idempotency** — duplicate helper calls do not duplicate or overwrite a review decision.

The package should not implement transition or review idempotency by directly controlling those systems. It should pass and preserve accepted idempotency keys through adapters.

### Version pinning

A reproducible curation pass should pin, where applicable:

- package version and commit;
- contract and schema versions;
- descriptor version;
- source-head or artifact digest;
- validator and parser versions;
- policy version;
- review workflow version;
- fixture version in tests;
- operation and outcome contract version.

`latest`, ambient defaults, unversioned policy, and mutable file paths are insufficient for consequential decisions.

[Back to top](#top)

---

## Descriptor, registry, and activation boundary

The current package-local `src/manual_curation/descriptor.yaml` is a governance defect or migration placeholder—not a source authority record.

Its four fields do not satisfy the inspected SourceDescriptor v1 contract. More importantly, the steward workflow says manual curation does not own a descriptor for itself; it reads or helps prepare the descriptor of the source being curated.

### Local descriptor disposition

Until architecture review resolves the file:

- treat it as nonconforming;
- do not validate it as an accepted source record;
- do not register or activate it;
- do not infer rights or sensitivity from it;
- do not expose it to public clients;
- do not use it as a fixture without labeling it an explicit invalid/legacy case;
- do not silently expand it into a canonical descriptor;
- do not delete or move it in a documentation-only change.

### Required distinction

| Object or file | Safe interpretation |
|---|---|
| Package-local `descriptor.yaml` | Invalid placeholder or unresolved migration artifact. |
| Descriptor draft for source X | Candidate governance record for source X, pending validation and review. |
| Accepted SourceDescriptor for source X | Registry-governed source posture; still not claim truth or release approval. |
| Source activation decision for source X | Separate governed decision; not created by descriptor presence or package success. |
| Manual-curation run record | Process execution identity; not a source descriptor. |

### SourceDescriptor constraints

The inspected SourceDescriptor contract requires a rich v1 surface including source identity, type, role, authority, publisher/steward, rights, sensitivity, cadence, access, citation, source-head, admissibility limits, public-release posture, review state, release state, and lifecycle metadata.

A future helper may:

- check a caller-supplied descriptor candidate against the accepted schema;
- preserve validation errors;
- compare versions deterministically;
- identify missing required review or policy references;
- return a caller-owned remediation packet.

It may not:

- decide that a source exists because a descriptor file exists;
- select a source ID by guessing;
- assign source role or authority rank by convenience;
- convert unknown rights or sensitivity into permissive defaults;
- set review or release state to approved;
- activate, deprecate, withdraw, or supersede a source;
- write directly to the source registry;
- resolve the current singular/plural schema-path conflict locally.

### Activation boundary

Source activation requires independently owned descriptor, policy, review, authorization, and registry/control-plane decisions. Package output may indicate missing prerequisites or prepare a candidate request. It may not issue or persist the final decision.

### Schema-path conflict

The inspected populated singular-path schema declares a plural path canonical, while the plural schema is an empty permissive scaffold. This package must not choose one as canonical through imports, copied models, or local validation shortcuts.

Until resolved:

1. surface the conflict;
2. fail closed for governance-significant validation if authority cannot be determined;
3. pin the exact schema used in tests or experiments;
4. do not advertise source activation or conformance;
5. route the question to schema/architecture governance.

[Back to top](#top)

---

## Source role, review, and separation of duties

Source role is a property of the source being curated, not the manual-curation process.

A helper may preserve, validate, and compare an explicit source role. It may not assign a stronger role because:

- the source was manually reviewed;
- the source is official-looking;
- a file parsed successfully;
- a steward supplied a narrative;
- multiple weak sources agree;
- an AI summary sounds confident;
- a validator passed structural checks;
- the material reached RAW or PROCESSED state;
- the catalog contains a record;
- a prior release existed.

### Role anti-collapse

Keep these concepts separate:

- source type;
- source role;
- authority rank;
- domain scope;
- admissible claim roles;
- evidence sufficiency;
- reviewer decision;
- policy decision;
- catalog state;
- release state.

A future contract should represent conflicts explicitly rather than selecting the most permissive value.

### Review boundary

The package may prepare or preserve:

- review-request references;
- required reviewer roles;
- review scope;
- materiality or risk indicators;
- prior review references;
- missing-review reasons;
- redacted review packet summaries;
- correction or re-review triggers.

It may not:

- appoint reviewers;
- impersonate a reviewer;
- mark a review approved;
- accept a self-review where separation of duties is required;
- suppress dissenting or superseded reviews;
- infer review from a pull request merge, commit, test result, or administrator action.

### Separation of duties

For consequential source, rights, sensitivity, consent, sovereignty, catalog, or release decisions, a mature workflow should separate preparation, review, and approval where policy or materiality requires it.

The package should preserve actor and role references but should not enforce organizational identity through hard-coded usernames or local allowlists unless an accepted authorization contract explicitly places that adapter here.

### Review state examples

The exact enum is contract-owned. A helper should at minimum preserve distinctions equivalent to:

- not requested;
- requested;
- in review;
- changes required;
- approved within scope;
- denied;
- expired;
- superseded;
- withdrawn;
- unknown.

Do not collapse these into a boolean.

[Back to top](#top)

---

## Rights, sensitivity, consent, sovereignty, and access

These are independent, policy-significant dimensions. A positive value in one dimension does not clear the others.

### Rights

Preserve:

- rights status and basis;
- license or terms reference and version;
- attribution requirements;
- redistribution and derivative-work posture;
- commercial-use posture where material;
- verifier and verification time;
- scope and expiration;
- conflicts and unresolved questions.

Unknown, missing, no-assertion, restricted, permission-required, denied, stale, or conflicting rights fail closed for public release unless a later governed policy/review path resolves them.

### Sensitivity

Preserve:

- source-default sensitivity;
- record- or field-level overrides;
- domain-specific sensitivity;
- precision and location exposure;
- living-person status;
- ecological, archaeological, cultural, genomic, infrastructure, or security significance;
- transformations such as redaction, aggregation, generalization, masking, delay, or withholding;
- reviewer and policy references.

A package-local `public` string is not a sensitivity review.

### Consent and sovereignty

When applicable, preserve:

- consent status, scope, issuer, subject, time, expiration, revocation, and evidence reference;
- tribal, Indigenous, cultural, institutional, or jurisdictional governance requirements;
- rights-holder consultation status;
- data-sovereignty restrictions;
- permitted purposes and audiences;
- withdrawal or revocation requirements.

Unresolved consent or sovereignty concerns should route to hold, quarantine, denial, abstention, or specialized review—not a permissive default.

### Access

Access posture is not public-release posture.

A source may be technically reachable but legally restricted, sensitive, credentialed, internal, rate-limited, embargoed, or unsuitable for redistribution. The package may preserve access metadata or invoke a caller-supplied adapter under explicit authorization. It must not:

- read ambient credentials on import;
- log secrets or signed URLs;
- convert credentialed access into public availability;
- copy restricted material into fixtures or error reports;
- infer redistribution rights from successful download;
- bypass source-specific connector controls.

### High-risk material

Prefer hold, quarantine, redaction, generalization, staged access, delayed publication, specialized review, or denial when material includes:

- DNA or genomic data;
- living-person records;
- precise rare-species locations;
- archaeological or burial locations;
- culturally sensitive or sovereign data;
- critical infrastructure or security detail;
- credentials, secrets, or private endpoints;
- proprietary or contract-restricted data;
- harmful cross-dataset joins;
- uncertain rights or consent.

[Back to top](#top)

---

## Evidence, provenance, and claim boundary

Manual curation helps organize evidence-bearing material; it does not turn the material into evidence closure by itself.

### Evidence distinctions

| Item | What it can show | What it cannot show alone |
|---|---|---|
| Source descriptor | How KFM may treat a source | Claim truth, evidence sufficiency, release approval |
| Artifact digest | Identity of specific bytes | Correctness, rights, meaning, sensitivity clearance |
| Fetch or intake receipt | An operation occurred | Source truth or admission approval |
| Validation report | Checked conditions and results | Policy approval, claim proof, catalog closure |
| Steward note | Human observation or rationale | Independent review or EvidenceBundle closure |
| Citation | How to identify or credit material | Evidence resolution or permission to publish |
| EvidenceRef | Pointer to evidence | Complete, policy-safe EvidenceBundle until resolved |
| EvidenceBundle | Governed evidence closure for its stated scope | Automatic policy, catalog, or release approval |
| Review record | Review outcome within scope | Source truth outside scope or release approval |
| Catalog record | Catalog closure state | Publication without release authority |
| Release manifest | Governed release decision | Source truth beyond cited evidence and scope |

### Provenance minimums

A future helper should preserve, where applicable:

- source ID and descriptor version;
- upstream artifact URI or opaque reference;
- content digest and algorithm;
- source-head observation;
- acquisition or receipt reference;
- parser, validator, and transform versions;
- curation-run ID and parent run;
- actor and role references;
- assertion-versus-finding status;
- evidence references and resolution status;
- policy and review decision references;
- timestamps with explicit semantics and timezone;
- correction, supersession, withdrawal, and rollback references;
- contract, schema, and package versions.

### AI and watcher boundary

AI or watcher output may be included only as an explicitly identified advisory assertion or finding with producer, version, time, inputs, and limitations.

It must never be treated as:

- source authority;
- rights or sensitivity clearance;
- review approval;
- EvidenceBundle closure;
- policy decision;
- catalog closure;
- release approval;
- public truth.

When evidence is insufficient or cannot be safely resolved, the correct posture is to narrow the claim, abstain, deny, hold, or route for review.

[Back to top](#top)

---

## Proposed local dispositions

No accepted process-outcome contract was verified. The following finite dispositions are **PROPOSED local design labels** for future discussion and tests. They are not canonical lifecycle states, policy decisions, or release outcomes.

| Disposition | Proposed meaning | Must not imply |
|---|---|---|
| `REVIEW_REQUIRED` | Human or specialized review is required before the request can advance. | Review request created or review approved. |
| `HOLD` | Processing should pause pending named prerequisites. | QUARANTINE persistence or denial. |
| `QUARANTINE_CANDIDATE` | Caller may submit material to governed quarantine orchestration. | Material has been written to QUARANTINE. |
| `RAW_CANDIDATE` | Caller may submit an admissible candidate to governed RAW orchestration. | RAW persistence, source activation, or validation success. |
| `DENY` | The requested helper operation is not allowed under the supplied accepted decision context. | Global policy denial unless backed by a policy decision reference. |
| `ABSTAIN` | Evidence, authority, or scope is insufficient to produce a supported result. | Error or approval. |
| `CONFLICT` | Inputs or governing references disagree materially. | Automatic precedence selection. |
| `NOOP` | Equivalent work is already represented or no change is required. | External state was checked unless a reference proves it. |
| `ERROR` | The helper could not complete because of a technical or contract failure. | Policy denial, review denial, or source invalidity. |

### Result envelope expectations

A future accepted result should contain enough information for a caller and reviewer to understand:

- outcome and outcome-contract version;
- source, descriptor, artifact, and curation-run references;
- requested operation;
- evaluated prerequisites;
- reason codes;
- missing or conflicting references;
- assertion/finding status;
- redacted human-readable explanation;
- remediation or next-gate suggestions;
- deterministic idempotency key;
- package, contract, schema, validator, and policy references used;
- no embedded source payload, secret, or sensitive detail by default.

### Boundary with governed finite outcomes

Public runtime outcome vocabularies such as `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` belong to governed API/runtime contracts. The local labels above must not be exported to public clients or assumed equivalent without an accepted adapter and contract.

[Back to top](#top)

---

## Failure contract

A safe process helper makes failures explicit, bounded, deterministic, and non-authoritative.

### Failure classes

| Failure class | Example | Proposed safe result |
|---|---|---|
| Invalid input shape | Required reference absent or malformed | `ERROR` with schema/contract reason; no side effect. |
| Unknown source identity | No stable source reference | `REVIEW_REQUIRED` or `ABSTAIN`; never invent an ID. |
| Nonconforming descriptor | Local four-field YAML or incomplete draft | `HOLD` or `REVIEW_REQUIRED`; deny authority use. |
| Schema-authority conflict | Singular/plural schema disagreement | `CONFLICT`; pin evidence and escalate. |
| Unknown rights | No verified rights basis | `HOLD`, `QUARANTINE_CANDIDATE`, or `DENY` per accepted policy reference. |
| Unknown sensitivity | Missing or stale sensitivity review | `REVIEW_REQUIRED` or `QUARANTINE_CANDIDATE`. |
| Consent/sovereignty unresolved | Missing permission or governance review | `HOLD`, `DENY`, or specialized review. |
| Source-role conflict | Supplied roles disagree | `CONFLICT`; do not upgrade. |
| Evidence unresolved | EvidenceRef cannot resolve safely | `ABSTAIN` or `REVIEW_REQUIRED`; no evidence closure. |
| Review missing | Consequential operation lacks required review | `REVIEW_REQUIRED`. |
| Policy missing or stale | No applicable accepted decision | `HOLD` or `ABSTAIN`; do not choose policy locally. |
| Lifecycle skip requested | Caller requests direct catalog/publish write | `DENY`; no side effect. |
| Authorization missing | Actor or operation scope absent | `DENY` or `ERROR`, depending on accepted contract. |
| Duplicate request | Equivalent idempotency key already represented | `NOOP` with reference, when externally verified. |
| Adapter unavailable | Registry, review, or policy service unavailable | `ERROR` or `HOLD`; do not silently downgrade. |
| Timeout or resource bound | Bounded operation exceeds limits | `ERROR`; preserve safe retry metadata. |
| Sensitive logging risk | Error text would expose protected content | Redacted `ERROR`; preserve opaque reference only. |

### Error hygiene

Errors should be:

- free of full source payloads, secrets, tokens, signed URLs, private paths, personal data, exact protected coordinates, and proprietary text;
- stable enough for tests and dashboards;
- explicit about whether failure occurred before any external side effect;
- linked to a request/run ID rather than embedding sensitive context;
- separated from policy denial, review denial, abstention, and conflict;
- replay-safe when the operation is pure;
- bounded in size.

### Retry posture

Do not retry:

- policy denial;
- rights, sensitivity, consent, sovereignty, or review holds;
- malformed immutable input;
- authorization denial;
- source-role conflict;
- unsupported operation.

Bounded retry may be appropriate for transient adapter or service failures only when:

- the caller authorizes retry;
- the operation is idempotent;
- attempt count and backoff are bounded;
- the same version-pinned inputs are retained;
- no hidden side effect occurred;
- retries are observable without leaking protected details.

### Fail-closed rule

When the helper cannot distinguish safe from unsafe behavior, it must not select the permissive path.

[Back to top](#top)

---

## Lifecycle, catalog, release, and publication boundary

KFM's lifecycle invariant is:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move and not a local function return.

### Package relationship to lifecycle

| Lifecycle concern | Package may | Package must not |
|---|---|---|
| Candidate preparation | Return a caller-owned RAW or QUARANTINE candidate. | Persist the candidate or select a sink. |
| RAW admission | Preserve prerequisites and operation references. | Claim RAW admission occurred without a governed receipt. |
| WORK / QUARANTINE | Preserve state and reason references. | Move or copy material into lifecycle roots directly. |
| PROCESSED | Validate supplied processed-artifact references. | Create processed authority merely by transforming data. |
| CATALOG / TRIPLET | Report missing closure prerequisites. | Close catalog/triplet records or mint graph truth. |
| PUBLISHED | Preserve release references supplied by the caller. | Publish, expose, tile, index, summarize, or answer publicly. |

### RAW and QUARANTINE candidates

A future package may prepare a candidate envelope only after accepted contracts exist. The envelope should be caller-owned and should include:

- source and descriptor references;
- artifact identity or opaque reference;
- requested target class;
- reason codes;
- rights, sensitivity, consent, sovereignty, source-role, evidence, policy, and review references;
- unresolved conditions;
- idempotency key;
- package/contract/schema versions;
- correction and rollback references when applicable.

It should not include a caller-selected filesystem path as authority or write the material itself.

### Catalog closure

Catalog closure requires independently governed source, validation, evidence, policy, review, catalog, correction, and rollback records appropriate to the release significance.

This package may report that prerequisites appear present under accepted contracts. It may not:

- issue the closure decision;
- mint STAC, DCAT, PROV, domain, triplet, graph, or search authority;
- mark a record release-eligible;
- treat packet completeness as evidence closure;
- use a local test to bypass catalog review.

### Release and public path

Release authority remains outside this folder. Public clients and normal UI surfaces must use governed APIs and released artifacts. They must not read:

- package-local candidates;
- review packets;
- unresolved descriptors;
- RAW, WORK, or QUARANTINE material;
- internal registry/control-plane records directly;
- direct model output;
- local helper logs or caches;
- package-local YAML as public metadata.

A release needs appropriate identity, rights, sensitivity, validation, provenance, integrity, evidence, policy, review, correction, withdrawal, and rollback support. A helper success state is never sufficient.

### Correction and rollback

Future helpers should preserve correction, supersession, withdrawal, and rollback references without applying them directly.

Do not overwrite prior state to make the current packet appear clean. Reversibility depends on durable version and lineage references.

[Back to top](#top)

---

## Orchestration, persistence, and side effects

This package should be a bounded helper library, not an orchestration engine.

### Default side-effect posture

By default, future package imports and pure functions should perform no:

- network access;
- credential lookup;
- filesystem mutation;
- registry mutation;
- lifecycle writes;
- review-system writes;
- policy-service calls;
- catalog or release writes;
- telemetry emission containing source content;
- dynamic plugin installation;
- environment-based authority selection.

### Adapter boundary

External interactions, when accepted, should be supplied through explicit caller-owned adapters with narrow interfaces, such as:

- descriptor resolver;
- schema validator;
- policy-decision resolver;
- review-reference resolver;
- evidence resolver;
- lifecycle candidate submitter;
- correction/rollback reference resolver;
- clock and ID providers for testability;
- redacted audit-event sink.

These are **PROPOSED interface categories**, not verified module names or files.

Adapters should:

- expose explicit version and capability information;
- accept scoped authorization;
- return finite, typed results;
- preserve denied, absent, stale, conflict, timeout, and error distinctions;
- be replaceable in tests;
- avoid returning raw secrets;
- never grant more authority than the underlying system.

### Persistence boundary

No package function should discover a lifecycle, registry, catalog, proof, receipt, or release path by convention and write to it.

The caller or governed orchestration layer owns persistence. The package may construct an accepted candidate object or invoke an explicit submitter adapter after authorization, but the resulting external record remains owned by the target system.

### Transaction posture

If a future operation coordinates multiple external systems:

- do not hide partial success;
- preserve each external operation reference;
- use idempotency keys;
- report compensation or rollback requirements;
- avoid distributed commit claims without actual support;
- fail closed when authority or final state is uncertain.

### No administrative bypass

An administrator flag must not disable source-role, rights, sensitivity, consent, sovereignty, evidence, review, lifecycle, catalog, or release gates in the normal path.

Emergency or break-glass behavior, if ever accepted, requires separate policy, authorization, audit, expiration, review, and public-path exclusion. It is not designed here.

[Back to top](#top)

---

## Security, privacy, and observability

Manual-curation packets can contain highly sensitive cross-domain information. The package should assume the input may reveal more through joins and metadata than through the primary payload alone.

### Data minimization

Future helpers should:

- consume opaque references instead of payloads when possible;
- request only fields necessary for the current operation;
- avoid copying material into local caches;
- keep derived summaries bounded;
- separate identifiers from display labels;
- avoid retaining source content in exceptions, snapshots, or test artifacts;
- preserve redaction/generalization decisions as explicit transforms;
- support purpose and scope limits supplied by accepted contracts.

### Secrets

Never commit or log:

- credentials;
- API tokens;
- cookies;
- signed URLs;
- private keys;
- passwords;
- internal endpoint secrets;
- sensitive environment dumps.

Credential resolution belongs to an accepted external configuration or secret-management surface and should occur only in an authorized adapter call, not at import time.

### Path and reference safety

Treat caller-supplied paths, URIs, filenames, labels, and links as untrusted.

A future implementation should prevent:

- path traversal;
- symlink escape;
- unsafe archive expansion;
- remote-file inclusion by convenience;
- unsupported URI schemes;
- local network or metadata-service access;
- reference confusion between public and restricted stores;
- logs that reveal private mount points.

The exact file-content inspection boundary belongs primarily to source-specific connectors such as local upload, not to a generic manual-curation process helper.

### Observability

Safe audit and metric fields may include:

- request/run ID;
- operation name and contract version;
- outcome and reason code;
- duration and bounded resource metrics;
- adapter name/version;
- source, descriptor, artifact, policy, review, and evidence references in opaque or redacted form;
- retry count;
- missing-gate count;
- conflict count;
- whether any external side effect was attempted or confirmed.

Do not expose:

- source payload excerpts;
- review narratives by default;
- personal or genomic identifiers;
- exact sensitive coordinates;
- credentials or signed links;
- full private URIs or paths;
- proprietary content;
- internal policy rationale that is not approved for the audience.

### Audit versus proof

An audit event shows what the helper reports it did. It is not by itself a receipt, proof, review decision, policy decision, catalog record, or release record.

[Back to top](#top)

---

## Child boundary documents

The parent README coordinates but does not duplicate the full detail of its child contracts.

| Child surface | Confirmed posture | Parent relationship |
|---|---|---|
| `src/README.md` | v0.2 source-layout and process-ownership boundary | Defines package layout, imports, dependencies, and placement tension. |
| `src/manual_curation/README.md` | v0.2 package and steward-gate boundary | Defines bounded package behavior, inputs/outputs, descriptor defect, lifecycle stop, and implementation sequence. |
| `tests/README.md` | v0.2 negative-first connector-local test boundary | Defines local proof scope, fixture split, required test families, and CI limits. |

### Consistency rule

The parent and children should agree on:

- process-not-source posture;
- current `0.0.0` scaffold state;
- nonconforming descriptor status;
- no-network and no-import-side-effects default;
- caller-owned candidate outputs;
- no direct lifecycle writes;
- no activation, review approval, evidence closure, catalog closure, release, or publication authority;
- unresolved permanent placement;
- bounded truth claims about tests and CI.

When one document changes materially, review all three sibling/child boundaries for drift. Documentation consistency does not prove runtime consistency, but contradiction creates avoidable implementation risk.

### Authority rule

Child READMEs may narrow responsibilities. They may not enlarge authority beyond the parent, Directory Rules, contracts, schemas, policy, registries, tests, or release controls.

[Back to top](#top)

---

## Tests, fixtures, and CI

The connector-local test lane is documentation-only at the named probes. No test runner, framework, collection, coverage, pass rate, fixture inventory, or substantive connector CI result is established.

### Connector-local tests should prove

After behavior exists, local tests should prove narrow package mechanics, including:

- import performs no network, credential, filesystem, registry, lifecycle, review, or telemetry side effect;
- package-local descriptor is rejected for authority use;
- assertions remain distinct from findings and accepted decisions;
- source identity does not collapse into process or artifact identity;
- source role cannot be defaulted or upgraded;
- unknown rights, sensitivity, consent, sovereignty, access, evidence, policy, or review state fails closed;
- EvidenceRef values remain unresolved until an external resolver confirms an EvidenceBundle;
- local success cannot activate, persist lifecycle state, close catalog, release, or publish;
- finite outcomes and reason codes are deterministic;
- idempotency keys are stable;
- correction, withdrawal, supersession, and rollback references are preserved;
- logs and errors redact protected material;
- adapters preserve absence, denial, conflict, timeout, stale, and error distinctions;
- duplicated requests do not create duplicated external submissions in adapter tests.

### Root trust-spine tests should prove

Canonical root tests should verify cross-system behavior, including:

- accepted descriptor and registry admission;
- source-role enforcement across ingest, evidence, catalog, API, UI, and AI paths;
- rights/sensitivity/consent/sovereignty policy;
- governed lifecycle transitions and receipts;
- EvidenceRef-to-EvidenceBundle resolution or abstention;
- policy and review separation;
- catalog/proof closure;
- release, correction, withdrawal, supersession, and rollback;
- public API and UI refusal to read unresolved/internal material;
- denial and abstention behavior under missing or conflicting evidence.

Connector-local tests do not replace these tests.

### Fixture routing

KFM documents a split:

- `tests/fixtures/` for small unit-test-scoped fixtures;
- root `fixtures/` for cross-cutting reusable fixtures.

This README does not select a manual-curation child lane. Before adding fixtures, verify:

1. the consumer test owner;
2. whether the fixture is local or cross-cutting;
3. schema and contract version;
4. rights and sensitivity safety;
5. synthetic or transformed status;
6. expected outcome and reason;
7. correction/rollback case when material;
8. no duplication across fixture homes.

Real source payloads, review packets, sensitive details, credentials, and production records do not belong in connector-local fixtures.

### Minimum fixture matrix

A future safe matrix should include compact synthetic cases for:

- valid structure but unresolved source identity;
- nonconforming local descriptor;
- unknown, restricted, denied, and conflicting rights;
- public, restricted, unknown-review-required, and high-risk sensitivity;
- missing consent, revoked consent, and sovereignty review required;
- explicit candidate source role and prohibited role upgrade;
- unresolved and resolved EvidenceRef references;
- missing and conflicting policy/review references;
- lifecycle-skip request;
- correction, supersession, withdrawal, and rollback references;
- duplicate/idempotent request;
- adapter timeout, denied, stale, and malformed result;
- redaction of protected fields in logs and errors.

### CI reality

The inspected connector and source-descriptor workflows run TODO echo steps. Therefore:

- green workflow completion is not package validation;
- source-descriptor validation is not proven substantive;
- connector tests are not proven collected;
- no package install or import check is proven;
- no coverage or mutation threshold is proven;
- no no-network enforcement is proven;
- no fixture-safety scan is proven;
- no trust-spine integration is proven.

Future CI should report collection count, pass/skip/xfail state, failure details, versions, and artifact references appropriate to policy. It must not expose sensitive fixture data.

### Proposed future gates

Before implementation maturity is claimed, a review should verify gates equivalent to:

1. package metadata and isolated install;
2. import and no-side-effect checks;
3. formatter, linter, and type checks if adopted;
4. unit and negative tests;
5. deterministic replay;
6. no-network and filesystem-write guards;
7. descriptor-invalidity regression test;
8. fixture safety and secret scan;
9. contract/schema version checks;
10. root trust-spine integration tests;
11. docs consistency checks;
12. rollback and correction scenarios.

These are proposed requirements, not current workflow names.

[Back to top](#top)

---

## Validation

Validation should be layered and should not convert a lower-level success into higher authority.

### Layer 1 — Input and package mechanics

- accepted input contract version present;
- required references present;
- identifiers and digests syntactically valid;
- values canonicalized deterministically;
- unsupported fields rejected or preserved per contract;
- resource limits enforced;
- no hidden side effects.

### Layer 2 — Cross-reference integrity

- source ID matches descriptor source ID;
- descriptor version is explicit;
- artifact references and digests are consistent;
- policy and review references match requested scope;
- EvidenceRef syntax and declared resolution state are consistent;
- correction, supersession, withdrawal, and rollback references are not contradictory;
- source, curation-run, artifact, review, catalog, and release identities remain separate.

### Layer 3 — Governance prerequisites

The package may check presence and consistency, but final decisions remain external:

- source-role posture;
- rights;
- sensitivity;
- consent and sovereignty;
- access and purpose limits;
- policy decision;
- review decision and separation of duties;
- evidence resolution;
- operation authorization;
- lifecycle transition permission;
- catalog closure prerequisites;
- release prerequisites.

### Layer 4 — Outcome constraints

- outcome is finite and contract-defined;
- reason codes are stable;
- unresolved state is visible;
- no local result claims external persistence or approval;
- no sensitive data leaks;
- next-step guidance names the owning gate;
- retry posture is explicit;
- idempotency key is deterministic;
- package/contract/schema versions are recorded.

### Validation does not equal authority

A structurally valid packet can still be denied, held, quarantined, abstained, or returned for review because of rights, sensitivity, source role, evidence, policy, review, lifecycle, catalog, or release state.

### Unsupported cases

Unsupported or ambiguous cases should not be coerced into a generic success object. Return a bounded error, conflict, abstention, hold, or review-required result under the accepted contract.

[Back to top](#top)

---

## Package configuration, dependencies, and imports

The current `pyproject.toml` contains only project name and version. No build backend, dependency declaration, Python requirement, package discovery, command, or test configuration is established.

### Package metadata required before installability claims

A future implementation should explicitly decide and test:

- build backend;
- supported Python versions;
- package discovery for the `src/` layout;
- runtime dependencies;
- optional development/test dependencies;
- command or entry-point policy, if any;
- version source;
- license and metadata posture;
- import surface;
- typing and compatibility posture;
- reproducible lock or dependency policy where required.

### Dependency rule

Dependencies must follow responsibility direction.

The package may depend on accepted shared contract models, validation interfaces, and narrow adapters. It should not depend directly on:

- public UI or browser packages;
- release implementation;
- canonical data stores;
- internal database details;
- source-specific connector internals unless an accepted adapter contract requires it;
- model runtimes for governance decisions;
- packages that create circular authority between policy, review, evidence, and connector layers.

### Import rule

Importing `manual_curation` should not:

- access the network;
- read credentials;
- scan directories;
- create files;
- configure global logging;
- register a source;
- validate or activate the local descriptor;
- contact policy, review, registry, evidence, catalog, or release services;
- import heavy optional integrations by default;
- mutate global state.

### Public API rule

Do not export an API until accepted contracts and tests establish:

- object names and versions;
- stable error and outcome semantics;
- side-effect boundary;
- adapter ownership;
- backward-compatibility posture;
- deprecation and rollback path.

The empty `__init__.py` currently proves no public API.

### Configuration rule

Configuration should specify mechanism, not authority. Environment variables or config files may select endpoints, timeouts, resource bounds, or adapter implementations. They must not unilaterally set:

- source authority;
- source role;
- rights clearance;
- sensitivity clearance;
- review approval;
- evidence closure;
- catalog closure;
- release approval;
- public visibility.

[Back to top](#top)

---

## Review burden

Changes to this component should be reviewed according to what they affect, not merely by file location.

| Change | Minimum review burden |
|---|---|
| README wording with no behavior change | Package/connector maintainer + Docs steward; confirm truth labels and child consistency. |
| Package metadata, imports, or dependency direction | Package maintainer + architecture/dependency reviewer + test steward. |
| Input/output or outcome contract | Contract steward + schema steward + package maintainer + test steward. |
| Descriptor, registry, or activation behavior | Source steward + contract/schema stewards + policy steward + architecture review. |
| Source-role behavior | Source steward + domain or evidence steward + policy/test review. |
| Rights, sensitivity, consent, sovereignty, or access | Appropriate rights/sensitivity/policy reviewers and domain/rights-holder representation where required. |
| Evidence resolution or claim support | Evidence steward + contract/schema + policy/test review. |
| Lifecycle candidate or persistence adapter | Lifecycle/pipeline/data steward + policy + test + rollback review. |
| Catalog or release integration | Catalog/release stewards + policy + evidence + independent review. |
| Public API/UI/AI exposure | Governed API/UI owners + security/privacy + policy/evidence/release review. |
| Permanent path or responsibility change | Directory Rules check + architecture owner + drift register + ADR/migration plan and rollback. |

### Materiality triggers

Increase review burden when a change can:

- expose more precise or sensitive data;
- broaden accepted inputs or source roles;
- make a deny/hold path more permissive;
- add side effects;
- add credentials or network access;
- create or change a lifecycle transition;
- change evidence sufficiency;
- alter catalog or release prerequisites;
- affect correction, withdrawal, supersession, or rollback;
- add an administrative shortcut;
- change public behavior.

### Documentation review questions

Reviewers should ask:

1. Does the README distinguish confirmed scaffold facts from proposed design?
2. Does it describe manual curation as a process, not a source?
3. Does it deny authority to the local descriptor?
4. Are lifecycle and public-path boundaries explicit?
5. Do child READMEs agree?
6. Are tests and CI described honestly?
7. Are paths responsibility-grounded?
8. Are open decisions visible?
9. Is rollback concrete?
10. Does any sentence imply runtime or governance maturity without evidence?

[Back to top](#top)

---

## Smallest safe implementation sequence

This sequence is **PROPOSED**. Each step should be a small, reviewable, reversible change with independent validation.

### Step 0 — Resolve ownership and scope

- decide whether the package remains under `connectors/`;
- define its responsibility in one sentence;
- decide whether the local descriptor is removed, relocated, or retained only as an invalid fixture/migration artifact;
- record architecture/drift decisions;
- identify owners and reviewers.

No runtime work should proceed while the package is ambiguously modeled as a source.

### Step 1 — Accept contracts before code

Define or adopt versioned contracts for:

- curation request;
- source/artifact/assertion/finding references;
- review and policy references;
- local process result;
- finite reason codes;
- idempotency key;
- redacted audit event;
- adapter result semantics.

Place contracts and schemas in their authority roots, not inside this package.

### Step 2 — Complete package metadata

- select build backend and supported Python;
- configure `src/` package discovery;
- declare minimal dependencies;
- define development/test dependencies;
- document install and test commands only after they work;
- add import/no-side-effect tests.

### Step 3 — Implement pure normalization and validation

Start with pure, offline functions that:

- accept contract-shaped inputs;
- preserve assertions and statuses;
- validate references against accepted schemas;
- produce deterministic local outcomes;
- make no network or filesystem writes;
- redact errors.

### Step 4 — Add negative-first tests and fixtures

Implement tests for:

- invalid local descriptor;
- missing source identity;
- role conflict;
- unknown rights/sensitivity/consent/sovereignty;
- unresolved evidence;
- missing review/policy;
- lifecycle-skip request;
- forbidden side effects;
- sensitive logging;
- deterministic replay and idempotency.

Select fixture homes through the documented split.

### Step 5 — Add explicit read-only resolvers

Only after contracts and tests exist, add caller-supplied read-only adapters for accepted registry, policy, review, or evidence references.

Prove:

- no ambient credentials;
- scoped authorization;
- finite denied/absent/stale/conflict/error states;
- version pinning;
- no authority inflation;
- redacted observability.

### Step 6 — Add candidate-submission adapter if justified

If architecture retains this responsibility, add a narrow caller-supplied adapter that submits an accepted candidate to governed orchestration.

It must:

- require explicit operation authorization;
- use an idempotency key;
- return an external record reference;
- never select the target path locally;
- preserve partial failure;
- support safe retry;
- remain unable to catalog or publish.

### Step 7 — Add root trust-spine integration

Root tests should exercise the package through real accepted boundaries and prove source, policy, evidence, lifecycle, catalog, release, correction, rollback, and public-path protections.

### Step 8 — Make CI substantive

Replace TODO-only gates with tested commands, collection reporting, no-network enforcement, fixture safety, secret scans, version checks, docs consistency, and trust-spine integration.

### Step 9 — Update docs from observed behavior

Only after the commands, interfaces, tests, and workflows are observed should this README gain a supported quickstart or implementation claims.

[Back to top](#top)

---

## Definition of done

This component is not implementation-ready merely because documentation, scaffolding, or placeholder workflows exist.

A mature, retained process helper should satisfy all applicable criteria below.

### Ownership and placement

- [ ] Permanent responsibility is accepted and documented.
- [ ] Process-not-source modeling is explicit.
- [ ] Local descriptor disposition is resolved.
- [ ] No parallel contract, schema, policy, registry, fixture, evidence, catalog, or release home exists.
- [ ] Owners and reviewers are assigned.

### Package

- [ ] Build backend, Python support, discovery, dependencies, and versioning are explicit.
- [ ] Isolated installation succeeds.
- [ ] Import is side-effect free.
- [ ] Public API and compatibility posture are documented.
- [ ] No hidden network, credential, filesystem, or lifecycle behavior exists.

### Contracts

- [ ] Accepted versioned request/result/reason/audit contracts exist in canonical roots.
- [ ] Source, artifact, run, review, policy, evidence, lifecycle, catalog, and release identities remain separate.
- [ ] Finite outcomes distinguish error, denial, abstention, conflict, review, hold, and candidates.
- [ ] Idempotency and version pinning are explicit.

### Governance

- [ ] Package cannot activate a source or itself.
- [ ] Package cannot assign or upgrade source role.
- [ ] Rights, sensitivity, consent, sovereignty, access, and purpose limits fail closed.
- [ ] AI/watcher outputs remain advisory.
- [ ] EvidenceRef does not become EvidenceBundle closure locally.
- [ ] Review and policy decisions remain external and independently owned.

### Lifecycle and publication

- [ ] Package cannot write lifecycle state directly.
- [ ] Candidate submission uses an explicit governed adapter and authorization.
- [ ] Package cannot close catalog/triplet/graph records.
- [ ] Package cannot release or publish.
- [ ] Correction, withdrawal, supersession, and rollback references remain visible.
- [ ] Public clients cannot read package-local material.

### Tests and CI

- [ ] Executable negative-first connector-local tests exist.
- [ ] Fixture routing and safety are accepted.
- [ ] No-network and no-side-effect enforcement exists.
- [ ] Descriptor-invalidity and authority-inflation regressions exist.
- [ ] Determinism, replay, redaction, resource bounds, and idempotency are tested.
- [ ] Root trust-spine integration exists.
- [ ] CI runs substantive commands and reports collection/results.
- [ ] Test evidence is reviewable without exposing sensitive data.

### Documentation and operations

- [ ] Supported install/test/run commands are observed and documented.
- [ ] Parent and child READMEs agree.
- [ ] Known conflicts are in drift/ADR/migration records.
- [ ] Observability distinguishes audit from proof.
- [ ] Operational failure and recovery paths are documented.
- [ ] Rollback has concrete commit, configuration, data, and compatibility targets where applicable.

Until these are verified, component maturity remains greenfield.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/manual_curation/README.md` prior blob `3d39acf027befb3899147873832ca3fe06bf744e` | **CONFIRMED** | Parent target existed as v0.1 generic boundary. | Did not reflect exact package/test state. |
| `connectors/manual_curation/pyproject.toml` | **CONFIRMED** | Project name and version `0.0.0`. | No build, dependency, discovery, Python, or command evidence. |
| `src/README.md` v0.2 | **CONFIRMED** | Exact named source layout, process-ownership conflict, import/dependency/lifecycle boundaries. | Documentation, not runtime proof. |
| `src/manual_curation/README.md` v0.2 | **CONFIRMED** | Exact package scaffold, descriptor defect, steward-gate and candidate-output boundaries. | Documentation, not runtime proof. |
| Empty `__init__.py` | **CONFIRMED** | No current public package API. | Does not prove absent dynamically generated behavior outside the named file. |
| Comment-only `fetch.py` and `admit.py` | **CONFIRMED** | No supported named fetch/admit mechanics. | Differently named or later-added code remains outside this claim. |
| Four-field `descriptor.yaml` | **CONFIRMED** | Local placeholder exists with unresolved role/rights and `public` sensitivity floor. | Not a conforming descriptor or authority record. |
| `tests/README.md` v0.2 | **CONFIRMED** | README-only named test lane, exact conventional absences, proposed negative-first proof contract. | No runner, collection, coverage, or pass state. |
| Manual-curation methodology v3 | **CONFIRMED DOCUMENT** | Human-governed source-to-catalog methodology and core doctrine. | Operational paths and tools remain mixed/proposed. |
| Steward curation workflow v0.2 | **CONFIRMED DOCUMENT** | Process-not-source distinction; workflow does not own SourceDescriptor. | Draft workflow; exact runtime integration remains unverified. |
| Directory Rules v1.4 | **CONFIRMED DOCTRINE** | Responsibility-root placement and lifecycle invariant. | Specific future home for this cross-source process is not decided. |
| SourceDescriptor contract v0.3 | **CONFIRMED DOCUMENT / PROPOSED CONTRACT** | Rich descriptor meaning and required surface. | Schema-path and runtime/registry maturity remain conflicted or unverified. |
| Source authority register | **CONFIRMED EMPTY ENTRIES AT INSPECTED EVIDENCE** | No machine source activation established through that register. | Later or differently governed authority surfaces remain outside this claim. |
| Source/rights/sensitivity policy READMEs | **CONFIRMED STUB SURFACES** | Policy roots exist as documentation placeholders. | No executable package-specific policy proof. |
| Generic connector and descriptor workflows | **CONFIRMED TODO-ONLY AT INSPECTED BODIES** | Workflow scaffolds exist. | Green status is not substantive package validation. |

### Evidence limits

This revision did not execute package code, install the distribution, import the package, collect tests, inspect all recursively named files, query a live registry, resolve EvidenceBundles, invoke policy or review systems, inspect deployment, or verify release behavior.

Statements about future contracts, adapters, outcomes, tests, fixtures, and implementation sequence are `PROPOSED` unless explicitly labeled otherwise.

[Back to top](#top)

---

## Open decisions and ADR triggers

The following decisions are unresolved and should not be settled implicitly in package code or README prose.

| Decision | Current status | Trigger for ADR, migration note, or governed decision |
|---|---:|---|
| Permanent responsibility root | **CONFLICTED / NEEDS VERIFICATION** | Moving or redefining the package as cross-source workflow infrastructure. |
| Package name and distribution identity | **NEEDS VERIFICATION** | Renaming, aliasing, publishing, or making it a shared dependency. |
| Disposition of `descriptor.yaml` | **CONFLICTED** | Removing, moving, converting, or reclassifying the file. |
| Canonical SourceDescriptor schema path | **CONFLICTED** | Selecting singular/plural path or migrating validators/records. |
| Curation request/result contracts | **PROPOSED / ABSENT** | Creating canonical object families or public/stable interfaces. |
| Finite local outcome vocabulary | **PROPOSED** | Sharing across packages, pipelines, APIs, or persisted records. |
| Review-system ownership and adapter | **UNKNOWN** | Writing review requests or consuming authoritative review decisions. |
| Lifecycle candidate submission owner | **UNKNOWN** | Adding external writes or orchestration responsibility. |
| Fixture child lane | **NEEDS VERIFICATION** | Adding manual-curation fixtures. |
| Source authority and activation flow | **NOT ESTABLISHED** | Creating accepted registry/control-plane records or activation decisions. |
| Policy packages | **STUB / UNKNOWN** | Adding executable source/rights/sensitivity policy behavior. |
| CI gates | **TODO-ONLY** | Making checks substantive or required for promotion. |
| Public/runtime integration | **DENIED / OUT OF SCOPE** | Any proposal to expose helper output through API, UI, map, graph, search, or AI. |

### Drift handling

When implementation and doctrine disagree:

- record the exact conflicting paths, versions, and evidence;
- avoid parallel authorities;
- choose the smallest reversible interim posture;
- use the drift register where appropriate;
- add an ADR or migration note when responsibility, authority, compatibility, or lifecycle meaning changes;
- preserve rollback targets.

### No decision by convention

Do not settle an open decision merely because:

- a placeholder file already exists;
- another connector uses a similar shape;
- a local class name seems convenient;
- a workflow is green;
- a package imports successfully;
- documentation lists a proposed tree;
- a user interface needs the data;
- an AI recommends a path.

[Back to top](#top)

---

## Rollback

This revision is documentation-only and changes one file.

### Before merge

Close or abandon the review branch or pull request. No runtime, lifecycle, registry, policy, evidence, catalog, or release state is affected by this README change.

### After merge

Restore the previous parent README through a reviewed commit using either:

```text
base commit: b2db8a4f84754c111b28d756cbaac145fa0fcd84
prior blob: 3d39acf027befb3899147873832ca3fe06bf744e
```

or revert the commit that introduces this v0.2 revision.

### Rollback triggers

Rollback or correct this README if it:

- is used to claim executable package behavior;
- is used to treat manual curation as an upstream source;
- is used to validate or activate the local descriptor;
- grants the package source-role, rights, sensitivity, review, evidence, policy, lifecycle, catalog, release, or publication authority;
- names speculative paths as repository facts;
- conflicts materially with accepted child boundaries or governing doctrine;
- exposes sensitive implementation or source details;
- documents commands that do not work;
- hides a known drift or migration requirement.

### Documentation rollback is not operational rollback

Reverting this README does not revert any future package code, dependency, descriptor, registry, policy, fixture, test, workflow, data, review, catalog, or release change. Each material implementation change needs its own rollback plan.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm recursive package inventory beyond named files. | **NEEDS VERIFICATION** | Commit-pinned recursive tree or mounted workspace. |
| Decide permanent responsibility root. | **CONFLICTED** | Directory Rules review, consumers, dependency analysis, ADR/migration decision. |
| Resolve package-local descriptor disposition. | **CONFLICTED** | Architecture/source-governance decision and migration/test plan. |
| Resolve SourceDescriptor schema authority. | **CONFLICTED** | Accepted ADR/migration, schema contents, validators, fixtures, CI. |
| Define curation request/result/reason contracts. | **PROPOSED / ABSENT** | Contract/schema review and compatibility plan. |
| Define orchestration and adapter ownership. | **UNKNOWN** | Architecture, authorization, side-effect, and deployment evidence. |
| Confirm source authority and activation path. | **NOT ESTABLISHED** | Accepted registry/control-plane records, decisions, and tests. |
| Confirm policy enforcement. | **STUB / UNKNOWN** | Executable source/rights/sensitivity policies, decisions, tests, logs. |
| Confirm test framework and commands. | **UNKNOWN** | Package metadata, test dependencies, config, collection, logs. |
| Select fixture home and prove fixture safety. | **NEEDS VERIFICATION** | Fixture steward decision, synthetic payloads, metadata, tests. |
| Confirm no-network and no-side-effect enforcement. | **UNKNOWN** | Executable guards and CI evidence. |
| Confirm deterministic identity and idempotency. | **PROPOSED** | Accepted contracts, code, replay tests, adapter tests. |
| Confirm evidence resolver behavior. | **UNKNOWN** | Accepted interfaces, resolver implementation, root trust-spine tests. |
| Confirm review-system integration. | **UNKNOWN** | Authorization, actor/role, adapter, audit, and separation-of-duties tests. |
| Confirm lifecycle candidate handoff. | **UNKNOWN** | Contract, adapter, authorization, receipts, idempotency, rollback tests. |
| Confirm catalog/release/public-path denial. | **NEEDS VERIFICATION** | Root integration tests and governed API/UI checks. |
| Make connector workflows substantive. | **TODO-ONLY** | Workflow patches, commands, artifacts, branch-protection evidence. |
| Assign owners and CODEOWNERS. | **NEEDS VERIFICATION** | Reviewed ownership decision and repository configuration. |
| Reconcile parent/child docs after material changes. | **ONGOING** | Docs review and link/consistency checks. |

---

## Maintainer checklist

- [ ] Keep manual curation modeled as a process applied to sources.
- [ ] Keep the local descriptor denied for authority use until resolved.
- [ ] Keep confirmed scaffold facts separate from proposed design.
- [ ] Keep the package offline and side-effect free by default.
- [ ] Keep source, run, artifact, review, policy, evidence, lifecycle, catalog, and release identities distinct.
- [ ] Keep rights, sensitivity, consent, sovereignty, access, and review uncertainty visible.
- [ ] Keep EvidenceRef resolution and EvidenceBundle closure outside local packet assembly.
- [ ] Keep lifecycle persistence, catalog closure, release, and publication outside the package.
- [ ] Keep public clients on governed released interfaces.
- [ ] Keep tests negative-first and distinguish local proof from root trust-spine proof.
- [ ] Keep fixtures synthetic, public-safe, minimal, and correctly routed.
- [ ] Keep logs and errors redacted.
- [ ] Keep CI claims bounded to commands actually executed.
- [ ] Update parent and child READMEs together when boundaries change.
- [ ] Use ADR/migration discipline for path, descriptor, contract, or authority changes.
- [ ] Preserve concrete rollback targets.

Manual curation protects KFM only when the steward gates remain visible, independently owned, evidence-backed, reviewable, and reversible.

[Back to top](#top)
