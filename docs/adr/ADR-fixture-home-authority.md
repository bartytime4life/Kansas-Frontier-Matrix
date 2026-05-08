<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION-ADR-fixture-home-authority
title: ADR-fixture-home-authority
type: standard
version: v1
status: draft
owners: @bartytime4life
created: 2026-05-08
updated: 2026-05-08
policy_label: NEEDS_VERIFICATION
related: [./README.md, ./ADR-TEMPLATE.md, ./ADR-0001-schema-home.md, ./ADR-0002-responsibility-root-monorepo.md, ../../fixtures/README.md, ../../schemas/README.md, ../../schemas/tests/README.md, ../../tests/README.md, ../../tests/contracts/README.md, ../../policy/README.md, ../../tools/validate_fixtures.py, ../../tools/validate_fixture_schema_mapping.py, ../../tests/test_fixture_schema_mapping.py, ../../.github/workflows/baseline.yml, ../../.github/CODEOWNERS]
tags: [kfm, adr, fixtures, validation, schemas, tests, policy, governance, evidence]
notes: [Revises the existing proposed ADR stub for fixture placement authority. Decision remains proposed until active-checkout validation, owner review, and workflow evidence are verified. Policy label, branch protections, complete fixture inventory, and successful workflow run status remain NEEDS VERIFICATION.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-fixture-home-authority

Decide how KFM assigns fixture placement authority across `fixtures/`, `schemas/tests/fixtures/`, `tests/contracts/`, policy fixtures, and local test fixture lanes.

<p align="center">
  <img alt="ADR status: proposed" src="https://img.shields.io/badge/ADR-proposed-lightgrey">
  <img alt="document status: draft" src="https://img.shields.io/badge/document-draft-ffb000">
  <img alt="owner: bartytime4life" src="https://img.shields.io/badge/owner-%40bartytime4life-1f6feb">
  <img alt="authority: fixture placement" src="https://img.shields.io/badge/authority-fixture%20placement-5319e7">
  <img alt="posture: fail closed" src="https://img.shields.io/badge/posture-fail--closed-b60205">
  <img alt="truth: evidence bounded" src="https://img.shields.io/badge/truth-evidence--bounded-0a7ea4">
</p>

<p align="center">
  <a href="#adr-header">Header</a> ·
  <a href="#decision-summary">Decision</a> ·
  <a href="#context-and-problem">Context</a> ·
  <a href="#evidence-basis">Evidence</a> ·
  <a href="#fixture-placement-rules">Placement</a> ·
  <a href="#validation-plan">Validation</a> ·
  <a href="#impact-map">Impact</a> ·
  <a href="#rollback-and-supersession">Rollback</a> ·
  <a href="#acceptance-criteria">Acceptance</a>
</p>

> [!IMPORTANT]
> **Decision status:** `PROPOSED`.
>
> This ADR chooses a fixture authority model for review. It does **not** prove that every fixture path exists, that every fixture is consumed by tests, that CI is merge-blocking, or that branch protection enforces the proposed rule.

> [!NOTE]
> Fixtures are verification support. A fixture may prove that a schema, policy, validator, runtime envelope, or release dry-run recognizes a case correctly. A fixture is not source data, not a source registry, not an emitted receipt, not a proof pack, not a release manifest, not a publication, and not canonical truth.

---

## ADR header

| Field | Value |
|---|---|
| ADR ID | `ADR-fixture-home-authority` |
| Title | Fixture Home Authority |
| Status | `proposed` |
| Decision date | `2026-05-08` |
| Authors / owners | `@bartytime4life` |
| Reviewers | `REVIEWER_TBD_NEEDS_VERIFICATION` |
| Policy label | `NEEDS_VERIFICATION` |
| Scope | `repo-wide fixture placement / architecture governance / validation` |
| Affected paths | `fixtures/`, `schemas/tests/fixtures/`, `tests/contracts/`, `tests/fixtures/`, `tests/policy/`, `policy/fixtures/`, `tests/domains/`, `fixtures/domains/`, `tools/`, `.github/workflows/` |
| Related ADRs | [`./ADR-0001-schema-home.md`](./ADR-0001-schema-home.md), [`./ADR-0002-responsibility-root-monorepo.md`](./ADR-0002-responsibility-root-monorepo.md) |
| Supersedes | `none` |
| Superseded by | `none` |
| Decision confidence | `PROPOSED` |
| Review state | `draft` |
| Rollback target | Existing pre-revision ADR stub plus affected README/index state |

[Back to top](#top)

---

## Decision summary

KFM should adopt a **tiered fixture authority model**:

1. `fixtures/` is the proposed **shared fixture boundary** for small, deterministic, public-safe examples consumed across contracts, schemas, policy, validators, runtime envelopes, release dry-runs, and domain lanes.
2. `schemas/tests/fixtures/` is a **schema-adjacent fixture scaffold** for examples that stay close to versioned machine schemas.
3. `tests/contracts/` is the **executable contract-test family** for runners, manifests, reports, and contract-drift checks; it may host local fixtures only when they are explicitly test-local.
4. `policy/fixtures/` and `tests/policy/` own **policy-local examples and policy verification** when the main burden is allow, deny, restrict, quarantine, abstain, reason-code, or obligation behavior.
5. `tests/<family>/fixtures/` may hold **family-local test fixtures** when the examples are not shared authority.
6. `fixtures/domains/<domain>/` is the proposed shared home for **domain-specific public-safe fixture slices** until a narrower domain fixture authority is accepted.
7. No fixture home may store source-native custody, provider mirrors, RAW / WORK / QUARANTINE material, emitted receipts, proof packs, release manifests, secrets, exact sensitive locations, or generated publication artifacts.

### One-line decision rule

> Shared, cross-cutting fixtures live in `fixtures/`; schema-adjacent fixtures may live in `schemas/tests/fixtures/`; executable contract tests live in `tests/contracts/`; policy examples stay with policy lanes; every fixture must remain small, deterministic, public-safe, and subordinate to contracts, schemas, policy, validators, receipts, proofs, release, and publication state.

### One-line boundary rule

> A fixture proves a case exists for validation; it does not prove source approval, evidence closure, policy permission, proof emission, release approval, or public truth.

[Back to top](#top)

---

## Context and problem

The existing ADR stub names the decision area but does not yet decide the placement rule. The repo now exposes multiple fixture-adjacent surfaces:

- `fixtures/`
- `schemas/tests/fixtures/`
- `tests/contracts/`
- `tests/fixtures/`
- `tests/policy/`
- `policy/fixtures/`
- domain-specific fixture and test paths

That is healthy only if each lane has a distinct burden. Without an ADR, fixture examples can drift into duplicate authority: a schema-side example can become the hidden canonical fixture, a contract test can become a schema home, a policy fixture can imply permission, or a shared fixture can become mistaken for emitted proof.

### Why this is architecture-significant

KFM’s trust model depends on visible seams:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Fixtures sit near the seam between **declared trust objects** and **executable verification**. If fixture placement is ambiguous, the repo can accidentally blur:

- contract meaning and machine shape,
- schema validity and policy permission,
- test fixtures and source data,
- expected-output fragments and emitted receipts,
- proof examples and release proof,
- public-safe examples and real sensitive data.

This ADR keeps fixture authority useful without letting fixtures become a second source registry, a second schema home, or a hidden publication lane.

[Back to top](#top)

---

## Evidence basis

| Evidence item | Source / path / artifact | What it supports | Truth label |
|---|---|---|---|
| Existing target ADR | `docs/adr/ADR-fixture-home-authority.md` | A proposed fixture-home decision record exists, but it is a thin stub and asks for concrete file/path evidence before acceptance. | `CONFIRMED` |
| ADR template | `docs/adr/ADR-TEMPLATE.md` | ADRs should carry meta blocks, evidence basis, impact map, validation plan, rollback path, truth labels, and anti-overclaim warnings. | `CONFIRMED` |
| ADR index | `docs/adr/README.md` | `docs/adr/` is the human-facing decision ledger; ADRs record decisions and review burden, not enforcement proof. | `CONFIRMED` |
| Directory Rules | `Directory Rules.pdf` and ADR-0002 | Root folders are responsibility boundaries; `fixtures/` is an accepted responsibility root; domains belong under responsibility roots. | `CONFIRMED` |
| Fixture README | `fixtures/README.md` | `fixtures/` is a supporting verification surface for deterministic public-safe valid/invalid examples and explicitly not source data, proof, receipt, or release authority. | `CONFIRMED` |
| Schema README | `schemas/README.md` | `schemas/` recognizes fixture-home ambiguity and treats `schemas/tests/` as a nested fixture scaffold, not the singular governed fixture home. | `CONFIRMED` |
| Schema-side fixture README | `schemas/tests/README.md` | `schemas/tests/` is fixture-facing, not authority-facing; root `tests/contracts/` remains the stronger execution lane. | `CONFIRMED` |
| Tests README | `tests/README.md` | `tests/` is governed verification; it consumes schemas/contracts/policy/fixtures and must not become schema, policy, or proof authority. | `CONFIRMED` |
| Contract tests README | `tests/contracts/README.md` | `tests/contracts/` verifies contract behavior and drift; it does not own contract meaning, schema authority, policy logic, release approval, or publication state. | `CONFIRMED` |
| Schema-home ADR | `docs/adr/ADR-0001-schema-home.md` | `schemas/contracts/v1/` is proposed as machine schema home; `contracts/` meaning and `policy/` admissibility remain separate. | `CONFIRMED / PROPOSED` |
| Responsibility-root ADR | `docs/adr/ADR-0002-responsibility-root-monorepo.md` | `fixtures/` is a canonical responsibility root; domain work should be placed under responsibility roots rather than domain roots. | `CONFIRMED / ACCEPTED` |
| CODEOWNERS | `.github/CODEOWNERS` | Conservative owner routing covers `fixtures/`, `schemas/`, `tests/contracts/`, `docs/adr/`, and related trust surfaces through `@bartytime4life`. | `CONFIRMED` |
| Fixture validators | `tools/validate_fixtures.py`, `tools/validate_fixture_schema_mapping.py` | The repo has validation tooling that checks root fixtures and fixture-to-schema mappings. | `CONFIRMED` |
| Unit test wrapper | `tests/test_fixture_schema_mapping.py` | The fixture-to-schema mapping tool is exercised by the unit test suite. | `CONFIRMED` |
| Baseline workflow | `.github/workflows/baseline.yml` | The baseline workflow is configured to run fixture validation, schema conformance, fixture-to-schema mapping, schema-home checks, no-public-internal-path checks, source checks, promotion dry-run, release checks, and unittest discovery. | `CONFIRMED workflow file / NEEDS VERIFICATION successful run and branch protection` |

> [!CAUTION]
> Workflow YAML proves intended orchestration, not successful enforcement. Successful run status, branch protection, required-check policy, and full active-branch fixture inventory remain `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Scope and non-goals

### In scope

- Authority split among `fixtures/`, `schemas/tests/fixtures/`, `tests/contracts/`, `tests/fixtures/`, `policy/fixtures/`, and `tests/policy/`.
- Rules for valid, invalid, expected-output, allow, deny, quarantine, and domain fixtures.
- How fixtures relate to schemas, contracts, policy, validators, tests, receipts, proofs, releases, and data lifecycle zones.
- Validation required before this ADR moves from `proposed` to `accepted`.
- Rollback and supersession behavior if the fixture-home model changes.

### Non-goals

- Finalize schema-home authority. That belongs to ADR-0001.
- Define all contract schemas or object families.
- Define policy reason-code law.
- Define source registry placement.
- Define emitted receipt, proof, release, catalog, or publication homes.
- Approve any live connector or source activation.
- Prove CI is merge-blocking.
- Publish any fixture as evidence, proof, or release material.

[Back to top](#top)

---

## Requirements and constraints

### KFM invariants checked

| Invariant | Fixture-home implication | Status |
|---|---|---|
| `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED` | Fixtures must not become lifecycle data or public shortcuts around lifecycle state. | `CONFIRMED doctrine` |
| Public clients use governed interfaces and released artifacts | Fixtures may support tests for public payloads but must not be exposed as public claim authority. | `CONFIRMED doctrine` |
| `EvidenceRef` resolves to `EvidenceBundle` before consequential claims | Fixtures may test evidence closure; fixture presence is not evidence closure. | `CONFIRMED doctrine` |
| Promotion is a governed state transition | Fixture validation can support readiness; it cannot promote. | `CONFIRMED doctrine` |
| AI is interpretive and evidence-subordinate | AI/runtimes fixtures must use finite envelopes and cited/abstain behavior; generated text is not proof. | `CONFIRMED doctrine` |
| Derived surfaces do not replace canonical truth | Fixture examples, map tiles, story payloads, and expected fragments are all downstream support. | `CONFIRMED doctrine` |
| Rights, sensitivity, source-role, and policy checks fail closed | Fixtures with unclear rights or sensitivity should be synthetic, redacted, generalized, quarantined, or denied. | `CONFIRMED doctrine` |
| Receipts, proofs, releases, reviews, corrections, and rollback records remain separate | Fixtures may model these objects but must not store emitted instances as authority. | `CONFIRMED doctrine` |

### Assumptions

| Assumption | Why it is needed | Label | How to verify or retire |
|---|---|---|---|
| `fixtures/` should be the shared root fixture boundary after acceptance | Current root README and validator mappings already point to root fixtures. | `PROPOSED` | Confirm with maintainers, docs, validators, fixture inventory, and passing workflow run. |
| `schemas/tests/fixtures/` remains schema-adjacent, not global canonical | Current schema README and schemas/tests README describe it as a scaffold and companion. | `CONFIRMED role / NEEDS VERIFICATION inventory` | Inspect exact subtree and consumer mappings. |
| `tests/contracts/` should be runner/report authority rather than shared fixture authority | Current tests/contracts README states it consumes and verifies contract truth. | `CONFIRMED role` | Confirm runner manifests and fixtures after active branch inventory. |
| Workflow execution is configured but enforcement maturity is not proven | Workflow file exists, but run status and branch protection were not inspected. | `NEEDS VERIFICATION` | Inspect GitHub Actions run, required checks, and rulesets. |

[Back to top](#top)

---

## Options considered

| Option | Description | Benefits | Risks / costs | Evidence posture | Outcome |
|---|---|---|---|---|---|
| A. Root shared fixture home | Treat `fixtures/` as the shared public-safe fixture boundary; let specific lanes consume from it. | One visible shared place; aligns with root `fixtures/README.md`; matches current mapping validator. | Can become a dumping ground unless exclusions are strict. | `CONFIRMED root exists / PROPOSED authority` | **Accepted as proposed shared rule** |
| B. Schema-side canonical fixtures | Treat `schemas/tests/fixtures/` as canonical for all contract/schema fixtures. | Keeps examples near schemas. | Risks making schema side a second test authority; weaker for policy/runtime/release fixtures. | `CONFIRMED scaffold / NEEDS VERIFICATION authority` | Rejected as global rule |
| C. Contract-test canonical fixtures | Treat `tests/contracts/fixtures/` as the canonical home for contract fixtures. | Keeps examples near executable tests. | Blurs test runner and shared fixture authority; excludes policy/runtime/domain fixtures. | `PROPOSED local only` | Rejected as global rule |
| D. Distributed local fixtures only | Every test family owns its own fixtures. | Maximum locality. | Duplication, drift, inconsistent valid/invalid examples, weak cross-family reuse. | `PROPOSED` | Rejected |
| E. Tiered fixture authority | Shared fixtures in `fixtures/`; schema-adjacent fixtures near schemas; executable tests in `tests/contracts/`; policy-local examples in policy/test lanes. | Preserves locality and shared authority while preventing duplicate truth. | Requires clear README links and validator mappings. | `CONFIRMED adjacent docs / PROPOSED decision` | **Chosen** |

[Back to top](#top)

---

## Decision

### Chosen option

Adopt **Option E — tiered fixture authority**.

### Rationale

This option preserves KFM’s responsibility-root discipline without flattening all examples into one folder. It supports small public-safe shared fixtures while allowing schema-adjacent and test-local examples when their burden is narrow. It also matches the visible repo direction: root `fixtures/` carries shared fixture doctrine, `schemas/tests/` carries schema-side fixture scaffold doctrine, `tests/contracts/` carries executable contract-test doctrine, and existing tools map root fixtures to canonical schema paths.

### Operating rule

> Use the narrowest truthful fixture home, but keep shared fixture truth singular. When the same case is useful in multiple lanes, prefer one shared fixture with explicit consumers over duplicated payloads.

### Boundary rule

> No fixture may become canonical source data, source registry authority, policy law, emitted receipt, proof pack, release manifest, published artifact, runtime implementation, secret, or sensitive exact-location record.

[Back to top](#top)

---

## Fixture placement rules

### Placement matrix

| Fixture or example type | Proposed home | Role | Must not become |
|---|---|---|---|
| Shared valid/invalid trust-object fixture | `fixtures/<family>/` | Cross-cutting fixture authority for multiple validators/tests. | Contract, schema, policy, receipt, proof, or release authority. |
| Shared source fixture | `fixtures/source/<source-or-family>/` | Tiny source-admission example. | Source registry, provider mirror, source approval. |
| Shared evidence fixture | `fixtures/evidence/<object-family>/` | Evidence closure or citation-case example. | Emitted `EvidenceBundle` proof. |
| Shared runtime fixture | `fixtures/runtime/<surface>/` or existing `fixtures/ai/` pattern | Runtime envelope case such as `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`. | AI truth, direct model output, runtime implementation. |
| Shared policy decision fixture | `fixtures/policy/` when cross-cutting; `policy/fixtures/` when policy-local | Allow/deny/abstain example input or expected decision fragment. | Policy rule source. |
| Schema-adjacent fixture | `schemas/tests/fixtures/contracts/v1/{valid,invalid}/` | Example kept near versioned machine schemas. | Global fixture home unless explicitly referenced. |
| Contract-test local fixture | `tests/contracts/fixtures/` | Test-local case for contract runner only. | Shared fixture authority unless documented and mapped. |
| Root test fixture | `tests/fixtures/` | Test-suite-local examples. | Shared contract/schema/policy truth. |
| Policy test fixture | `tests/policy/fixtures/` or `policy/fixtures/` by local convention | Policy allow/deny/restrict/quarantine verification. | Contract or schema definition. |
| Domain shared fixture | `fixtures/domains/<domain>/` | Small public-safe domain slice reused across tests/tools. | Domain data custody. |
| Domain test-local fixture | `tests/domains/<domain>/fixtures/` | Local domain test case. | Shared domain fixture authority unless promoted through documentation and mapping. |
| Expected-output fragment | Same family as the consuming test, usually `fixtures/<family>/` or `tests/<family>/fixtures/` | Deterministic comparison target. | Emitted receipt/proof/release object. |

### Fixture authority states

| State | Meaning | Review rule |
|---|---|---|
| `shared` | Fixture is intended for cross-family reuse. | Prefer `fixtures/`; require mapping and README link. |
| `schema-adjacent` | Fixture exists to illustrate or pressure-test a versioned schema. | Prefer `schemas/tests/fixtures/`; require schema target and consumer link. |
| `test-local` | Fixture is only meaningful inside one test family. | Prefer `tests/<family>/fixtures/`; do not cite as shared authority. |
| `policy-local` | Fixture exists only to prove policy grammar or decision behavior. | Keep near `policy/` or `tests/policy/`; do not define policy by fixture alone. |
| `domain-shared` | Domain fixture has cross-test/tool use. | Prefer `fixtures/domains/<domain>/`; require sensitivity and rights review. |
| `quarantined` | Fixture is disputed, unsafe, rights-unclear, or potentially sensitive. | Do not run as public-safe; repair, redact, generalize, replace, or remove. |
| `deprecated` | Fixture remains for compatibility but should not guide new work. | Keep successor pointer and retirement plan. |
| `superseded` | Fixture is replaced by a newer fixture. | Preserve lineage until all consumers migrate. |

[Back to top](#top)

---

## Naming and metadata rules

### Naming pattern

Prefer names that make review possible before opening the file:

```text
<object-family>.<case>.valid.json
<object-family>.<failure-reason>.invalid.json
<object-family>.<case>.expected.json
<gate>.<case>.allow.json
<gate>.<failure-reason>.deny.json
<domain>.<object>.<case>.valid.json
```

Good examples:

```text
source_descriptor.public-rest.valid.json
source_descriptor.missing-rights.invalid.json
evidence_bundle.missing-citation.invalid.json
runtime_response.raw-work-reference.invalid.json
publish_gate.unresolved-rights.deny.json
release_manifest.missing-rollback.invalid.json
hydrology.huc12.synthetic.valid.json
```

Avoid vague names:

```text
sample.json
test.json
good.json
bad.json
fixture1.json
data.csv
```

### Minimum fixture metadata

Non-trivial JSON or YAML fixtures should carry or be covered by metadata with:

| Field | Purpose |
|---|---|
| `fixture_id` | Stable local identifier. |
| `object_family` | KFM object or domain family. |
| `case` | Human-readable case name. |
| `expected_result` | `valid`, `invalid`, `allow`, `deny`, `abstain`, `error`, or `expected`. |
| `network` | Should be `none` for default fixtures. |
| `knowledge_character` | Should be `SYNTHETIC_TEST` for synthetic valid fixtures when applicable. |
| `sensitivity` | Public-safety posture. |
| `schema_ref` | Canonical schema path or schema `$id` when shape validation is relevant. |
| `policy_ref` | Policy surface when admissibility is relevant. |
| `consumer` | Test, validator, or workflow expected to use the fixture. |
| `review_state` | `draft`, `reviewed`, `deprecated`, `quarantined`, or `superseded`. |

> [!TIP]
> Invalid fixtures are not noise. They are the easiest way to keep KFM’s deny-by-default, cite-or-abstain, no-public-raw-path, and rollback-required rules reviewable.

[Back to top](#top)

---

## Validation plan

### Required checks

| Check | Command / artifact | Expected result | Status |
|---|---|---|---|
| Fixture shape and intentional invalidity | `python tools/validate_fixtures.py` | Valid fixtures pass; invalid fixtures remain intentionally invalid. | `CONFIRMED command exists / NEEDS VERIFICATION current run` |
| Fixture-to-schema mapping | `python tools/validate_fixture_schema_mapping.py` | Mapped fixtures and schemas exist. | `CONFIRMED command exists / NEEDS VERIFICATION current run` |
| Fixture mapping unit test | `python -m unittest tests.test_fixture_schema_mapping` | Mapping validator is exercised through test suite. | `CONFIRMED test exists / NEEDS VERIFICATION current run` |
| Full unittest sweep | `python -m unittest discover -s tests` | Repo unit tests pass. | `CONFIRMED workflow step / NEEDS VERIFICATION current run` |
| Baseline workflow | `.github/workflows/baseline.yml` | Runs fixture, schema, mapping, directory, policy/source, promotion, release, and unit checks on push/PR. | `CONFIRMED workflow file / NEEDS VERIFICATION successful run and required-check status` |
| Fixture-home duplicate scan | `PROPOSED: repo-native drift check` | Duplicate fixture payloads must be linked as mirrors or fail review. | `PROPOSED` |
| Sensitive content scan | `PROPOSED: fixture safety validator` | Secrets, exact sensitive locations, RAW/WORK references, or provider mirrors fail closed. | `PROPOSED` |
| Documentation sync | ADR index and adjacent READMEs | Placement rules remain consistent. | `NEEDS VERIFICATION` |

### Negative-path behavior

| Failure condition | Expected outcome | Evidence / test |
|---|---|---|
| Public payload references `data/raw`, `data/work`, or `data/quarantine` | `DENY`, `ERROR`, or validation failure | Existing fixture validator includes raw-path invalid fixture logic; no-public-internal-path workflow step exists. |
| `ANSWER` fixture lacks citation support | Validation failure or `ABSTAIN` expectation | Existing fixture validator checks `ANSWER` requires citations for Focus response fixtures. |
| Release fixture lacks rollback target | Validation failure | Existing fixture validator checks release manifest rollback target and correction route. |
| Source fixture lacks rights or source role | Validation failure, `DENY`, or `QUARANTINE` | Mapping validator and policy/source checks should preserve this. |
| Sensitive exact geometry appears in public-safe fixture | `DENY` or `QUARANTINE` | Existing invalid fixture logic includes restricted exact-coordinate pattern. |
| Schema-side and root fixture payloads diverge silently | Drift check fails | `PROPOSED` duplicate/mirror validator. |
| Fixture is a provider mirror rather than a tiny slice | Review failure or quarantine | This ADR and `fixtures/README.md` exclusion rule. |

[Back to top](#top)

---

## Impact map

### File and documentation impact

| Area | Required update | Status |
|---|---|---|
| `docs/adr/` | Replace thin ADR stub with this evidence-backed decision record; update ADR index if needed. | `PROPOSED` |
| `fixtures/README.md` | Ensure shared fixture authority language matches this ADR after acceptance. | `NEEDS VERIFICATION` |
| `schemas/README.md` | Keep schema-home and fixture-home language aligned with ADR-0001 and this ADR. | `NEEDS VERIFICATION` |
| `schemas/tests/README.md` | Keep schema-adjacent fixture role explicit. | `NEEDS VERIFICATION` |
| `tests/README.md` | Keep governed verification and no-network fixture guidance aligned. | `NEEDS VERIFICATION` |
| `tests/contracts/README.md` | Clarify local fixtures versus shared fixture authority if needed. | `NEEDS VERIFICATION` |
| `policy/README.md` and `tests/policy/README.md` | Confirm policy-local fixture placement and deny/reason-code test placement. | `NEEDS VERIFICATION` |
| `tools/validate_fixtures.py` | Continue to enforce synthetic, finite-outcome, citation, sensitivity, and rollback fixture expectations. | `CONFIRMED exists / NEEDS VERIFICATION coverage` |
| `tools/validate_fixture_schema_mapping.py` | Continue to map shared fixtures to `schemas/contracts/v1/` schemas. | `CONFIRMED exists / NEEDS VERIFICATION coverage` |
| `.github/workflows/baseline.yml` | Keep fixture, schema, fixture-to-schema, directory, and no-public-internal-path checks wired. | `CONFIRMED file / NEEDS VERIFICATION run` |
| `.github/CODEOWNERS` | Review owner routing remains conservative until teams/stewards are verified. | `CONFIRMED baseline` |

### Lifecycle impact

| Lifecycle stage | Fixture-home effect | Guardrail |
|---|---|---|
| Source edge | Fixtures may model source admission only as tiny public-safe examples. | Real source descriptors and registries remain outside fixture authority. |
| RAW | No fixture may store source-native custody as RAW. | Provider mirrors and raw downloads are excluded. |
| WORK | Fixtures must not reference unpublished work records in public-facing cases. | Raw/work/quarantine references fail validation. |
| QUARANTINE | Unsafe or rights-unclear fixture candidates can be quarantined by review. | Do not run as public-safe until repaired. |
| PROCESSED | Fixtures can model normalized shapes but are not processed data. | Mark as synthetic or expected. |
| CATALOG / TRIPLET | Fixtures can model catalog/triplet examples but not emitted catalog truth. | Emitted instances stay in data/release lanes. |
| PUBLISHED | Fixtures cannot publish; they may test publication eligibility. | Promotion requires release gates and rollback target. |

### Trust-surface impact

| Surface | Effect | Required check |
|---|---|---|
| Governed API | Runtime fixtures can test finite outcomes and no-internal-path leakage. | Validate against runtime envelope schema and no-public-internal-path checks. |
| MapLibre shell | Layer/payload fixtures must remain downstream of released artifacts and EvidenceBundle routing. | Check layer/drawer contract tests when present. |
| Evidence Drawer | Drawer fixtures must preserve support, rights, sensitivity, review, freshness, and correction state. | Contract and accessibility tests when available. |
| Focus Mode / governed AI | AI response fixtures must use finite outcomes and citations or abstention. | `validate_fixtures.py`, citation validation, runtime envelope tests. |
| Review console / steward surfaces | Fixtures may test review records but not replace review. | Policy/review tests and reviewer routing. |
| Catalog / search / graph projections | Fixtures may model expected closure; projections remain derived. | Catalog closure tests and proof/release separation checks. |

[Back to top](#top)

---

## Consequences

### Positive consequences

- Gives maintainers a single rule for fixture placement.
- Preserves `fixtures/` as a shared verification boundary without making it source or proof authority.
- Keeps `schemas/tests/fixtures/` useful without turning it into global fixture law.
- Keeps `tests/contracts/` focused on executable proof instead of hidden schema or fixture authority.
- Makes policy-local fixtures and policy tests visible without smuggling policy into schemas.
- Supports existing fixture-to-schema mapping tools.
- Makes duplicate fixture payloads reviewable rather than accidental.
- Keeps public-safe fixture design compatible with KFM sensitivity and rights posture.

### Tradeoffs and risks

| Risk | Mitigation | Residual status |
|---|---|---|
| `fixtures/` could become a dumping ground. | Strict accepted-input and exclusion rules; size/safety review; no provider mirrors. | `PROPOSED mitigation` |
| Schema-adjacent fixtures may duplicate root fixtures. | Require one canonical shared fixture or explicit mirror/pointer with drift check. | `NEEDS VERIFICATION` |
| Contract tests may host too many local examples. | Allow local fixtures only when explicitly test-local. | `PROPOSED mitigation` |
| Policy fixtures may imply permission. | Policy rules and policy tests decide; fixtures only provide cases. | `CONFIRMED boundary` |
| CI intent may be mistaken for enforcement. | Keep workflow run and branch protection as `NEEDS VERIFICATION`. | `OPEN` |
| Sensitive real data could enter fixtures. | Require synthetic/public-safe fixtures; quarantine unclear cases. | `PROPOSED mitigation` |

[Back to top](#top)

---

## Rollback and supersession

### Rollback plan

If this ADR is rejected or superseded, revert to the existing stub decision state and preserve this revision as lineage. Do not delete fixture history or silently move examples. Instead:

1. mark this ADR `rejected`, `withdrawn`, or `superseded`;
2. link the successor ADR;
3. preserve the old placement matrix as lineage;
4. inventory affected fixtures;
5. migrate fixtures through documented rename or pointer records;
6. update root and child READMEs;
7. update validators and workflow references;
8. run fixture validation and fixture-to-schema mapping checks;
9. record any public-surface effect as a correction or review note if applicable.

### Rollback triggers

| Trigger | Required action |
|---|---|
| Active repo proves a different canonical fixture strategy | Supersede this ADR and update all fixture README links. |
| Duplicate fixture payloads diverge | Block merge, choose one authority, add mirror/pointer, or remove duplicate. |
| Fixture contains rights-unclear or sensitive material | Quarantine/remove fixture and replace with synthetic public-safe case. |
| Validator mapping breaks | Block acceptance until mapping is repaired. |
| Workflow run fails | Keep ADR proposed; do not claim enforcement. |
| Public client bypass discovered through fixture or runtime payload | Block release path and open policy/security review. |
| Schema-home ADR changes schema path | Update fixture-schema mapping and this ADR’s related paths. |

### Supersession rule

A successor ADR must state:

- whether `fixtures/` remains the shared fixture home;
- how `schemas/tests/fixtures/`, `tests/contracts/fixtures/`, `tests/fixtures/`, `policy/fixtures/`, and domain fixtures migrate;
- what validator enforces the new placement;
- what happens to old fixtures;
- how mirrors or compatibility aliases retire;
- which public or release surfaces are affected.

[Back to top](#top)

---

## Acceptance criteria

This ADR can move from `proposed` to `accepted` only when these are verified in the active checkout or review record:

- [ ] Maintainers accept `fixtures/` as the shared fixture boundary or explicitly narrow this ADR.
- [ ] `schemas/tests/fixtures/` is documented as schema-adjacent, not global authority.
- [ ] `tests/contracts/` is documented as runner/report verification authority, not hidden schema or fixture authority.
- [ ] Policy-local fixture placement is confirmed with `policy/` and `tests/policy/` docs.
- [ ] Fixture inventory is captured for `fixtures/`, `schemas/tests/fixtures/`, `tests/contracts/`, `tests/fixtures/`, `policy/fixtures/`, and `tests/policy/`.
- [ ] `tools/validate_fixtures.py` passes on current branch.
- [ ] `tools/validate_fixture_schema_mapping.py` passes on current branch.
- [ ] `python -m unittest tests.test_fixture_schema_mapping` passes on current branch.
- [ ] Default fixture validation remains no-network.
- [ ] At least one valid and one invalid fixture exist for each object family this ADR claims as first-wave shared coverage.
- [ ] Fixture filenames identify object family and case or failure reason.
- [ ] No fixture is a provider mirror, source registry, emitted receipt, proof pack, release manifest, public tile, secret, or exact sensitive-location artifact.
- [ ] Baseline workflow run is verified, or enforcement remains documented as manual/dry-run only.
- [ ] Branch protection or required-check status is verified before making merge-blocking claims.
- [ ] ADR index and adjacent READMEs are updated.
- [ ] Rollback/supersession path is preserved.

[Back to top](#top)

---

## Open verification backlog

| Item | Status | Why it matters |
|---|---:|---|
| Complete active-branch fixture inventory | `NEEDS VERIFICATION` | Required before accepting fixture placement authority. |
| Successful workflow run | `NEEDS VERIFICATION` | Workflow file exists, but successful run evidence was not inspected here. |
| Branch protection / required checks | `UNKNOWN` | Required before claiming enforcement. |
| Fixture-home duplicate scan | `PROPOSED` | Needed to prevent root/schema/test duplicate drift. |
| Policy-local fixture convention | `NEEDS VERIFICATION` | `policy/fixtures/` and `tests/policy/` must not split policy truth. |
| Domain fixture conventions | `NEEDS VERIFICATION` | Domain shared fixtures and domain test-local fixtures need a consistent lane. |
| Sensitive fixture scan | `NEEDS VERIFICATION` | Needed before broader domain fixtures are admitted. |
| Fixture metadata schema | `PROPOSED` | A shared fixture metadata shape would improve review and drift checks. |
| ADR index update | `NEEDS VERIFICATION` | This ADR should be listed with status and successor links. |
| Policy label | `NEEDS VERIFICATION` | Do not infer public/restricted classification from path alone. |

[Back to top](#top)

---

## Review checklist

<details>
<summary><strong>Pre-merge checklist</strong></summary>

- [ ] Meta block values are either evidence-backed or deliberately marked `NEEDS_VERIFICATION`.
- [ ] ADR status remains `proposed` unless acceptance criteria are met.
- [ ] Decision does not claim workflow success or branch protection.
- [ ] `fixtures/` role is stated as shared verification support, not truth authority.
- [ ] `schemas/tests/fixtures/` role is schema-adjacent and not global authority.
- [ ] `tests/contracts/` role is executable verification and not schema/policy authority.
- [ ] Policy-local fixtures do not define policy rules by example alone.
- [ ] Fixture placement does not bypass contracts, schemas, policy, validators, receipts, proofs, or release gates.
- [ ] No fixture class permits RAW, WORK, QUARANTINE, provider mirrors, source registries, emitted receipts, proof packs, release manifests, secrets, or exact sensitive locations.
- [ ] Validation plan includes positive and negative paths.
- [ ] Adjacent READMEs and ADR index updates are listed or completed.
- [ ] Rollback and supersession path is clear.
- [ ] The document preserves existing ADR identity and makes the revision stronger without inventing maturity.

</details>

[Back to top](#top)

---

## Appendix A — Inspection commands

<details>
<summary><strong>Run from repository root before accepting this ADR</strong></summary>

```bash
# Confirm repository context.
git rev-parse --show-toplevel
git branch --show-current
git status --short

# Inspect fixture-bearing lanes.
find fixtures -maxdepth 5 -type f | sort
find schemas/tests/fixtures -maxdepth 6 -type f 2>/dev/null | sort
find tests/contracts -maxdepth 6 -type f | sort
find tests/fixtures -maxdepth 6 -type f 2>/dev/null | sort
find policy -maxdepth 5 -type f | sort
find tests/policy -maxdepth 5 -type f 2>/dev/null | sort
find tests/domains fixtures/domains -maxdepth 6 -type f 2>/dev/null | sort

# Inspect authority docs together.
sed -n '1,260p' fixtures/README.md
sed -n '1,260p' schemas/README.md
sed -n '1,260p' schemas/tests/README.md
sed -n '1,260p' tests/README.md
sed -n '1,260p' tests/contracts/README.md
sed -n '1,260p' policy/README.md
sed -n '1,260p' docs/adr/ADR-0001-schema-home.md
sed -n '1,260p' docs/adr/ADR-0002-responsibility-root-monorepo.md

# Run current fixture and mapping checks.
python tools/validate_fixtures.py
python tools/validate_fixture_schema_mapping.py
python -m unittest tests.test_fixture_schema_mapping

# Run broader test surface when repo toolchain is available.
python -m unittest discover -s tests
bash scripts/validate_all.sh
```

</details>

[Back to top](#top)

---

## Appendix B — Anti-patterns this ADR rejects

<details>
<summary><strong>Fixture authority anti-patterns</strong></summary>

- Treating `schemas/tests/fixtures/` as canonical for all fixtures because it is near schemas.
- Treating `tests/contracts/fixtures/` as shared fixture authority because tests consume it.
- Copying the same fixture into root, schema-side, and test-local homes without mirror status or drift checks.
- Storing source-native provider payloads under fixture lanes.
- Treating a valid fixture as source approval.
- Treating a shape-valid fixture as policy approval.
- Treating an expected-output fixture as an emitted receipt or proof.
- Treating a release-manifest fixture as release approval.
- Treating an AI response fixture as proof of truth.
- Adding only happy-path fixtures.
- Using vague filenames like `good.json` and `bad.json`.
- Hiding sensitive exact coordinates in public-safe fixtures.
- Claiming CI enforcement from workflow YAML alone.
- Letting a fixture path override contracts, schemas, policy, or release objects.

</details>

[Back to top](#top)
