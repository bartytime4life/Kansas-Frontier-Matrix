<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-public-safe-readme
title: fixtures/public_safe/ — Public-safe Fixture Parent Lane
version: v0.2.0
type: readme; fixture-parent; public-safe; synthetic; cross-cutting
status: draft; CONFIRMED path; documentation-and-runtime-example lane; payload and consumer maturity NEEDS VERIFICATION
owners: OWNER_TBD — Fixture steward · Test/QA steward · Evidence steward · Policy steward · Sensitivity reviewer · Rights reviewer · UI steward · Docs steward
created: NEEDS VERIFICATION — README predates this revision
updated: 2026-07-22
policy_label: public-doc; fixtures; public-safe; synthetic-only; non-authoritative; release-gated
owning_root: fixtures/
current_path: fixtures/public_safe/README.md
truth_posture: CONFIRMED target, parent, settlement child, test-local fixture split, Directory Rules placement, and adjacent Archaeology compatibility lane at the pinned snapshot / PROPOSED scenario packaging and review fields / UNKNOWN complete child and payload inventory, consumers, validators, tests, runtime wiring, CI coverage, and public-safety review state / NEEDS VERIFICATION before any fixture is relied on by a consumer
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: d24c7bf9ee89c9bb3bd2cd14e0e60b1de6314bc0
  prior_blob: 7efa4537a55f286a32870c834a1f5e91983b0f19
  fixtures_root_blob: b096b0ed49c8e7d95ddb0d4c813d06ef40f1528d
  settlement_child_blob: bc774a004cd04d270ac60076e23a0959255f42a4
  tests_fixtures_blob: 2d0147e85eae86f687e85c5bea0d3e61f9c3a8f7
related:
  - ../README.md
  - ./settlement/README.md
  - ../domains/README.md
  - ../archaeology-public-safe/README.md
  - ../../tests/fixtures/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/truth-posture.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../docs/doctrine/ai-build-operating-contract.md
  - ../../CONTRIBUTING.md
tags: [kfm, fixtures, public-safe, synthetic, deterministic, generalized, evidence, sensitivity, rights, finite-outcomes, correction, rollback]
notes:
  - "This revision documents the parent lane only. It creates no fixture payload, contract, schema, policy decision, validator, test, consumer, release, or public route."
  - "Public-safe describes reviewed fixture construction and exposure posture; it does not establish real-world truth, policy approval, or release authority."
  - "The bounded repository review confirmed the settlement child and an adjacent Archaeology compatibility lane but did not establish a complete directory or payload inventory."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Public-safe fixtures

> Small, deterministic, synthetic examples designed for open review, documentation, and bounded runtime checks. A fixture may demonstrate governed behavior; it never establishes source truth, public eligibility, or release authority.

**Path:** `fixtures/public_safe/`  
**Role:** cross-cutting public-safe fixture parent  
**Owning root:** `fixtures/`  
**Audience:** fixture authors, test and validator maintainers, domain stewards, policy and sensitivity reviewers, UI/runtime maintainers, and documentation authors  
**Default posture:** synthetic-only, compact, deterministic, no secrets, no live-source dependency, and safe in stored bytes  
**Implementation posture:** path and documented child are CONFIRMED; complete payload inventory and consumer wiring are NEEDS VERIFICATION  
**Evidence snapshot:** `main@d24c7bf9ee89c9bb3bd2cd14e0e60b1de6314bc0`

> [!IMPORTANT]
> `public_safe` is a fixture classification, not a publication state. It is intended to mean the example has been constructed and reviewed so its stored bytes, joins, metadata, geometry, and expected output are suitable for open handling. The label alone does not prove that review occurred, and it never means an analogous real record may be exposed.

> [!WARNING]
> Never copy real source payloads into this lane and then call them synthetic or sanitized. If source-derived or potentially identifying material appears, stop the consumer, preserve evidence of the issue without widening exposure, and route the material through the governed quarantine and correction process.

**Quick navigation:** [Purpose](#purpose) · [Truth and authority](#truth-and-authority-boundary) · [Placement](#placement-basis) · [Inventory](#confirmed-lane-inventory) · [Choose a lane](#choose-the-correct-fixture-lane) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Scenario contract](#minimum-scenario-contract) · [Authoring workflow](#authoring-workflow) · [Review gates](#public-safety-review-gates) · [Consumers](#consumer-obligations) · [Outcomes](#finite-outcome-and-negative-case-matrix) · [Validation](#validation-and-review) · [Maintenance](#maintenance) · [Evidence](#verification-ledger) · [Rollback](#correction-and-rollback)

---

## Purpose

Use this lane for shared examples that need to be safe for open repository review and useful across documentation, renderer smoke checks, governed-API dry-runs, Evidence Drawer and Focus Mode examples, source-role and evidence-resolution checks, citation and policy negative cases, correction exercises, rollback exercises, and deterministic expected-output comparisons.

This parent README has four jobs:

1. define what `public_safe` means for fixtures;
2. route a scenario to the correct fixture home;
3. specify the minimum information needed to review and consume a scenario; and
4. keep fixture behavior separate from source, evidence, policy, proof, release, and publication authority.

Prefer the smallest lane that preserves ownership and review context. If an object family has a clear domain owner, use the domain-owned fixture lane. If a fixture belongs only to one test implementation, use the test-local fixture lane.

[Back to top](#top)

---

## Truth and authority boundary

Fixtures are examples and checking inputs. They can prove that a named consumer behaves as asserted when the exact test or validator is run; they cannot prove that the same assertion is true of the real world or approved for release.

| A public-safe fixture may demonstrate | It does not establish |
|---|---|
| a machine shape or contract example | schema or contract authority |
| a valid, invalid, denied, abstaining, or error path | policy authority or release approval |
| a toy `EvidenceRef` resolving to a toy `EvidenceBundle` | real evidence closure or source admission |
| generalized or invented geometry | permission to expose analogous real geometry |
| drawer, map, Focus Mode, API, or AI presentation behavior | public API, map, tile, UI, or AI truth authority |
| a correction or rollback exercise | an actual correction, withdrawal, or rollback record |
| deterministic expected output | proof pack, receipt, release manifest, or PUBLISHED state |

The KFM lifecycle remains outside this lane:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition. Copying a fixture, passing a test, rendering a map, or returning `ANSWER` does not cross the trust membrane.

[Back to top](#top)

---

## Placement basis

Directory Rules assigns golden, valid, invalid, and synthetic checking inputs to the canonical `fixtures/` responsibility root. It permits `tests/fixtures/` for test-local inputs only when the distinction from root fixtures is documented. This README preserves that split and creates no new root.

| Responsibility | Correct home | Boundary |
|---|---|---|
| Cross-cutting public-safe fixture | `fixtures/public_safe/` | This lane. Use only while no clearer domain or object-family owner applies. |
| Domain-owned reusable fixture | `fixtures/domains/<domain>/` | Preferred when ownership, policy, or sensitivity context is clear. |
| Unit-test-local fixture | `tests/fixtures/<area>/` | Owned by a particular test area; do not duplicate shared fixture authority. |
| Stable expected output | `fixtures/golden/` or an accepted domain-owned golden lane | Still a fixture, not a release or proof. |
| Broad negative/fail-closed example | `fixtures/invalid/` or an accepted domain-owned invalid lane | Keep the expected failure explicit. |
| Semantic meaning | `contracts/` | Fixtures exercise meaning; they do not define it. |
| Machine shape | `schemas/` | Fixtures exercise schemas; they do not become schemas. |
| Allow, deny, restrict, or abstain rules | `policy/` | Fixtures carry expected outcomes; they do not decide policy. |
| Real lifecycle material | `data/` | Never place real RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED material here. |
| Actual receipts, proofs, and release records | Their accepted governance roots | Toy shapes here never become authority-bearing records. |
| Generated CI/build output | `artifacts/` or the accepted output location | Generated output is not fixture authority. |

No ADR is needed for this documentation-only revision because the existing path, responsibility root, and child topology are unchanged.

[Back to top](#top)

---

## Confirmed lane inventory

The following inventory is intentionally bounded. Exact file reads confirmed these documentation surfaces at the evidence snapshot; no exhaustive Git tree or payload inventory was established.

| Lane | Confirmed posture | Routing rule |
|---|---|---|
| [`settlement/`](./settlement/README.md) | Existing shared public-safe settlement child. Its README distinguishes the singular fixture name from the working `settlements-infrastructure` domain slug. | Use for the bounded shared examples described by the child README; prefer the domain lane once ownership and consumers are established. |
| [`../domains/`](../domains/README.md) | Existing domain-owned fixture parent. | Prefer for stable reusable fixtures with a clear domain owner or sensitivity context. |
| [`../archaeology-public-safe/`](../archaeology-public-safe/README.md) | Existing top-level Archaeology compatibility lane, not a child of this directory. | Do not duplicate it here. Follow its freeze, sensitivity, and migration guidance. |
| [`../../tests/fixtures/`](../../tests/fixtures/README.md) | Existing test-local fixture parent with a documented split from root `fixtures/`. | Use only for inputs owned by a particular test area. |

The table is not proof that no other child, ignored file, generated file, Git LFS object, branch-local file, or externally stored corpus exists.

### Relationship to sibling fixture lanes

The root fixture index documents these sibling lanes. They remain separate because size, ownership, or expected outcome—not merely public-safe handling—controls their placement.

| Sibling lane | Relationship to this parent |
|---|---|
| `../slim/` | Preferred for small renderer/runtime fixtures that are not specifically organized as public-safe examples. |
| `../heavy/` | Stress-sized runtime fixtures; requires an explicit storage decision when ordinary review or repository size is affected. |
| `../golden/` | Stable deterministic expected outputs; pair by scenario ID and keep the consumer assertion explicit. |
| `../invalid/` | Broad fail-closed cases without a clearer domain or object-family owner. |
| `../ecology/` | Cross-domain ecology examples; prefer a domain lane when ownership or sensitivity context is clear. |
| `../hydrology/` | Hydrology runtime/staging examples; use the domain lane for stable domain-owned cases. |
| `../infrastructure-generalized/` | Generalized infrastructure examples with stricter review against inference and critical-asset exposure. |
| `../domains/` | Preferred reusable fixture home for a clearly owned domain object or policy context. |

Public-safe construction applies across these lanes when examples are open, but it does not erase the lane's more specific ownership, size, sensitivity, or outcome rules.

[Back to top](#top)

---

## Choose the correct fixture lane

| Question | If yes | If no |
|---|---|---|
| Is the material real source or lifecycle data? | Do not create a fixture copy; use governed source admission and lifecycle handling. | Continue. |
| Does the scenario contain or derive from restricted, identifying, culturally sensitive, infrastructure-sensitive, or exact-location material? | Default to deny/quarantine and require domain, rights, sensitivity, and policy review. | Continue. |
| Is there a clear domain owner? | Use `fixtures/domains/<domain>/` and that lane's stricter rules. | Continue. |
| Is the input owned by one test implementation only? | Use `tests/fixtures/<area>/`. | Continue. |
| Is it a stable expected output? | Pair it in `fixtures/golden/` or an accepted domain golden lane. | Continue. |
| Is it a broad fail-closed example? | Consider `fixtures/invalid/` unless a domain invalid lane owns it. | Continue. |
| Is it a small, cross-cutting, synthetic example safe for open handling? | This parent or an existing child may be appropriate. | Do not place it here. |

If two homes remain plausible, mark placement `NEEDS VERIFICATION` and ask the fixture and domain stewards before adding payloads. Do not solve uncertainty by copying the same scenario into multiple roots.

[Back to top](#top)

---

## Accepted material

This lane may contain compact, reviewable material such as:

- synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.geojson`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- invented identities, references, timestamps, citations, digests, reviewer IDs, policy IDs, release IDs, and geometries with no claimed real-world referent;
- positive and fail-closed cases for source roles, evidence resolution, citations, rights, sensitivity, review, correction, rollback, and release-readiness behavior;
- deterministic renderer, Evidence Drawer, Focus Mode, governed-API, or AI-response examples with explicit finite outcomes; and
- README or scenario notes that identify the consumer, governing references, expected assertion, public-safe rationale, and correction path.

Small source-inspired structures may be recreated only when no source bytes, real identifiers, sensitive coordinate patterns, restricted attributes, or re-identifying combinations are retained. Record the transformation and review basis; if that basis is uncertain, do not place the material here.

[Back to top](#top)

---

## Exclusions

Do not place any of the following in this lane:

- real source exports, live upstream payloads, scraped records, production logs, or copied samples presented as synthetic;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle material;
- real legal, census, tribal/community, historic-site, biological occurrence, land/title, DNA/genomic, health, person, or emergency records;
- exact or reverse-engineerable sensitive geometry, rare-species locations, archaeological locations, sacred or culturally restricted places, private person-land joins, or critical-infrastructure detail;
- secrets, credentials, tokens, private endpoints, private attachments, or unredacted error output;
- actual `SourceDescriptor`, `EvidenceBundle`, receipt, proof pack, policy decision, review approval, release manifest, correction notice, withdrawal notice, or rollback card;
- contracts, schemas, policy rules, validators, executable tests, application code, pipeline logic, or public API/map/tile artifacts; or
- model-generated claims presented as evidence, expected truth, or release authority.

Styling is not redaction. Hiding a label, lowering opacity, limiting zoom, or omitting a field in the UI does not make unsafe stored bytes public-safe.

[Back to top](#top)

---

## Minimum scenario contract

Every durable fixture or scenario bundle should document the fields below in a sibling README, manifest, or clearly named metadata object. The exact machine schema is **PROPOSED** until a contract and schema are accepted; do not present this table as a normative payload schema.

| Field | Minimum content |
|---|---|
| Scenario ID | Stable toy identifier that cannot be mistaken for a source or release ID. |
| Classification | `synthetic`, `public-safe`, and one of `valid`, `invalid`, `negative`, `expected`, or `golden`. |
| Purpose | Behavior or boundary the fixture is intended to exercise. |
| Object/domain owner | Named owner or `NEEDS VERIFICATION` with routing rationale. |
| Public-safe rationale | Why the stored bytes and combined attributes have no sensitive real-world referent. |
| Geometry posture | Invented, generalized, aggregated, withheld, or not applicable; include precision rationale. |
| Rights and sensitivity posture | Review result, reviewer role, and unresolved questions; never infer clearance from synthetic status. |
| Governing references | Existing contract, schema, policy, or doctrine references with their current status. |
| Consumer | Exact test, validator, renderer, API dry-run, UI example, or documentation page; `NEEDS VERIFICATION` if not wired. |
| Expected outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass/failure, renderer assertion, or deterministic output digest. |
| Non-authority statement | Explicitly says the fixture is not source, evidence, policy, proof, release, or real-world truth. |
| Determinism controls | Pinned ordering, timestamps, seeds, precision, locale, serialization, and network posture as applicable. |
| Correction and rollback | How to disable, replace, supersede, or revert the scenario and repair its consumers. |

### Suggested bundle

```text
<scenario-id>/
├── README.md          # purpose, posture, consumer, expected assertion, correction path
├── input.json         # synthetic input
├── expected.json      # deterministic expected result
└── negative.json      # optional fail-closed variant
```

This layout is a **PROPOSED convention**, not a claim about current payload inventory.

[Back to top](#top)

---

## Authoring workflow

1. **Classify the material.** Confirm it is genuinely synthetic and identify any source inspiration, real-world resemblance, domain ownership, rights, sensitivity, sovereignty, or re-identification risk.
2. **Choose the owner.** Apply the routing table above. Do not create a new child merely to avoid a domain or policy review.
3. **Define one behavior.** State the exact consumer and assertion. Split scenarios that mix unrelated gates or expected outcomes.
4. **Construct toy bytes.** Use invented IDs, values, geometry, citations, evidence refs, policy refs, dates, reviewers, digests, and release refs.
5. **Preserve semantic separation.** Keep schema validity, semantic validity, source role, evidence support, citation status, rights, sensitivity, review, policy, release, correction, and rollback independently observable.
6. **Declare the expected outcome.** Name the finite outcome or deterministic assertion and the gate that causes it.
7. **Review public safety.** Inspect stored bytes, metadata, filenames, comments, diffs, joins, expected output, and logs—not only the default rendering.
8. **Validate the consumer.** Run the exact test or validator that loads the fixture. Record the command and result only after it is verified.
9. **Link both directions.** The scenario identifies its consumer; the consumer or its README identifies the scenario.
10. **Plan correction.** State how to stop use, replace bytes, update expected output, repair references, and revert the change.

[Back to top](#top)

---

## Public-safety review gates

| Gate | Pass condition | Fail-closed response |
|---|---|---|
| Real-world referent | Identities and values are invented or proven non-identifying. | Reject or quarantine; do not relabel. |
| Geometry | Stored geometry cannot expose or reconstruct a sensitive location. | Generalize, aggregate, replace with invented geometry, or deny. |
| Join risk | Combining fields, sibling fixtures, or expected output does not re-identify a person, place, asset, community, or protected feature. | Split, reduce, replace, restrict, or deny. |
| Rights and sovereignty | No copied content or authority-bearing representation has unresolved rights, consent, cultural, or sovereignty implications. | Require the applicable reviewer; deny open handling while unresolved. |
| Evidence and citations | Toy refs are visibly synthetic and missing support remains missing. | `ABSTAIN` or validation failure; never fabricate closure. |
| Source roles | Primary, corroborating, contextual, and restricted roles remain distinct when exercised. | Reject source-role collapse. |
| Policy and release | The fixture cannot be mistaken for a real policy or promotion decision. | Rename/restructure or deny the scenario. |
| Secrets and network | No credentials, private URLs, live calls, or hidden network dependency. | Remove exposure and rotate credentials if necessary. |
| Determinism | Repeated runs produce the same relevant result under declared controls. | Pin inputs or classify the scenario as unsuitable for golden comparison. |
| Consumer assertion | The exact consumer and expected result are known and tested. | Mark `NEEDS VERIFICATION`; do not claim implementation coverage. |
| Correction path | Maintainers can disable, replace, and revert the scenario without losing provenance. | Hold adoption until the path is documented. |

Sensitive-domain reviewers may impose stricter gates. Passing this generic table never overrides a domain policy or release decision.

[Back to top](#top)

---

## Consumer obligations

A test, validator, renderer, governed-API dry-run, UI example, or documentation page that consumes this lane should:

- load the fixture by an explicit stable path or manifest entry;
- assert the documented outcome rather than merely checking that parsing succeeds;
- run without live source, model, tile, style, glyph, sprite, or vendor access unless the consumer explicitly tests a mocked boundary;
- keep invalid, denied, abstaining, and error cases distinct from valid cases;
- expose missing evidence, unresolved rights, sensitivity, review, or release gates instead of substituting plausible values;
- avoid presenting the fixture as production data in screenshots, examples, API responses, maps, or generated text;
- preserve source-role and evidence-reference distinctions;
- fail closed when the fixture is missing, malformed, unexpectedly changed, or no longer public-safe; and
- update the input, expected output, assertion, documentation, and correction notes together when behavior intentionally changes.

A fixture with no verified consumer is documentation or backlog material. Label it accordingly; do not count it as test coverage.

[Back to top](#top)

---

## Finite-outcome and negative-case matrix

| Case | Expected posture |
|---|---|
| Toy evidence resolves; policy, sensitivity, review, and release gates represented as passing | Bounded synthetic `ANSWER` or consumer-specific pass; never real release authority. |
| Evidence or citation is missing, stale, invalid, or conflicted | `ABSTAIN` or validation failure with the missing support visible. |
| Rights, sensitivity, sovereignty, or access policy forbids exposure | `DENY`; do not downgrade to a vague warning. |
| Payload, schema binding, identity, or consumer execution is malformed | `ERROR` or explicit validation failure; do not silently coerce. |
| Expected output differs from the reviewed digest or assertion | Fail the comparison and require review of input, behavior, and correction lineage. |
| A previously safe fixture becomes unsafe when joined or reinterpreted | Disable consumers, quarantine or remove unsafe bytes, issue the appropriate correction, and restore the last reviewed scenario. |

The expected outcome must identify the gate responsible. A generic `success: false` or `safe: true` is not enough for trust-significant behavior.

[Back to top](#top)

---

## Validation and review

No single repository command was verified as the runner for every fixture in this parent lane. Validation is therefore consumer-specific.

Before relying on a fixture:

- [ ] verify the target path and current bytes;
- [ ] verify its scenario contract and public-safe rationale;
- [ ] verify every repository-relative link;
- [ ] identify and run the exact consumer test or validator;
- [ ] exercise the documented positive and fail-closed outcome as applicable;
- [ ] confirm deterministic serialization, ordering, timestamps, seeds, precision, and network behavior;
- [ ] inspect stored input, expected output, generated logs, snapshots, and screenshots for leakage;
- [ ] obtain required domain, rights, sensitivity, cultural, sovereignty, infrastructure, or policy review;
- [ ] confirm no consumer treats the fixture as production source, evidence, release, map, tile, or API material; and
- [ ] record the command, commit, result, and unresolved limitations in the PR or scenario note.

Documentation checks can establish Markdown quality and link integrity. They cannot establish fixture safety, consumer correctness, runtime wiring, evidence closure, or release readiness.

[Back to top](#top)

---

## Maintenance

- Keep this file focused on parent routing, shared rules, and evidence boundaries.
- Update the inventory when a child lane is added, moved, frozen, deprecated, or removed.
- Require each stable scenario to identify its exact consumer and expected assertion.
- Move stable domain-owned examples to the owning domain lane through a reviewed change that repairs references and preserves rollback.
- Do not duplicate a scenario across `fixtures/`, `fixtures/domains/`, and `tests/fixtures/`; document a justified split when separate representations are genuinely required.
- Keep payloads small enough for ordinary code review unless an explicit storage decision exists.
- Re-run public-safety review when fields, geometry, joins, consumers, renderers, screenshots, or expected outputs change.
- Treat orphaned, stale, ambiguous, or unreviewed fixtures as `NEEDS VERIFICATION`, not as coverage.
- Record supersession and correction. Do not silently rewrite a stable expected output used by multiple consumers.

### Definition of done for a new durable scenario

- [ ] correct responsibility and domain lane selected;
- [ ] synthetic and public-safe rationale reviewed;
- [ ] minimum scenario contract documented;
- [ ] exact consumer and assertion verified;
- [ ] relevant valid and fail-closed cases executed;
- [ ] deterministic/no-network posture confirmed;
- [ ] rights, sensitivity, join, and geometry gates passed;
- [ ] non-authority boundary visible;
- [ ] correction and rollback path documented; and
- [ ] parent/child indexes and consumer references updated without parallel authority.

[Back to top](#top)

---

## Verification ledger

Evidence was read at `main@d24c7bf9ee89c9bb3bd2cd14e0e60b1de6314bc0`.

| Check | Result | Evidence / limit |
|---|---|---|
| Target README | **CONFIRMED** | Existing blob `7efa4537a55f286a32870c834a1f5e91983b0f19` was read before this revision. |
| Placement under `fixtures/` | **CONFIRMED** | Supplied Directory Rules assigns reusable golden, valid, invalid, and synthetic checking inputs to `fixtures/`. |
| Root fixture boundary | **CONFIRMED** | `fixtures/README.md` separates reusable fixtures from lifecycle data, generated artifacts, authority roots, and test-local fixtures. |
| `tests/fixtures/` split | **CONFIRMED documented posture** | `tests/fixtures/README.md` defines a unit-test-local lane distinct from root fixtures. |
| Settlement child | **CONFIRMED** | `fixtures/public_safe/settlement/README.md` exists and documents the shared singular child. |
| Domain fixture parent | **CONFIRMED path** | `fixtures/domains/README.md` exists; complete child maturity is outside this review. |
| Archaeology compatibility lane | **CONFIRMED adjacent path** | `fixtures/archaeology-public-safe/README.md` exists outside this directory and directs domain-owned work toward the Archaeology domain lane. |
| Complete child and payload inventory | **NOT ESTABLISHED** | Bounded file reads and code search are not an exhaustive tree, history, LFS, ignored-file, generated-file, branch, or external-store inventory. |
| Consumers, validators, tests, and CI | **NEEDS VERIFICATION** | No parent-wide runner or complete wiring map was established. |
| Runtime public-safety enforcement | **NEEDS VERIFICATION** | Documentation defines posture; it does not prove enforcement. |
| Contracts, schemas, policy, release, and public routes changed | **NO** | This revision changes one README only. |

### Open verification register

- Which additional direct children, payloads, generated files, LFS objects, or branch-local fixtures exist under `fixtures/public_safe/`?
- Which exact consumers load each scenario, and what assertions do they make?
- Is a common scenario manifest contract and schema accepted, or should metadata remain README-local?
- Which owners approve generic public-safe fixtures and each sensitive domain override?
- Which CI jobs enforce no-network, deterministic output, link integrity, and leak checks for this lane?
- Which scenarios should move to domain-owned or test-local fixture homes?

[Back to top](#top)

---

## Correction and rollback

If a fixture is discovered to contain real, restricted, identifying, source-derived, rights-conflicted, culturally sensitive, infrastructure-sensitive, or reverse-engineerable material:

1. stop and disable affected consumers and examples;
2. avoid reproducing unsafe bytes in issues, logs, screenshots, or PR descriptions;
3. route the material through the governed quarantine, security, privacy, rights, sensitivity, and correction process appropriate to the risk;
4. identify every consumer, copy, cache, generated artifact, snapshot, and published derivative;
5. replace or remove unsafe material and restore the last reviewed synthetic scenario;
6. record the correction, reviewer, affected scope, and follow-up validation; and
7. rotate credentials or secrets immediately if exposure is involved.

For this README revision, abandon the feature branch before merge or revert the documentation commit after merge. Do not rewrite shared history. The preceding target blob at the evidence snapshot is `7efa4537a55f286a32870c834a1f5e91983b0f19`.

Rollback is mandatory if this lane is described or used as source authority, evidence closure, policy permission, proof, release state, canonical truth, public API data, public map/tile material, or a shortcut around the trust membrane.

<p align="right"><a href="#top">Back to top</a></p>
