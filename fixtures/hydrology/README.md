<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-hydrology-readme
title: fixtures/hydrology/README.md — Hydrology Runtime Fixture Compatibility Boundary
type: readme; directory-readme; hydrology-fixture-compatibility-lane; non-authoritative
version: v0.2
status: draft; repository-grounded; transitional; direct-inventory-bounded; consumer-wiring-unverified; dedicated-validation-unestablished; non-authoritative
owners:
  - "@bartytime4life — verified GitHub CODEOWNER for /fixtures/ review routing"
  - "OWNER_TBD — Hydrology fixture stewardship and compatibility-lane disposition"
created: NEEDS VERIFICATION — file predates this revision
updated: 2026-07-21
supersedes: pre-contract top-level Hydrology runtime fixture README
policy_label: public-doc; fixtures; hydrology; compatibility; transitional; synthetic-only; deterministic; no-network-default; public-safe; source-role-preserving; evidence-aware; sensitivity-aware; release-subordinate; correction-aware; rollback-aware; no-emergency-authority; no-publication
current_path: fixtures/hydrology/README.md
truth_posture:
  CONFIRMED:
    - fixtures/hydrology/README.md exists at the checked base
    - fixtures/ is the repository responsibility root for reusable checking inputs
    - Directory Rules place domain-owned Hydrology fixtures under fixtures/domains/hydrology/
    - fixtures/domains/hydrology/ exists with decision-envelope, evidence-bundle, run-receipt, source, valid, invalid, negative, and golden README lanes
    - tests/fixtures/hydrology/ documents a separate compatibility and test-local scope
    - sampled canonical-domain HUC12 and NFHL JSON fixtures are explicitly PROPOSED placeholders
    - the Hydrology smoke test is an executable placeholder
    - the domain-hydrology workflow checks fixtures/domains/hydrology/ and explicit readiness holds, not this top-level path
    - .github/CODEOWNERS routes /fixtures/ review to @bartytime4life
    - the Makefile fixtures target is TODO-only and the default test target does not execute this lane
  PROPOSED:
    - fixtures/hydrology/ is a transitional compatibility and routing surface, not a second reusable Hydrology fixture authority
    - new domain-owned Hydrology payloads go to fixtures/domains/hydrology/ and new cross-cutting runtime payloads go to the narrowest appropriate shared lane
    - any compatibility pointer retained here names its canonical target, consumer, owner, expiry, expected outcome, and removal path
  UNKNOWN:
    - exhaustive tracked, ignored, generated, and externally stored child inventory; active consumers; compatibility dependencies; branch-protection enforcement; and release dependency
  NEEDS_VERIFICATION:
    - whether any payload besides this README exists under fixtures/hydrology/
    - whether any executable consumer still requires this top-level path
    - accepted semantic owners, migration deadline, deprecation mechanism, and retirement decision
evidence_state_qualifiers:
  CONFLICTED:
    - fixtures/README.md describes fixtures/hydrology/ as a top-level runtime staging lane, while Directory Rules domain placement and the populated fixtures/domains/hydrology/ lane make a second Hydrology fixture authority unsafe
    - the repository contains overlapping Directory Rules documents; CONTRIBUTING.md directs live contribution preflight to docs/architecture/directory-rules.md
  NARROWED:
    - direct inventory and consumer conclusions are bounded to exact connector reads and indexed repository search, not a byte-complete recursive tree walk
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: eac8668ca9786773fcb015f9ba099e0e1dadeb35
  target_prior_blob: dab1a46361cce833d88ed21c453339b006b35a0b
  related_repository_blobs:
    contributing: 935f8bbefd8f966275887c9f58277746b9c67c28
    directory_rules_live_preflight: 18653c00ba193a4afaa3e07a0924452807fb98ef
    fixtures_root_readme: b096b0ed49c8e7d95ddb0d4c813d06ef40f1528d
    fixtures_domain_hydrology_readme: 24e97fe01336e28caf0b87d5ecc82d5b4852479f
    tests_fixtures_hydrology_readme: 393111bde70286f8e5006bd5a00398872a53daae
    hydrology_domain_readme: 57e5662e9481f8590238c21936b5d5e25f5176bb
    hydrology_boundary: e25d76925846b908d182f921503f7857ad64a8b0
    hydrology_domain_workflow: ae95407e2a026115e7ab37019f3a57d622ce7514
    codeowners: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
    makefile: 51537af34ee065c2de571134688415042b83b22a
notes:
  - "This revision changes documentation only."
  - "Hydrology fixtures are synthetic checking inputs, not water truth, regulatory findings, emergency guidance, proof, release authority, or publication material."
  - "README presence, filenames, hashes, fixture parsing, or a passing smoke check do not prove semantic correctness, evidence closure, source admission, policy admissibility, release readiness, or current hydrologic conditions."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `fixtures/hydrology/` — Hydrology runtime fixture compatibility boundary

> **One-line purpose.** `fixtures/hydrology/` is a transitional compatibility and routing lane for legacy top-level Hydrology fixture references; the canonical reusable domain fixture home is [`fixtures/domains/hydrology/`](../domains/hydrology/README.md).

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Class: transitional compatibility" src="https://img.shields.io/badge/class-transitional__compatibility-orange">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-blue">
  <img alt="Inventory: bounded" src="https://img.shields.io/badge/inventory-bounded-orange">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture__only-red">
</p>

> [!IMPORTANT]
> Add reusable Hydrology fixtures to [`fixtures/domains/hydrology/`](../domains/hydrology/README.md), not here. Use this lane only to document or temporarily bridge a verified legacy consumer while its canonical reference is adopted.

> [!CAUTION]
> Hydrology fixture success proves only a bounded synthetic expectation. It does not establish current water conditions, flood extent, forecast accuracy, source admission, regulatory meaning, engineering suitability, evidence closure, policy approval, release readiness, or public safety.

> [!WARNING]
> Never place live gauge readings, real source responses, exact private-well details, critical-infrastructure exposure, person-parcel joins, credentials, operational alerts, evacuation instructions, or other protected or time-sensitive material in this public fixture lane.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs here](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed)

---

## Purpose

This README prevents the top-level path from becoming a second Hydrology fixture authority. It helps maintainers:

- route reusable Hydrology examples to the domain-owned fixture tree;
- distinguish cross-cutting runtime fixtures from domain-owned objects and test-local wrappers;
- identify and retire legacy consumers without silently breaking them;
- preserve source role, temporal role, evidence, rights, sensitivity, release, correction, and rollback boundaries;
- keep NFHL regulatory context separate from observed inundation, forecasts, models, and operational warnings;
- require deterministic, synthetic, public-safe, no-network examples; and
- record what remains unknown when inventory, consumer, validator, or ownership evidence is incomplete.

This lane does not provide a staging shortcut for unsorted Hydrology payloads. Unclear ownership is a reason to pause and classify the fixture, not a reason to create another permanent home.

### Routing rule

| Fixture purpose | Preferred home |
|---|---|
| Reusable Hydrology object, source-role, evidence, receipt, outcome, valid, invalid, negative, or golden case | [`fixtures/domains/hydrology/`](../domains/hydrology/README.md) or its narrowest child |
| Small cross-cutting renderer or runtime smoke input whose Hydrology meaning is incidental | [`fixtures/slim/`](../slim/README.md) |
| Scale-dependent cross-cutting stress corpus | [`fixtures/heavy/`](../heavy/README.md), subject to its admission and storage rules |
| Cross-cutting expected output | [`fixtures/golden/`](../golden/README.md), only when no domain owner applies |
| One-test-only wrapper or parametrization | [`tests/fixtures/hydrology/`](../../tests/fixtures/hydrology/README.md) or the owning test subtree |
| Verified legacy reference to `fixtures/hydrology/` | Temporary pointer or wrapper here, with canonical target and retirement plan |
| Real source, lifecycle, evidence, proof, release, or publication material | Not a fixture; use the governed responsibility root and lifecycle |

[Back to top](#top)

## Authority level

**Compatibility / transitional fixture-routing lane; non-authoritative for Hydrology meaning, machine shape, policy, source admission, evidence, proof, release, current conditions, emergency guidance, and publication.**

The live contribution guide directs placement preflight to [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md). Directory Rules assign reusable domain fixtures to `fixtures/domains/<domain>/` and warn against competing fixture homes. The populated [`fixtures/domains/hydrology/`](../domains/hydrology/README.md) tree therefore carries the reusable Hydrology fixture responsibility. This top-level path remains only as a compatibility surface until its actual inventory and consumers are verified.

> [!NOTE]
> [`fixtures/README.md`](../README.md) currently describes this path as a top-level runtime/staging lane. That repository prose conflicts with the Domain Placement Law and the existing domain-owned fixture tree. This README narrows the top-level path without deleting or moving files. Resolving, migrating, deprecating, or retiring the path remains **PROPOSED / NEEDS VERIFICATION**.

| Responsibility | Owning surface | Boundary for this lane |
|---|---|---|
| Hydrology domain meaning | [`contracts/domains/hydrology/`](../../contracts/domains/hydrology/README.md) | Compatibility fixtures may imitate accepted meaning but never define it. |
| Hydrology machine shape | [`schemas/contracts/v1/domains/hydrology/`](../../schemas/contracts/v1/domains/hydrology/README.md) | Examples may exercise schemas but never become schema authority. |
| Hydrology policy and admissibility | [`policy/domains/hydrology/`](../../policy/domains/hydrology/README.md) and sensitivity policy | Expected denial or abstention does not make a fixture a policy rule. |
| Canonical reusable Hydrology fixtures | [`fixtures/domains/hydrology/`](../domains/hydrology/README.md) | This lane points there; it must not duplicate or supersede it. |
| Executable Hydrology tests | [`tests/domains/hydrology/`](../../tests/domains/hydrology/README.md) | Tests consume fixtures; a fixture is not an assertion. |
| Test-local compatibility wrappers | [`tests/fixtures/hydrology/`](../../tests/fixtures/hydrology/README.md) | Keep one-test-only material there. |
| Source identity and admission | [`data/registry/sources/hydrology/`](../../data/registry/sources/hydrology/README.md) | Synthetic source-shaped examples do not admit or activate sources. |
| Lifecycle data | `data/` phase roots | Fixtures remain outside RAW through PUBLISHED. |
| Proof-bearing records | Accepted evidence, receipt, and proof roots | Fixture-shaped records are synthetic and non-authoritative. |
| Candidate review and release | [`release/candidates/hydrology/`](../../release/candidates/hydrology/README.md) and release authority | A fixture or check never approves promotion or release. |
| Public maps, APIs, exports, and AI | Governed public surfaces | Public clients do not read fixtures as truth. |

The lifecycle invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Fixtures do not enter, shortcut, or substitute for this lifecycle. A commit, pull request, merge, passing check, map render, or generated summary is not KFM publication.

[Back to top](#top)

## Status

| Evidence field | Current bounded result |
|---|---|
| Repository snapshot | `bartytime4life/Kansas-Frontier-Matrix` at `main@eac8668ca9786773fcb015f9ba099e0e1dadeb35` |
| Prior README blob | `dab1a46361cce833d88ed21c453339b006b35a0b` |
| Path existence | **CONFIRMED** — the directory and README exist. |
| Placement class | **PROPOSED / CONFLICTED** — transitional compatibility is the safe classification pending consumer and migration evidence. |
| Canonical reusable domain lane | **CONFIRMED** — `fixtures/domains/hydrology/` and eight documented child families exist. |
| Direct top-level payload inventory | **NARROWED / NEEDS VERIFICATION** — the connector confirmed a directory but did not expose a recursive listing. |
| Indexed top-level consumers | **NOT ESTABLISHED** — bounded indexed search returned no executable reference to `fixtures/hydrology/`. |
| Sampled domain payloads | **CONFIRMED placeholders** — `huc12_kansas_sample.json` and `nfhl_context_sample.json` declare `status: PROPOSED` and placeholder notes. |
| Hydrology smoke test | **CONFIRMED placeholder** — `test_hydrology_smoke.py::test_placeholder` only asserts true. |
| Domain workflow | **CONFIRMED readiness workflow** — read-only PR execution checks domain boundaries and explicit holds; it does not consume this top-level lane. |
| Review route | **CONFIRMED** — `.github/CODEOWNERS` maps `/fixtures/` to `@bartytime4life`; enforcement remains **UNKNOWN**. |
| Fixture regeneration | **CONFIRMED TODO-only** — the root `Makefile` fixture target prints a readiness marker. |
| Dedicated top-level validation | **NOT ESTABLISHED**. |
| Release or public dependency | **UNKNOWN**. |

### Current safe conclusions

- **CONFIRMED:** the target README, canonical domain fixture root, compatibility test-fixture lane, Hydrology boundary docs, contract/schema/policy/test roots, workflow, and review-routing entry exist at the pinned commit.
- **CONFIRMED:** current Hydrology domain CI is readiness-oriented and explicitly disclaims source admission, truth, proof, release, emergency, and publication authority.
- **PROPOSED:** stop admitting new payloads to this top-level lane and treat it as a temporary compatibility router.
- **CONFLICTED:** parent fixture prose permits a top-level Hydrology staging lane, while current Directory Rules direct domain material to `fixtures/domains/hydrology/`.
- **UNKNOWN:** exhaustive child inventory, legacy consumers, ignored or generated files, external stores, required-check significance, and release coupling.
- **NEEDS VERIFICATION:** whether the lane can retire, requires a compatibility window, or must keep a narrowly documented pointer contract.

### Maturity matrix

| Capability | Status | Evidence-bounded conclusion |
|---|---:|---|
| Directory README | `CONFIRMED` | Existing documentation is replaced with the required ordered contract. |
| Compatibility classification | `PROPOSED` | Safe posture; acceptance and migration owner remain unverified. |
| Recursive child inventory | `NOT ESTABLISHED` | No byte-complete listing was available. |
| Active consumers | `NOT ESTABLISHED` | No indexed consumer surfaced. |
| Canonical target | `CONFIRMED` | `fixtures/domains/hydrology/` is present and Directory-Rules-aligned. |
| Migration manifest | `NOT ESTABLISHED` | Required if payloads or consumers are discovered. |
| Redirect or wrapper validator | `NOT ESTABLISHED` | No executable compatibility enforcement was confirmed. |
| Deterministic regeneration | `NOT ESTABLISHED` | Root fixture command is a TODO marker. |
| Dedicated CI collection | `NOT ESTABLISHED` | Broad workflows do not prove this lane is consumed. |
| Hydrology truth authority | `DENIED` | Fixtures never establish real water conditions. |
| Emergency authority | `DENIED` | KFM is not a warning or life-safety system. |
| Release authority | `DENIED` | Fixtures never approve promotion or publication. |

[Back to top](#top)

## What belongs here

Until the lane's inventory and consumers are verified, admission is intentionally narrow:

- this README and other human-readable routing notes required to explain the compatibility boundary;
- a small compatibility manifest that points to one canonical fixture under [`fixtures/domains/hydrology/`](../domains/hydrology/README.md), only when a named executable consumer still requires this path;
- a temporary wrapper whose content is fully synthetic, deterministic, public-safe, no-network, and not duplicated from the canonical fixture;
- deprecation, migration, correction, and retirement notes tied to exact old and new paths;
- expected finite outcome and reason-code notes that help a legacy consumer fail visibly during migration; and
- checksums or immutable target identifiers needed to prove that a pointer resolves to the intended canonical fixture.

### Compatibility admission contract

Every retained item must declare:

| Field | Required meaning |
|---|---|
| `compatibility_id` | Stable toy identifier for the compatibility item. |
| `canonical_fixture_ref` | Exact target under the accepted fixture lane. |
| `consumer` | Exact executable consumer that still requires the old path. |
| `reason` | Why the consumer cannot use the canonical path yet. |
| `owner` | Accountable migration owner; use `OWNER_TBD` only with a review reason. |
| `introduced_at` | Commit or version that created the dependency, when known. |
| `expires_or_reviews_on` | Date or concrete trigger for re-evaluation. |
| `expected_outcome` | Bounded compatibility result such as `PASS`, `ABSTAIN`, `DENY`, or `ERROR`. |
| `source_role` | `synthetic` for the wrapper; any imitated domain role stays explicit and subordinate. |
| `network` | `disabled` by default. |
| `content_hash` | Hash of the canonical target or manifest when identity matters. |
| `uses_real_source_data` | Must be `false`. |
| `authorizes_publication` | Must be `false`. |
| `removal_plan` | Consumer update, verification, and rollback steps. |

An item without a canonical target, real consumer, owner, and removal trigger does not belong here.

[Back to top](#top)

## What does NOT belong here

- New reusable Hydrology fixtures; place them under the narrowest child of [`fixtures/domains/hydrology/`](../domains/hydrology/README.md).
- Unsorted or speculative Hydrology payloads waiting for ownership.
- Copies of canonical domain fixtures, golden outputs, or test-local wrappers.
- Real source exports, live API responses, operational feeds, current observations, production snapshots, caches, logs, or source-registry records.
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle data.
- Actual SourceDescriptors, EvidenceBundles, receipts, proofs, PolicyDecisions, ReviewRecords, release manifests, correction notices, withdrawal notices, or rollback cards.
- Contracts, schemas, policy rules, validators, executable tests, pipelines, connector code, renderer code, API code, UI code, or AI runtime code.
- Generated CI reports, screenshots, flame graphs, rendered tiles, map exports, build products, or public artifacts.
- Live gauge readings, forecasts, flood warnings, advisories, evacuation instructions, navigation guidance, engineering conclusions, insurance determinations, or regulatory decisions.
- NFHL material represented as observed inundation, a forecast, hydraulic-model output, or emergency warning.
- Model outputs represented as observations; aggregates represented as place-level truth; administrative records represented as observed events.
- Exact private-well coordinates, owner or parcel joins, dam internals, intake or levee exposure, restricted water-use detail, credentials, secrets, or private endpoints.
- A mutable remote URL, ambient credential, current-clock dependency, or live-network fallback.
- A second fixture registry, manifest authority, source authority, policy home, proof home, release home, or publication surface.

[Back to top](#top)

## Inputs

Compatibility material may derive only from:

- a verified legacy consumer that still resolves `fixtures/hydrology/`;
- a canonical synthetic fixture under [`fixtures/domains/hydrology/`](../domains/hydrology/README.md);
- accepted semantic contracts and machine schemas referenced by that canonical fixture;
- reviewed source-role, rights, sensitivity, temporal, and policy expectations;
- deterministic generation or normalization notes; and
- a migration decision that preserves correction and rollback.

### Hydrology invariant set

Any compatibility wrapper must preserve these boundaries:

1. **Regulatory is not observed.** FEMA NFHL is regulatory flood context, never observed inundation, forecast, or operational warning.
2. **Context is not emergency authority.** KFM never issues life-safety or evacuation instructions.
3. **Model is not observation.** Reconstructed or modeled hydrographs retain their model role and receipt.
4. **Aggregate is not place-level truth.** Watershed summaries do not become property, parcel, site, or person claims.
5. **Source role never upgrades by join.** Authority, observation, regulatory/context, model, aggregate, administrative, candidate, and synthetic roles stay distinct.
6. **Temporal roles remain separate.** Observed, valid, source, retrieval, release, expiry, stale, correction, and withdrawal times do not collapse.
7. **Evidence resolves before claim-like answers.** A synthetic `ANSWER` case must model `EvidenceRef -> EvidenceBundle` closure; otherwise use `ABSTAIN`, `DENY`, or `ERROR`.
8. **The most restrictive sensitivity posture wins.** Private wells, critical infrastructure, ownership joins, and exact exposure fail closed or generalize.
9. **No-network is the default.** Fixtures never silently call USGS, FEMA, NOAA, state offices, map services, model runtimes, or public release services.
10. **Release stays independent.** A valid fixture, green check, or expected output never creates release state.

### Canonical family routing

| Fixture family | Canonical destination |
|---|---|
| Runtime `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` envelope | [`decision_envelope/`](../domains/hydrology/decision_envelope/README.md) |
| Evidence refs, citations, rights, sensitivity, transforms, checksums, or claim scope | [`evidence_bundle/`](../domains/hydrology/evidence_bundle/README.md) |
| Run identity, provenance, replay, validation refs, or stage outcome | [`run_receipt/`](../domains/hydrology/run_receipt/README.md) |
| Source role, cadence, freshness, source head, rights, sensitivity, or admission example | [`sources/`](../domains/hydrology/sources/README.md) |
| Broad positive-path case | [`valid/`](../domains/hydrology/valid/README.md) |
| Stable fail-closed case | [`invalid/`](../domains/hydrology/invalid/README.md) |
| Draft negative case awaiting precise classification | [`negative/`](../domains/hydrology/negative/README.md) |
| Stable expected output | [`golden/`](../domains/hydrology/golden/README.md) |

[Back to top](#top)

## Outputs

This lane may support only:

- human-readable routing from the old top-level path to a canonical fixture;
- a bounded compatibility pointer or wrapper for a named legacy consumer;
- explicit migration, deprecation, correction, and retirement signals;
- deterministic identity or checksum evidence for a canonical target; and
- finite compatibility outcomes that fail visibly when the canonical target, consumer contract, or safety boundary is missing.

It does not emit or authorize:

- a Hydrology observation or claim;
- source admission, activation, or freshness approval;
- an EvidenceBundle, receipt, proof, PolicyDecision, or ReviewRecord;
- lifecycle promotion;
- a map layer, tile set, API response, AI answer, emergency message, or public export;
- release, deployment, publication, correction execution, or rollback execution; or
- production-capacity, regulatory, engineering, insurance, navigation, or life-safety conclusions.

Generated comparison reports or migration diagnostics belong in accepted temporary or non-authoritative artifact locations. They do not become fixtures, proofs, or releases merely because a workflow produced them.

[Back to top](#top)

## Validation

### Current executable boundary

- The root `make fixtures` target is a TODO readiness marker and does not regenerate or validate this lane.
- The root `make test` target runs configured schema and contract tests, not this top-level directory.
- [`domain-hydrology.yml`](../../.github/workflows/domain-hydrology.yml) uses a read-only token and performs static readiness checks plus explicit holds.
- That workflow requires the canonical domain fixture README and parses two sampled placeholder JSON files under `fixtures/domains/hydrology/valid/`; it does not reference this top-level path.
- The Hydrology smoke test contains `test_placeholder`, so the workflow treats executable Hydrology validation as not established.
- The documentation build and link-check workflows are explicit readiness holds. A green held job does not prove this README rendered or its links were checked.
- No dedicated compatibility-pointer validator, recursive inventory check, orphan detector, migration check, or consumer-backlink gate was confirmed.

### Required compatibility checks

1. **Inventory:** enumerate every tracked, ignored, generated, and externally stored child.
2. **Consumer graph:** identify every inbound reference, executable consumer, generated mirror, and documentation backlink.
3. **Canonical target:** require each retained item to resolve to one exact canonical fixture.
4. **No duplication:** compare hashes and semantics so compatibility wrappers do not become divergent copies.
5. **Synthetic-only:** reject real observations, source responses, identities, sensitive locations, and operational material.
6. **No-network:** fail if a loader reaches a live source, map service, model runtime, public API, or release service.
7. **Role separation:** reject NFHL-as-observed, model-as-observation, aggregate-as-place, or alert-authority collapse.
8. **Temporal separation:** reject collapsed observed, valid, retrieval, release, expiry, stale, and correction times.
9. **Evidence and policy:** require synthetic closure for claim-like `ANSWER`; otherwise return a finite fail-closed outcome.
10. **Backlinks:** canonical target and consumer both reference the compatibility manifest; reject orphan pointers.
11. **Expiry:** fail or alert when an owner, review date, migration target, or retirement trigger is missing or stale.
12. **Non-vacuity:** zero collected cases, all skipped cases, missing targets, or unsupported consumers are not success.
13. **Correction and rollback:** prove replacement and reversion leave consumers visibly correct or fail closed.
14. **Retirement:** after consumers migrate, remove the compatibility item through a reviewed, history-preserving change.

### Outcome vocabulary

| Vocabulary | Meaning here | Boundary |
|---|---|---|
| `PASS` | Compatibility pointer or wrapper satisfies its bounded test contract. | Does not mean a Hydrology claim is true. |
| `ANSWER` | Synthetic runtime example models evidence-resolved, policy-allowed output. | Does not create a real answer or release. |
| `ABSTAIN` | Evidence, identity, temporal, freshness, citation, or review support is insufficient. | Preferred over guessing. |
| `DENY` | Source role, policy, rights, sensitivity, emergency, precision, or release boundary blocks exposure. | Fail-closed governance outcome. |
| `ERROR` | Fixture, pointer, loader, schema, or runtime setup is malformed, missing, nondeterministic, or network-dependent. | Operational failure, not policy denial. |

Do not collapse test pass/fail, runtime outcomes, policy decisions, review states, release states, and lifecycle states into one status field.

### README validation performed for this revision

- Verified one H1 and the twelve required directory-README H2 headings in the mandated order.
- Verified every repository-relative file link used by the revision against the pinned base.
- Checked balanced fenced blocks, unique heading anchors, final newline, and absence of trailing whitespace.
- Reviewed the proposed content for secrets, private data, exact sensitive locations, live hydrologic data, and new external dependencies.
- Compared the remote branch against the pinned base and required exactly one changed path.
- Did not claim fixture regeneration, recursive inventory, consumer execution, live-source access, Hydrology correctness, or release validation.

[Back to top](#top)

## Review burden

`.github/CODEOWNERS` routes `/fixtures/` changes to `@bartytime4life`. This is a verified GitHub review route, not proof of semantic ownership, independent review, completed approval, or branch-protection enforcement.

Review should cover every materially affected responsibility:

- fixture stewardship for placement, compatibility, deterministic identity, and retirement;
- Hydrology domain stewardship for object meaning and source-role boundaries;
- the exact consumer owner for any retained wrapper;
- schema and contract owners when a fixture claims conformance;
- source, evidence, policy, rights, sensitivity, temporal, and release reviewers when those concerns appear;
- security review for archive, decompression, parser, path, network, credential, or generated-output risk;
- privacy, land, infrastructure, or groundwater review for precise wells, ownership joins, or critical exposure; and
- Hazards or emergency-boundary review for flood, warning, or life-safety-adjacent cases.

| Change class | Minimum review concern |
|---|---|
| README-only clarification | Fixture and Hydrology documentation boundary. |
| New compatibility pointer | Consumer owner, canonical target, expiry, no-duplication, and removal plan. |
| New synthetic wrapper | Fixture, consumer, Hydrology, reproducibility, no-network, rights, and sensitivity review. |
| New source-role or NFHL case | Hydrology source-role and policy review; negative counterpart required. |
| New private-well or infrastructure case | Sensitivity and security review; use generalized synthetic values only. |
| Expected outcome change | Contract, consumer, policy, and evidence rationale plus rollback target. |
| Path migration or retirement | Complete inventory, reference update, compatibility window, drift/migration note, and rollback. |
| Release-gating use | Separate release authority and independently reviewed failure behavior. |

Do not preserve a legacy path merely for symmetry, and do not retire it merely because indexed search was empty. Both decisions require a complete enough consumer and inventory audit.

[Back to top](#top)

## Related folders

| Path | Relationship |
|---|---|
| [`fixtures/README.md`](../README.md) | Parent fixture-root scope; currently contains the conflicting top-level staging description. |
| [`fixtures/domains/hydrology/README.md`](../domains/hydrology/README.md) | Canonical reusable Hydrology fixture root and family index. |
| [`fixtures/domains/hydrology/decision_envelope/`](../domains/hydrology/decision_envelope/README.md) | Bounded runtime outcome examples. |
| [`fixtures/domains/hydrology/evidence_bundle/`](../domains/hydrology/evidence_bundle/README.md) | Synthetic evidence-support examples. |
| [`fixtures/domains/hydrology/run_receipt/`](../domains/hydrology/run_receipt/README.md) | Synthetic governed-run provenance examples. |
| [`fixtures/domains/hydrology/sources/`](../domains/hydrology/sources/README.md) | Synthetic source-role and admission-posture examples. |
| [`fixtures/domains/hydrology/valid/`](../domains/hydrology/valid/README.md) | Broad positive-path examples. |
| [`fixtures/domains/hydrology/invalid/`](../domains/hydrology/invalid/README.md) | Stable fail-closed examples. |
| [`fixtures/domains/hydrology/negative/`](../domains/hydrology/negative/README.md) | Draft negative-path staging. |
| [`fixtures/domains/hydrology/golden/`](../domains/hydrology/golden/README.md) | Domain-owned expected outputs. |
| [`fixtures/slim/README.md`](../slim/README.md) | Small cross-cutting runtime fixtures when Hydrology ownership is incidental. |
| [`fixtures/heavy/README.md`](../heavy/README.md) | Scale-dependent cross-cutting stress inputs. |
| [`fixtures/golden/README.md`](../golden/README.md) | Cross-cutting expected outputs when no domain owner applies. |
| [`tests/fixtures/hydrology/README.md`](../../tests/fixtures/hydrology/README.md) | Compatibility and test-local Hydrology wrappers. |
| [`tests/domains/hydrology/README.md`](../../tests/domains/hydrology/README.md) | Executable domain test boundary. |
| [`docs/domains/hydrology/README.md`](../../docs/domains/hydrology/README.md) | Domain scope, object families, source roles, sensitivity, publication, and open verification. |
| [`docs/domains/hydrology/BOUNDARY.md`](../../docs/domains/hydrology/BOUNDARY.md) | Regulatory/observed, alert-authority, cross-lane, and deny-by-default boundaries. |
| [`contracts/domains/hydrology/README.md`](../../contracts/domains/hydrology/README.md) | Semantic Hydrology contract index. |
| [`schemas/contracts/v1/domains/hydrology/README.md`](../../schemas/contracts/v1/domains/hydrology/README.md) | Machine-shape index. |
| [`policy/domains/hydrology/README.md`](../../policy/domains/hydrology/README.md) | Domain policy home. |
| [`data/registry/sources/hydrology/README.md`](../../data/registry/sources/hydrology/README.md) | Governed source-registry boundary. |
| [`release/candidates/hydrology/README.md`](../../release/candidates/hydrology/README.md) | Pre-publication candidate review boundary. |
| [`domain-hydrology.yml`](../../.github/workflows/domain-hydrology.yml) | Current read-only readiness workflow and explicit holds. |
| [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md) | Live contribution-preflight placement and required README contract. |
| [`docs/registers/DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) | Drift register; no entry for this top-level/domain fixture conflict was found at the evidence snapshot. |

[Back to top](#top)

## ADRs

No accepted ADR authorizing `fixtures/hydrology/` as a second reusable domain fixture home was established. The bounded evidence instead supports the existing Directory Rules placement under `fixtures/domains/hydrology/`.

Relevant Hydrology ADR files are present but remain draft/proposed:

| ADR | Current status at the evidence snapshot | Relevance |
|---|---|---|
| [`ADR-0009 — Hydrology Is the First Proof-Bearing Lane`](../../docs/adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md) | `draft` / `proposed`; ADR number conflict and acceptance remain unresolved | Proposes sequencing and acceptance gates; does not prove implementation or authorize this compatibility path. |
| [`ADR-0026 — Hydrology source spine starts with WBD HUC12`](../../docs/adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md) | `draft` / `proposed`; number and acceptance need verification | Proposes the first canonical domain fixture under `fixtures/domains/hydrology/`; does not authorize live source use or this top-level lane. |

The repository also contains overlapping Directory Rules documents. [`CONTRIBUTING.md`](../../CONTRIBUTING.md) directs live contribution preflight to `docs/architecture/directory-rules.md`; this README follows that instruction without claiming the document-identity conflict is resolved.

An accepted ADR or equally explicit governed migration decision is required before a change:

- creates or ratifies a parallel Hydrology fixture authority;
- changes the canonical domain placement rule;
- establishes a new schema, contract, policy, source-registry, proof, release, or publication home;
- changes the lifecycle, trust membrane, source-role, emergency, or public-path invariant;
- turns compatibility pointers into a permanent mirror authority; or
- changes object meaning rather than supplying a synthetic example.

Routine README correction and removal of an unused compatibility wrapper may use a focused reviewed change when complete inventory and consumer evidence show no invariant or authority change. Any actual move must preserve history, references, tests, validation, correction, and rollback.

[Back to top](#top)

## Last reviewed

| Field | Value |
|---|---|
| Review date | `2026-07-21` |
| Evidence base | `main@eac8668ca9786773fcb015f9ba099e0e1dadeb35` |
| Review scope | Target README; fixture parent and canonical Hydrology fixture family READMEs; test-local fixture and domain-test guidance; Hydrology domain and boundary docs; contracts, schemas, policy, source-registry, candidate, ADR, drift, contribution, CODEOWNERS, Makefile, and workflow evidence; exact placeholder payload/test reads; bounded indexed searches. |
| Inventory limit | No byte-complete recursive top-level directory listing, ignored-file inventory, external-store inventory, branch-protection proof, runtime trace, or release dependency graph was available. |
| Next scheduled review | By `2027-01-21`, or earlier on any trigger below. |

Review this README immediately when:

- any payload, pointer, wrapper, manifest, consumer, generator, validator, or workflow begins using this path;
- a canonical Hydrology fixture or family changes location or identity;
- the parent fixture README resolves the top-level/domain placement conflict;
- a migration, deprecation, redirect, or retirement decision is accepted;
- NFHL, observed flood, model, forecast, warning, well, infrastructure, parcel, rights, or sensitivity posture changes;
- CI begins collecting this lane, stops collecting it, reports zero cases, or changes required-check status;
- a Hydrology ADR is accepted, superseded, renumbered, or rejected; or
- six months pass without a documented review.

### Correction, migration, and rollback

For a documentation-only revision, rollback is a transparent revert of the scoped commit. If compatibility material exists:

1. identify the exact item, consumer, canonical target, hashes, and affected revisions;
2. stop unsafe or ambiguous consumers from resolving the item;
3. quarantine prohibited real, sensitive, rights-unclear, or operational material through the appropriate governed incident path;
4. restore the last reviewed synthetic wrapper or fail closed if none is safe;
5. update the canonical fixture, compatibility pointer, consumer, expected outcome, and backlinks together;
6. record the correction reason, source-role and temporal impact, and retirement state;
7. rerun deterministic, no-network, role-separation, evidence, policy, sensitivity, and nonempty-collection checks; and
8. remove the compatibility item only after consumer migration and rollback are verified.

Do not rewrite shared history or delete external objects casually. If secrets, protected data, exact sensitive locations, or live operational content enter Git history, stop normal fixture work and use the repository's security, credential-revocation, legal, and incident-response procedures.

### Open verification register

| Item | Status | Closure evidence |
|---|---|---|
| Complete top-level child inventory | `NEEDS VERIFICATION` | Byte-complete recursive listing plus ignored, generated, LFS, and external-store review. |
| Active consumers and inbound references | `NEEDS VERIFICATION` | Complete code, workflow, docs, generated-source, and runtime dependency graph. |
| Compatibility classification acceptance | `NEEDS VERIFICATION` | Fixture and Hydrology steward approval plus parent README reconciliation. |
| Migration or retirement owner and deadline | `NEEDS VERIFICATION` | Accepted stewardship record and dated migration plan. |
| Canonical target for every retained item | `NEEDS VERIFICATION` | Manifest and remote hash validation. |
| No-duplication and deterministic identity | `NEEDS VERIFICATION` | Clean no-network regeneration or pointer-resolution checks with matching hashes. |
| Source-role and NFHL denial coverage | `NEEDS VERIFICATION` | Collected negative tests with expected reason codes. |
| Temporal-role and stale-state coverage | `NEEDS VERIFICATION` | Collected tests preserving observed, valid, retrieval, release, expiry, and correction time. |
| Rights, sensitivity, well, and infrastructure safeguards | `NEEDS VERIFICATION` | Reviewed synthetic fixtures and fail-closed policy/test evidence. |
| Dedicated compatibility validation | `NEEDS VERIFICATION` | Named CI job rejects orphan, duplicate, missing target, network use, zero collection, and expired wrapper. |
| Semantic ownership and required review | `NEEDS VERIFICATION` | Accepted owner assignments and verified branch-protection behavior. |
| Release or public dependency | `UNKNOWN` | Accepted release contract or consumer inventory proving presence or absence. |

[Back to top](#top)
