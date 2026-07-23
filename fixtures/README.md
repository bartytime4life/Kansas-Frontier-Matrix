<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-readme
title: fixtures/ — Canonical Reusable Fixture Root
type: README
version: v0.1
status: draft; repository-grounded; canonical-reusable-fixture-root; mixed-maturity; no-network-default; non-authoritative
owner: NEEDS VERIFICATION — CODEOWNERS routes /fixtures/ to @bartytime4life; no accepted fixture steward, required-review enforcement, or independent approval control was verified
created: NEEDS VERIFICATION — the file predates this first versioned documentation contract
updated: 2026-07-23
supersedes: prior documentation at the same path; no fixture payload, validator, test, workflow, schema, policy, release object, or runtime behavior is superseded
policy_label: repository-facing; fixtures; deterministic; synthetic; public-safe; no-network-default; fail-closed; correction-aware; rollback-aware; non-publisher
owning_root: fixtures/
responsibility: own reusable cross-cutting fixture corpora and expected outputs shared by tests, validators, pipelines, runtime smoke checks, documentation examples, and bounded release-governance dry-runs
truth_posture: cite-or-abstain; a fixture result supports only its declared consumer and expected condition and never proves source authority, claim truth, evidence closure, policy approval, release, publication, or production parity
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 005aa64f6d42aa5961646e733289a2b857292357
  prior_blob: b096b0ed49c8e7d95ddb0d4c813d06ef40f1528d
  directory_rules_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  tests_readme_blob: 55ac53c6c08f9a2b77149645d0a22de3ea680732
  tests_fixtures_readme_blob: 2d0147e85eae86f687e85c5bea0d3e61f9c3a8f7
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  makefile_blob: 51537af34ee065c2de571134688415042b83b22a
  validator_inventory_blob: f734a3e0944346bf2635fb9188702f13b45c8a64
related:
  - ../CONTRIBUTING.md
  - ../docs/architecture/directory-rules.md
  - ../.github/CODEOWNERS
  - ../tests/README.md
  - ../tests/fixtures/README.md
  - ../contracts/README.md
  - ../schemas/README.md
  - ../policy/README.md
  - ../tools/validators/README.md
  - ../release/README.md
  - ../data/README.md
  - ../artifacts/README.md
notes:
  - "This is a same-path Markdown modernization. It creates no sibling README, root, authority surface, fixture payload, release object, or publication state."
  - "Directory Rules §15 controls the required canonical-root README section order."
  - "The root fixture split is explicit: fixtures/ owns reusable cross-cutting examples; tests/fixtures/ owns test-local examples."
  - "make fixtures is a readiness marker that prints TODO output; it is not a fixture validator or regeneration proof."
  - "Existing child documentation may contain inherited renderer terminology that is not normalized by this one-file change. New renderer-specific fixture work must follow current Directory Rules and accepted ADRs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `fixtures/` — Canonical Reusable Fixture Root

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: canonical reusable fixture root](https://img.shields.io/badge/authority-canonical%20reusable%20fixture%20root-1f6feb?style=flat-square)](#authority-level)
[![Network: denied by default](https://img.shields.io/badge/network-denied%20by%20default-15803d?style=flat-square)](#validation)
[![Scope: synthetic and public-safe](https://img.shields.io/badge/scope-synthetic%20%26%20public--safe-8250df?style=flat-square)](#what-belongs-here)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)

> **One-line purpose.** `fixtures/` owns reusable, deterministic, synthetic or public-safe examples and expected outputs that multiple tests, validators, pipelines, runtime smoke checks, and documentation surfaces can consume without the fixture tree becoming truth, policy, evidence, release, or publication authority.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related roots](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed)

> [!IMPORTANT]
> A fixture is a **controlled carrier for a bounded check**. It may demonstrate a positive path, rejection, abstention, denial, hold, stale state, correction, rollback, or expected output. It does **not** establish source authority, claim truth, EvidenceBundle closure, policy approval, review approval, release state, public safety, production behavior, or KFM publication.

> [!CAUTION]
> Default fixture use is local and **no-network**. Live source, API, tile, model, vendor, or public-service probes require a separately governed integration or watcher workflow. They must not be disguised as ordinary fixture validation.

---

## Purpose

`fixtures/` is KFM's canonical responsibility root for **reusable fixture material**. It answers a bounded operational question:

> What compact, deterministic, reviewable input or expected output can be shared across multiple consumers to exercise a declared contract, schema, policy boundary, validator, pipeline, runtime envelope, renderer surface, release prerequisite, correction path, or rollback condition?

This root serves fixture authors, validator and test maintainers, pipeline owners, application and runtime teams, domain stewards, policy and sensitivity reviewers, documentation authors, and reviewers who need reproducible examples without importing real lifecycle material into the repository's checking surface.

A useful fixture should make these points inspectable:

- the scenario and object family under exercise;
- the intended consumer or consumers;
- whether the example is valid, invalid, denied, abstained, held, quarantined, stale, error-producing, correction-bearing, rollback-bearing, or golden output;
- which schema, contract, policy, validator, test, pipeline, or runtime boundary applies;
- the expected finite outcome and failure interpretation;
- the rights, sensitivity, temporal, spatial, and public-safety posture when material;
- the deterministic generation or authoring method;
- what a passing check proves and what it explicitly does not prove.

[Back to top](#top)

---

## Authority level

| Field | Authority |
|---|---|
| **Directory class** | **Canonical, validation-supporting root** |
| **Primary responsibility** | Reusable cross-cutting fixture corpora and expected outputs |
| **May own** | Synthetic or public-safe inputs, valid and invalid examples, deny/abstain/hold/error cases, compact benchmark corpora, golden outputs, deterministic generation notes, and fixture-lane READMEs |
| **Must not own** | Semantic contracts, canonical schemas, executable policy, source registries, lifecycle data, real evidence records, canonical receipts or proofs, review approvals, release decisions, public artifacts, application code, or runtime authority |
| **Public-path posture** | **DENY direct public use.** Fixtures may support documentation or smoke checks, but clients must consume governed APIs and released artifacts rather than fixture paths |
| **Promotion posture** | A fixture may support a validation or promotion prerequisite; it is never a `PromotionDecision`, review approval, release manifest, or publication event |
| **Truth posture** | Cite or abstain; fixture success is bounded evidence about the declared check only |

Directory Rules place a file by **primary responsibility**, not topic. The existing path `fixtures/README.md` is correctly placed because `fixtures/` owns reusable deterministic examples. This same-path documentation update creates no root, moves no path, changes no lifecycle phase, and requires no ADR.

### Fixture-home split

KFM currently uses two fixture homes with a strict responsibility split:

| Home | Owns | Guardrail |
|---|---|---|
| `fixtures/` | Reusable cross-cutting fixtures and expected outputs shared by multiple tests, validators, pipelines, runtime checks, or documentation surfaces | Do not duplicate test-local material or become a second schema, policy, evidence, release, or data authority |
| [`tests/fixtures/`](../tests/fixtures/README.md) | Small fixtures whose ownership and use are local to a particular test area | Do not harden into the reusable cross-cutting fixture registry |

When an example begins local to one test and later gains multiple consumers, move it through a reviewed change, repair references, preserve expected outcomes, and document the migration. Do not copy it into both homes and allow the copies to diverge.

### Responsibility boundary

| Responsibility | Authority home | Role of `fixtures/` |
|---|---|---|
| Semantic meaning and invariants | [`contracts/`](../contracts/README.md) | Exercise examples; never redefine meaning |
| Machine-checkable shape | [`schemas/`](../schemas/README.md) | Supply valid and invalid inputs; never become schema authority |
| Admissibility, rights, sensitivity, and access | [`policy/`](../policy/README.md) | Exercise reviewed rules or explicit mocks; never approve exposure |
| Reusable validator implementation | [`tools/validators/`](../tools/validators/README.md) | Supply deterministic inputs and expected diagnostics |
| Authored enforceability proof | [`tests/`](../tests/README.md) | Be consumed by tests; never substitute for assertions |
| Test-local examples | [`tests/fixtures/`](../tests/fixtures/README.md) | Stay separate unless a reviewed migration establishes cross-cutting reuse |
| Lifecycle material and source records | [`data/`](../data/README.md) | Use synthetic or public-safe representations only; never store real lifecycle state |
| Release, correction, withdrawal, and rollback decisions | [`release/`](../release/README.md) | Exercise dry-run shapes and denial paths only; never authorize or reverse real state |
| Temporary generated QA output | [`artifacts/`](../artifacts/README.md) | Remain separate; generated artifacts are not fixture authority |

> [!WARNING]
> `fixtures/` must not become a parallel contract, schema, policy, source registry, data store, receipt store, proof store, release system, application, renderer, AI runtime, or publication root.

[Back to top](#top)

---

## Status

Snapshot: `main@005aa64f6d42aa5961646e733289a2b857292357`, inspected on 2026-07-23.

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| `fixtures/README.md` | **CONFIRMED** at prior blob `b096b0ed49c8e7d95ddb0d4c813d06ef40f1528d`; this revision is the first versioned root contract | The root README exists and is modernized in place |
| Root/`tests` fixture split | **CONFIRMED** in [`tests/README.md`](../tests/README.md) and [`tests/fixtures/README.md`](../tests/fixtures/README.md) | Reusable and test-local fixtures have distinct responsibilities |
| Contract fixture lane | **CONFIRMED** through [`fixtures/contracts/v1/README.md`](contracts/v1/README.md) | Versioned contract fixture families exist and are organized around schema-backed examples and snapshots |
| Aggregate fixture-backed validators | **CONFIRMED configured** in [`tools/validators/_common/run_all.py`](../tools/validators/_common/run_all.py) | Six top-level validators run in `--fixtures` mode; this is partial coverage, not a complete fixture suite |
| `make schemas` | **CONFIRMED command-bearing** in the [`Makefile`](../Makefile) | Runs the configured aggregate fixture-backed validators |
| `make validate` | **CONFIRMED partial aggregate** in the [`Makefile`](../Makefile) | Runs `make schemas` plus narrow schema/contract tests; it is not a full repository suite |
| `make fixtures` | **CONFIRMED readiness marker only** in the [`Makefile`](../Makefile) | Prints `TODO: regenerate deterministic fixtures`; zero exit is not regeneration or validation evidence |
| Top-level lane inventory | **PARTIALLY CONFIRMED** from the prior README, current child README fetches, and repository search | The navigation table below is useful but is not a complete recursive tree listing |
| Fixture payload inventory | **UNKNOWN / incomplete** | This README does not claim every fixture payload, consumer, schema binding, or expected output was inspected |
| Live-network fixture tier | **UNKNOWN / not established as a root contract** | Default remains no-network; any live tier requires explicit workflow, permissions, source, rights, and failure controls |
| Required checks and branch protection | **NEEDS VERIFICATION** | File and workflow presence do not prove ruleset enforcement |
| Release, publication, and production parity | **DENIED as inference** | Fixture and test presence cannot establish operational release or public state |

### Material corrections in this revision

- Adds the confirmed `contracts/v1/` lane to the root navigation surface.
- Reorganizes the README into the Directory Rules §15 canonical-root section order.
- Makes the reusable-root versus test-local fixture split explicit and links both sides.
- Replaces generic validation language with repository-grounded commands and scope limits.
- States clearly that `make fixtures` is a non-enforcing readiness marker.
- Uses the live Directory Rules cross-reference at [`docs/architecture/directory-rules.md`](../docs/architecture/directory-rules.md); the duplicate Directory Rules identity/path question remains unresolved outside this file.
- Narrows renderer wording: new renderer-specific fixture work must follow current Directory Rules and accepted ADRs. Existing child README references to retired or disputed renderer terminology are inherited drift and remain **NEEDS VERIFICATION**; this one-file change does not move or delete them.

[Back to top](#top)

---

## What belongs here

This root may contain compact, deterministic, reviewable material such as:

- synthetic or public-safe `*.json`, `*.jsonl`, `*.geojson`, `*.yaml`, `*.yml`, `*.svg`, `*.md`, tile, raster, vector, or bounded binary fixture examples when repository review remains practical;
- valid, invalid, positive, negative, denied, abstained, held, stale, error, correction, rollback, and golden expected-output cases;
- toy `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `PolicyDecision`, review, receipt, manifest, runtime-envelope, drawer-payload, Focus Mode, map-layer, correction, and rollback shapes;
- small renderer and governed-API smoke inputs that contain no live endpoint dependency and no sensitive exact geometry;
- deterministic expected outputs paired with stable inputs;
- metadata and generation notes that identify purpose, consumer, rights posture, sensitivity posture, generation method, source note where applicable, and expected outcome;
- README files that define fixture-lane scope, ownership, consumer relationships, and verification limits.

### Scenario families

| Scenario family | Expected posture | Minimum documentation |
|---|---|---|
| Valid / positive | Validation or behavior pass | Governing schema/contract/policy, consumer, and what the pass proves |
| Invalid / negative | Deterministic validation or behavior failure | Expected diagnostic, failure class, and no unsafe fallback |
| Denied / restricted | `DENY` or restricted output | Policy reason or mock boundary; no sensitive payload leakage |
| Abstained / unsupported | `ABSTAIN` | Missing, stale, conflicted, or out-of-scope support made explicit |
| Held / quarantined | `HOLD`, review-required, or quarantine posture | Unresolved rights, sensitivity, identity, quality, or review reason |
| Stale / superseded | Stale-state or supersession handling | Source/release time, replacement reference, and expected UI/runtime state |
| Error | `ERROR` or system failure | Stable failure injection, safe diagnostic, and no allow-on-error path |
| Correction / rollback | Corrected, withdrawn, or prior-state restoration path | Lineage, expected target, and reversibility boundary |
| Golden / expected output | Deterministic comparison artifact | Input pairing, normalization rules, and update procedure |

### Current top-level navigation inventory

The lanes below are carried forward from the prior root README, with `contracts/v1/` added from current repository evidence. This table is a routing aid, not proof of complete payload, validator, test, workflow, or release coverage.

| Lane | Purpose | Expected posture |
|---|---|---|
| `slim/` | Small runtime and renderer smoke inputs, governed-API dry-runs, Evidence Drawer and Focus Mode examples, and lightweight performance checks | Synthetic, compact, public-safe, bounded output |
| `heavy/` | Larger public-safe runtime or benchmark stress corpora when `slim/` is insufficient | Synthetic stress input; explicit storage and review decision required |
| `valid/` | Broad positive-path examples not yet routed to a stable object or domain owner | Validation pass or bounded positive outcome |
| `invalid/` | Broad fail-closed examples not yet routed to a stable object or domain owner | Validation failure, `ABSTAIN`, `DENY`, `ERROR`, or review-required outcome |
| `golden/` | Stable synthetic expected outputs paired with input fixtures | Deterministic expected output; not proof or release |
| `public_safe/` | Public-safe documentation and runtime examples | Generalized, redacted, bounded, or finite governed output |
| `public_safe/settlement/` | Public-safe synthetic settlement-side examples | Generalized examples only; not municipal, census, historic-site, land, infrastructure, or release authority |
| `synthetic/` | Synthetic compatibility examples before ownership is clear | Temporary routing surface; move to stable object/domain lane when ownership is established |
| `synthetic/people-dna-land/` | Toy People/DNA/Land compatibility cases | Deny-first, public-safe, synthetic-only, fail-closed |
| `contracts/v1/` | Versioned contract-family fixtures used by schema harnesses and related checks | Valid/invalid schema examples and bounded snapshots; never contract or schema authority |
| `release/` | Synthetic release-governance dry-runs | Candidate and denial examples only; not release state |
| `release/promotion_decision/` | Synthetic `PromotionDecision` family and its positive/negative cases | Approve/deny/abstain examples; never promotion authority |
| `infrastructure-generalized/` | Generalized infrastructure runtime cases | Public-safe, synthetic context only |
| `hydrology/` | Hydrology compatibility/runtime staging examples | Defer stable domain-owned cases to `domains/hydrology/` |
| `ecology/` | Cross-domain ecology examples | Public-safe synthetic ecology; domain lane preferred when ownership is clear |
| `fauna/` | Fauna compatibility/staging examples | Public-safe synthetic fauna; domain lane preferred when ownership is clear |
| `generated_receipt/` | Generated-receipt shape and validator examples | Fixture representations only; not canonical receipt storage |
| `domains/` | Domain-owned fixture roots | Preferred home when object ownership, policy context, or sensitivity context is clear |

### Shared fixture design contract

- Keep fixtures synthetic, compact, deterministic, reviewable, and public-safe.
- Prefer `slim/` before `heavy/` unless the scenario genuinely requires a larger corpus.
- Prefer an object-family or domain-specific lane when ownership is clear.
- Use toy identifiers, references, geometry, timestamps, hashes, people, organizations, places, and narrative text.
- Keep schema validity, semantic validity, evidence resolution, citation validity, rights, sensitivity, source role, temporal validity, policy result, release posture, runtime behavior, UI rendering, correction, rollback, replay, and expected-output state distinct.
- Pair stable inputs with deterministic expected outputs when practical.
- Record normalization rules before updating a golden output.
- Do not use client-side hiding as protection for sensitive geometry or fields; transform, generalize, redact, withhold, or deny before fixture delivery.
- Do not treat recurrence, realism, visual polish, or a passing check as authority.

[Back to top](#top)

---

## What does NOT belong here

| Excluded material | Correct responsibility home or action |
|---|---|
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED material | The correct governed phase under [`data/`](../data/README.md) |
| Real source exports, live upstream payloads, or source-registry authority | Governed source intake and `data/registry/`; quarantine when rights or sensitivity are unresolved |
| Sensitive exact geometry, living-person records, DNA/genomic material, private land detail, archaeology locations, rare-species precision, critical infrastructure detail, credentials, or secrets | Do not commit; use public-safe transformations, quarantine, staged access, or denial |
| Semantic object definitions | [`contracts/`](../contracts/README.md) |
| Canonical machine schemas | [`schemas/`](../schemas/README.md) |
| Executable policy or release permission | [`policy/`](../policy/README.md) and governed release controls |
| Reusable validator code | [`tools/validators/`](../tools/validators/README.md) |
| Executable tests and assertions | [`tests/`](../tests/README.md) |
| Test-local-only fixture material | [`tests/fixtures/`](../tests/fixtures/README.md) |
| Actual `EvidenceBundle`, receipt, proof, review, promotion, correction, rollback, or release record | The accepted evidence, `data/receipts/`, `data/proofs/`, or [`release/`](../release/README.md) home |
| Generated CI/build reports | [`artifacts/`](../artifacts/README.md) under an accepted retention and cleanup boundary |
| Application, API, renderer, pipeline, model, or runtime implementation | The accepted `apps/`, `packages/`, `pipelines/`, `tools/`, or `runtime/` responsibility root |
| Public API material, public map/tile products, exports, or published artifacts | Governed APIs and released artifacts only |
| Direct model output or private reasoning | Governed AI envelopes and receipts where applicable; never fixture truth |

A fixture that accidentally contains real, restricted, sensitive, or lifecycle material must be removed from this root, routed through the correct quarantine or responsibility process, and documented through a correction path. Do not merely rename the file or hide fields in a README.

[Back to top](#top)

---

## Inputs

Fixtures may be authored or generated from these bounded sources:

| Input class | Admission rule |
|---|---|
| Hand-authored synthetic example | Use toy values; document scenario, consumer, expected outcome, and governing surfaces |
| Deterministic generator output | Pin generator path/version or content identity, normalization rules, and regeneration command when verified |
| Public-safe transformation of a reference shape | Record source note, rights posture, transform/generalization reason, and why redistribution is allowed |
| Schema/contract example | Reference the owning contract and schema; do not copy their authority into the fixture |
| Validator/test failure canary | Make the expected diagnostic or finite outcome stable and safe |
| Runtime/UI/map smoke example | Keep local, no-network, released-state-safe, and free of direct canonical-store or model-runtime access |
| Release-governance dry-run | Use synthetic IDs and states; make clear that no real release, correction, withdrawal, or rollback occurs |

### Minimum fixture intake record

Every stable or shared fixture should document, in the file, a sibling note, or the owning lane README:

- stable or human-readable fixture identifier;
- scenario and expected outcome;
- consumer paths;
- governing contract, schema, policy, or validator when applicable;
- deterministic authoring or generation method;
- rights and redistribution posture;
- sensitivity and public-safety posture;
- spatial and temporal assumptions where material;
- correction, replacement, or rollback procedure for the fixture itself;
- verification status and last review date.

Unknown rights, unclear sensitivity, real personal or restricted data, and unexplained provenance are stop conditions. Use a smaller synthetic example rather than importing questionable material.

[Back to top](#top)

---

## Outputs

This root supports downstream checks by emitting or preserving:

- reusable deterministic inputs for validators, tests, pipelines, runtime smoke checks, and documentation examples;
- valid and invalid examples with explicit expected behavior;
- deny, abstain, hold, stale, and error canaries;
- public-safe expected payloads for governed API, Evidence Drawer, Focus Mode, map, UI, correction, and rollback checks;
- golden outputs and normalized comparison snapshots;
- fixture metadata, generation notes, and consumer mappings.

| Output | What it may support | What it cannot establish |
|---|---|---|
| Valid fixture | Schema/validator positive path | Claim truth, source admission, policy approval, release, or production parity |
| Invalid or deny fixture | Fail-closed behavior and diagnostic stability | That every unsafe case is covered |
| Golden output | Deterministic regression comparison | That the output is authoritative, released, accessible, or visually correct on every host |
| Runtime/UI/map example | Smoke and presentation checks | Public truth, browser/device parity, accessibility completeness, or release state |
| Release-governance example | Dry-run contract and denial-path checks | Promotion, review approval, rollback execution, or publication |
| Generation note | Reproducibility guidance | A canonical `RunReceipt`, proof, or attestation unless emitted through its owning system |

Fixtures do not publish. A commit, pull request, merge, badge, green test, rendered example, or generated snapshot does not make fixture content KFM `PUBLISHED`.

[Back to top](#top)

---

## Validation

### Default execution posture

- Local and no-network by default.
- Deterministic inputs and stable expected outcomes.
- No credentials, secrets, private endpoints, or direct model clients.
- No writes to canonical or lifecycle stores.
- No publish, promote, correct, withdraw, or rollback side effects.
- Live probes, when separately authorized, run as explicit integration or watcher workflows with source, rights, sensitivity, rate-limit, failure, and receipt controls.

### Repository-grounded commands

Run the narrowest command that matches the changed fixture family. The commands below are verified as repository surfaces; their scope limits are part of the contract.

```bash
# Six configured top-level validators in fixture mode.
python tools/validators/_common/run_all.py

# Makefile alias for the configured aggregate validators.
make schemas

# Aggregate validators plus narrow schema/contract tests.
make validate

# The narrow test portion invoked by make validate.
python -m pytest tests/schemas tests/contracts -q
```

> [!WARNING]
> `make fixtures` is **not** a validator or regeneration command. It currently prints `TODO: regenerate deterministic fixtures` and exits successfully as a readiness marker. Do not cite it as proof that fixtures were regenerated, validated, complete, or current.

The configured aggregate currently invokes fixture-backed checks for:

- `SourceDescriptor`;
- `EvidenceRef`;
- `EvidenceBundle`;
- `RuntimeResponseEnvelope`;
- `DecisionEnvelope`;
- `RunReceipt`.

This list is partial. It does not prove that every fixture lane, schema family, policy outcome, domain, renderer scenario, release prerequisite, correction case, or rollback case is covered.

### Validation layers

| Layer | Check | Failure meaning |
|---|---|---|
| Source and file integrity | Parseability, encoding, file size, naming, stable path, optional hash | Corrupt, misplaced, oversized, or non-deterministic fixture; do not continue silently |
| Schema shape | Valid cases pass; invalid cases fail for the intended reason | Fixture/schema mismatch or stale expected diagnostic |
| Semantic boundary | Example respects the owning contract's meaning | Shape alone is insufficient; fix the example or contract relationship |
| Policy and sensitivity | Expected allow/restrict/hold/abstain/deny behavior; no protected detail leaks | Fail closed and remove or transform unsafe material |
| Evidence and citation | References resolve or the case explicitly models missing/conflicted support | Do not convert missing evidence into a positive answer |
| Temporal and spatial | Time, CRS, bounds, precision, and stale-state assumptions are explicit where material | Mark stale/invalid/held; do not guess |
| Runtime/API/UI/map | Finite outcomes, trust membrane, no direct store/model access, display-safe payload | Block the consumer path; fixture polish does not cure boundary failure |
| Release/correction/rollback | Candidate versus released state, correction lineage, and rollback expectations remain distinct | Deny release-like claims; fix the scenario and owning controls |
| Golden output | Canonical normalization and comparison are deterministic | Review intentional change; do not auto-approve a new golden file |

### Failure interpretation

| Result | Interpretation |
|---|---|
| `PASS` | The declared check passed for the exact fixture, code revision, configuration, and environment used |
| Expected validation failure | The negative case failed for the expected reason; unexpected reasons require investigation |
| `ANSWER` | The bounded runtime example has admissible support for the modeled question only |
| `ABSTAIN` | Support is missing, stale, conflicted, or outside scope; no answer is fabricated |
| `DENY` | Policy or sensitivity blocks exposure or operation |
| `HOLD` / quarantine | Review, rights, identity, quality, or sensitivity remains unresolved |
| `ERROR` | The checker or system failed; never reinterpret as allow or pass |
| Skipped / not collected | No validation claim; document the reason and required follow-up |

### What passing does not prove

A passing fixture check does not prove:

- factual truth or source authority;
- complete EvidenceBundle or citation closure beyond the declared check;
- rights or sensitivity approval beyond the reviewed fixture posture;
- policy approval for production exposure;
- complete test, validator, domain, browser, device, accessibility, or performance coverage;
- release readiness, PromotionDecision, publication, correction execution, or rollback execution;
- production configuration, deployment parity, branch-protection enforcement, or operational health.

### Change validation checklist

- [ ] The fixture remains in the correct reusable or test-local home.
- [ ] The scenario, consumer, expected outcome, and authority limits are explicit.
- [ ] No real, restricted, sensitive, lifecycle, credential, or private material was introduced.
- [ ] Valid and invalid/deny/abstain cases remain paired where the risk warrants them.
- [ ] Schema, contract, policy, evidence, temporal, spatial, release, correction, and rollback meanings remain separate.
- [ ] Golden outputs were regenerated only through a documented deterministic process.
- [ ] Relevant targeted validators or tests ran, or the change states why a check is not applicable.
- [ ] Live-network behavior was not introduced into default fixture validation.
- [ ] Added relative links and anchors resolve.
- [ ] The diff contains no unrelated fixture or authority-root changes.

[Back to top](#top)

---

## Review burden

Current [CODEOWNERS](../.github/CODEOWNERS) routes `/fixtures/` changes to `@bartytime4life`. That is GitHub review routing only; it is not a stewardship assignment, policy approval, release approval, or proof that independent review occurred.

| Change type | Minimum review concern |
|---|---|
| README-only clarification | Fixture-root boundary, links, truth labels, and no-overclaim posture |
| New reusable lane | Ownership, duplicate-home search, consumer need, naming, rights, sensitivity, and maintenance burden |
| New or changed fixture payload | Object/domain owner, validator/test consumer, expected outcome, public safety, deterministic generation, and diff review |
| Sensitive-domain case | Domain and sensitivity review; synthetic/generalized/denied posture; no precise protected detail |
| Schema/contract fixture change | Owning contract/schema reviewer plus validator/test impact |
| Policy outcome fixture | Policy reviewer; expected obligations and fail-closed path |
| Golden-output change | Consumer owner; normalization rules; intentional-delta evidence; rollback to prior expected output |
| Heavy or binary corpus | Storage, licensing, reviewability, reproducibility, retention, and removal plan |
| Live-network or external-service dependency | Separate integration/workflow review; permissions, terms, rate limits, failure behavior, and receipts |

### Update rules

- Update this README when top-level lanes, fixture-home rules, aggregate validation commands, default network posture, storage rules, or root authority boundaries change.
- Update a child README when its payloads, consumers, expected outcomes, generation recipe, rights/sensitivity posture, or validation wiring changes.
- Link each stable fixture to its exact consumer only after that relationship is verified.
- Move stable domain-owned examples into the owning `fixtures/domains/<domain>/` lane when ownership is clear.
- Remove obsolete fixtures only after confirming no active consumer, preserving needed lineage, and documenting replacement or rollback.
- Keep ordinary fixture changes in focused branches and draft pull requests; do not bundle unrelated cleanup.

### Rollback

Documentation rollback is a same-path revert of the README commit. Fixture-content rollback restores the prior reviewed input/expected-output pair and repairs consumers together. Neither rollback is a KFM release rollback unless the governed release system separately records and executes one.

[Back to top](#top)

---

## Related folders

| Surface | Relationship |
|---|---|
| [`tests/`](../tests/README.md) | Owns authored enforceability proof and consumes reusable fixtures |
| [`tests/fixtures/`](../tests/fixtures/README.md) | Owns test-local fixtures; must not duplicate the reusable root |
| [`contracts/`](../contracts/README.md) | Defines object meaning and invariants |
| [`schemas/`](../schemas/README.md) | Defines machine-checkable shape |
| [`policy/`](../policy/README.md) | Defines admissibility, rights, sensitivity, and access behavior |
| [`tools/validators/`](../tools/validators/README.md) | Owns reusable validator implementations |
| [`data/`](../data/README.md) | Owns lifecycle material, registries, receipts, proofs, catalogs, and published artifacts in their proper lanes |
| [`release/`](../release/README.md) | Owns release-governance decisions, manifests, corrections, and rollback records |
| [`artifacts/`](../artifacts/README.md) | Transitional generated-output boundary; not fixture or trust authority |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | Defines focused branch, review, validation, and reversible-change expectations |
| [Directory Rules](../docs/architecture/directory-rules.md) | Governs responsibility-root placement and the required README contract |
| [CODEOWNERS](../.github/CODEOWNERS) | Routes GitHub review requests; does not establish approval or stewardship authority |

### Verified child documentation

- [`contracts/v1/`](contracts/v1/README.md) — versioned contract fixture-family index.
- [`slim/`](slim/README.md) — compact runtime fixture lane.

Other lanes in the navigation inventory are retained as repository routes from the prior README and targeted search. Their complete payload and child-README coverage remain **NEEDS VERIFICATION** until recursively inventoried.

[Back to top](#top)

---

## ADRs

No accepted fixture-root-specific ADR was verified for this documentation update.

- [`ADR-0001 — Schema Home`](../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) is **proposed**. It documents the configured `schemas/contracts/v1/` machine-shape surface and does not turn `fixtures/contracts/v1/` into schema authority.
- Directory Rules currently identify duplicate-fixture sprawl as an anti-pattern and require the reusable-root versus test-local split to be documented. This README and [`tests/fixtures/README.md`](../tests/fixtures/README.md) record that split.
- The Directory Rules document-location conflict (`docs/architecture/` versus `docs/doctrine/`) remains an open governance question. New links in this file follow the current contribution guidance and point to the live architecture-path artifact; this README does not resolve or supersede that conflict.

An accepted ADR and migration plan are required before removing or renaming the canonical `fixtures/` root, collapsing it into `tests/fixtures/`, creating another reusable fixture authority, or changing a fixture path in a way that changes governed object identity or lifecycle responsibility.

[Back to top](#top)

---

## Last reviewed

**2026-07-23**

Evidence snapshot: `bartytime4life/Kansas-Frontier-Matrix` at `main@005aa64f6d42aa5961646e733289a2b857292357`, prior target blob `b096b0ed49c8e7d95ddb0d4c813d06ef40f1528d`.

Review this root README again when any of these conditions occurs:

- six months pass without review;
- a top-level fixture lane is added, moved, renamed, consolidated, or retired;
- the reusable-root versus test-local split changes;
- the aggregate validator inventory or Makefile command behavior changes;
- a canonical fixture generator or full fixture suite is established;
- live-network tests are admitted;
- rights, sensitivity, large-corpus storage, or binary-fixture rules change;
- Directory Rules or an accepted ADR changes fixture placement;
- a new renderer or runtime authority decision changes fixture routing;
- a fixture-related correction or rollback exposes a gap in this contract.

### Open verification register

- Complete recursive inventory of top-level and domain fixture lanes.
- Exact fixture payload counts, file types, sizes, and ownership.
- Consumer mapping for every stable fixture and golden output.
- Complete schema, contract, policy, validator, pipeline, runtime, UI, map, correction, rollback, and CI coverage.
- Accepted full-suite and deterministic regeneration commands.
- Branch-protection and required-check coupling.
- Fixture steward assignment and independent review thresholds.
- Legacy renderer terminology in child READMEs and any affected fixture paths.
- Large-corpus storage, Git LFS, external object storage, retention, and rights posture.

> [!NOTE]
> This README is a repository-grounded documentation contract. It does not claim that fixture payloads were regenerated, that the full repository test suite ran, that all child lanes are complete, or that any fixture is released or published.

[Back to top](#top)
