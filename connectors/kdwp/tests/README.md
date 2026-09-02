<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kdwp-tests-readme
title: connectors/kdwp/tests/ — KDWP Greenfield Connector Test Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas/KDWP source steward · Fauna steward · Flora steward · Habitat steward · Rights reviewer · Sensitivity/privacy reviewer · Security reviewer · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; greenfield-tests; compatibility-path; source-admission; source-role-conflict; rights-fail-closed; sensitivity-fail-closed; sensitive-location-deny-default; no-network; negative-first; no-activation; no-publication
current_path: connectors/kdwp/tests/README.md
truth_posture: CONFIRMED documentation-only local test lane beside a 0.0.0 package scaffold with empty initializer, comment-only fetch/admit modules, and a nonconforming four-field descriptor; named conventional executable tests were not found in the inspected evidence / CONFLICTED package migration, source-role vocabulary, SourceDescriptor authority, fixture home, test routing, and product decomposition / PROPOSED negative-first compatibility test contract / UNKNOWN differently named tests, discovered test count, coverage, runtime behavior, live source access, current rights, substantive CI enforcement, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  prior_blob: 09c3ba43fd8e8eee81031747482545449f28fb20
related:
  - ../README.md
  - ../pyproject.toml
  - ../src/README.md
  - ../src/kdwp/README.md
  - ../src/kdwp/__init__.py
  - ../src/kdwp/fetch.py
  - ../src/kdwp/admit.py
  - ../src/kdwp/descriptor.yaml
  - ../../README.md
  - ../../kansas/README.md
  - ../../kansas/kdwp/README.md
  - ../../kansas/kdwp_flora/README.md
  - ../../kansas/kdwp_ert/README.md
  - ../../../CONTRIBUTING.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../../docs/sources/catalog/kansas/kdwp.md
  - ../../../docs/standards/SENSITIVITY_RUBRIC.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../data/registry/sources/README.md
  - ../../../data/registry/sources/habitat/kdwp.yaml
  - ../../../data/registry/fauna/sources/kdwp_species.yaml
  - ../../../control_plane/source_authority_register.yaml
  - ../../../fixtures/README.md
  - ../../../tests/README.md
  - ../../../tests/fixtures/README.md
  - ../../../policy/rights/README.md
  - ../../../policy/sensitivity/README.md
  - ../../../release/
  - ../../../.github/workflows/connector-gate.yml
  - ../../../.github/workflows/source-descriptor-validate.yml
tags: [kfm, connectors, kdwp, tests, python, greenfield, compatibility, kansas, wildlife, sinc, listed-species, fauna, flora, habitat, source-admission, source-role, rights, sensitivity, privacy, fixtures, no-network, negative-first, raw, quarantine, no-publication]
notes:
  - "The inspected local test lane contains this README; conventional executable test files named test_fetch.py, test_admit.py, test_descriptor.py, and conftest.py were not established by the adjacent repository evidence."
  - "The package under test is version 0.0.0 with an empty __init__.py, comment-only fetch.py and admit.py files, and a nonconforming descriptor.yaml placeholder."
  - "The Kansas-family coordination lane connectors/kansas/kdwp/ exists, but package migration, final test routing, fixture placement, source IDs, and product decomposition remain unresolved."
  - "KDWP authority, listed-status/regulatory context, observations, range products, habitat/stewardship products, ERT outputs, and generated carriers must not collapse into one test fixture or source role."
  - "The connector-gate and source-descriptor-validate workflows are TODO-only scaffolds; a green workflow run cannot establish package imports, test discovery, descriptor conformance, rights review, activation, or connector behavior."
  - "Only this Markdown file is changed. No code, package metadata, descriptor, registry entry, fixture, test, workflow, policy, schema, source payload, credential, activation decision, lifecycle artifact, release object, path move, or public artifact is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KDWP Greenfield Connector Test Boundary

> Repository-grounded test contract for the documentation-only lane at `connectors/kdwp/tests/`. The adjacent package is a non-operational `0.0.0` scaffold. This README defines what future tests must prove; it does not claim that executable tests, coverage, source access, or substantive CI enforcement already exist.

**Document lifecycle:** `draft v0.2`  
**Current maturity:** `CONFIRMED` README-only local test lane beside a greenfield package scaffold  
**Owner:** `OWNER_TBD`  
**Authority:** test-boundary documentation only; tests prove behavior but do not own source identity, contracts, schemas, policy, lifecycle state, evidence, release, or publication  
**Default posture:** synthetic fixtures · no network · no credentials · no lifecycle writes · no public output

> [!IMPORTANT]
> The package currently supplies no supported fetch or admission behavior to test. An empty initializer, comment-only modules, a placeholder descriptor, this README, a pull request, or a green workflow does not establish test discovery, coverage, source authority, activation, or readiness.

> [!CAUTION]
> KDWP material can include listed-status, SINC rank, precise ecological locations, monitoring observations, range products, habitat or stewardship context, review-tool outputs, and cross-source joins. Test fixtures must not become an accidental public disclosure channel. Unknown rights, sensitivity, geometry, role, product identity, or review state fails closed.

**Quick links:** [Purpose](#purpose) · [Current test lane](#current-test-lane) · [Repository fit](#repository-fit) · [Test authority](#test-authority-boundary) · [Package under test](#package-under-test) · [Product boundaries](#kdwp-product-and-source-role-boundaries) · [Fixture safety](#fixture-safety) · [Required families](#required-test-families) · [No-network contract](#no-network-and-side-effect-contract) · [Descriptor tests](#descriptor-and-activation-tests) · [Sensitivity tests](#rights-sensitivity-and-geometry-tests) · [Lifecycle tests](#lifecycle-and-output-boundary-tests) · [Migration tests](#migration-and-routing-tests) · [Validation matrix](#validation-matrix) · [CI limits](#ci-and-observability) · [Evidence](#evidence-basis) · [Review](#review-burden) · [Definition of done](#definition-of-done) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

This README turns the local KDWP test directory into an explicit, fail-closed verification boundary.

It exists to:

- distinguish documented expectations from executable proof;
- bind future tests to the actual package scaffold and unresolved migration posture;
- require source-role, product, rights, sensitivity, identity, time, geometry, and lifecycle checks before source access is considered;
- keep default tests deterministic, synthetic, no-network, credential-free, and side-effect-free;
- prevent test fixtures, snapshots, logs, failure output, or generated artifacts from exposing sensitive ecological information;
- define finite negative outcomes for incomplete or unsafe candidates;
- make zero-test discovery, skipped negative cases, TODO-only workflows, and permissive placeholders visible failures rather than false confidence.

This lane does not activate a source, approve terms, establish a canonical connector path, create a `SourceDescriptor`, decide public precision, close an `EvidenceBundle`, authorize release, or prove that a KDWP claim is true.

[Back to top](#top)

---

## Current test lane

The directly evidenced local test surface is:

```text
connectors/kdwp/tests/
└── README.md                         # this test-boundary document
```

Adjacent package evidence records exact `Not Found` probes for these conventional local files:

```text
connectors/kdwp/tests/conftest.py
connectors/kdwp/tests/test_fetch.py
connectors/kdwp/tests/test_admit.py
connectors/kdwp/tests/test_descriptor.py
```

Those statements are bounded to the inspected repository evidence. Differently named, generated, unindexed, or concurrently added test files remain `UNKNOWN` until directly read at the commit under review.

### Current maturity

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| This README | Documentation contract exists. | Test intent is documented; no executable proof follows from documentation alone. |
| Local executable tests | Not established at the named conventional probes. | Discovered count, pass/fail state, coverage, and negative-case enforcement are `UNKNOWN`. |
| Package | `kfm-connector-kdwp` version `0.0.0`. | Greenfield placeholder; build and import support are not established. |
| Package modules | Empty `__init__.py`; comment-only `fetch.py` and `admit.py`. | No supported network, parse, admission, quarantine, or handoff behavior exists. |
| Local descriptor | Four-field placeholder with unresolved role and rights plus `sensitivity_floor: public`. | Invalid as activation, sensitivity clearance, or release evidence. |
| Connector workflows | TODO echo steps in the inspected workflow definitions. | Green completion proves workflow execution only, not KDWP behavior or test coverage. |

[Back to top](#top)

---

## Repository fit

Directory Rules assign one primary responsibility to each root:

| Responsibility | Owning surface | Test-lane relationship |
|---|---|---|
| Source-specific fetch, probe, parsing, packaging, and admission mechanics | `connectors/` | Local unit tests may verify connector mechanics without becoming source authority. |
| Object meaning | `contracts/` | Tests consume accepted meaning; they do not redefine it. |
| Machine shape | `schemas/` | Tests validate against accepted schemas; snapshots do not become schema authority. |
| Allow, deny, restrict, redact, abstain, or hold decisions | `policy/` | Tests exercise policy decisions with safe fixtures; they do not mint policy. |
| Source identity, role, rights, sensitivity, cadence, and activation state | accepted registry/control-plane surfaces | Tests resolve or mock reviewed records; local fixtures cannot activate a source. |
| Canonical enforceability proof | root `tests/` and accepted validator lanes | Connector-local tests provide narrow package proof; final routing remains `CONFLICTED / NEEDS VERIFICATION`. |
| Golden and negative samples | accepted `fixtures/` lanes | Local test data must follow the repository fixture decision; do not create a parallel fixture authority. |
| Lifecycle material | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` | Default tests must not write to live lifecycle roots. |
| Evidence and process memory | proof and receipt lanes | Test reports are not EvidenceBundles, source receipts, or release proofs. |
| Promotion, release, correction, and rollback | `release/` | A passing connector test cannot publish anything. |

The local test directory remains useful only when it proves narrow implementation behavior and routes broader enforceability to the accepted root-level test and validator surfaces.

[Back to top](#top)

---

## Test authority boundary

Tests may prove that code behaves according to accepted inputs and constraints. They must not be treated as authority for the inputs or constraints themselves.

A local KDWP test may prove:

- imports are side-effect-free;
- a parser preserves source-native identity and metadata;
- an adapter rejects an invalid descriptor;
- a candidate is held or quarantined when rights or sensitivity is unresolved;
- a role mismatch is rejected;
- a fixture cannot produce a public artifact;
- no network or credential access occurs in the default suite;
- no write escapes a caller-owned temporary directory;
- deterministic inputs produce deterministic candidate output and reason codes.

A local KDWP test cannot prove:

- current KDWPT source terms, endpoint availability, division ownership, or legal effect;
- that a catalog page or local YAML is a conforming `SourceDescriptor`;
- that `connectors/kdwp/` or `connectors/kansas/kdwp/` is the final package home;
- that one package should represent every KDWP product;
- that an exact ecological location is public-safe;
- that a record is authoritative outside its declared product and source role;
- that a candidate has completed evidence, catalog, policy, review, or release closure;
- that a workflow, commit, pull request, merge, map, export, or generated explanation is publication.

[Back to top](#top)

---

## Package under test

The bounded package snapshot documented by the adjacent package README is:

```text
connectors/kdwp/
├── pyproject.toml                  # project kfm-connector-kdwp, version 0.0.0
├── src/
│   └── kdwp/
│       ├── __init__.py             # empty
│       ├── fetch.py                # comment-only
│       ├── admit.py                # comment-only
│       └── descriptor.yaml         # nonconforming placeholder
└── tests/
    └── README.md                   # this file
```

The first executable test increment must not pretend to test unimplemented transport or admission behavior. It should instead establish the test harness and prove one synthetic negative boundary at a time.

### Smallest safe first increment

1. Add one compact invented KDWP-shaped record with no real taxon, person, property, coordinate, credential, endpoint, or source payload.
2. Add one accepted test configuration that blocks network and credential access.
3. Add one negative test that rejects the local placeholder descriptor or an equivalent invented invalid descriptor.
4. Assert a deterministic `HOLD`, `QUARANTINE`, `DENY`, `ABSTAIN`, or `ERROR` result with machine-readable reasons.
5. Assert no lifecycle, registry, receipt, proof, catalog, release, map, API, or public-file side effect.
6. Make zero discovery and unexpected skips fail CI.

[Back to top](#top)

---

## KDWP product and source-role boundaries

One agency umbrella does not imply one claim role or one safe fixture.

| Product or record family | Permitted test focus | Required anti-collapse assertion |
|---|---|---|
| Listed-status or legal-status records | Preserve issuing authority, status vocabulary, effective time, jurisdiction, citation, and review requirements. | Do not treat legal or regulatory status as an occurrence, range, habitat observation, or field measurement. |
| SINC rank or sensitivity context | Preserve rank vocabulary, scope, effective time, source role, review state, and redaction requirements. | Never interpret a permissive package default as public-location clearance. |
| Monitoring, survey, mortality, disease, or agency observations | Preserve observation identity, method, time, geometry provenance, uncertainty, qualifiers, and source URI. | Do not promote observation evidence into legal status, modeled range, or habitat truth. |
| Range or distribution products | Preserve model or compilation identity, vintage, scale, uncertainty, method, and fitness limits. | A range polygon is not an exact occurrence and is not proof of presence at a selected point. |
| Habitat, stewardship, or conservation-planning products | Preserve product type, model/administrative role, scale, vintage, lineage, and limitations. | Modeled habitat, stewardship context, and regulatory boundaries are distinct. |
| Ecological Review Tool outputs | Preserve input scope, review date, policy context, reviewer state, disclaimer, and non-authoritative output limits. | An ERT result is not a permit, legal clearance, field survey, absence finding, or release approval. |
| Portal, index, or carrier records | Preserve upstream record identity, source links, product family, and retrieval metadata. | A carrier or index does not inherit every upstream authority role. |
| Generated normalizations, joins, maps, summaries, or AI text | Preserve input references, transform identity, uncertainty, policy labels, and reality boundary. | Generated carriers cannot mint source authority or reveal withheld information. |

A mixed fixture must either be split into product/role-specific fixtures or be explicitly constructed to prove that mixed-role admission fails.

[Back to top](#top)

---

## Fixture safety

### Allowed fixture classes

| Fixture class | Use | Required controls |
|---|---|---|
| Fully synthetic shape fixture | Parser, schema, identity, failure, and boundary tests. | Invented names and IDs; impossible or clearly fictional geometry; no live endpoint or copied payload. |
| Minimal public and rights-reviewed sample | Compatibility test requiring source-native syntax. | Source-steward and rights review; explicit fixture provenance; minimized fields; sensitivity review. |
| Redacted or generalized sample | Sensitive-field and public-transform tests. | Transform documented; original not committed; precision and withheld fields proven absent. |
| Invalid fixture | Fail-closed tests. | Clearly marked invalid; contains no real sensitive material; deterministic reason code expected. |
| Golden normalized candidate | Determinism and regression tests. | Derived only from an approved fixture; stable serialization; no claim or release authority. |

### Forbidden fixture content

Do not commit:

- exact or realistically precise locations for protected, listed, sensitive, denning, nesting, roosting, breeding, hibernating, translocated, captive, or disease-affected taxa;
- private-land, owner, contact, residence, access, collector, submitter, or living-person identifiers;
- credentials, tokens, cookies, session state, API keys, signed URLs, or private endpoints;
- bulk source exports, production snapshots, unpublished reviews, internal notes, or unreviewed media;
- unclear-rights text, images, attachments, GIS packages, or copied upstream payloads;
- fixture geometry that can be joined back to a sensitive feature through obvious attributes;
- logs or snapshots containing request headers, secrets, exact coordinates, or unredacted source responses.

### Join-induced sensitivity

Tests must evaluate the output of joins, not just the sensitivity of each input. A public administrative boundary joined to a generalized occurrence, private parcel, access route, residence, landowner, review result, or infrastructure layer may create a more revealing product. The joined candidate inherits the most restrictive applicable posture until policy and review say otherwise.

[Back to top](#top)

---

## Required test families

All families below are `PROPOSED` until executable files, discovery output, logs, and CI evidence exist.

| Test family | Minimum proof | Required negative case |
|---|---|---|
| Import and smoke | Package imports without network, credentials, file writes, environment mutation, logging secrets, or registration side effects. | Import fails if it contacts a source, reads a credential, writes outside a temp directory, or changes global state. |
| Descriptor shape | Accepted descriptor fixture validates against the accepted schema and registry posture. | Missing, placeholder, legacy-only, wrong-role, unknown-rights, or permissive-sensitivity descriptor fails closed. |
| Activation gate | Explicit reviewed activation state is required before an opt-in source client can run. | Missing, draft, denied, quarantined, retired, fixture-only, or unreviewed activation cannot contact a source. |
| Product dispatch | Each record is routed to an explicit KDWP product family. | Unknown or mixed product family is held; no umbrella fallback silently assigns meaning. |
| Source-role separation | Role is explicit and compatible with the claim/candidate type. | Listed-status context cannot become observation; observation cannot become legal status; carrier cannot become original authority. |
| Identity preservation | Stable upstream IDs, product ID, record version, source URI, and amendment/supersession references are preserved. | Missing or colliding identity is held; later retrieval does not overwrite history silently. |
| Temporal preservation | Source, observed, effective/valid, retrieval, review, release, and correction times stay distinct where material. | Missing required time or substituted retrieval time fails or produces an explicit bounded hold. |
| Taxonomy and status | Taxon concepts, names, rank/status vocabulary, and crosswalk versions are preserved without silent canonicalization. | Unresolved taxon/status mapping cannot become a public claim. |
| Geometry and uncertainty | Native geometry method, CRS/datum, precision, derivation, uncertainty, and generalization state are preserved. | Missing or false precision, invalid geometry, or unsafe exact location fails closed. |
| Rights and terms | Rights state, attribution, redistribution, disclaimer, permitted use, and review references are explicit. | Unknown, noassertion, denied, expired, or contradictory rights blocks activation and public output. |
| Sensitivity and privacy | Product-level and record-level sensitivity, withheld fields, geometry policy, and reviewer state are applied. | Public default, missing review, unsafe join, or leaked precise field fails. |
| Parsing and normalization | Source-native values and qualifiers are retained; normalized candidate is deterministic. | Unknown field/value does not disappear silently or become a guessed canonical value. |
| Failure outcomes | Unsafe or incomplete input returns a finite result and stable reason codes. | No implicit success, empty-success object, warning-only promotion, or permissive fallback. |
| Handoff boundary | Candidate remains caller-owned and can be routed only after accepted orchestration. | Package/test code cannot write directly to RAW, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, registry, proof, receipt, or release roots. |
| No-publication | No map, tile, API response, catalog record, evidence claim, release manifest, or public export is created. | Any publication-like side effect fails the test. |
| Migration and import compatibility | Accepted losing-path behavior and import aliases are explicit and time-bounded. | Current top-level path cannot declare itself canonical or create a second evolving implementation. |
| Determinism | Same fixture, descriptor, config, and clock inputs yield identical normalized output and reason codes. | Hidden current time, random IDs, network state, machine path, or unordered serialization causes failure. |

[Back to top](#top)

---

## No-network and side-effect contract

Default local and CI tests must run with network unavailable or actively denied.

### Required assertions

- Importing the package performs no HTTP, DNS, socket, subprocess, browser, credential, registry, or cloud-client action.
- Tests do not read the user's home directory, keychain, browser profile, shell history, cloud configuration, or secret manager.
- Tests use caller-provided temporary directories and do not write to repository lifecycle or authority roots.
- Environment variables are explicit test inputs; no production credential variable is required.
- Time, UUID generation, randomness, and filesystem paths are controlled where they affect output.
- Logs and failure messages are safe to preserve in CI.
- Any future live-source probe is opt-in, separately reviewed, rate-limited, terms-aware, credential-safe, and excluded from required default CI.

### Network-denial test

At least one test must fail deliberately when code attempts a network operation. A test suite that simply does not happen to use the network is weaker than a suite that proves network access is blocked.

[Back to top](#top)

---

## Descriptor and activation tests

The connector-local `descriptor.yaml` is a migration placeholder, not a valid activation basis.

Future tests must prove that:

1. the accepted descriptor resolves from the accepted registry/control-plane path;
2. `object_type`, schema version, stable source ID, descriptor version, product scope, source type, source role, authority, publisher/steward, rights, sensitivity, cadence, access, citation, source head, admissibility limits, review, activation, lifecycle, and public-release posture satisfy the accepted schema and policy;
3. legacy aliases are rejected or migrated intentionally rather than treated as canonical new fields;
4. one umbrella descriptor cannot silently authorize every KDWP product and role;
5. unknown rights, unresolved sensitivity, missing source role, missing product scope, missing review, or missing activation fails closed;
6. fixture-only descriptors can never authorize real source access or public claims;
7. connector code cannot upgrade descriptor authority, role, rights, sensitivity, review state, activation state, or release state.

### Required placeholder rejection

A negative fixture equivalent to this local placeholder must fail:

```yaml
name: kdwp
role: TBD
rights: TBD
sensitivity_floor: public
```

The expected failure should identify unresolved stable source identity, product scope, source role, rights, sensitivity/review posture, activation state, and schema conformance without logging sensitive values.

[Back to top](#top)

---

## Rights, sensitivity, and geometry tests

### Rights

Tests must distinguish at least:

- verified open use within stated limits;
- verified restricted use;
- permission required;
- unknown or no assertion;
- denied or expired use.

Unknown or denied rights must force public release false and prevent live activation unless a separately governed restricted workflow explicitly permits access.

### Sensitivity

Tests must cover:

- public-safe metadata with no sensitive payload;
- restricted or review-required records;
- sensitive location or withheld geometry;
- living-person or private-property joins;
- steward-controlled or controlled records;
- unknown-review-required state;
- a generated public derivative whose transform and redaction receipt are absent.

The last case must fail. A candidate is not public-safe merely because sensitive fields were omitted informally.

### Geometry

Tests must preserve and validate:

- native geometry type;
- source CRS and datum;
- coordinate method or derivation;
- precision and uncertainty;
- observed versus inferred/generalized geometry;
- withheld or null geometry reason;
- transform/generalization identity;
- output precision appropriate to policy and product role.

Tests must reject false precision, undocumented centroiding, coordinate swaps, invalid ranges, missing datum where material, and joins that reconstruct withheld locations.

[Back to top](#top)

---

## Lifecycle and output boundary tests

The package may eventually return caller-owned candidates. It must not own lifecycle persistence or promotion.

| Attempted behavior | Required result |
|---|---|
| Return a validated in-memory candidate with explicit hold/quarantine reasons | Allowed after implementation and accepted contracts exist. |
| Write directly to `data/raw/` | Fail unless an accepted external orchestrator owns the write and the package only returns the candidate. |
| Write directly to `data/quarantine/` | Same boundary: orchestration owns persistence; package returns disposition and reasons. |
| Write to `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/`, proofs, receipts, registry, rollback, or `release/` | Fail. |
| Create a public map, tile, API payload, report, summary, citation, or AI answer | Fail. |
| Treat a commit, PR, merge, green workflow, copied file, or directory move as promotion | Fail. |
| Continue after missing descriptor, rights, sensitivity, role, product, identity, geometry, or review state | Hold, quarantine, deny, abstain, or error with deterministic reasons. |

Temporary files used within a test must stay under the test-owned temporary directory and be removed or retained only as explicit safe CI artifacts.

[Back to top](#top)

---

## Migration and routing tests

The repository contains a top-level KDWP package scaffold and a Kansas-family KDWP coordination lane. Final package placement, product topology, fixture home, and test routing remain unresolved.

Future migration tests should prove:

- one accepted implementation home and one documented compatibility policy;
- no duplicate live client, descriptor, credential, activation, fixture corpus, test suite, source-head state, or receipt lineage across old and new paths;
- import aliases are explicit, deprecation-warned, versioned, and removed through a documented schedule;
- source IDs and product IDs do not change silently with a path move;
- registry, policy, test, fixture, workflow, documentation, and consumer references migrate together;
- losing-path behavior is read-only, redirect-only, compatibility-only, or removed according to an accepted decision;
- rollback restores a coherent prior state without force-pushing or rewriting shared history.

Directory presence or the wording “canonical” in an older README is not sufficient migration evidence.

[Back to top](#top)

---

## Failure contract

Unsafe or incomplete input must produce one finite, inspectable outcome.

| Outcome | Test meaning |
|---|---|
| `HOLD` | Candidate is structurally parseable but lacks required governance or review state. |
| `QUARANTINE` | Candidate may be useful but cannot safely advance; reasons are recorded. |
| `DENY` | Requested access, transform, exposure, or use is forbidden. |
| `ABSTAIN` | Evidence or mapping is insufficient to make the requested interpretation. |
| `ERROR` | Deterministic operational or contract failure; no permissive fallback. |

The accepted project vocabulary remains `NEEDS VERIFICATION`. Tests must use the final contract terms rather than inventing incompatible local enums. Until resolved, documentation may describe the semantics above while implementation remains blocked.

Every failure result should carry:

- stable reason code;
- safe human-readable explanation;
- affected field or gate without leaking restricted content;
- source/product/descriptor reference when safe;
- retryability or remediation class;
- no partial public output;
- no side effect outside caller-owned temporary state.

[Back to top](#top)

---

## Validation matrix

| Condition | Required result |
|---|---|
| Zero executable tests discovered after the suite is implemented | Fail CI. |
| Required negative test skipped or xfailed without accepted issue/expiry | Fail or require explicit governed waiver. |
| Package import attempts network, credentials, subprocess, browser, or write | Fail. |
| Local placeholder descriptor used as activation basis | Fail. |
| SourceDescriptor missing or unresolved | Hold/quarantine/deny; no source access. |
| Activation missing, draft, denied, retired, quarantined, fixture-only, or unreviewed | No source access. |
| Unknown or denied rights | No public output; fail closed. |
| Unknown sensitivity or missing review | No public output; fail closed. |
| Missing product family or source role | Hold/quarantine; no umbrella fallback. |
| Listed-status context treated as observation | Fail. |
| Observation treated as legal/listed status | Fail. |
| Range or modeled habitat treated as exact occurrence | Fail. |
| ERT output treated as permit, clearance, field survey, or absence proof | Fail. |
| Taxon/status mapping unresolved | Hold/abstain; preserve source value. |
| Missing upstream identity, amendment, or supersession relationship | Hold or deterministic error. |
| Retrieval time substituted for effective/observed time | Fail. |
| Invalid, false-precision, or reconstructable sensitive geometry | Fail or quarantine. |
| Sensitive join becomes less restrictive than an input | Fail. |
| Fixture includes secret, real sensitive location, private identifier, or unclear-rights payload | Fail fixture review and CI where detectable. |
| Output writes to repository lifecycle/authority roots | Fail. |
| Test or package creates map, API, evidence, catalog, release, or public artifact | Fail. |
| Current path declares itself canonical without accepted decision | Fail migration test. |
| Same controlled inputs produce non-deterministic result | Fail. |
| Workflow only echoes TODO and no substantive test command runs | Do not count as implementation proof; fail readiness review. |

[Back to top](#top)

---

## CI and observability

### Current limitation

The inspected `connector-gate` and `source-descriptor-validate` workflows contain TODO echo steps. Their successful execution cannot prove:

- package installation or import;
- test collection or discovered count;
- parser or normalizer behavior;
- descriptor conformance;
- network denial;
- rights or sensitivity enforcement;
- geometry or temporal validation;
- lifecycle side-effect prevention;
- package migration safety;
- source activation or release readiness.

### Future minimum CI evidence

A substantive test job should report:

- exact environment and dependency lock identity;
- exact test command;
- collected, passed, failed, skipped, and xfailed counts;
- proof that zero discovery fails;
- proof that required negative cases ran;
- network-denial configuration;
- safe fixture inventory and hashes;
- coverage only after meaningful code exists;
- deterministic failure reason codes;
- no secret or sensitive-data leakage in logs and artifacts;
- commit and package/config identity.

Coverage percentage alone is not readiness. A small negative-first suite with strong boundary assertions is more valuable than broad shallow execution over placeholder code.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| `connectors/kdwp/tests/README.md` prior blob | **CONFIRMED** | Existing v0.1 test documentation and rollback target. | Executable tests or passing coverage. |
| `connectors/kdwp/pyproject.toml` | **CONFIRMED** | Project name and `0.0.0` version. | Build system, installability, dependencies, entry points, or runtime. |
| `connectors/kdwp/src/kdwp/` package files | **CONFIRMED** | Empty initializer, comment-only fetch/admit modules, and placeholder descriptor. | Supported connector behavior. |
| `connectors/kdwp/src/kdwp/README.md` | **CONFIRMED documentation** | Bounded package inventory, exact conventional-test probes, descriptor conflict, product boundaries, and migration posture. | Runtime, activation, source terms, or release. |
| `connectors/kdwp/src/README.md` | **CONFIRMED existing documentation; revision may be reviewed separately** | Source-layout boundary. | Executable package or tests. |
| Kansas-family KDWP READMEs | **CONFIRMED documentation** | Family coordination and distinct Flora/ERT lanes. | Final package migration, activation, or product authority. |
| KDWP source catalog | **CONFIRMED draft documentation** | Product classes, source-role distinctions, and sensitivity pressure. | Machine descriptor, source access approval, or current terms. |
| SourceDescriptor contracts/schemas | **CONFIRMED repository surfaces; authority remains conflicted** | Candidate field and fail-closed requirements. | A conforming KDWP descriptor or activation decision. |
| KDWP registry files and source-authority register | **CONFIRMED placeholders/empty authority state in adjacent evidence** | Current lack of established machine authority. | Source admission or activation. |
| Rights and sensitivity policy READMEs | **CONFIRMED greenfield surfaces** | Responsibility boundaries. | Current KDWP terms or record-level exposure decisions. |
| Connector and descriptor workflows | **CONFIRMED TODO-only definitions** | Workflow scaffolding. | Substantive test or enforcement coverage. |
| Directory Rules | **CONFIRMED doctrine** | `tests/` proves enforceability; `fixtures/` holds samples; responsibility roots must not collapse. | Final connector-local versus root-test routing without repo/ADR resolution. |

No live KDWP source, endpoint, credential, payload, current terms page, runtime log, deployed service, release manifest, or public client was inspected for this documentation change.

[Back to top](#top)

---

## Review burden

Before executable tests or fixtures are accepted, review should include:

| Reviewer role | Required review focus |
|---|---|
| Connector/package maintainer | Package API, import behavior, side effects, determinism, and migration compatibility. |
| Kansas/KDWP source steward | Product decomposition, source identity, current access method, source-native fields, cadence, and amendments. |
| Fauna/Flora/Habitat stewards | Domain ownership, taxonomy/status semantics, range/occurrence/habitat distinctions, and cross-lane routing. |
| Rights reviewer | Terms, attribution, redistribution, fixture reuse, screenshots/media, and stored source material. |
| Sensitivity/privacy reviewer | Exact locations, protected taxa, private-property/living-person joins, public precision, logs, and fixture safety. |
| Security reviewer | Network denial, credentials, request logging, dependency risk, archive/media parsing, and CI artifacts. |
| Contract/schema reviewer | Accepted SourceDescriptor and candidate/failure shapes; legacy migration handling. |
| Test/validation steward | Discovery, negative cases, reason codes, no-side-effect assertions, fixture receipts, and substantive CI. |
| Migration/architecture reviewer | Final package/test/fixture routing, aliases, deprecation, backlinks, history, and rollback. |

Named individual reviewers remain `UNKNOWN`; do not invent accounts or request teams without repository evidence or user instruction.

[Back to top](#top)

---

## Definition of done

### Documentation revision

- [x] Current README-only test-lane maturity is explicit.
- [x] Adjacent `0.0.0` scaffold and placeholder descriptor are recorded.
- [x] Named conventional test absence is bounded rather than overgeneralized.
- [x] Directory Rules responsibility boundaries are preserved.
- [x] KDWP product and source-role anti-collapse rules are explicit.
- [x] Rights, sensitivity, privacy, geometry, time, fixture, lifecycle, and migration controls fail closed.
- [x] CI limitations and TODO-only workflow posture are explicit.
- [x] Rollback uses an exact prior blob and transparent history.

### Executable test readiness remains open

- [ ] Accepted package path, import name, product topology, source IDs, test routing, and fixture home.
- [ ] Accepted SourceDescriptor contract/schema/registry authority and KDWP product descriptors.
- [ ] Current source access, terms, attribution, redistribution, disclaimer, cadence, limits, and source-head behavior.
- [ ] Safe reviewed fixtures with provenance and sensitivity controls.
- [ ] Import/network/descriptor/role/rights/sensitivity/identity/time/geometry/lifecycle/migration negative tests.
- [ ] Exact test command, non-zero discovered count, logs, substantive CI, owners, and review records.
- [ ] Demonstrated failure when a required boundary is removed or made permissive.

Documentation readiness does not imply executable test coverage, connector readiness, source admission, activation, rights clearance, sensitivity clearance, evidence closure, release approval, or publication.

[Back to top](#top)

---

## Rollback

Rollback is required if this README is used to claim executable coverage, package readiness, source authority, live access, activation, rights or sensitivity clearance, safe exact-location exposure, canonical-path resolution, lifecycle authority, evidence closure, or release.

Before merge, close the draft pull request and abandon the scoped branch if the revision is rejected.

After merge, restore prior README blob:

```text
09c3ba43fd8e8eee81031747482545449f28fb20
```

through a transparent revert commit or revert pull request, then rerun applicable documentation, link, connector-boundary, policy, and test-discovery checks. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Complete recursive inventory of `connectors/kdwp/tests/` | **UNKNOWN** | Non-truncated tree receipt or mounted checkout at the reviewed commit. |
| Exact conventional and differently named test-file presence | **NOT ESTABLISHED / UNKNOWN** | Direct file reads and test collection output. |
| Final package and test home | **CONFLICTED** | Accepted ADR/migration, consumer inventory, import plan, backlinks, and rollback. |
| Root `tests/` versus connector-local test routing | **CONFLICTED / NEEDS VERIFICATION** | Directory Rules application, repository convention, and accepted test architecture. |
| Fixture home and fixture receipt model | **CONFLICTED / NEEDS VERIFICATION** | Accepted fixture registry, sensitivity/rights review, and test configuration. |
| Product-family and source-role vocabulary | **NEEDS VERIFICATION** | Current source inventory plus contract/schema/domain/source-steward decision. |
| SourceDescriptor schema and validator authority | **CONFLICTED / NEEDS VERIFICATION** | One accepted schema, validator, fixture set, CI command, and migration. |
| KDWP descriptor records and authority entries | **PLACEHOLDER / NOT ESTABLISHED** | Conforming product-level records and reviewed control-plane entries. |
| Activation decision and source-head evidence | **NOT ESTABLISHED** | Reviewed activation record and observed approved source-head receipt. |
| Current source surfaces, endpoint/access modality, cadence, limits, and corrections | **NEEDS VERIFICATION** | Current authoritative KDWP documentation and source-steward review. |
| Rights, attribution, redistribution, disclaimers, and fixture reuse | **NEEDS VERIFICATION** | Current terms and signed rights review. |
| Sensitivity, public geometry, redaction/generalization, and join policy | **NEEDS VERIFICATION** | Policy, transforms, fixtures, receipts, tests, and reviewer decisions. |
| Taxonomy, status, range, occurrence, habitat, and ERT semantics | **NEEDS VERIFICATION** | Product contracts, crosswalks, fixtures, and domain-steward review. |
| Executable package behavior | **NOT IMPLEMENTED IN NAMED MODULES** | Code, package configuration, imports, tests, and logs. |
| Substantive CI and zero-discovery enforcement | **NOT ESTABLISHED** | Workflow command, collected test count, logs, and a demonstrated negative failure. |
| Owners and review routing | **UNKNOWN** | Accepted CODEOWNERS or ownership register. |
| Repository-wide promotion prerequisites | **NEEDS VERIFICATION** | Trusted workflow results and required doctrine/release artifacts. |

[Back to top](#top)

---

## Maintainer note

Keep this lane negative-first and evidence-bounded.

The safest progression is:

1. settle package, test, fixture, descriptor, product, and source-role routing;
2. add one invented invalid descriptor fixture;
3. prove import and network denial;
4. prove one deterministic fail-closed disposition with no side effects;
5. add product/role, rights, sensitivity, identity, time, geometry, and migration negatives;
6. only then consider a reviewed opt-in source probe.

A larger suite is not better if it masks zero discovery, uses unsafe fixtures, accepts permissive placeholders, or tests generated output as though it were source truth.

[Back to top](#top)
