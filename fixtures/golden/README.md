# `fixtures/golden/` — Cross-Cutting Golden Expected-Output Fixture Boundary

> Repository-grounded parent contract for stable, synthetic, cross-cutting expected outputs. This lane supports deterministic regression comparisons when no single domain or narrower fixture family owns the expected result; it does not own executable tests, runtime truth, domain truth, evidence, policy, review, release approval, or published artifacts.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-golden-readme
title: fixtures/golden/README.md — Cross-Cutting Golden Expected-Output Fixture Boundary
type: readme; directory-readme; golden-fixture-parent; expected-output-index; non-authoritative
version: v0.2
status: draft; repository-grounded; top-level-golden-parent; payload-inventory-unverified; consumer-wiring-unverified; ci-unestablished; non-authoritative
owners: OWNER_TBD — Fixture steward · Test/QA steward · Runtime steward · Domain stewards · Contract/schema steward · Source-role steward · Evidence steward · Policy steward · Rights/sensitivity reviewer · Release steward · Correction/rollback steward · Security reviewer · CI steward · Docs steward
created: NEEDS VERIFICATION — file predates this revision
updated: 2026-07-16
supersedes: v0.1 top-level golden fixture README
policy_label: public-doc; fixtures; golden; expected-output; synthetic-only; deterministic; no-network-default; public-safe; source-role-preserving; evidence-aware; policy-aware; sensitivity-aware; release-subordinate; correction-aware; rollback-aware; no-publication
current_path: fixtures/golden/README.md
truth_posture:
  CONFIRMED:
    - Directory Rules assign fixtures and tests to validation/operation responsibilities rather than truth, policy, evidence, release, or lifecycle authority
    - fixtures/README.md separates reusable/runtime fixtures from tests/fixtures and lifecycle data
    - this target README exists at the checked base
    - multiple domain-specific golden README lanes exist under fixtures/domains/
    - bounded repository search did not surface direct payload or consumer files under fixtures/golden/
    - Makefile fixtures target is TODO-only and default make test excludes this lane
  PROPOSED:
    - this parent owns cross-cutting golden admission, pairing, manifest, consumer-backlink, determinism, sensitivity, update-review, and migration rules
    - stable domain-owned golden outputs move to fixtures/domains/<domain>/golden/
    - a future machine-readable golden manifest may enumerate input, expected output, consumer, hashes, profile, and review state
  UNKNOWN:
    - exhaustive payload inventory, generated/ignored files, external golden stores, active consumers, current pass rates, CI retention, branch-protection significance, and release dependency
  NEEDS_VERIFICATION:
    - accepted owners and CODEOWNERS
    - exact admission threshold between top-level and domain/object-family golden lanes
    - substantive golden payloads, active consumers, two-way backlinks, nonempty coverage, no-network enforcement, and CI ownership
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 9741610a833bc7112a1d42a766fae592baf8f1af
  target_prior_blob: 7a48967074841b0df227f04f80442e6fab4ec876
  related_repository_blobs:
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    fixtures_root_readme: b096b0ed49c8e7d95ddb0d4c813d06ef40f1528d
    agriculture_golden_readme: b99f7b99982b20902791888d68cfa44b242acdf8
    makefile: 4dc8cf633581893d83fba53219c6ea847992e6be
notes:
  - "This revision changes documentation only."
  - "Golden fixtures are expected-output carriers, not sovereign truth or publication authority."
  - "README presence, filenames, or a passing comparison do not prove semantic correctness, evidence closure, policy admissibility, release readiness, or production behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-blue">
  <img alt="Lane: golden expected output" src="https://img.shields.io/badge/lane-golden__expected__output-purple">
  <img alt="Inventory: unverified" src="https://img.shields.io/badge/inventory-unverified-orange">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture__only-red">
</p>

> [!IMPORTANT]
> `fixtures/golden/` is the **cross-cutting expected-output lane of last resort**. Use a domain, object-family, runtime, renderer, or test-local golden lane whenever that narrower owner is clear.

> [!CAUTION]
> A golden comparison proves only that a named implementation produced the expected bytes or normalized structure for a declared synthetic case. It does **not** prove source truth, semantic truth, evidence closure, policy approval, release readiness, current-world accuracy, or safe publication.

> [!WARNING]
> Golden files must never freeze sensitive exact geometry, private identities, living-person information, DNA/genomic material, archaeology locations, rare-species localities, critical-infrastructure detail, credentials, live alerts, or reverse-engineerable protected information into repository history.

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose-and-audience) · [Authority](#authority-and-directory-rules-basis) · [Placement](#golden-fixture-placement-law) · [Inventory](#current-inventory-and-maturity) · [Admission](#golden-case-admission-contract) · [Pairing](#input-expected-output-and-consumer-pairing) · [Manifest](#minimum-golden-manifest-contract) · [Determinism](#determinism-normalization-and-hashing) · [Outcomes](#outcome-vocabulary-separation) · [Domains](#domain-and-object-family-routing) · [Runtime](#runtime-renderer-ui-api-and-ai-boundaries) · [Sensitivity](#rights-sensitivity-and-public-safety) · [Evidence](#evidence-policy-review-release-and-lifecycle-separation) · [Updates](#golden-update-review-contract) · [Security](#no-network-filesystem-and-side-effect-boundary) · [Coverage](#consumer-backlinks-orphans-and-nonempty-coverage) · [CI](#runner-ci-and-promotion-boundary) · [Correction](#correction-withdrawal-deprecation-and-rollback) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Ledger](#evidence-ledger)

---

## Status and evidence boundary

**Evidence snapshot:** `main@9741610a833bc7112a1d42a766fae592baf8f1af`  
**Prior target blob:** `7a48967074841b0df227f04f80442e6fab4ec876`  
**Direct payload inventory:** not established by bounded search  
**Direct consumer inventory:** not established by bounded search  
**Dedicated golden CI gate:** not established  
**Makefile fixture refresh:** TODO-only  
**Default `make test`:** does not include this lane

### Safe conclusions

- **CONFIRMED:** the top-level golden README exists.
- **CONFIRMED:** domain-specific golden README lanes exist and should own domain-specific expected outputs.
- **CONFIRMED:** `fixtures/` is separate from `tests/fixtures/`, `artifacts/`, and governed lifecycle data.
- **CONFIRMED:** no direct golden payload or active consumer was surfaced in bounded repository search.
- **CONFIRMED:** `make fixtures` currently echoes a TODO.
- **UNKNOWN:** exhaustive payload inventory, ignored/generated files, external stores, active consumers, current pass rates, and promotion dependency.
- **NEEDS VERIFICATION:** whether this lane should remain README-only or host narrowly scoped cross-cutting golden cases.

### Maturity matrix

| Capability | Status | Evidence-bounded conclusion |
|---|---:|---|
| Parent README | `CONFIRMED` | Routing and governance surface exists. |
| Direct golden payloads | `NOT ESTABLISHED` | No direct payload was surfaced in bounded search. |
| Input/output pairing | `NOT ESTABLISHED` | No direct pair inventory was verified. |
| Consumer backlinks | `NOT ESTABLISHED` | No direct test or validator consumer was surfaced. |
| Machine-readable manifest | `NOT ESTABLISHED` | Proposed below; not accepted implementation. |
| Deterministic normalization | `NOT ESTABLISHED` | Required for substantive golden use. |
| Hash or identity registry | `NOT ESTABLISHED` | Proposed below. |
| No-network enforcement | `NOT ESTABLISHED` | Documentation requires it; executable proof was not found. |
| Orphan/duplicate detection | `NOT ESTABLISHED` | Required future gate. |
| CI collection | `NOT ESTABLISHED` | No dedicated workflow was confirmed. |
| Release authority | `DENIED` | Golden fixtures never approve publication. |

[Back to top](#top)

---

## Purpose and audience

This README serves maintainers who need to:

- decide whether an expected output belongs in this top-level lane or a narrower owner;
- create stable, reviewable regression anchors without turning snapshots into authority;
- keep an input, expected output, consumer, normalization profile, and review reason connected;
- preserve finite KFM outcomes without collapsing them into test pass/fail language;
- prevent sensitive, stale, nondeterministic, or environment-specific values from entering golden history;
- update or retire golden expectations transparently;
- audit orphaned, duplicated, vacuous, or unconsumed golden files.

This lane is useful only when an expected result is genuinely cross-cutting, runtime-wide, renderer-wide, or temporarily unresolved in ownership.

[Back to top](#top)

---

## Authority and Directory Rules basis

Directory Rules make placement a statement of responsibility.

| Responsibility | Correct home | Golden-lane boundary |
|---|---|---|
| Cross-cutting reusable expected output | `fixtures/golden/` | Owned here only when no narrower owner applies. |
| Domain expected output | `fixtures/domains/<domain>/golden/` | Preferred when domain ownership is clear. |
| Test-local expected output | `tests/fixtures/` or owning test subtree | Use when the fixture exists only for one test package. |
| Executable assertions | `tests/` | Golden files are inputs, not tests. |
| Object meaning | `contracts/` | Fixtures imitate accepted meaning; they do not define it. |
| Machine shape | `schemas/` | Fixtures exercise schemas; they do not create schemas. |
| Policy and admissibility | `policy/` | Fixtures may represent decisions; they do not decide them. |
| Evidence and proofs | accepted evidence/proof roots | Golden content is not EvidenceBundle or proof authority. |
| Receipts | accepted receipt roots | Golden receipt-shaped examples are synthetic only. |
| Release and rollback decisions | `release/` | Golden comparisons do not approve or reverse releases. |
| Lifecycle data | `data/` roots | Golden material is outside RAW → PUBLISHED state. |
| Generated CI output | `artifacts/` | Build output must not be committed as golden authority by accident. |

The governing lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Golden fixtures do not enter, shortcut, or substitute for this lifecycle.

[Back to top](#top)

---

## Golden fixture placement law

Use the narrowest stable owner.

1. **One domain owns the expected output:** use `fixtures/domains/<domain>/golden/`.
2. **One object family owns it:** use the accepted object-family fixture lane.
3. **One executable test owns it:** use that test's local fixture convention.
4. **One runtime or renderer subsystem owns it:** use the subsystem fixture lane when present.
5. **Multiple domains participate but one relation/join owns the result:** use the accepted relation or cross-domain fixture lane.
6. **No narrower owner is accepted:** use `fixtures/golden/` temporarily, record the unresolved owner, and migrate once resolved.

Do not create parallel copies merely to satisfy directory symmetry.

### Relocation triggers

Move a golden case out of this lane when:

- domain ownership becomes clear;
- a dedicated runtime or renderer lane is accepted;
- a single test becomes the only consumer;
- the expected output becomes a reusable object-family fixture;
- the file starts resembling evidence, a receipt, a release record, or lifecycle data;
- sensitivity or rights require a more controlled lane;
- the expected output becomes obsolete, superseded, or unconsumed.

[Back to top](#top)

---

## Current inventory and maturity

Bounded repository search surfaced domain golden README lanes for Agriculture, Archaeology, Atmosphere, Fauna, Flora, Geology, Hazards, Hydrology, and People/DNA/Land, among others. Their existence supports the narrow-owner rule.

This README does **not** claim that each lane contains substantive payloads, active consumers, accepted manifests, passing tests, or CI enforcement.

A README, directory, planned filename, or illustrative JSON body is not coverage.

[Back to top](#top)

---

## Golden case admission contract

A new golden case belongs here only when all required questions have explicit answers.

| Question | Required answer |
|---|---|
| What is the scenario? | Stable scenario ID and concise purpose. |
| Why top-level? | No accepted narrower owner, or the case is genuinely cross-cutting. |
| What is the input? | Exact synthetic input path or deterministic generator reference. |
| What is expected? | Exact expected output path and comparison profile. |
| Who consumes it? | Named test, validator, renderer check, API check, or documentation harness. |
| What contract/schema applies? | Exact references, versions, and compatibility profile. |
| What outcome applies? | Runtime, policy, validation, render, or comparison outcome stated explicitly. |
| What is ignored? | Documented nondeterministic fields and why exclusion is safe. |
| What sensitivity applies? | Public-safe, synthetic, generalized, withheld, or denied posture. |
| Why is update safe? | Change rationale, reviewer burden, and regression effect. |
| How is it retired? | Deprecation, supersession, consumer update, and deletion plan. |

Reject or relocate a case when any answer is missing.

[Back to top](#top)

---

## Input, expected-output, and consumer pairing

Every substantive golden fixture should form a traceable triple:

```text
synthetic input
    + declared normalization/comparison profile
    + named executable consumer
    -> expected golden output
```

Recommended naming:

```text
<scenario>.input.json
<scenario>.expected.json
<scenario>.golden.yaml
<scenario>.expected.geojson
<scenario>.expected.svg
```

Recommended pairing rules:

- scenario IDs match exactly across files;
- input and expected output declare compatible contract/schema versions;
- the consumer path is recorded in a manifest or README;
- expected output does not contain undeclared nondeterministic fields;
- negative and fail-closed cases name the expected reason or class;
- corrections update input, expected output, manifest, consumer, and review note together;
- one expected output is not silently reused for incompatible profiles.

Golden files without consumers are orphans. Consumers without declared golden identity are untraceable.

[Back to top](#top)

---

## Minimum golden manifest contract

The following is **PROPOSED**, not an accepted schema:

```yaml
golden_id: golden:<stable-scenario-id>
version: 1
status: active
owner: OWNER_TBD
scope: cross-cutting
input_ref: ../path/to/scenario.input.json
expected_ref: ./scenario.expected.json
consumer_refs:
  - tests/path/to/test_case.py
contract_refs:
  - contracts/path/to/contract.md
schema_refs:
  - schemas/contracts/v1/path/to/schema.json
comparison:
  mode: semantic-json
  ignored_paths: []
  ordering: canonical
  numeric_tolerance: null
outcome:
  vocabulary: runtime
  expected: ABSTAIN
sensitivity:
  posture: synthetic-public-safe
network: denied
filesystem_writes: denied
input_sha256: "<computed>"
expected_sha256: "<computed>"
supersedes: null
review:
  reason: "<why this expectation is correct>"
  approved_by: []
```

Do not invent accepted field names, enum values, registry IDs, tolerances, or approval states from this example.

[Back to top](#top)

---

## Determinism, normalization, and hashing

Golden output must be reproducible under the declared profile.

Required controls where applicable:

- canonical JSON key ordering;
- stable list ordering or explicit order-insensitive comparison;
- normalized timestamps or fixture-pinned times;
- stable UUIDs, IDs, and hashes;
- normalized line endings and Unicode;
- explicit coordinate precision;
- declared numeric tolerance rather than hidden rounding;
- stable locale and timezone;
- stable random seeds;
- no hostnames, usernames, absolute paths, process IDs, ports, or temporary directories;
- no network-derived values;
- no environment-specific package metadata unless intentionally pinned;
- no generated-at timestamps unless fixture-controlled.

Hashing a file proves byte identity only. It does not prove semantic correctness, policy safety, evidence closure, or release readiness.

[Back to top](#top)

---

## Outcome vocabulary separation

Keep these vocabularies distinct.

| Vocabulary | Example values | Meaning |
|---|---|---|
| KFM runtime | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Governed response posture. |
| Policy | allow, restrict, hold, deny, review-required | Admissibility or obligation posture. |
| Validation | valid, invalid, warning, unresolved | Contract/schema/check result. |
| Renderer/UI | rendered, blocked, degraded, fallback, hidden | Surface behavior. |
| Test runner | pass, fail, skip, xfail, error | Execution result. |
| Release | candidate, approved, denied, withdrawn, superseded | Governed publication state. |

A test passing because an expected `DENY` was returned does not mean the policy result was allow. A golden `ANSWER` does not mean release approval.

[Back to top](#top)

---

## Domain and object-family routing

Use domain-specific golden lanes for domain-owned semantics and sensitivity.

Examples surfaced in repository evidence include:

- `fixtures/domains/agriculture/golden/`
- `fixtures/domains/archaeology/golden/`
- `fixtures/domains/atmosphere/golden/`
- `fixtures/domains/fauna/golden/`
- `fixtures/domains/flora/golden/`
- `fixtures/domains/geology/golden/`
- `fixtures/domains/hazards/golden/`
- `fixtures/domains/hydrology/golden/`
- `fixtures/domains/people-dna-land/golden/`

This list is not exhaustive and does not prove payload maturity.

Cross-domain output should preserve each domain's ownership, source role, sensitivity, rights, evidence, and temporal semantics. A top-level golden file must not flatten those differences.

[Back to top](#top)

---

## Runtime, renderer, UI, API, and AI boundaries

Golden fixtures may support bounded comparisons for:

- governed API envelopes;
- MapLibre or tile-renderer inputs and normalized outputs;
- Evidence Drawer payloads;
- Focus Mode responses;
- search and graph projections;
- export summaries;
- runtime replay;
- AI adapter envelopes or bounded generated explanations.

They must not become:

- public API payload authority;
- style or tile release authority;
- UI truth state;
- direct model prompt memory;
- proof that an AI answer is correct;
- a route contract substitute;
- a production snapshot;
- a current-world cache.

AI-generated expected text requires especially careful review. Generated fluency cannot substitute for EvidenceBundle support, policy state, or accepted wording contracts.

[Back to top](#top)

---

## Rights, sensitivity, and public safety

All golden material must be synthetic or demonstrably public-safe.

Deny repository inclusion of:

- real precise rare-species, rare-plant, nest, den, roost, spawning, telemetry, or stewardship locations;
- archaeological sites, burials, sacred places, collection-security details, or culturally restricted knowledge;
- living-person records, DNA/genomic data, consent records, private relationships, or private parcels;
- critical-infrastructure details, access controls, vulnerabilities, or operational dependencies;
- exact private wells, regulated facility details, or reverse-engineerable protected joins;
- credentials, tokens, private endpoints, production logs, or source dumps;
- live emergency warnings or life-safety instructions.

The strictest applicable domain, rights, consent, sovereignty, cultural, privacy, infrastructure, or release posture wins.

[Back to top](#top)

---

## Evidence, policy, review, release, and lifecycle separation

Golden files can imitate trust-bearing objects for tests, but remain synthetic examples.

| Object or state | Golden fixture limit |
|---|---|
| EvidenceRef / EvidenceBundle | May use toy refs; does not establish evidence closure. |
| SourceDescriptor | May use synthetic descriptor shape; does not admit a source. |
| PolicyDecision | May represent an expected decision; does not make policy. |
| ReviewRecord | May exercise shape; does not record actual approval. |
| Receipt | May test validation; does not become an operational receipt. |
| ReleaseManifest | May support dry-run comparison; does not release anything. |
| CorrectionNotice | May test propagation; does not correct production state. |
| RollbackCard | May test rollback shape; does not authorize rollback. |

Public clients and normal UI surfaces still require governed interfaces and released public-safe derivatives.

[Back to top](#top)

---

## Golden update review contract

Changing a golden expectation is a behavior change, not routine formatting.

Every substantive update should state:

1. what implementation or contract changed;
2. why the prior expected output is no longer correct;
3. whether the change is intended, corrective, or compatibility-driven;
4. which consumers are affected;
5. whether policy, sensitivity, evidence, or release semantics changed;
6. whether downstream snapshots, caches, exports, or docs must change;
7. whether the old golden remains useful as a negative or compatibility case;
8. the rollback target.

Prohibited update pattern:

```text
test failed
-> regenerate all goldens
-> commit without inspection
```

Required pattern:

```text
behavior or contract change
-> inspect semantic delta
-> verify authority and sensitivity
-> update only affected cases
-> run named consumers
-> review diff
-> record reason and rollback
```

[Back to top](#top)

---

## No-network, filesystem, and side-effect boundary

Golden generation and comparison should be hermetic by default.

Required posture:

- no live APIs, websites, tile servers, glyph servers, model services, or databases;
- no writes outside declared temporary or artifact locations;
- no mutation of fixture inputs;
- no publication, upload, notification, or release side effects;
- no reads from canonical/internal stores as a shortcut;
- no dependency on current time, locale, user home, or machine path;
- no hidden fixture regeneration during comparison;
- explicit failure when required input, expected output, or consumer is missing.

Optional external smoke checks must be separate from golden acceptance and must never rewrite committed expectations automatically.

[Back to top](#top)

---

## Consumer backlinks, orphans, and nonempty coverage

A future substantive gate should fail when:

- a golden file has no declared consumer;
- a consumer references a missing golden file;
- input and expected output scenario IDs differ;
- duplicate golden IDs exist;
- the lane contains zero substantive cases when coverage is required;
- every case is skipped;
- generated output is compared to itself;
- ignored paths remove all meaningful assertions;
- a domain-owned case remains indefinitely in the top-level lane without reason;
- a sensitive fixture lacks a public-safe review posture;
- an expected output changes without a review reason.

Coverage is case-specific. Counting README files or empty directories is not coverage.

[Back to top](#top)

---

## Runner, CI, and promotion boundary

Current repository evidence does not establish a dedicated top-level golden runner.

The root Makefile currently includes:

```make
fixtures:
	@echo "TODO: regenerate deterministic fixtures"
```

and the default test target runs schema and contract tests rather than this lane.

A future gate should:

- discover accepted manifests deterministically;
- fail on zero collected cases when coverage is expected;
- verify input/output/consumer backlinks;
- enforce no-network and no-write rules;
- validate contract/schema references;
- compare through declared normalization profiles;
- emit reviewable diffs;
- preserve the primary failure;
- retain only public-safe artifacts;
- never auto-approve release.

CI success means only that configured checks passed. It does not prove truth, completeness, policy correctness, or release approval.

[Back to top](#top)

---

## Correction, withdrawal, deprecation, and rollback

When a golden case is wrong:

1. mark it disputed or failing;
2. stop treating it as the accepted expectation;
3. identify affected consumers and derived documentation;
4. determine whether the implementation or fixture is wrong;
5. create a reviewed correction;
6. preserve the prior case when needed for regression history;
7. update hashes, manifests, links, and review notes;
8. run the named consumers;
9. record a rollback target.

When ownership changes, move the case through a transparent commit that updates all backlinks. Do not leave duplicate active copies.

For this README revision, rollback is restoring prior blob `7a48967074841b0df227f04f80442e6fab4ec876` through a transparent revert commit.

[Back to top](#top)

---

## Definition of done

This parent is operationally complete only when:

- [ ] accepted ownership and CODEOWNERS exist;
- [ ] top-level admission criteria are accepted;
- [ ] substantive payload inventory is known;
- [ ] every golden case has an input, expected output, manifest, and consumer;
- [ ] every case has deterministic normalization and identity;
- [ ] domain-owned cases are routed to domain lanes;
- [ ] no sensitive or private information is present;
- [ ] no-network and side-effect controls are executable;
- [ ] orphan, duplicate, zero-case, and vacuous-comparison checks exist;
- [ ] golden updates require semantic review;
- [ ] CI executes the named consumers;
- [ ] correction, deprecation, migration, and rollback are tested;
- [ ] documentation matches current behavior.

Until then, this README is a governed design and routing boundary, not proof of implemented golden-fixture enforcement.

[Back to top](#top)

---

## Open verification register

- [ ] Assign owners and CODEOWNERS.
- [ ] Inventory direct files under `fixtures/golden/`.
- [ ] Identify active consumers.
- [ ] Verify whether payloads are generated, ignored, external, or branch-local.
- [ ] Decide the accepted top-level admission threshold.
- [ ] Decide the manifest home and schema.
- [ ] Establish stable golden IDs and versions.
- [ ] Establish canonical normalization profiles.
- [ ] Establish numeric and geometry tolerance rules.
- [ ] Establish allowed ignored-field rules.
- [ ] Add input/output/consumer backlink checks.
- [ ] Add orphan and duplicate detection.
- [ ] Add nonempty and non-vacuous coverage checks.
- [ ] Add no-network and filesystem isolation.
- [ ] Add sensitive-content scanning and reviewer requirements.
- [ ] Add domain ownership migration checks.
- [ ] Add update-reason and rollback requirements.
- [ ] Add substantive CI collection.
- [ ] Confirm artifact retention and public-safety rules.
- [ ] Confirm promotion gates do not treat golden pass as release approval.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limitation |
|---|---|---|---|
| `fixtures/golden/README.md` prior blob `7a48967074841b0df227f04f80442e6fab4ec876` | `CONFIRMED` | Existing top-level golden guidance. | Did not establish payloads, consumers, or CI. |
| `fixtures/README.md` blob `b096b0ed...` | `CONFIRMED` | Reusable/runtime fixture root and separation from tests, artifacts, and data. | Does not prove this lane's payload inventory. |
| Directory Rules blob `2affb080...` | `CONFIRMED` doctrine | Responsibility-root placement and lifecycle separation. | Specific implementation remains repository-evidence dependent. |
| `fixtures/domains/agriculture/golden/README.md` blob `b99f7b99...` | `CONFIRMED README` | Domain-specific golden ownership and non-authority posture. | Its payload inventory also remains unverified. |
| Repository search at `main@9741610a833bc7112a1d42a766fae592baf8f1af` | `PARTIAL` | Multiple domain golden README lanes exist; no direct top-level payload/consumer surfaced. | Search is bounded and not an exhaustive recursive filesystem listing. |
| Makefile blob `4dc8cf63...` | `CONFIRMED` | `fixtures` target is TODO; default test excludes this lane. | Does not prove all workflow behavior. |

---

## Documentation correction and rollback

This revision changes one Markdown file only. It adds no fixture payload, executable test, validator, schema, contract, policy, workflow, data object, receipt, proof, release record, runtime behavior, or public artifact.

Rollback options:

- before merge: leave the draft PR unmerged or add a transparent revert commit;
- after merge: revert the documentation commit or restore prior blob `7a48967074841b0df227f04f80442e6fab4ec876`;
- do not reset or force-push shared history.

[Back to top](#top)
