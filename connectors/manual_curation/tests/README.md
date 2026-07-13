<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-manual-curation-tests-readme
title: connectors/manual_curation/tests/ — Manual Curation Greenfield Test and Steward-Gate Proof Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Test steward · Fixture steward · Source steward · Review-workflow steward · Architecture steward · Rights reviewer · Sensitivity reviewer · Policy steward · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; connector-tests; greenfield-package; manual-curation; process-not-source; steward-gate; negative-first; synthetic-only; no-network; no-side-effects; rights-fail-closed; sensitivity-fail-closed; quarantine-aware; no-activation; no-publication
current_path: connectors/manual_curation/tests/README.md
truth_posture: CONFIRMED README-only named connector test lane, exact absence of conventional conftest/fetch/admit/descriptor/review-routing tests and local fixture README at the pinned base, repository-present 0.0.0 package scaffold, empty initializer, comment-only fetch/admit modules, four-field nonconforming descriptor, merged v0.2 package and source-layout boundaries, empty source-authority register, SourceDescriptor schema-path conflict, stub source/rights/sensitivity policy surfaces, canonical root tests and split fixture doctrine, and TODO-only connector workflows / CONFLICTED whether connector-local tests remain the correct permanent home for a cross-source manual-curation process package / PROPOSED negative-first connector-local test contract, steward-gate matrix, safe fixture routing, deterministic outcome assertions, and smallest safe implementation sequence / UNKNOWN differently named tests, framework, runner, collection, package installation, fixtures, coverage, substantive CI, runtime behavior, activation, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 5f06485d910ee1b4855aff3274623f801a798d11
  prior_blob: e5478c2c61afdbce97ac7f81504e98ca6aaf0d45
related:
  - ../README.md
  - ../pyproject.toml
  - ../src/README.md
  - ../src/manual_curation/README.md
  - ../src/manual_curation/__init__.py
  - ../src/manual_curation/fetch.py
  - ../src/manual_curation/admit.py
  - ../src/manual_curation/descriptor.yaml
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/connector-gate.yml
  - ../../../.github/workflows/source-descriptor-validate.yml
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/sources/catalog/manual_curation/README.md
  - ../../../docs/sources/catalog/manual_curation/steward-curation-workflow.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/README.md
  - ../../../policy/source/README.md
  - ../../../policy/rights/README.md
  - ../../../policy/sensitivity/README.md
  - ../../../tests/README.md
  - ../../../tests/fixtures/README.md
  - ../../../fixtures/README.md
  - ../../../release/
tags: [kfm, connectors, manual-curation, manual_curation, tests, steward-review, source-admission, descriptor, source-role, rights, sensitivity, policy, validation, evidence, raw, quarantine, no-network, no-side-effects, no-publication, governance]
notes:
  - "Direct reads at the pinned base confirm that the test lane contains this README while exact probes for conftest.py, test_fetch.py, test_admit.py, test_descriptor.py, test_review_routing.py, and tests/fixtures/README.md returned Not Found."
  - "Absence statements are bounded to the named paths and pinned commit. Differently named tests, helpers, or fixtures remain UNKNOWN until directly inspected."
  - "The adjacent package is a 0.0.0 scaffold with an empty initializer, comment-only fetch.py and admit.py, and a four-field descriptor.yaml placeholder. No supported package behavior exists for tests to exercise."
  - "The local descriptor leaves role and rights unresolved and asserts sensitivity_floor: public. Tests must reject it as source authority, activation, rights clearance, sensitivity clearance, review approval, or release authorization."
  - "The merged package and source-layout v0.2 READMEs define the process-not-source placement conflict, caller-owned candidate boundary, steward-gate requirements, no-network posture, no lifecycle writes, and no-publication posture. This test README converts those boundaries into proposed enforceability requirements without claiming implementation."
  - "Only this Markdown file is in scope. No package code, metadata, dependency, descriptor, registry record, policy, schema, fixture, executable test, workflow, source material, credential, lifecycle artifact, evidence object, catalog record, release object, path move, or public artifact is created or changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Manual Curation Greenfield Test and Steward-Gate Proof Boundary

> Repository-grounded test boundary for `connectors/manual_curation/tests/`. The lane currently contains documentation, not an executable suite. Its future job is to prove that manual-curation helper mechanics preserve steward review, source-role separation, rights and sensitivity uncertainty, evidence-reference non-closure, caller-owned candidate outputs, and KFM lifecycle/publication boundaries.

**Document lifecycle:** `draft v0.2`  
**Current test maturity:** `CONFIRMED` README-only at the named probes; no test run or coverage is established  
**Owner:** `OWNER_TBD`  
**Authority:** connector-local behavior proof only; no contract, schema, policy, source, review, fixture, lifecycle, evidence, catalog, release, or publication authority  
**Default posture:** synthetic only · no network · no side effects · negative first · deterministic failure · fail closed

> [!IMPORTANT]
> The adjacent package is a non-operational `0.0.0` scaffold. A test README, proposed filename, green workflow, or future passing unit test cannot prove source activation, rights clearance, sensitivity clearance, EvidenceBundle closure, review approval, catalog closure, release readiness, or public safety.

> [!CAUTION]
> `manual_curation` is a process applied **to** sources, not an upstream publisher. Tests must not normalize the package-local `descriptor.yaml` into source authority, and `sensitivity_floor: public` must be rejected as a public-safety decision.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Current state](#current-test-lane) · [Repository fit](#repository-fit-and-placement-tension) · [Local versus root proof](#connector-local-versus-root-trust-spine-proof) · [What belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Environment](#test-environment-contract) · [Fixtures](#fixture-routing-and-safety) · [Required families](#required-test-families) · [Steward gates](#steward-gate-test-matrix) · [Outcomes](#finite-outcome-and-failure-assertions) · [Lifecycle](#lifecycle-evidence-catalog-release-and-public-path-tests) · [Determinism](#determinism-replay-and-observability) · [CI](#collection-runner-and-ci-boundary) · [Validation](#validation) · [Evidence](#evidence-basis) · [Review](#review-burden) · [Implementation sequence](#smallest-safe-implementation-sequence) · [Definition of done](#definition-of-done) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/manual_curation/tests/` is reserved for tests of narrow behavior owned by the current manual-curation helper package.

Its future responsibilities are to prove that package code:

- imports without network, filesystem mutation, credential lookup, lifecycle writes, registry writes, or review-system side effects;
- treats source files, notes, filenames, labels, citations, uploader or steward assertions, generated summaries, and watcher findings as inputs that require explicit status;
- distinguishes source identity, curation-run identity, artifact identity, review identity, disposition state, and final governance decisions;
- rejects the package-local descriptor as governance authority;
- preserves explicit source role without convenience upgrades;
- routes unknown rights, sensitivity, consent, sovereignty, access, or review state to a safe unresolved outcome;
- preserves EvidenceRef values without claiming EvidenceBundle closure;
- preserves validation defects, conflicts, caveats, and remediation requirements;
- returns caller-owned review, hold, quarantine, deny, abstain, conflict, error, or RAW-candidate results rather than selecting lifecycle sinks;
- never approves source activation, policy, catalog closure, release, or publication;
- preserves correction, supersession, withdrawal, and rollback references when supplied;
- does not leak protected content, secrets, personal data, exact protected locations, private paths, or proprietary material through logs, exceptions, snapshots, or assertion messages;
- remains deterministic and reviewable under replay.

This lane does not prove the entire KFM trust spine by itself. Cross-system enforcement belongs in canonical root `tests/` lanes.

[Back to top](#top)

---

## Authority level

**Connector-local test documentation and future package-behavior proof only.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Current path | **CONFIRMED** | `connectors/manual_curation/tests/README.md` exists at the pinned base. |
| Permanent owning component | **CONFLICTED / NEEDS VERIFICATION** | Manual curation is a cross-source process; connector-local test placement follows the current package but does not settle permanent ownership. |
| Executable tests | **NOT FOUND AT NAMED PROBES / OTHERWISE UNKNOWN** | Exact conventional paths returned `Not Found`; differently named tests remain unknown. |
| Test framework and runner | **UNKNOWN** | No accepted runner, configuration, marker set, dependency, invocation, or collection evidence was verified. |
| Package under test | **CONFIRMED PLACEHOLDER** | `kfm-connector-manual_curation` is version `0.0.0`; initializer is empty; fetch/admit modules are comment-only. |
| Local descriptor | **NONCONFORMING / MUST BE REJECTED** | Four minimal fields cannot establish source identity, role, rights, sensitivity, activation, review, or release. |
| Stable fixtures | **NOT ESTABLISHED FOR THIS LANE** | No connector-local fixture README was found; exact routing and payload inventory remain unresolved. |
| Root test authority | **CONFIRMED DOCTRINE** | Root `tests/` owns cross-system enforceability proof. |
| Fixture split | **CONFIRMED DOCUMENTED / CHILD PLACEMENT NEEDS VERIFICATION** | `tests/fixtures/` is test-local; root `fixtures/` is cross-cutting. The manual-curation child lane is not selected here. |
| Source authority | **NOT ESTABLISHED** | The machine source-authority register is `PROPOSED` with `entries: []`. |
| Schema authority | **CONFLICTED** | The populated singular SourceDescriptor schema points to an empty plural scaffold as canonical. |
| Policy enforcement | **STUB ONLY** | Source, rights, and sensitivity policy README files are greenfield stubs, not executable proof. |
| Connector CI | **TODO-ONLY** | Named connector and descriptor workflows execute placeholder echo steps. |
| Test results and coverage | **NONE VERIFIED** | No collection, pass, skip, xfail, coverage, mutation, resource, or security result was observed. |
| Source activation | **DENIED / NOT VERIFIED** | Tests cannot substitute for accepted descriptor, policy, review, and activation decisions. |
| Public release | **NONE** | A connector-local test cannot approve or create public output. |

A test proves only the behavior it executes with controlled inputs. It cannot create governance authority through assertion text.

[Back to top](#top)

---

## Current test lane

### Bounded repository snapshot

Direct reads at base commit `5f06485d910ee1b4855aff3274623f801a798d11` support this named surface:

```text
connectors/manual_curation/
├── README.md
├── pyproject.toml                         # project name + version 0.0.0 only
├── src/
│   ├── README.md                          # source-layout boundary v0.2
│   └── manual_curation/
│       ├── README.md                      # package boundary v0.2
│       ├── __init__.py                    # empty
│       ├── fetch.py                       # comment-only placeholder
│       ├── admit.py                       # comment-only placeholder
│       └── descriptor.yaml                # four-field placeholder
└── tests/
    └── README.md                          # this test boundary
```

Exact probes returned `Not Found` for:

```text
connectors/manual_curation/tests/conftest.py
connectors/manual_curation/tests/test_fetch.py
connectors/manual_curation/tests/test_admit.py
connectors/manual_curation/tests/test_descriptor.py
connectors/manual_curation/tests/test_review_routing.py
connectors/manual_curation/tests/fixtures/README.md
```

These are bounded absence statements. They do not prove that no differently named file exists now or will exist later.

### Current maturity table

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| Test README | v0.1 before this revision | Documentation existed; no execution evidence followed. |
| Conventional test modules | Not found at the named probes | No named import, fetch, admit, descriptor, or review-routing coverage. |
| Test-local fixture documentation | Not found at the named probe | No connector-local fixture authority or inventory established. |
| Package metadata | Name and `0.0.0` only | Test dependencies, framework, runner, Python support, and installation remain unknown. |
| Package behavior | Empty/comment-only scaffold | There is no supported behavior for positive-path tests to exercise. |
| Descriptor | `name: manual_curation`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public` | Tests should reject it as authority rather than normalize it into acceptance. |
| Adjacent READMEs | Source-layout and package boundaries are v0.2 | Test requirements can be derived, but implementation is still absent. |
| Workflows | TODO echo steps | A green run would prove only that the placeholder step executed. |

There is no supported test quickstart. Any command would be speculative until package metadata, test dependencies, framework, configuration, and collection behavior are accepted and observed.

[Back to top](#top)

---

## Repository fit and placement tension

Directory Rules separate package mechanics, connector-local tests, canonical trust-spine tests, fixtures, schemas, policy, lifecycle data, evidence, catalog, release, and public applications.

| Responsibility | Owning surface | Relationship to this lane |
|---|---|---|
| Manual-curation package mechanics | Current `connectors/manual_curation/src/manual_curation/` | Subject under test if retained here. |
| Connector-local package tests | Current `connectors/manual_curation/tests/` | This lane while the package remains under the connector root. |
| Cross-system enforceability | Root `tests/` | Proves source, policy, lifecycle, evidence, catalog, release, correction, rollback, and public-path boundaries. |
| Unit-test-scoped fixtures | `tests/fixtures/` under an accepted child lane | Candidate home for small test-specific fixtures; exact manual-curation placement remains to be ratified. |
| Cross-cutting reusable fixtures | Root `fixtures/` under an accepted child lane | Shared synthetic corpora; not owned here. |
| Human-facing methodology and workflow | `docs/sources/catalog/manual_curation/` | Tests follow it; they do not redefine it. |
| Object meaning | `contracts/` | Tests assert accepted semantics; they do not mint contracts. |
| Machine shape | `schemas/` | Tests validate against accepted schemas; snapshots do not become schema authority. |
| Source identity and activation | Registry/control-plane surfaces | Tests use reviewed fixture records; they cannot activate a source. |
| Rights, sensitivity, access, consent, and release policy | `policy/` | Tests assert policy behavior; they do not decide policy. |
| Lifecycle persistence | `data/` through governed orchestration | Tests use isolated temporary or in-memory fakes; they do not write real lifecycle state. |
| Evidence closure | Evidence/proof responsibility roots | Tests may assert non-closure or resolver behavior; they do not produce production evidence. |
| Catalog and release | Catalog/release responsibility roots | Tests may use toy records; they do not close or publish. |
| Public API and map behavior | Governed applications and root integration tests | Connector-local tests must not expose package internals as a public path. |

### Placement determination

The current test location follows the repository-present package. It does not prove that a cross-source manual-curation process belongs permanently under `connectors/`.

Until architecture review resolves that tension:

- do not move tests independently from the package;
- do not create duplicate test suites under multiple roots;
- do not call this lane canonical beyond its current connector-local role;
- record future movement through drift tracking, migration notes, and an ADR where Directory Rules require one;
- preserve history, compatibility expectations, and rollback.

[Back to top](#top)

---

## Connector-local versus root trust-spine proof

Connector-local tests should prove pure package mechanics. Root tests should prove governed integration.

| Concern | Connector-local lane | Root trust-spine lane |
|---|---|---|
| Side-effect-free import | **Yes** | May corroborate through packaging checks. |
| Pure candidate construction | **Yes** | Optional integration coverage. |
| Descriptor rejection | **Yes** | Schema/registry enforcement belongs at root. |
| Source-role preservation | **Yes** | Cross-source anti-collapse belongs at root. |
| Rights/sensitivity routing | Pure local behavior only | Policy packages and integration gates. |
| Evidence-reference preservation | Pure local behavior only | Evidence resolver and closure tests. |
| Review candidate construction | **Yes** | Review service and separation-of-duties integration. |
| Lifecycle sink prohibition | **Yes**, through spies/fakes | Canonical state-transition and filesystem/API boundary tests. |
| Catalog/release prohibition | **Yes** | Catalog closure and release-gate integration. |
| Correction/rollback references | Preserve and validate local shape | Replay, release, correction, and rollback proof. |
| Public path denial | No public interfaces in package | API/UI routing and authorization tests. |
| Deployment/readiness | No | CI, runtime, release, and operational evidence. |

Do not duplicate root integration tests under the connector merely to obtain local coverage. Route each invariant to the smallest test layer that can prove it truthfully.

[Back to top](#top)

---

## What belongs here

After package contracts, test configuration, and fixture routing are accepted, this lane may contain:

- import-safety tests;
- pure helper unit tests for explicit inputs and returned candidates;
- descriptor-rejection tests;
- source-role anti-collapse tests;
- rights and sensitivity uncertainty-routing tests;
- review-candidate and disposition-candidate construction tests;
- validation-defect and conflict-preservation tests;
- evidence-reference preservation and non-closure tests;
- caller-owned output and sink-prohibition tests;
- deterministic finite-outcome and reason-code tests;
- correction, supersession, withdrawal, and rollback-reference tests;
- redacted logging and exception tests;
- replay and idempotency tests;
- connector-local synthetic fixture loaders;
- test-only fakes and spies that do not become reusable production packages.

Every executable test should identify:

- the exact contract or package invariant under test;
- the controlled input and expected finite outcome;
- whether the assertion is local behavior or cross-system integration;
- the fixture safety posture;
- the forbidden side effects being monitored;
- the failure meaning and owning remediation surface.

[Back to top](#top)

---

## What does not belong here

Do not place or perform these under `connectors/manual_curation/tests/`:

- production source material, steward case files, local uploads, private documents, or lifecycle records;
- real living-person, genomic, archaeological, rare-species, infrastructure, sovereign, cultural, proprietary, or credential-bearing data;
- live network calls in the default suite;
- real credentials, API keys, cookies, tokens, signed URLs, or private endpoints;
- direct writes to `data/raw/`, `data/quarantine/`, `data/receipts/`, `data/work/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/proofs/`, `data/published/`, registry roots, or `release/`;
- a second contract, schema, policy, source registry, fixture authority, evidence authority, catalog authority, or release authority;
- tests that approve source activation, source-role upgrade, policy, review, catalog closure, release, or publication;
- snapshots containing protected content or generated summaries presented as evidence;
- package-internal tests that reach public APIs, UI routes, maps, or direct model endpoints;
- auto-generated tests treated as review or release approval;
- network recordings that preserve secrets, personal data, source payloads, or sensitive responses;
- test helpers with import-time filesystem, network, credential, registry, or lifecycle side effects.

Administrative or steward status does not reduce test-data safety requirements.

[Back to top](#top)

---

## Test environment contract

The future default test environment should be:

| Property | Required posture |
|---|---|
| Network | Disabled or actively blocked by default. |
| Filesystem | Temporary and isolated; repository and lifecycle roots read-only or inaccessible. |
| Credentials | Absent; environment access monitored or explicitly denied. |
| Time | Fixed or injected where behavior depends on time. |
| Randomness | Seeded or eliminated. |
| Locale/time zone | Fixed where parsing or comparison depends on them. |
| Package import | No network, file writes, credential lookup, registry mutation, adapter startup, or lifecycle side effects. |
| External adapters | Injected fakes with explicit behavior and version labels. |
| Logs | Captured and scanned for secret, personal, location, path, and payload leakage. |
| Outcomes | Explicit and finite; unexpected success is a failure. |
| Cleanup | Deterministic and verified. |

Tests should fail when package code attempts to:

- discover sinks from the repository or local machine;
- inspect credentials implicitly;
- connect to a live source;
- write to governed roots;
- create activation, policy, evidence, catalog, or release records;
- return success after an indeterminate adapter result;
- suppress conflicts or validation defects;
- convert an unknown state into an allow state.

[Back to top](#top)

---

## Fixture routing and safety

### Current fixture state

No connector-local fixture README was found at the exact probe:

```text
connectors/manual_curation/tests/fixtures/README.md
```

The repository documents two fixture homes:

| Home | Intended use | Manual-curation posture |
|---|---|---|
| `tests/fixtures/` | Unit-test-scoped synthetic fixtures local to a test area. | Preferred candidate for small manual-curation test fixtures if an accepted child lane is created. |
| `fixtures/` | Cross-cutting reusable synthetic fixtures shared across tests and pipelines. | Use only for genuinely reusable trust-spine fixtures. |

This README does not create a child fixture path or choose a permanent fixture taxonomy.

### Fixture requirements

Any future fixture must be:

- synthetic, minimized, and public-safe;
- explicit about source role, rights, sensitivity, consent, sovereignty, access, review, and expected disposition when material;
- free of real credentials, personal records, exact protected locations, private paths, proprietary text, or production identifiers;
- paired with metadata describing why it is safe and what behavior it proves;
- immutable or versioned where replay matters;
- linked to an accepted contract/schema version where applicable;
- prohibited from being copied into lifecycle, registry, evidence, catalog, release, or public surfaces.

### Minimum fixture classes

A credible suite should include compact cases for:

1. conforming reviewable candidate with no authority upgrade;
2. nonconforming package-local descriptor;
3. unknown source role;
4. attempted source-role elevation;
5. unknown or restricted rights;
6. unknown or sensitive classification;
7. missing review reference;
8. unresolved conflict between sources or stewards;
9. missing EvidenceRef;
10. preserved but unresolved EvidenceRef;
11. validation defects;
12. caller-owned RAW candidate;
13. caller-owned QUARANTINE candidate;
14. deny, abstain, conflict, and error outcomes;
15. correction, supersession, withdrawal, and rollback references;
16. log-redaction canaries;
17. sink-write attempts;
18. network and credential-access attempts;
19. nondeterministic timestamp or identifier attempts;
20. duplicate artifact/content identity without collapsing curation-run identity.

[Back to top](#top)

---

## Required test families

### 1. Import and packaging safety

Prove that:

- importing the namespace has no side effects;
- package metadata can be read without network or mutation once packaging exists;
- unsupported imports fail explicitly;
- no implicit plugin, credential, or adapter discovery occurs;
- import behavior is deterministic.

### 2. Descriptor rejection and authority separation

Prove that:

- the current four-field `descriptor.yaml` is rejected for authority use;
- missing required SourceDescriptor v1 fields do not receive defaults that create authority;
- deprecated aliases are not mistaken for a complete accepted descriptor;
- `sensitivity_floor: public` does not clear content for public use;
- descriptor validation does not equal activation, rights approval, sensitivity approval, review approval, or release.

### 3. Source-role anti-collapse

Prove that:

- input roles remain explicit;
- `TBD`, unknown, candidate, context, corroborating, and authoritative roles do not collapse;
- a user, watcher, AI, or helper cannot upgrade source role;
- secondary roles do not silently replace the primary role;
- conflicting role assertions route to review or conflict.

### 4. Rights, sensitivity, consent, and access

Prove that:

- unknown rights route to hold, quarantine, abstain, or deny;
- restricted rights cannot become public by a successful parse or review-packet build;
- unknown sensitivity fails closed;
- consent, sovereignty, cultural-review, living-person, DNA/genomic, exact-location, and infrastructure concerns remain explicit;
- access credentials or private endpoints are never surfaced in output or logs;
- package findings cannot clear risk.

### 5. Review and separation of duties

Prove that:

- package output is a review candidate, not a ReviewRecord approval;
- missing reviewer or review reference remains unresolved;
- author and reviewer identity remain distinct where supplied;
- package code cannot self-approve;
- AI and watcher summaries remain advisory;
- review conflict and recusal states are preserved.

### 6. Validation defects and conflicts

Prove that:

- all validation defects remain visible;
- defect severity is not silently downgraded;
- conflict between evidence, descriptors, rights, roles, sensitivity, or review state is preserved;
- conflict cannot be converted into success by choosing one input silently;
- remediation requirements remain addressable and deterministic.

### 7. Evidence-reference preservation and non-closure

Prove that:

- EvidenceRef values are preserved exactly or transformed only under an accepted rule;
- missing or unresolved EvidenceRef causes a safe outcome;
- package code does not create an EvidenceBundle;
- generated text, summaries, scores, and notes do not become evidence;
- evidence resolution remains an external governed responsibility.

### 8. Candidate outputs and lifecycle sink prohibition

Prove that:

- outputs are caller-owned in-memory or explicit candidate objects;
- the package does not select RAW versus QUARANTINE without accepted decision inputs;
- package code cannot write to lifecycle, registry, receipt, proof, catalog, release, or public roots;
- sink attempts are detected and fail the test;
- candidate outputs do not claim promotion or publication.

### 9. Correction, supersession, withdrawal, and rollback

Prove that:

- supplied correction and lineage references are preserved;
- superseded material is not presented as current;
- withdrawn material cannot return a public-ready result;
- rollback references remain explicit;
- replay after correction yields a deterministic state change without deleting history.

### 10. Logging, privacy, and no-leak behavior

Prove that logs and failures do not expose:

- source payloads or excerpts;
- living-person data;
- DNA/genomic or health data;
- exact sensitive coordinates;
- credentials or signed URLs;
- private filesystem paths;
- proprietary or culturally restricted content;
- unredacted review notes.

Use canary values and scan captured output.

### 11. Determinism and replay

Prove that:

- identical controlled inputs and versions produce equivalent candidates and reason codes;
- identifier generation follows an accepted deterministic rule;
- time and randomness are injected or fixed;
- source/candidate ordering does not alter meaning unexpectedly;
- replay preserves lineage and does not mutate prior artifacts.

### 12. Public-path and authority denial

Prove that package output cannot become:

- a public API response;
- a MapLibre layer or popup payload;
- an AI answer;
- a catalog-closed record;
- a proof or release manifest;
- an activation or policy decision;
- a public preview or export.

Root integration tests should corroborate these boundaries at governed interfaces.

[Back to top](#top)

---

## Steward-gate test matrix

| Condition | Connector-local expected outcome | Root integration responsibility |
|---|---|---|
| Conforming candidate inputs, no unresolved gate | Return reviewable candidate only. | Review/policy/lifecycle services decide next state. |
| Package-local descriptor supplied as authority | Reject or mark nonconforming. | Schema/registry tests enforce accepted descriptor authority. |
| Source role `TBD` or missing | Hold, review, conflict, or error. | Source-admission tests enforce role vocabulary. |
| Attempted role elevation | Deny elevation; preserve attempted claim. | Policy and authority-register tests enforce role limits. |
| Rights unknown | Hold, quarantine candidate, abstain, or deny. | Rights policy tests decide admissibility. |
| Sensitivity unknown | Hold or quarantine candidate. | Sensitivity policy and redaction tests decide exposure. |
| Review missing | Return unresolved review candidate. | Review service/separation-of-duties tests enforce approval. |
| Conflicting descriptor or evidence refs | Conflict or hold; preserve both. | Evidence/source governance tests resolve or abstain. |
| EvidenceRef unresolved | Abstain/hold; no EvidenceBundle. | Evidence resolver tests control closure. |
| Validation defect | Invalid/hold/quarantine candidate. | Validator and lifecycle tests govern progression. |
| Correction or withdrawal reference | Preserve state and restrict candidate. | Release/correction/rollback tests govern public state. |
| Attempted lifecycle write | Error and fail test. | Root boundary tests verify no filesystem/API path exists. |
| Attempted catalog/release emission | Error and fail test. | Catalog/release gates enforce authority. |
| Attempted public response | Error and fail test. | Governed API/UI tests deny direct package exposure. |
| Network or credential access | Error and fail test. | CI sandbox and security tests corroborate. |
| Adapter returns indeterminate state | Hold/quarantine/error. | Integration tests preserve indeterminate state. |

These semantic outcomes remain proposed until an accepted contract defines exact enums and reason codes.

[Back to top](#top)

---

## Finite outcome and failure assertions

Tests should not use generic truthy success when a bounded outcome is required.

A future accepted package contract may use outcomes such as:

- `REVIEW_CANDIDATE`
- `RAW_CANDIDATE`
- `QUARANTINE_CANDIDATE`
- `HOLD`
- `DENY`
- `ABSTAIN`
- `CONFLICT`
- `NO_OP`
- `ERROR`

Exact names are **PROPOSED / NEEDS VERIFICATION**.

Every outcome assertion should cover:

- code/value;
- reason code;
- human-safe explanation;
- unresolved fields;
- preserved source/artifact/review references;
- policy/evidence/release non-authority;
- retry or remediation posture;
- redaction of protected content;
- deterministic serialization where required.

Tests must reject:

- unbounded `success`;
- empty reason codes for denied or unresolved cases;
- implicit allow on unknown state;
- exception messages that leak inputs;
- fallback from error to public-safe result without a governed rule;
- AI-generated explanations used as the asserted truth source.

[Back to top](#top)

---

## Lifecycle, evidence, catalog, release, and public-path tests

KFM's lifecycle remains:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

The package sits before or at the source-admission edge and may prepare caller-owned candidates only.

Connector-local tests should prove absence of authority to:

- persist RAW or QUARANTINE directly;
- create WORK or PROCESSED objects;
- emit CatalogRecord, STAC, DCAT, PROV, or triplet authority records;
- resolve EvidenceRef into a production EvidenceBundle;
- emit proof packs or release manifests;
- approve correction, withdrawal, rollback, or promotion;
- serve a browser, map, public API, Focus Mode, or model endpoint.

Use fakes or spies that fail if any governed writer, filesystem path, database client, registry client, catalog client, release client, or public transport is invoked.

Root tests should separately prove:

- public clients cannot import or invoke the package;
- unresolved candidates are inaccessible through governed APIs;
- RAW and QUARANTINE are not normal UI surfaces;
- policy, evidence, catalog, release, correction, and rollback gates remain mandatory;
- promotion is a governed state transition, not a connector result.

[Back to top](#top)

---

## Determinism, replay, and observability

### Determinism

Tests should verify, where the package contract requires it:

- stable normalization of explicitly allowed metadata;
- stable ordering of defects, conflicts, and references;
- deterministic candidate IDs from accepted inputs;
- fixed serialization and canonicalization rules;
- injected timestamps, clocks, and ID factories;
- no dependence on filesystem iteration order, locale, environment, or network state.

### Replay

Replay tests should preserve:

- input identities and versions;
- package, adapter, contract, schema, and policy versions;
- review and disposition history;
- correction, supersession, withdrawal, and rollback lineage;
- prior outcomes without destructive overwrite.

### Observability

Test assertions should cover structured, redacted events such as:

- operation start/end;
- candidate type;
- finite outcome;
- reason codes;
- defect counts;
- unresolved gate counts;
- adapter versions;
- duration/resource counters;
- correlation and replay IDs.

Observability records are not EvidenceBundles, approvals, receipts, proofs, or release records unless an accepted object contract explicitly says so.

[Back to top](#top)

---

## Collection, runner, and CI boundary

### Current CI state

No supported local test command was verified because:

- `pyproject.toml` declares only project name and version;
- no test framework dependency is declared;
- no runner configuration was inspected for this package;
- conventional named test modules were not found;
- the connector and descriptor workflows contain TODO echo steps.

Therefore this README does not publish a quickstart command as fact.

### Future minimum runner proof

Before a command is documented as supported, verify:

- package installation or import path;
- supported Python version;
- test framework and version;
- dependency lock or reproducible environment;
- test discovery;
- markers and network blocking;
- temporary filesystem isolation;
- fixture paths;
- expected pass/fail examples;
- CI invocation parity.

### CI requirements

Substantive CI should eventually prove:

1. test discovery is nonzero;
2. import safety passes;
3. network is denied by default;
4. lifecycle/registry/catalog/release writers are inaccessible or mocked and asserted unused;
5. nonconforming descriptor cases fail;
6. role/rights/sensitivity/review/evidence unknown states fail closed;
7. log-redaction canaries pass;
8. deterministic replay passes;
9. fixture safety checks pass;
10. at least one expected failing canary proves the gate is real.

A green TODO-only workflow is not validation evidence.

[Back to top](#top)

---

## Validation

### Documentation validation

This README should be checked for:

- one H1;
- balanced fenced code blocks;
- unique section headings;
- resolved internal quick links;
- current base commit and prior blob;
- no unsupported test-result claims;
- no placeholder rollback SHA;
- no path claim presented as settled when it is conflicted.

### Future executable validation

A credible test lane should report:

| Measure | Required evidence |
|---|---|
| Collection | Count and names of collected tests. |
| Results | Pass, fail, skip, xfail, error counts. |
| Coverage | Meaningful branch/negative-path coverage, not only line percentage. |
| Network | Proof that default tests cannot reach the network. |
| Side effects | Proof that imports and pure calls do not mutate governed state. |
| Fixtures | Inventory, safety review, and schema/version bindings. |
| Negative cases | Descriptor, role, rights, sensitivity, review, evidence, conflict, sink, and public-path failures. |
| Determinism | Replay or property evidence under fixed versions. |
| Security/privacy | Redaction and secret/personal/location leakage checks. |
| CI | Workflow, job, commit, and log references. |
| Rollback | Reproducible way to revert test and documentation changes. |

Passing tests must not upgrade package, source, policy, evidence, catalog, or release maturity beyond what the executed scope proves.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| `connectors/manual_curation/tests/README.md` prior blob | **CONFIRMED** | A test-boundary document existed. | Executable tests, runner, fixtures, CI, or pass state. |
| Exact named test probes | **CONFIRMED NOT FOUND AT PINNED BASE** | Conventional test files and local fixture README were absent at those paths. | Absence of all differently named files. |
| Parent connector README | **CONFIRMED** | Manual-curation connector boundary and no-publication posture. | Runtime behavior. |
| Source-layout README v0.2 | **CONFIRMED** | Actual package tree and process-ownership conflict. | Buildability or imports. |
| Child package README v0.2 | **CONFIRMED** | Greenfield scaffold, candidate-only outputs, descriptor rejection, steward-gate and lifecycle boundaries. | Implemented package behavior. |
| `pyproject.toml` | **CONFIRMED PLACEHOLDER** | Project name and `0.0.0`. | Build backend, dependencies, Python support, runner, or installability. |
| `__init__.py`, `fetch.py`, `admit.py` | **CONFIRMED EMPTY / COMMENT-ONLY** | No named executable behavior in those files. | Absence of differently named implementation. |
| `descriptor.yaml` | **CONFIRMED NONCONFORMING PLACEHOLDER** | Current minimal fields and unsafe unresolved posture. | Source authority or public safety. |
| Root `tests/README.md` | **CONFIRMED DOCTRINE** | Canonical trust-spine testing responsibility. | This connector's executable coverage. |
| `tests/fixtures/README.md` | **CONFIRMED DOCUMENTED** | Unit-test-scoped fixture posture and split from root `fixtures/`. | Manual-curation child fixture existence. |
| Source authority register | **CONFIRMED EMPTY ENTRIES** | No machine source authority entry. | Future activation decisions. |
| SourceDescriptor schemas | **CONFIRMED CONFLICTED** | Populated singular schema and permissive plural scaffold. | Accepted final schema authority. |
| Policy READMEs | **CONFIRMED STUBS** | Source, rights, and sensitivity policy surfaces are greenfield. | Enforced policy. |
| Connector workflows | **CONFIRMED TODO-ONLY AT INSPECTED BODIES** | Workflow names and placeholder commands. | Substantive validation or branch protection. |

Memory, previous generated prose, a green badge, or a merged README is not implementation evidence.

[Back to top](#top)

---

## Review burden

A future executable change to this test lane should receive review from the owners materially affected.

| Change | Minimum review concern |
|---|---|
| Test framework, runner, packaging, or CI | Package maintainer · test/CI steward |
| Descriptor and source-role cases | Source steward · contract/schema steward |
| Rights or licensing cases | Rights reviewer · policy steward |
| Sensitivity, living-person, DNA, cultural, exact-location, or infrastructure cases | Relevant sensitivity/domain reviewer |
| Review workflow or separation of duties | Review-workflow steward · governance reviewer |
| EvidenceRef/EvidenceBundle behavior | Evidence steward |
| Lifecycle or sink-boundary assertions | Pipeline/data steward |
| Catalog or release denial | Catalog/release steward |
| Logs, secrets, filesystem, network, or credentials | Security reviewer |
| Fixture placement or safety | Fixture steward · test steward |
| Package/test relocation | Architecture steward · Directory Rules review; ADR/migration review if required |

Tests involving sensitive classes should be reviewed for harmful combinations, not only individual fixture fields.

[Back to top](#top)

---

## Smallest safe implementation sequence

1. **Resolve package/test ownership posture.** Keep test movement coupled to the process-not-source architecture decision.
2. **Accept a test framework and package runner.** Add reproducible package metadata and a supported Python version.
3. **Add import-safety tests first.** Prove no network, filesystem, credential, registry, lifecycle, or adapter side effects.
4. **Add descriptor rejection tests.** The current YAML must fail authority use.
5. **Define candidate and outcome contracts.** Do not invent enums independently in tests.
6. **Create compact synthetic fixtures.** Select a governed child lane and document the split from root fixtures.
7. **Add source-role, rights, sensitivity, review, conflict, and evidence non-closure tests.**
8. **Add sink-prohibition spies.** Fail on lifecycle, registry, catalog, evidence, release, or public-interface access.
9. **Add correction, supersession, withdrawal, rollback, and replay tests.**
10. **Add log-redaction canaries.**
11. **Add root trust-spine integration tests.** Keep package-local and cross-system proof separate.
12. **Replace TODO workflows with substantive commands and negative canaries.**
13. **Capture CI evidence.** Record collection counts, outcomes, environment, commit, and logs.
14. **Claim only the maturity proven by the executed tests.**

Do not start with live source access, real steward case files, production credentials, lifecycle writes, or public UI integration.

[Back to top](#top)

---

## Definition of done

Do not call this test lane implemented, comprehensive, CI-enforced, production-ready, or release-gating until all applicable conditions are proven:

- [ ] Permanent package and test ownership is decided or explicitly time-bounded.
- [ ] Package metadata defines a reproducible test environment.
- [ ] Supported Python and test framework versions are recorded.
- [ ] Test discovery is nonzero and deterministic.
- [ ] Imports are no-network and side-effect free.
- [ ] Current nonconforming descriptor is rejected for authority use.
- [ ] Source-role anti-collapse is tested.
- [ ] Rights, sensitivity, consent, sovereignty, access, and review uncertainty fail closed.
- [ ] Review candidates cannot self-approve.
- [ ] Validation defects and conflicts remain visible.
- [ ] EvidenceRef preservation and EvidenceBundle non-closure are tested.
- [ ] Candidate outputs are caller-owned and cannot select lifecycle sinks.
- [ ] Direct registry, lifecycle, catalog, evidence, release, and public-interface writes are impossible or detected.
- [ ] Correction, supersession, withdrawal, rollback, and replay are tested.
- [ ] Logs and exceptions do not leak protected material.
- [ ] Fixtures are synthetic, public-safe, versioned, and routed to an accepted home.
- [ ] Connector-local and root integration responsibilities are not duplicated.
- [ ] CI executes substantive tests and includes an expected-failure canary.
- [ ] Collection, results, coverage, network, side-effect, fixture, and CI evidence are retained.
- [ ] Review responsibilities and separation-of-duties expectations are recorded.
- [ ] Public clients have no direct path to the package or unresolved candidates.
- [ ] Every maturity claim cites current executable evidence.

A passing connector-local suite still does not activate a source, resolve evidence, close a catalog, approve a release, or publish a claim.

[Back to top](#top)

---

## Rollback

This revision changes documentation only.

**Base commit:** `5f06485d910ee1b4855aff3274623f801a798d11`  
**Prior README blob:** `e5478c2c61afdbce97ac7f81504e98ca6aaf0d45`

Before merge, rollback means closing or abandoning the review branch and leaving `main` unchanged. After merge, rollback means a transparent revert of the documentation commit or restoration of the prior blob through a new reviewed commit.

Rollback is required if this README is used to claim:

- executable tests that do not exist;
- test collection, coverage, CI success, or runtime proof without logs;
- SourceDescriptor conformance or activation from the local YAML;
- public sensitivity clearance from `sensitivity_floor: public`;
- accepted test placement despite the process-not-source conflict;
- source-role, rights, sensitivity, review, evidence, catalog, release, or publication authority;
- fixture safety without inventory and review;
- direct lifecycle or public-path access.

Do not delete history, force-push shared branches, or silently replace correction lineage.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Decide whether connector-local tests remain the correct permanent home. | **CONFLICTED / NEEDS VERIFICATION** | Architecture decision aligned with package ownership, drift entry, and migration/ADR note if required. |
| Confirm differently named tests or helpers. | **UNKNOWN** | Complete tree inspection or mounted checkout. |
| Select and configure the test framework and runner. | **PROPOSED** | Package metadata, lock/reproducible environment, collection output, and accepted command. |
| Confirm package installation and import behavior. | **UNKNOWN** | Isolated install/build and import test. |
| Define accepted candidate, review, disposition, conflict, and reason-code contracts. | **PROPOSED** | Contracts, schemas, examples, and versioning rules. |
| Resolve singular/plural SourceDescriptor schema authority. | **CONFLICTED** | Accepted ADR/migration, canonical schema, fixtures, validator parity, and registry update. |
| Decide future of package-local `descriptor.yaml`. | **NEEDS VERIFICATION** | Source-governance decision separating process metadata from source identity. |
| Select manual-curation fixture home. | **NEEDS VERIFICATION** | Fixture steward decision and child README. |
| Create synthetic valid/invalid/denied/abstain/conflict/rollback fixtures. | **PROPOSED** | Reviewed public-safe payloads with metadata. |
| Confirm source-role, rights, sensitivity, consent, and review-routing behavior. | **UNKNOWN** | Accepted policy, package code, fixtures, tests, and integration evidence. |
| Confirm evidence-reference preservation and non-closure. | **UNKNOWN** | Evidence contract integration and negative tests. |
| Confirm caller-owned RAW/QUARANTINE candidates and sink prohibition. | **UNKNOWN** | Accepted interface, code, spies/fakes, and tests. |
| Confirm no-network and side-effect-free defaults. | **UNKNOWN** | Executable tests and CI logs. |
| Confirm log, secret, privacy, and protected-location redaction. | **UNKNOWN** | Canary fixtures, captured output, and security review. |
| Confirm correction, supersession, withdrawal, rollback, and replay behavior. | **UNKNOWN** | Contracts, code, fixtures, deterministic tests, and runtime evidence. |
| Add root trust-spine integration coverage. | **PROPOSED** | Root tests proving lifecycle, evidence, policy, catalog, release, and public-path boundaries. |
| Replace TODO-only connector workflows. | **PROPOSED** | Real commands, permissions review, negative canary, and passing/failing evidence. |
| Assign semantic owners and reviewers. | **NEEDS VERIFICATION** | CODEOWNERS and governance review aligned to actual teams. |
| Confirm runtime, deployment, activation, and release posture. | **UNKNOWN** | Runtime traces, deployment config, activation record, release evidence, and rollback proof. |

[Back to top](#top)

---

## Maintainer checklist

Before adding executable tests:

- verify package and test ownership;
- preserve manual curation as a process, not a fabricated source;
- reject the local descriptor for authority use;
- keep real source materials and sensitive case files out of tests;
- select the correct fixture home;
- default to no network, no credentials, and no side effects;
- test unknown and denied states before positive paths;
- keep source role, rights, sensitivity, review, evidence, lifecycle, catalog, and release states separate;
- assert caller-owned outputs and forbidden sinks;
- preserve conflicts, defects, corrections, and rollback lineage;
- keep package-local tests separate from root trust-spine integration;
- pair every test-maturity claim with collection, logs, and current evidence.

**Core rule:** prove that helper mechanics preserve steward gates; never let tests become the gate authority.

[Back to top](#top)
