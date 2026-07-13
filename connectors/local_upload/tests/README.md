<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-local-upload-tests-readme
title: connectors/local_upload/tests/ — Local Upload Greenfield Test and Trust-Edge Proof Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Test steward · Fixture steward · Source-intake steward · Rights reviewer · Privacy/sensitivity reviewer · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; connector-tests; greenfield-package; local-upload; trust-edge; untrusted-bytes; negative-first; synthetic-only; no-network; no-execution; rights-fail-closed; sensitivity-fail-closed; quarantine-first; no-activation; no-publication
current_path: connectors/local_upload/tests/README.md
truth_posture: CONFIRMED README-only named connector test lane, exact absence of conventional conftest/fetch/admit/descriptor/archive-safety tests and local fixture README at the pinned base, repository-present 0.0.0 package scaffold, empty initializer, comment-only fetch/admit modules, four-field nonconforming descriptor, merged v0.2 package and source-layout boundaries, empty source-authority register, SourceDescriptor schema conflict, absent named local-upload policy README, canonical root tests and split fixture doctrine, and TODO-only connector workflows / PROPOSED negative-first connector-local test contract, arbitrary-file security matrix, safe fixture routing, deterministic outcome assertions, and smallest safe implementation sequence / UNKNOWN differently named tests, test framework, runner, collection, package installation, scanner/parser integration, fixture payloads, coverage, substantive CI, runtime behavior, activation, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: ca4b6eac54103e25bf4d08a3285fcbd29751f1b5
  prior_blob: 106f3e9f3cdb9c4b83722e0487d5fc4ae27fec6b
  readme_introduction_commit: b45cb13fc8e5428d8e4eb566c898366ae576dc0f
related:
  - ../README.md
  - ../pyproject.toml
  - ../src/README.md
  - ../src/local_upload/README.md
  - ../src/local_upload/__init__.py
  - ../src/local_upload/fetch.py
  - ../src/local_upload/admit.py
  - ../src/local_upload/descriptor.yaml
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/connector-gate.yml
  - ../../../.github/workflows/source-descriptor-validate.yml
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../../docs/sources/ADMISSION_PROCESS.md
  - ../../../docs/sources/catalog/local_upload/README.md
  - ../../../docs/sources/catalog/local_upload/user-file-upload.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/README.md
  - ../../../policy/rights/README.md
  - ../../../policy/sensitivity/README.md
  - ../../../tests/README.md
  - ../../../tests/fixtures/README.md
  - ../../../fixtures/README.md
  - ../../../release/
tags: [kfm, connectors, local-upload, local_upload, tests, trust-edge, untrusted-files, negative-first, candidate, source-admission, descriptor, rights, sensitivity, privacy, security, archives, provenance, raw, quarantine, no-network, no-execution, no-publication]
notes:
  - "Direct reads at the pinned base confirm that the test lane contains this README while exact probes for conftest.py, test_fetch.py, test_admit.py, test_descriptor.py, test_archive_safety.py, and tests/fixtures/README.md returned Not Found."
  - "Absence statements are bounded to the named paths and pinned commit. Differently named tests, helpers, or fixtures remain UNKNOWN until directly inspected."
  - "The adjacent package is a 0.0.0 scaffold with an empty initializer, comment-only fetch.py and admit.py, and a four-field descriptor.yaml placeholder. No supported package behavior exists for tests to exercise."
  - "The local descriptor leaves role and rights unresolved and asserts sensitivity_floor: public. Tests must reject it as source authority, activation, rights clearance, sensitivity clearance, or release authorization."
  - "The merged package and source-layout v0.2 READMEs define arbitrary-file, archive, active-content, privacy, secret, candidate-output, lifecycle, and public-path boundaries. This test README turns those boundaries into proposed enforceability requirements without claiming implementation."
  - "Only this Markdown file is in scope. No package code, metadata, dependency, descriptor, registry record, policy, schema, fixture, executable test, workflow, uploaded payload, credential, lifecycle artifact, evidence object, release object, or public artifact is created or changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Local Upload Greenfield Test and Trust-Edge Proof Boundary

> Repository-grounded test boundary for `connectors/local_upload/tests/`. The lane currently contains documentation, not an executable suite. Its future job is to prove that local-upload package mechanics treat every submitted file as untrusted bytes plus unverified claims and cannot bypass KFM source, policy, lifecycle, evidence, release, correction, or public-access controls.

**Document lifecycle:** `draft v0.2`  
**Current test maturity:** `CONFIRMED` README-only at the named probes; no test run or coverage is established  
**Owner:** `OWNER_TBD`  
**Authority:** connector-local behavior proof only; no contract, schema, policy, source, fixture, lifecycle, evidence, release, or publication authority  
**Default posture:** synthetic only · no network · no active-content execution · negative first · deterministic failure · fail closed

> [!IMPORTANT]
> The adjacent package is a non-operational `0.0.0` scaffold. A test README, proposed test name, green workflow, or future passing unit test cannot prove source activation, rights clearance, sensitivity clearance, EvidenceBundle closure, release readiness, or public safety.

> [!CAUTION]
> Real uploaded files do not belong in this test lane. User submissions can contain personal or genomic data, protected locations, credentials, proprietary material, hidden metadata, active content, malicious archives, or harmful joins. Tests must use compact synthetic or explicitly reviewed public-safe fixtures and must prove that unsafe or indeterminate cases fail closed.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Current state](#current-test-lane) · [Repository fit](#repository-fit) · [Local versus root proof](#connector-local-versus-root-trust-spine-proof) · [What belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Environment](#test-environment-contract) · [Fixtures](#fixture-routing-and-safety) · [Required families](#required-test-families) · [Security matrix](#arbitrary-file-security-test-matrix) · [Outcomes](#finite-outcome-and-failure-assertions) · [Lifecycle](#lifecycle-evidence-release-and-public-path-tests) · [Determinism](#determinism-replay-and-observability) · [CI](#collection-runner-and-ci-boundary) · [Validation](#validation) · [Evidence](#evidence-basis) · [Review](#review-burden) · [Implementation sequence](#smallest-safe-implementation-sequence) · [Definition of done](#definition-of-done) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/local_upload/tests/` is reserved for tests of narrow behavior owned by the local-upload connector package.

Its future responsibilities are to prove that package code:

- imports without network, filesystem, credential, scanner, or lifecycle side effects;
- treats filenames, extensions, MIME types, paths, metadata, and uploader statements as untrusted hints;
- preserves upload-event identity separately from content identity;
- calculates byte length and content digests deterministically when that behavior exists;
- enforces explicit resource and container limits;
- never executes active content from an upload;
- rejects unsafe archive members and extraction paths;
- represents scanner or parser uncertainty explicitly;
- preserves candidate source role and unresolved rights and sensitivity states;
- rejects the package-local descriptor as governance authority;
- returns caller-owned findings or admission candidates rather than selecting lifecycle sinks;
- cannot emit an EvidenceBundle, proof, catalog item, release object, public preview, or publication decision;
- does not leak payload bytes, secrets, personal data, exact coordinates, private paths, or proprietary content through logs and failures;
- remains deterministic and reviewable under replay.

This lane does not prove the entire KFM trust spine by itself. Cross-system enforcement belongs in the canonical root `tests/` responsibility lanes.

[Back to top](#top)

---

## Authority level

**Connector-local test documentation and future package-behavior proof only.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Owning responsibility | **CONFIRMED** | Connector-local tests may live beside the source-specific connector whose mechanics they exercise. |
| Current path | **CONFIRMED** | `connectors/local_upload/tests/README.md` exists at the pinned base. |
| Executable tests | **NOT FOUND AT NAMED PROBES / OTHERWISE UNKNOWN** | Exact conventional test paths returned `Not Found`; differently named tests remain unknown. |
| Test framework and runner | **UNKNOWN** | No accepted runner, configuration, collection command, marker set, dependency, or invocation was verified. |
| Package under test | **CONFIRMED PLACEHOLDER** | `kfm-connector-local_upload` is version `0.0.0`; initializer is empty; fetch/admit modules are comment-only. |
| Local descriptor | **NONCONFORMING / MUST BE REJECTED** | Minimal fields cannot establish source identity, role, rights, sensitivity, activation, or release. |
| Stable fixtures | **NOT ESTABLISHED FOR THIS LANE** | No connector-local fixture README was found; exact routing and payload inventory remain unresolved. |
| Root test authority | **CONFIRMED DOCTRINE** | Root `tests/` owns cross-system enforceability proof. |
| Fixture split | **CONFIRMED DOCUMENTED / CHILD PLACEMENT NEEDS VERIFICATION** | `tests/fixtures/` is test-local; root `fixtures/` is cross-cutting. The exact local-upload child lane is not selected here. |
| Source authority | **NOT ESTABLISHED** | The machine source-authority register is `PROPOSED` with `entries: []`. |
| Schema authority | **CONFLICTED** | The populated singular SourceDescriptor schema points to an empty plural scaffold as canonical. |
| Lane-specific policy | **NOT FOUND AT NAMED PATH** | The named local-upload policy README was not present at the inspected base. |
| Connector CI | **TODO-ONLY** | Named connector and descriptor workflows execute placeholder echo steps. |
| Test results and coverage | **NONE VERIFIED** | No collection, pass, skip, xfail, coverage, mutation, resource, or security result was observed. |
| Source activation | **DENIED / NOT VERIFIED** | Tests cannot substitute for accepted descriptor, policy, review, and activation decisions. |
| Public release | **NONE** | A connector-local test cannot approve or create public output. |

A test can prove only the behavior it actually executes with controlled inputs. It cannot create governance authority through assertion text.

[Back to top](#top)

---

## Current test lane

### Bounded repository snapshot

Direct reads at base commit `ca4b6eac54103e25bf4d08a3285fcbd29751f1b5` support this named surface:

```text
connectors/local_upload/
├── README.md                              # parent connector boundary v0.1
├── pyproject.toml                         # kfm-connector-local_upload, version 0.0.0
├── src/
│   ├── README.md                          # source-layout boundary v0.2
│   └── local_upload/
│       ├── README.md                      # package trust-edge boundary v0.2
│       ├── __init__.py                    # empty
│       ├── fetch.py                       # comment-only placeholder
│       ├── admit.py                       # comment-only placeholder
│       └── descriptor.yaml                # four-field placeholder
└── tests/
    └── README.md                          # this test boundary
```

Exact probes returned `Not Found` for:

```text
connectors/local_upload/tests/conftest.py
connectors/local_upload/tests/test_fetch.py
connectors/local_upload/tests/test_admit.py
connectors/local_upload/tests/test_descriptor.py
connectors/local_upload/tests/test_archive_safety.py
connectors/local_upload/tests/fixtures/README.md
```

These are bounded absence statements. They do not prove that no differently named file exists now or will exist later.

### Current maturity table

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| Test README | v0.1 before this revision | Documentation existed; no execution evidence followed. |
| Conventional test modules | Not found at the named probes | No named import, fetch, admit, descriptor, or archive-safety coverage. |
| Test-local fixture documentation | Not found at the named probe | No connector-local fixture authority or inventory established. |
| Package metadata | Name and `0.0.0` only | Test dependencies, framework, runner, Python support, and package installation remain unknown. |
| Package behavior | Empty/comment-only scaffold | There is no supported behavior for positive-path tests to exercise. |
| Descriptor | `name: local_upload`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public` | Tests should reject it as authority rather than normalize it into acceptance. |
| Workflows | TODO echo steps | A green run would prove only that the placeholder step executed. |

There is no supported test quickstart. Any command would be speculative until package metadata, test dependencies, framework, configuration, and collection behavior are accepted and observed.

[Back to top](#top)

---

## Repository fit

Directory Rules separate source-specific implementation, connector-local behavior tests, canonical trust-spine tests, fixtures, schemas, policy, lifecycle data, evidence, and release.

| Responsibility | Owning surface | Relationship to this lane |
|---|---|---|
| Local-upload package mechanics | `connectors/local_upload/src/local_upload/` | Subject under test after behavior exists. |
| Connector-local package tests | `connectors/local_upload/tests/` | This lane. |
| Cross-system enforceability | Root `tests/` | Proves source, policy, lifecycle, evidence, release, correction, rollback, and public-path boundaries. |
| Test-local fixtures | `tests/fixtures/` under an accepted child lane | Candidate home for small test-specific fixtures; exact local-upload placement remains to be ratified. |
| Cross-cutting reusable fixtures | Root `fixtures/` under an accepted child lane | Shared synthetic corpora; not owned here. |
| Human-facing source doctrine | `docs/sources/` | Tests follow it; they do not redefine it. |
| Object meaning | `contracts/` | Tests assert accepted meaning; local helpers do not become contracts. |
| Machine shape | `schemas/` | Tests validate accepted schemas; snapshots do not become schema authority. |
| Source identity and activation | Registry and control-plane authority surfaces | Tests use synthetic or reviewed references; they cannot activate sources. |
| Rights, sensitivity, privacy, security, access, and release policy | `policy/` | Tests exercise decisions; they do not decide policy. |
| Lifecycle persistence | `data/` through governed orchestration | Tests must use isolated temporary state and cannot write real lifecycle data. |
| Evidence closure | Evidence/proof responsibility roots | Tests may use toy objects but cannot create real EvidenceBundles or proofs. |
| Release, correction, withdrawal, and rollback | `release/` | Tests verify contracts and gates; they do not approve releases. |
| Public API and UI behavior | Governed applications and root tests | Connector-local tests do not expose or approve public upload access. |

[Back to top](#top)

---

## Connector-local versus root trust-spine proof

The test split must remain explicit.

### Connector-local tests may prove

- pure function behavior owned by the `local_upload` package;
- deterministic upload-event and content-identity helpers;
- safe filename and declared-versus-detected media-type handling;
- bounded content inspection helpers;
- archive-member inventory and path rejection;
- scanner/parser adapter contracts using fakes;
- descriptor-placeholder rejection;
- candidate outcome construction;
- redacted error and log payloads;
- import-time and default-test no-network behavior;
- refusal to select lifecycle or release destinations.

### Root trust-spine tests must prove

- accepted descriptor and source-activation workflows;
- contract/schema/policy integration;
- rights and sensitivity decisions across responsibility roots;
- governed RAW or QUARANTINE landing through orchestration;
- evidence resolution and cite-or-abstain behavior;
- catalog and triplet closure;
- release, correction, withdrawal, supersession, retention, deletion, and rollback;
- public client denial for RAW, WORK, QUARANTINE, and unpublished candidates;
- separation of uploader, reviewer, and release authority;
- end-to-end audit receipts and policy-denial evidence.

A connector-local passing suite cannot be cited as end-to-end release proof.

[Back to top](#top)

---

## What belongs here

After package contracts and test tooling are accepted, this lane may contain:

- connector-local unit tests for pure package behavior;
- import and packaging smoke tests that remain offline and side-effect-free;
- deterministic tests for byte counts, hashes, and identity preservation;
- declared-versus-detected metadata tests;
- bounded inspection and limit tests;
- archive and compound-container rejection tests;
- scanner/parser adapter tests using inert fakes or reviewed safe adapters;
- descriptor rejection and candidate-state preservation tests;
- finite-outcome tests for admit-candidate, hold, quarantine-candidate, deny, abstain, no-op, rate-limit, and error semantics once contracts are accepted;
- secret-safe logging and exception tests;
- synthetic exact-versus-generalized geometry separation tests;
- tests proving caller-owned candidates do not become lifecycle writes;
- package-local test helpers with no production authority;
- README files that document scope, fixture routing, and verification status.

Every executable test must identify the behavior it proves and the authority it does not prove.

[Back to top](#top)

---

## What does not belong here

This lane must not contain or become:

- real user uploads, source exports, personal files, genomic data, proprietary documents, exact protected locations, credentials, or malware specimens;
- a browser endpoint, CLI service, watcher, upload queue, scanner daemon, parser service, or public route;
- production code or implementation shortcuts embedded in tests;
- authoritative SourceDescriptors, activation decisions, rights decisions, sensitivity decisions, policy bundles, schemas, contracts, registries, receipts, proofs, release records, or lifecycle data;
- direct writes to `data/raw/`, `data/quarantine/`, `data/work/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/proofs/`, `data/published/`, or `release/`;
- network calls to live sources, scanners, model services, geocoders, fonts, schemas, or metadata endpoints in the default suite;
- extraction into the repository, user home, shared temporary directories, or lifecycle roots;
- execution of uploaded scripts, binaries, macros, notebooks, PDF actions, office automation, shell commands, or embedded objects;
- snapshots containing payload fragments, personal data, secrets, precise locations, private paths, signed URLs, or proprietary content;
- a parallel fixture authority under `connectors/local_upload/tests/fixtures/` without an accepted placement decision;
- tests that pass solely because all cases are skipped, xfailed, deselected, or uncollected;
- assertions that a clean scan, recognized type, successful parse, valid schema, passing unit test, or green workflow proves truth or publication safety.

[Back to top](#top)

---

## Test environment contract

The default connector-local suite must be hermetic enough to run without privileged infrastructure.

### Required defaults

- no live network;
- no production credentials or environment-dependent secrets;
- no writes outside a caller-owned temporary workspace;
- no access to user home directories, browser profiles, SSH material, cloud credentials, system keychains, or production configuration;
- no reliance on wall-clock time, random ordering, external locale, host timezone, or nondeterministic UUIDs without controlled injection;
- no scanner, parser, native plugin, OCR engine, model, database, or service startup on package import;
- no mutation of repository files, lifecycle data, fixture sources, or shared caches;
- explicit resource limits for tests that exercise size, recursion, archive, image, page, row, or decompression behavior;
- process isolation for any later complex parser or scanner integration tests;
- cleanup assertions for every temporary object and process;
- redacted failure output.

### Environment-controlled behavior

When behavior depends on time, randomness, actor identity, path, policy state, scanner version, parser version, or operation mode, tests should inject those values explicitly rather than discover them from the host.

### Network assertion

A default test run should fail when package code attempts network access. Network-enabled integration tests, if ever accepted, require an explicit non-default mode, isolated credentials, bounded endpoints, source-steward review, and separate CI treatment.

[Back to top](#top)

---

## Fixture routing and safety

No local-upload fixture lane is established by this README.

### Fixture-home decision

| Fixture need | Candidate responsibility | Current posture |
|---|---|---:|
| Tiny values created inside a test | Test code or test helper | **PROPOSED**, provided values are synthetic and not reused as authority. |
| Temporary byte streams and archive members | Caller-owned temporary workspace | **PROPOSED**, generated during the test and deterministically cleaned. |
| Stable unit-test-specific fixtures | Accepted child beneath `tests/fixtures/` | **NEEDS VERIFICATION** for exact local-upload path and ownership. |
| Cross-cutting reusable corpora | Accepted child beneath root `fixtures/` | **NEEDS VERIFICATION** for exact local-upload path and ownership. |
| Real uploaded or lifecycle material | Not a fixture | **FORBIDDEN** in test and fixture roots. |
| Generated CI output | Governed artifact/report lane | **OUTSIDE** fixture authority. |

### Fixture metadata expectations

Each stable fixture should record or make discoverable:

- synthetic or reviewed-public-safe status;
- purpose and owning test family;
- generation method or source note;
- rights and sensitivity posture;
- expected detected type and supplied type;
- byte length and checksum when material;
- expected outcome and reason;
- resource limits used by the test;
- whether geometry is precise, generalized, redacted, or absent;
- whether the fixture contains active-content canaries, secret-like canaries, or archive-risk canaries;
- review date and steward;
- replacement or supersession relationship when changed.

### Safe adversarial fixtures

Adversarial fixtures must be inert. Use toy strings, tiny archives, fake tokens, non-routable domains, synthetic coordinates, harmless headers, and non-executable canaries. Do not commit live credentials, functioning malware, exploit payloads, real private paths, or harmful precision data.

### Fixture mutation

Tests must not mutate stable fixtures. Copy or generate inputs into isolated temporary storage before exercising behavior.

[Back to top](#top)

---

## Required test families

The following families are **PROPOSED requirements**, not claims of current coverage.

### 1. Package and import boundary

Prove that:

- base import is offline and side-effect-free;
- no file, directory, cache, scanner, parser, credential, or lifecycle sink is discovered on import;
- only accepted public symbols are exported;
- optional heavy dependencies do not import unless explicitly invoked;
- package metadata does not imply source activation or publication;
- alternate or duplicate import namespaces fail unless migration-approved.

### 2. Descriptor rejection and authority separation

Prove that the current local YAML:

```yaml
name: local_upload
role: TBD
rights: TBD
sensitivity_floor: public
```

cannot:

- satisfy the accepted SourceDescriptor contract;
- establish a stable per-upload source identity;
- assign an elevated role;
- clear rights;
- clear sensitivity;
- authorize source contact or admission;
- set public precision;
- approve release.

Tests must preserve uploader claims separately from reviewed governance fields.

### 3. Upload-event and content identity

Prove that:

- upload-event identity is distinct from content identity;
- identical bytes submitted in separate events preserve separate actor, time, consent, rights, review, and correction lineage;
- filenames and timestamps do not become content identity;
- checksums and byte counts are deterministic for fixed bytes;
- duplicate-content detection does not silently discard an upload event;
- correction, withdrawal, and supersession references remain representable without mutation.

### 4. Filename and media-type distrust

Prove that:

- supplied filename and normalized display name remain distinct;
- client-declared and detected media types remain distinct;
- extension alone never determines parser, role, rights, sensitivity, or release;
- path separators, control characters, Unicode confusables, reserved names, and excessive names fail safely;
- filenames never select extraction, lifecycle, or public destinations.

### 5. Resource-bound inspection

Prove deterministic outcomes for:

- byte limit;
- wall-time limit;
- CPU or operation budget;
- memory budget where enforceable;
- page limit;
- row or record limit;
- image dimension and pixel-count limit;
- nested-object depth;
- archive member count;
- archive nesting depth;
- cumulative expanded size;
- compression-ratio limit;
- parser or scanner timeout;
- partial and truncated content.

Limit exhaustion must return an explicit hold, quarantine, or bounded error outcome rather than partial promotion.

### 6. Archive and container safety

Prove rejection or safe quarantine for:

- absolute paths;
- parent traversal;
- drive-letter and alternate-separator paths;
- path normalization ambiguity;
- symbolic and hard links;
- device files, pipes, sockets, and special files;
- duplicate member names;
- case-folding and Unicode-normalization collisions;
- recursive or excessively nested archives;
- encrypted or password-protected members without an accepted restricted mode;
- split, multipart, damaged, and unsupported containers;
- executables, scripts, macros, active content, and unsupported embedded objects;
- declared-versus-detected member-type conflicts;
- expansion bombs and cumulative extraction limits.

Tests should prefer member inventory without extraction. Any extraction test must use an isolated caller-owned temporary workspace and assert safe path joining, no-follow behavior, bounded permissions, no execution, and cleanup.

### 7. Active-content non-execution

Prove that uploads cannot trigger:

- shell commands;
- import execution;
- office macros;
- PDF actions;
- notebook cells;
- embedded scripts;
- native plugin callbacks;
- media callbacks;
- external link fetching;
- font or schema loading;
- geocoding or metadata callbacks;
- model or OCR execution without explicit reviewed adapters.

### 8. Scanner and parser adapter behavior

Using fakes or inert reviewed adapters, prove that:

- clean, suspicious, malicious, unsupported, timeout, unavailable, and indeterminate results remain distinct;
- scanner success does not clear rights, sensitivity, accuracy, source role, or release state;
- parser success does not prove truth;
- tool name, version, signature set, configuration, and limits are preserved where required;
- unavailable or indeterminate results route to hold or quarantine;
- adapter errors do not leak payload content or secrets;
- hidden network access fails the test.

### 9. Rights, sensitivity, privacy, and secrets

Prove fail-closed outcomes for synthetic canaries representing:

- unknown license or redistribution rights;
- uploader-supplied rights claims without review;
- living-person identifiers and linked profiles;
- DNA, genomic, health, biometric, and ancestry data;
- protected ecological locations;
- archaeology, burial, sacred, cultural, and sovereignty-governed material;
- private-property and owner-linked joins;
- infrastructure access, vulnerability, or precise facility context;
- proprietary, confidential, privileged, embargoed, or contract-restricted material;
- API keys, tokens, cookies, private keys, passwords, signed URLs, and connection strings;
- hidden sheets, tracked changes, comments, EXIF, thumbnails, embedded files, and revision history;
- joins that create greater sensitivity than individual inputs;
- synthetic or generated material presented as observed reality.

Tests must use fake or inert canaries and assert that sensitive values do not appear in logs, exceptions, snapshots, reports, or generated prompts.

### 10. Geometry and temporal preservation

Prove that:

- source geometry and proposed generalized geometry remain separate;
- CRS, datum, derivation, precision, and uncertainty are preserved when present;
- unresolved coordinate context fails closed;
- exact geometry cannot become public geometry by default;
- uploader timestamps, filesystem timestamps, embedded timestamps, received time, observed/effective time, and review time remain distinguishable;
- stale, superseded, corrected, or incomplete material retains state.

### 11. Candidate outcomes and lifecycle isolation

Prove that package outputs, once implemented, are caller-owned and cannot:

- select a real lifecycle directory;
- write or mutate lifecycle data;
- create a reviewed SourceDescriptor;
- create an EvidenceBundle or proof;
- create a catalog or triplet record;
- create a ReleaseManifest;
- expose a public preview or download;
- treat a checksum, scanner result, parser result, commit, merge, or test pass as promotion.

### 12. Logging, errors, and observability

Prove that:

- stable identifiers and reason codes are preferred over payload fragments;
- original content, secrets, personal data, precise coordinates, private paths, signed URLs, and proprietary material are redacted;
- unsupported and indeterminate conditions remain observable;
- cleanup failures are visible without exposing sensitive paths;
- error output is deterministic where practical;
- audit correlation does not embed credentials or raw content.

[Back to top](#top)

---

## Arbitrary-file security test matrix

| Risk | Required synthetic test | Expected posture |
|---|---|---|
| Filename spoofing | Extension conflicts with detected signature. | Preserve both; hold or quarantine. |
| Polyglot or ambiguous content | Tiny inert file with conflicting signatures. | Unsupported or indeterminate; no parser selection by convenience. |
| Truncated content | Header present, body incomplete. | Bounded error or quarantine. |
| Encrypted content | Inert encrypted-container canary. | Hold or quarantine; no password guessing. |
| Archive traversal | Member path contains parent traversal. | Deny or quarantine; no extraction. |
| Link escape | Archive member is a symbolic/hard-link canary. | Deny or quarantine. |
| Name collision | Case-folding or Unicode-normalization collision. | Deny or quarantine with explicit finding. |
| Expansion attack | Tiny synthetic compression-ratio canary within safe test limits. | Resource-limit outcome; no large expansion. |
| Active content | Harmless macro/script marker. | No execution; deny or quarantine. |
| Secret canary | Fake token pattern. | Restricted finding; value redacted from output. |
| Personal-data canary | Toy identifiers. | Hold or quarantine; no public output. |
| Protected-location canary | Synthetic precise coordinate. | Restricted; generalized only after downstream review. |
| Scanner unavailable | Fake adapter raises unavailable state. | Hold or quarantine; no fabricated clean result. |
| Parser indeterminate | Fake adapter returns ambiguous result. | Hold or quarantine with preserved evidence. |
| Network attempt | Fake parser tries an external request. | Test failure. |
| Lifecycle write | Fake sink points to a forbidden root. | Error and fail closed. |
| Duplicate bytes | Same bytes, distinct event contexts. | Shared content digest; distinct event lineage. |
| Log leakage | Synthetic secret and coordinate included in input. | Neither appears in captured logs or exceptions. |

Security tests must remain small enough for ordinary review and must not reproduce dangerous payloads.

[Back to top](#top)

---

## Finite outcome and failure assertions

Until machine contracts are accepted, these are semantic test requirements rather than claimed enums.

| Condition | Expected semantic result |
|---|---|
| Valid bounded synthetic bytes but no accepted descriptor authority | Restricted intake finding; no source activation. |
| Missing operation authorization | Deny governed admission. |
| Unknown rights | Hold, quarantine, or abstain. |
| Unknown sensitivity | Hold or quarantine. |
| Uploader claims elevated source role | Preserve as unverified; hold for review. |
| Declared/detected type mismatch | Hold or quarantine. |
| Unsupported or malformed content | Hold, quarantine, or bounded error. |
| Resource limit exceeded | Hold, quarantine, or bounded error. |
| Active or executable content | Deny or isolated quarantine. |
| Archive path or expansion hazard | Deny or quarantine. |
| Scanner unavailable or indeterminate | Hold or quarantine. |
| Secret detected | Deny normal flow and use a redacted incident handoff. |
| Sensitive exact location | Deny public output; preserve restricted candidate state. |
| Duplicate content | Preserve distinct event; return duplicate-content finding. |
| Package attempts network on import/default test | Error and fail test. |
| Package attempts lifecycle or release write | Error and fail test. |
| Fixed safe input replay | Same content identity, findings, and reason semantics. |

Tests must assert both the returned result and the forbidden side effects that did not occur.

[Back to top](#top)

---

## Lifecycle, evidence, release, and public-path tests

KFM's lifecycle invariant remains:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

Connector-local tests must prove that package mechanics stop before persistence. Root tests must prove the governed transitions.

### Connector-local negative assertions

Package code must not:

- discover or choose a lifecycle path;
- write to RAW or QUARANTINE directly;
- write receipts, proofs, catalog records, or release objects;
- move, overwrite, delete, or promote files;
- expose uploaded bytes to a public route;
- resolve evidence or approve citations;
- treat an intake receipt as an EvidenceBundle;
- approve redaction, generalization, correction, withdrawal, retention, deletion, or release.

### Root test obligations

Root trust-spine tests should later prove:

- caller-owned orchestration selects exactly one governed RAW or QUARANTINE landing operation;
- append-only source capture and receipt behavior;
- policy and review state before promotion;
- EvidenceRef resolution or abstention;
- catalog/triplet closure before release;
- public denial for unpublished candidates;
- correction, withdrawal, supersession, retention, deletion, and rollback;
- denial logs and review evidence without sensitive leakage.

[Back to top](#top)

---

## Determinism, replay, and observability

A fixed synthetic input and fixed injected context should produce stable:

- content digest;
- byte count;
- normalized safe display metadata;
- supplied-versus-detected media-type finding;
- archive-member inventory ordering;
- resource-limit findings;
- scanner/parser fake results;
- candidate identity inputs;
- semantic outcome;
- reason-code ordering once a vocabulary exists;
- redacted log shape;
- cleanup result.

Tests should control:

- time;
- randomness;
- actor and operation context;
- path roots;
- locale and timezone;
- scanner/parser version and result;
- configuration and resource limits;
- ordering of archive members and findings.

Replay equivalence does not mean two upload events are identical. Event identity and content identity remain separate.

[Back to top](#top)

---

## Collection, runner, and CI boundary

No test runner or collection command is verified for this connector.

A future accepted setup must prove:

- the intended tests are collected;
- zero collected tests fails rather than passes silently;
- unexpected skips, xfails, deselections, import failures, and plugin failures are visible;
- default execution is offline and credential-free;
- package installation mode is explicit;
- test dependencies are pinned or governed;
- fixture paths and temporary storage are isolated;
- security and resource-limit tests cannot exhaust shared CI resources;
- sensitive test output is redacted;
- test reports do not become proofs or release decisions;
- workflows run substantive commands instead of `echo TODO`;
- the exact command, environment, dependency lock, commit, collection count, pass/fail/skip totals, and artifacts are inspectable.

### CI gates that should eventually exist

- package import and packaging gate;
- no-network and no-side-effect gate;
- descriptor-placeholder rejection gate;
- content identity and deterministic replay gate;
- archive and active-content negative gate;
- secret and sensitive-output no-leak gate;
- lifecycle sink-denial gate;
- zero-test and unexpected-skip gate;
- root trust-spine integration gate before activation.

Workflow names, commands, and required-check status remain **PROPOSED / NEEDS VERIFICATION**.

[Back to top](#top)

---

## Validation

### Documentation validation for this revision

- [x] One H1.
- [x] Current path, base commit, prior blob, and introduction commit recorded.
- [x] Named absent tests and local fixture README recorded as bounded probes.
- [x] Adjacent `0.0.0` scaffold and v0.2 package/source-layout boundaries reflected.
- [x] Current test framework, runner, collection, coverage, and results stated as unknown or absent.
- [x] Stale blank-file and placeholder rollback claims removed.
- [x] No external badge or image dependency added.
- [x] No real upload, credential, personal record, coordinate, proprietary payload, malware sample, or endpoint included.
- [x] Connector-local and root trust-spine proof responsibilities separated.
- [x] Fixture split documented without selecting an unverified child path as canonical.
- [x] No test, fixture, schema, policy, lifecycle, evidence, release, or publication authority created.

### Required future connector-local validation

- [ ] accepted test framework, runner, dependencies, and collection command;
- [ ] deterministic offline package installation and import;
- [ ] no-network and no-side-effect enforcement;
- [ ] descriptor-placeholder rejection;
- [ ] upload-event/content-identity separation;
- [ ] bounded resource and content-type behavior;
- [ ] archive traversal, link, collision, recursion, encryption, and expansion defenses;
- [ ] no active-content execution;
- [ ] scanner/parser fake and indeterminate-state coverage;
- [ ] rights, sensitivity, privacy, secret, geometry, and harmful-join negative cases;
- [ ] redacted logs and exceptions;
- [ ] caller-owned candidate outcomes without lifecycle writes;
- [ ] deterministic replay;
- [ ] fixture provenance and safety metadata;
- [ ] zero-test and unexpected-skip failure behavior;
- [ ] substantive CI commands and observed logs.

### Required future root validation

- [ ] accepted source descriptors and activation decisions;
- [ ] policy enforcement and review separation;
- [ ] governed RAW or QUARANTINE persistence;
- [ ] EvidenceBundle closure or abstention;
- [ ] catalog/triplet and release gates;
- [ ] public-path denial for unpublished uploads;
- [ ] correction, withdrawal, supersession, retention, deletion, and rollback;
- [ ] end-to-end auditability without sensitive leakage.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---:|---|---|
| This README at base `ca4b6eac…` | **CONFIRMED** | Current v0.1 content and prior blob. | Documentation does not prove executable tests. |
| Exact named test probes | **CONFIRMED NAMED ABSENCE** | No named conftest, fetch, admit, descriptor, or archive-safety test at the pinned base. | Differently named or later-added files remain unknown. |
| Connector-local fixture README probe | **CONFIRMED NAMED ABSENCE** | No `connectors/local_upload/tests/fixtures/README.md` at the pinned base. | Does not resolve the correct future fixture child path. |
| Parent `pyproject.toml` | **CONFIRMED** | Distribution name and version `0.0.0`. | No test framework, dependency, runner, or install support follows. |
| Package files | **CONFIRMED** | Empty initializer and comment-only fetch/admit scaffold. | No runtime behavior to test. |
| Package and source-layout v0.2 READMEs | **CONFIRMED** | Current arbitrary-file, archive, privacy, secret, package, candidate-output, lifecycle, validation, and rollback boundaries. | They define constraints; they do not implement or test them. |
| Local descriptor | **CONFIRMED** | Four-field placeholder with unresolved role/rights and permissive-looking sensitivity alias. | Not authority, activation, policy, or release evidence. |
| Root `tests/README.md` | **CONFIRMED** | Canonical trust-spine test authority and separation from implementation roots. | Runner and executable depth remain partly unverified. |
| `tests/fixtures/README.md` and `fixtures/README.md` | **CONFIRMED** | Test-local versus cross-cutting fixture split and synthetic/public-safe rules. | Exact local-upload fixture child placement and payload inventory remain unresolved. |
| Local-upload source catalog | **CONFIRMED DRAFT DOC** | Highest-uncertainty intake; candidate role; unknown rights; conservative sensitivity; public denial. | Several object and implementation details remain proposed. |
| Directory Rules | **CONFIRMED DOCTRINE** | Responsibility-root placement, connector boundary, canonical test/fixture roots, and no publication. | Does not select a test framework or exact child fixture path. |
| ADR-0012 | **CONFIRMED DRAFT ADR** | Proposed numbered codification of RAW/QUARANTINE-only connector output. | Draft/proposed; Directory Rules remain governing authority. |
| Source-authority register | **CONFIRMED** | Register is `PROPOSED` with `entries: []`. | No local-upload source authority or activation exists. |
| Singular and plural SourceDescriptor schemas | **CONFIRMED CONFLICT** | Populated singular schema points to empty plural scaffold as canonical. | Not sufficient for stable governed validation. |
| Local-upload policy README probe | **NOT FOUND AT NAMED PATH** | Named lane policy documentation is absent. | Other files or differently named policy paths remain unknown. |
| Connector workflows | **CONFIRMED TODO-ONLY** | Named workflows execute placeholder echo steps. | Green completion cannot prove test coverage or behavior. |

When documentation and implementation evidence conflict, direct file reads and observed tests constrain claims about current behavior. Doctrine still governs required boundaries.

[Back to top](#top)

---

## Review burden

At minimum, future executable tests require review appropriate to their effects:

- package maintainer for tested public and internal behavior;
- connector steward for source-intake boundaries;
- test steward for collection, determinism, assertions, and failure quality;
- fixture steward for placement, provenance, safety, and reuse;
- source-intake steward for upload-event and candidate semantics;
- security reviewer for arbitrary-file handling, active content, scanners, parsers, archives, resource limits, isolation, secrets, and incident handoff;
- rights reviewer;
- privacy/sensitivity reviewer;
- validation steward;
- applicable domain steward after content classification;
- specialist reviewer for living-person, genomic, ecological, archaeological, cultural, sovereignty, infrastructure, or other material concerns;
- docs steward;
- release reviewer for root tests that model public-use decisions.

The uploader must not be the sole reviewer, policy authority, or release authority for material uploads.

An ADR or explicit design decision is required before tests create a new fixture authority, introduce privileged bypasses, require live network or production credentials, execute active content, move lifecycle ownership, or treat connector-local results as release proof.

[Back to top](#top)

---

## Smallest safe implementation sequence

The smallest useful, reversible sequence is **PROPOSED**:

1. **Resolve authority surfaces.** Ratify SourceDescriptor schema authority, candidate role mapping, upload-event/content-identity meaning, finite outcomes, reason codes, and receipt boundaries.
2. **Select test tooling.** Define supported Python, test framework, dependencies, package installation mode, collection command, and zero-test behavior.
3. **Add import/no-side-effect tests.** Prove no network, credential discovery, filesystem mutation, scanner startup, parser startup, or lifecycle access.
4. **Add descriptor rejection tests.** Prove the current four-field placeholder cannot activate or release a source.
5. **Add pure content-identity tests.** Use tiny synthetic bytes to prove deterministic length/digest and distinct upload-event lineage.
6. **Add declared-versus-detected type tests.** Use inert fixtures and no complex parsers.
7. **Add resource-limit tests.** Exercise bounded bytes, nesting, member count, and timeout behavior with tiny inputs.
8. **Add archive negative tests.** Reject traversal, links, collisions, encryption, nesting, and expansion canaries without unsafe extraction.
9. **Add secret/privacy/sensitivity no-leak tests.** Use fake canaries and captured log assertions.
10. **Add scanner/parser adapter fakes.** Cover clean, suspicious, malicious, unsupported, unavailable, timeout, and indeterminate states.
11. **Add candidate-output and lifecycle-denial tests.** Prove no package code selects or writes sinks.
12. **Add fixture metadata and routing.** Ratify test-local versus cross-cutting fixture homes and document provenance.
13. **Wire substantive CI.** Enforce collection, no-network, no-leak, zero-test, skip, and resource boundaries.
14. **Add root trust-spine tests.** Prove governed persistence, policy, evidence, public denial, release, correction, retention, withdrawal, and rollback before activation.

Each step should be independently reviewable and revertible. Do not start with a broad upload-service integration test before pure negative controls and authority surfaces exist.

[Back to top](#top)

---

## Definition of done

This README revision is ready for review when:

- [x] README-only current state is explicit.
- [x] Named absent tests and fixture README are bounded to exact probes.
- [x] Adjacent package maturity is recorded without overclaiming.
- [x] Connector-local and root trust-spine proof are separated.
- [x] Fixture routing is described without inventing a canonical child path.
- [x] No-network, no-execution, resource, archive, secret, privacy, geometry, and lifecycle boundaries are visible.
- [x] Current runner, collection, coverage, and pass rates remain unknown rather than implied.
- [x] Proposed test families are labeled as requirements, not implementation.
- [x] Exact rollback blob is recorded.

An executable test lane is not ready until:

- [ ] package metadata and test dependencies are complete and reviewed;
- [ ] test framework, runner, collection, markers, and reporting are accepted;
- [ ] package behavior exists in a bounded implementation slice;
- [ ] safe synthetic positive and negative fixtures exist in accepted homes;
- [ ] fixture provenance, rights, sensitivity, and expected outcomes are recorded;
- [ ] no-network, no-side-effect, no-execution, and no-secret-leak enforcement passes;
- [ ] descriptor rejection, identity, resource, archive, scanner/parser, privacy, geometry, and lifecycle-denial tests pass;
- [ ] zero-test discovery and unexpected skips fail CI;
- [ ] workflows execute substantive commands and logs are inspectable;
- [ ] root trust-spine tests prove source, policy, lifecycle, evidence, release, correction, withdrawal, retention, deletion, and rollback;
- [ ] public applications cannot reach uploads or unpublished derivatives;
- [ ] owners and CODEOWNERS coverage are assigned;
- [ ] activation is explicitly approved for a bounded operation mode.

[Back to top](#top)

---

## Rollback

Before merge, close the draft PR if this revision is rejected.

After merge, restore the prior blob:

```text
106f3e9f3cdb9c4b83722e0487d5fc4ae27fec6b
```

Use a transparent revert commit or revert PR. Do not reset, force-push, or rewrite shared history. Re-run applicable documentation, link, connector-boundary, test-structure, fixture, security, policy, and rollback checks after the revert.

Rollback is required if this README is used to claim executable coverage, CI success, package maturity, safe arbitrary-file handling, source activation, uploader-controlled authority, rights or sensitivity clearance, secret safety, lifecycle persistence, EvidenceBundle closure, release readiness, public preview safety, or publication without observed test evidence.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Verify complete recursive connector-local test inventory. | **NEEDS VERIFICATION** | Commit-pinned tree or mounted repository inspection. |
| Select test framework, runner, dependencies, and package installation mode. | **NOT ESTABLISHED** | Package metadata, lock/config files, commands, and observed collection. |
| Resolve canonical SourceDescriptor schema and role vocabulary. | **CONFLICTED** | Accepted schema authority, validator, role crosswalk, fixtures, and tests. |
| Define upload-event, content identity, candidate descriptor, finite outcome, reason-code, and receipt contracts. | **PROPOSED** | Contract/schema decisions and review. |
| Ratify connector-local versus root test responsibilities. | **NEEDS VERIFICATION** | Test architecture decision and lane ownership. |
| Select exact test-local and cross-cutting fixture child paths. | **NEEDS VERIFICATION** | Fixture steward decision, Directory Rules check, and migration note if needed. |
| Establish synthetic fixture provenance and safety metadata. | **NEEDS VERIFICATION** | Fixture records, generation notes, expected outcomes, and reviews. |
| Establish lane-specific rights, sensitivity, privacy, secret, access, retention, and release policy. | **NOT FOUND / NEEDS VERIFICATION** | Accepted policy files, tests, and reviewer decisions. |
| Define file-size, time, CPU, memory, archive, page, row, image, recursion, and decompression limits. | **PROPOSED** | Threat model, configuration contract, fixtures, and negative tests. |
| Select scanner and complex-parser isolation model. | **PROPOSED** | Security review, dependency policy, sandbox design, and failure tests. |
| Establish archive traversal, link, collision, encryption, and expansion defenses. | **PROPOSED** | Implementation, inert adversarial fixtures, and observed tests. |
| Establish active-content non-execution proof. | **PROPOSED** | Isolation design, inert canaries, hooks, and observed tests. |
| Establish secret-detection and redacted incident handoff. | **NEEDS VERIFICATION** | Security policy, reason codes, runbook, and no-leak tests. |
| Establish upload-event/content-identity replay proof. | **PROPOSED** | Implementation, fixed inputs, deterministic outputs, and tests. |
| Establish caller-owned candidate and lifecycle sink-denial tests. | **PROPOSED** | Accepted interfaces, fake sinks, side-effect assertions, and tests. |
| Prove public clients cannot reach uploads or unpublished derivatives. | **UNKNOWN** | Dependency graph, API/UI route tests, access policy, runtime proof, and denial logs. |
| Replace connector workflow TODO steps. | **PROPOSED** | Workflow commands, logs, required-check policy, and failure evidence. |
| Prove zero-test and unexpected-skip enforcement. | **UNKNOWN** | Runner configuration and observed failing CI examples. |
| Assign owners and CODEOWNERS coverage. | **UNKNOWN** | Maintainer and governance decision. |
| Prove correction, withdrawal, supersession, retention, deletion, release, and rollback integration. | **UNKNOWN** | Root end-to-end tests, review records, receipts/proofs, and drills. |

---

## Maintainer note

Test the denial paths before the convenience paths. A local-upload suite should make it difficult to accidentally trust filenames, execute content, leak secrets, erase provenance, infer authority, or write lifecycle state. Keep fixtures synthetic, failures explicit, outputs finite, and connector-local claims narrow. Let canonical tests, governed registries, policy, evidence closure, review, release, correction, and rollback carry the rest of the trust burden.

[Back to top](#top)
