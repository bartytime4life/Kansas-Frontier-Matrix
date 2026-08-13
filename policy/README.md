<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-readme
title: policy/ — Canonical Admissibility Root
type: readme
version: v0.4.0
status: draft; repository-grounded; current-state-reconciled; mixed-maturity; direct-child-coverage-audited; bounded-Rego-evaluation; general-evaluator-unbound; active-bundle-unaccepted; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes /policy/ to @bartytime4life; accepted policy stewardship and independent approval controls were not established
created: 2026-07-23
updated: 2026-08-13
current_path: policy/README.md
owning_root: policy/
policy_label: public; policy; root-contract; mixed-maturity; non-release; non-publication
responsibility: Define the canonical policy-source root, direct-child boundaries, maturity evidence, validation posture, and trust membrane without becoming semantic, schema, evidence, runtime, release, or publication authority.
base_commit: 737dce6357d670e48df85e94ec0641aaa1a365cb
prior_blob: 6c5021f9d92778581a4e9331a9dd6ddb7efc5e35
directory_governance: ADR-0029 accepted Directory Rules v2 for placement; ADR-0003 remains proposed for the policy/policies compatibility decision
truth_posture: CONFIRMED canonical singular policy root, accepted Directory Rules placement, active Root Registry projection, exact 40-directory direct-child map, 523-entry recursive policy tree, 73 README files, 34 substantive direct-child READMEs, five one-byte direct-child README placeholders, one direct child without a README, 173 Rego files with exactly one native Rego test, one bounded PROPOSED_INACTIVE release-gate profile with checksum-pinned OPA 1.19.0 CI, multiple inactive fixture-first profiles and validators, 18-test structural boundary suite, placeholder policy-runtime package, and broad readiness holds / PROPOSED root contract, direct-lane completion, active-evaluator sequence, threshold values and bindings, and future consumer binding / CONFLICTED or unresolved source-vs-sources and test-vs-tests naming, compatibility-lane placement, schema homes, and inactive native-to-outward outcome binding / UNKNOWN repository-wide bundle selector, accepted evaluator, required-check configuration, production consumers, decision receipts, replay, promotion integration, deployment enforcement, and independent release approval
[/KFM_META_BLOCK_V2] -->

# policy

> **One-line purpose.** `policy/` is KFM's canonical responsibility root for admissibility rules: it decides whether a bounded operation may proceed, must be restricted or held, should abstain, or must fail closed—without becoming semantic truth, machine shape, evidence, runtime implementation, lifecycle storage, release approval, or publication authority.

<a id="top"></a>

| Placement | Direct lanes | Substantive child READMEs | Native Rego tests | General evaluator | Publisher |
|---|---:|---:|---:|---|---|
| [Accepted `policy/` root](#authority-level) | [40](#current-direct-child-map) | [34](#readme-coverage) | [1 bounded profile](#validation) | [Unbound](#current-maturity) | **No** |

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [Direct children](#current-direct-child-map) · [README coverage](#readme-coverage) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Maturity](#current-maturity) · [Outcomes](#outcome-vocabularies) · [Authoring](#policy-authoring-contract) · [Sensitive policy](#rights-sensitivity-consent-and-public-exposure) · [Trust membrane](#runtime-and-public-trust-membrane) · [Rollback](#correction-and-rollback) · [Open verification](#open-verification-register)

> [!IMPORTANT]
> **Safe current conclusion:** `policy/` is the adopted placement for policy source. Its direct documentation surface is now broad but not complete: 34 of 40 direct child lanes have substantive READMEs, five retain one-byte placeholder READMEs, and `policy/test/` has no README. One bounded, `PROPOSED_INACTIVE` Pass 12 release-gate profile has executable Rego, the repository's only native Rego test, exact-polarity fixtures, stable deny reasons, and checksum-pinned OPA 1.19.0 CI. These surfaces do **not** establish a repository-wide active bundle, accepted general evaluator, functional policy-runtime package, authenticated `PolicyDecision` flow, production consumer, promotion authority, release approval, deployment enforcement, or publication.

> [!CAUTION]
> A policy result cannot create evidence, clear rights by assertion, infer consent, downgrade sensitivity, authenticate review, promote lifecycle state, approve release, make generated language authoritative, or turn a map, tile, file path, workflow, commit, or pull request into public truth.

---

## Purpose

`policy/` owns KFM's **admissibility posture** and reviewed policy source.

It answers one bounded question:

> Given an explicit operation, actor or caller, audience, governed object references, source and evidence context, rights, consent, sensitivity, lifecycle state, review state, release context, and policy version, may the operation proceed—and under which enforceable obligations?

Policy decisions should be operation-specific, evidence-aware, reason-coded, obligation-bearing, replayable where practical, and fail-closed when required context is missing or untrusted. `policy/` decides admissibility; it does not decide whether a claim is factually true.

[Back to top](#top)

---

## Authority level

**Canonical responsibility root for admissibility and policy source; non-semantic, non-schema, non-evidence, non-runtime, non-release, and non-publication authority.**

Accepted [ADR-0029](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) makes Directory Rules v2 effective for placement and names singular `policy/` as the policy-source root. [ADR-0003](../docs/adr/ADR-0003-policy-singular-is-canonical-%28policies-is-compatibility%29.md) remains **proposed** for the narrower compatibility and migration decision; its status does not undo the adopted Directory Rules placement.

The [`Root Registry`](../control_plane/root_registry.yaml) projects this accepted placement as `root.policy`: canonical, durable, internally exposed, versioned, limited to `policy_rule`, and explicitly prohibited from containing `data_instance`, `release_decision`, or `schema` artifacts. That machine projection is a consistency surface, not authority to create roots, activate rules, migrate paths, or publish.

| Responsibility | Owning surface | `policy/` role |
|---|---|---|
| Policy rules and admissibility | `policy/` | Own reviewed rule source, inactive candidate registries, and policy-family boundaries. |
| Object meaning | [`contracts/policy/`](../contracts/policy/README.md) | Consume meaning; never redefine it here. |
| Machine shape | [`schemas/contracts/v1/policy/`](../schemas/contracts/v1/policy/README.md) | Require accepted shapes; never become schema authority. |
| Evidence and source authority | evidence and registry roots | Evaluate supplied status; never invent it. |
| Evaluation mechanics | [`packages/policy-runtime/`](../packages/policy-runtime/README.md) or an accepted evaluator | Supply accepted rules; do not place reusable runtime code here. |
| Validation and tests | [`tools/validators/policy/`](../tools/validators/policy/README.md), `tests/`, `fixtures/` | Prove bounded shape and semantic behavior; passing is not a decision instance. |
| Release and rollback | [`release/`](../release/README.md) | Supply required gate results; never approve or publish by itself. |
| Public enforcement | governed APIs and applications | Consume normalized decisions; never load policy source directly. |

[Back to top](#top)

---

## Status

| Surface | Current status at `main@737dce6357d670e48df85e94ec0641aaa1a365cb` | Safe conclusion |
|---|---|---|
| `policy/README.md` | **CONFIRMED v0.3.1 baseline; blob `6c5021f9d92778581a4e9331a9dd6ddb7efc5e35`** | v0.4.0 refreshes evidence and navigation in place; it changes no rule or decision. |
| Singular `policy/` root | **CONFIRMED / accepted placement** | Directory Rules v2 is effective through ADR-0029; no second policy root is authorized. |
| Root Registry projection | **CONFIRMED `root.policy` / `ACTIVE` registry status** | Projects accepted placement and artifact constraints; it does not create authority or activate rules. |
| Recursive tree | **CONFIRMED 523 entries: 365 files and 158 directories** | Inventory proves tracked presence only. |
| Direct-child topology | **CONFIRMED 40 directories and no direct file besides this README** | The prior `living_persons_geoprivacy.md` entry was deleted in `9d41bd04f559e25ea0cf2fc51c3e06955f9771b1` and is removed from the current map. |
| README coverage | **CONFIRMED 73 total; 34 substantive direct-child READMEs** | Five direct children retain one-byte README placeholders; `policy/test/` has no README. Documentation coverage is not implementation maturity. |
| Rego source inventory | **CONFIRMED 173 `.rego` files** | Exactly one tracked file matches the repository's native Rego-test naming convention; no broader test-to-source coverage is inferred. Source presence alone is not activation or correct evaluation. |
| Pass 12 release gate | **CONFIRMED bounded executable profile; `PROPOSED_INACTIVE`** | `policy/rego/release_gate_v1.rego` defaults deny and exposes deterministic reasons. |
| Native Rego tests | **CONFIRMED exactly one bounded test file** | `policy/rego/release_gate_v1_test.rego` is exercised by its dedicated workflow; no repository-wide native-test convention is accepted. |
| OPA execution | **CONFIRMED in dedicated hosted workflow** | `.github/workflows/pass12-release-policy-v1.yml` checksum-pins OPA 1.19.0 and runs format, unit, fixture-polarity, and deny-reason checks. |
| `policy/bundles/` | **CONFIRMED documentation plus inactive Pass 12 packaging profile** | No non-document bundle payload, accepted manifest, selector, signature, or active bundle is established. |
| Policy runtime | **CONFIRMED `0.0.0` placeholder** | No functional general evaluator, adapter, public API, or consumer library is established. |
| Policy validator lane | **CONFIRMED multiple deterministic Python validators** | They validate inactive contracts, schemas, identities, and bindings; they do not evaluate policy or emit authoritative decisions. |
| `PolicyInputBundle` | **CONFIRMED permissive parent plus explicit profile v1** | The profile checks bounded context for `ANSWER`, `RENDER`, `EXPORT`, `PROMOTE`, and `RELEASE`; passing proves coherence only. |
| Decision vocabulary and semantics | **CONFIRMED inactive registries/profiles** | Stable reason, obligation, reviewer-role, and outward-outcome candidates exist; activation and runtime normalization remain unaccepted. |
| Policy evaluation binding | **CONFIRMED declared-only, digest-bound profile** | It binds exact fixture bytes and evaluator declarations; it does not prove evaluator execution or decision authenticity. |
| Obligation carriers | **CONFIRMED fixture-first candidate surfaces** | Structured duties and reduction checks exist without enforcement or release effect. |
| Enforcement maturity | **CONFIRMED fixture-only assessment profile** | A workflow file is not evidence that a check is merge-, promotion-, or runtime-blocking. |
| `policy-test` workflow | **CONFIRMED broad readiness hold plus bounded-lane wiring checks** | It evaluates no repository-wide bundle and emits no `PolicyDecision`, receipt, proof, release, or publication authority. |
| `policy-boundary-guards` | **CONFIRMED 18-test structural/static/API suite** | It protects selected trust boundaries; it is not policy-bundle, rights, sensitivity, or release proof. |
| Repository-wide `make policy` | **CONFIRMED TODO-only target** | There is no accepted repository-native general policy evaluation command. |
| Domain-policy routing | **CONFIRMED 14 direct children under `policy/domains/`** | Thirteen canonical domain lanes have substantive boundaries; a residual `people/` marker conflicts with the canonical `people-dna-land/` identity. |
| Active evaluator, bundle selector, decision receipts, governed consumer, promotion integration | **UNKNOWN / NEEDS VERIFICATION** | No complete governed evaluation flow was proved. |
| Required checks and independent approval | **UNKNOWN / NEEDS VERIFICATION** | Workflow presence and CODEOWNERS routing are not branch-protection or separation-of-duties evidence. |

[Back to top](#top)

---

## What belongs here

- this root README and child policy-lane READMEs;
- reviewed Rego, OPA-compatible, or equivalent declarative policy modules;
- operation-specific access, evidence, consent, sensitivity, rights, render, export, AI, lifecycle, promotion, release-gate, correction, and rollback policy source;
- domain-specific admissibility rules under a domain segment, not a new root;
- fail-closed defaults preserving unknown, missing, stale, conflicted, restricted, and false as distinct states;
- stable rule package names, entrypoints, versions, reason codes, obligations, reviewer-role candidates, and supersession notes;
- inactive registries or bundle-packaging profiles whose status and non-effects are explicit;
- synthetic or public-safe native policy tests when the owning policy lane and test convention are reviewable;
- links to paired contracts, schemas, fixtures, tests, validators, receipts, proofs, consumers, release gates, correction paths, and rollback targets.

A file belongs here because its primary responsibility is **admissibility**, not because it mentions privacy, security, AI, maps, release, or a domain.

[Back to top](#top)

---

## What does NOT belong here

| Do not put this in `policy/` | Correct responsibility |
|---|---|
| Semantic definitions | `contracts/` |
| JSON Schema, DTO, enum, or field shape | `schemas/contracts/v1/` |
| Source payloads, credentials, or registry instances | connectors, secret stores, or accepted `data/registry/` lanes |
| EvidenceBundles, proof packs, citations, or claim truth | evidence/proof roots |
| RAW through PUBLISHED data | `data/<phase>/` |
| Emitted decisions, receipts, reviews, validation reports, or proofs | accepted lifecycle, receipt, proof, review, or report roots |
| Evaluator, adapter, CLI, server, or reusable package code | `packages/`, `apps/`, `runtime/`, or `tools/` by responsibility |
| Validator implementation | `tools/validators/` |
| Reusable generic fixtures and tests | root `fixtures/` and `tests/` |
| Release manifests, approvals, rollback cards, corrections, withdrawals | `release/` |
| Public API routes, UI, MapLibre logic, exports, or AI responses | governed application/runtime roots |
| Real sensitive locations, living-person records, DNA/genomic content, or consent tokens | denied; use synthetic/redacted references |
| A second independently evolving policy root | compatibility or migration only after accepted authority |
| Generated prose presented as a policy grant or approval | governed review; generated language is interpretive only |

[Back to top](#top)

---

## Inputs

Policy evaluation must use an **explicit, versioned input bundle** and must not silently fetch missing facts.

| Input class | Minimum governed context | Fail-closed trigger |
|---|---|---|
| Operation | stable capability, request/candidate ID, family, evaluation time | unknown or overly broad operation |
| Actor and audience | subject/service class, purpose, public/restricted/steward audience | missing identity context where access differs |
| Object and scope | stable refs, domain, space/time scope, requested precision | raw payload substituted for governed refs |
| Source and evidence | SourceDescriptor refs, source roles, EvidenceBundle status, citations, freshness | unresolved source role, terms, or support |
| Rights, consent, sensitivity | license/terms, consent applicability/revocation, classification, transform decisions | unknown, expired, revoked, or unsupported posture |
| Lifecycle, review, release | current/requested state, validation/proof refs, reviewer state, release/correction/rollback refs | skipped state, missing review, or ungoverned public exposure |
| Policy execution | bundle ID/version/digest, evaluator profile/version, entrypoint, input hash | unaccepted or non-replayable evaluator context |

The permissive parent `PolicyInputBundle` shape remains separate from [`policy_input_bundle_profile_v1`](../contracts/policy/policy_input_bundle_profile_v1.md). The explicit profile makes one bounded subset machine-checkable and fail-closed, but it remains `PROPOSED_INACTIVE`, fixture-only, and non-evaluator.

[Back to top](#top)

---

## Outputs

A policy evaluation may produce:

- an engine-native result such as the Pass 12 profile's `allow`, `deny`, and sorted `deny_reasons`;
- a normalized `PolicyDecision` candidate using the closed outward vocabulary;
- public-safe reason codes and enforceable obligations;
- governed object, bundle, evaluator, review, release, correction, and rollback references;
- receipt-ready input and result digests;
- an explicit readiness hold or operational error.

Policy outputs do **not** by themselves prove a claim, authenticate evidence or review, authorize a lifecycle transition, approve release, satisfy missing rights or sensitivity review, or become public merely because their shape validates or a workflow passes.

[Back to top](#top)

---

## Validation

| Surface | What it proves now | What it does not prove |
|---|---|---|
| `pass12-release-policy-v1` | Checksum-pinned OPA 1.19.0 can format and test the bounded Rego profile; fixtures preserve allow/deny polarity and named deny reasons. | Active bundle selection, cryptographic attestation verification, reviewer authentication, `PolicyDecision` normalization, promotion, release, or publication. |
| `policy-test / OPA readiness hold` | Required files, the bounded Rego lane, its dedicated workflow, the placeholder runtime, and the absence of a repository-wide bundle payload remain explicit. | Repository-wide policy evaluation or an accepted general command. |
| Focused policy validators | Inactive input, decision, binding, obligation, reviewer-role, and maturity candidates satisfy their documented shape and semantic invariants. | Policy execution, consumer enforcement, rights clearance, or release approval. |
| Schema harness | Selected schemas and fixtures validate structurally. | Correct policy, source authority, evidence, rights, sensitivity, or review. |
| `policy-boundary-guards` | Eighteen selected structural/static/API tests in four named modules preserve control-plane, connector/pipeline non-publisher, Explorer adapter/store, and governed-API boundaries. | Policy-bundle evaluation, rights/sensitivity matrices, evidence closure, or release decisions. |
| Documentation validators | Local links/fragments, required metadata, document-graph reachability, and bounded freshness are checked deterministically for this README. | Correct policy semantics, accepted ownership, operational enforcement, or external-link availability. |
| Repository-topology ratchet | Adopted placement rules are checked against exact inherited fingerprints. | Rule activation, consumer closure, migration approval, deletion authority, or policy correctness. |

Current command posture:

```bash
# Root-document QA; no external URL is requested.
python tools/validators/docs/link-check/check_links.py policy/README.md
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required policy/README.md
python tools/validators/docs/document-graph/check_document_graph.py \
  --entrypoint policy/README.md policy/README.md
python tools/validators/docs/stale-scan/check_stale_docs.py \
  --as-of 2026-08-13 --profile bounded-required policy/README.md

# Adopted placement ratchet; baseline findings remain implementation waivers.
python tools/validators/directory_governance/validate_repository_topology.py

# Bounded executable Rego lane — implemented by the dedicated hosted workflow.
opa fmt --fail policy/rego/release_gate_v1.rego policy/rego/release_gate_v1_test.rego
opa test policy/rego/release_gate_v1.rego policy/rego/release_gate_v1_test.rego

# Representative fixture-first policy profile checks.
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_policy_input_bundle_profile_v1.py' \
  --verbose

python tools/validators/policy/validate_policy_obligation_set.py --fixtures

# Structural trust-boundary suite; not a policy evaluator.
make boundary-guards-ci
```

Repository qualifications:

- the root `Makefile` `policy` target still prints a TODO command;
- the recursive policy tree contains 173 Rego files but exactly one native Rego test file;
- the OPA binary is installed only by the dedicated workflow; no repository-wide checked-in evaluator or accepted general bundle selector exists;
- the broad `policy-test` job is intentionally static and fail-closed;
- `packages/policy-runtime` remains a comment-only `0.0.0` placeholder;
- Python policy validators are deterministic, no-network candidate validators, not evaluator adapters.

Before executable policy is treated as generally active, require an accepted evaluator and bundle contract, selector and digest binding, complete input assembly, native positive and negative tests, deterministic repository-native command, explicit native-to-outward normalization, reason and obligation enforcement, governed consumer, decision receipts and replay, correction/expiry/rollback tests, sensitive negative cases, read-only CI, and observed required-check plus independent-review evidence.

[Back to top](#top)

---

## Review burden

CODEOWNERS routes `/policy/` changes to `@bartytime4life`. That is review routing, not an accepted stewardship assignment or proof of independent approval.

| Change class | Minimum review posture |
|---|---|
| README-only clarification | Policy-aware maintainer plus docs review. |
| Rule module or native test | Policy steward, affected owner, and validation reviewer. |
| Access/identity/capability | Policy + security/identity + application owner. |
| Rights/consent/living-person/DNA/cultural/archaeology/rare-species/infrastructure | Relevant specialist plus policy, privacy/security, and release reviewer; fail closed without ownership. |
| Bundle, selector, signing, evaluator activation | Policy-runtime, supply-chain/security, validation, and release review. |
| Outcome normalization, reason registry, or obligations | Policy, contracts, schemas, runtime consumer, and API/UI review. |
| Contract/schema change | Contract + schema + policy + validator/test + migration review. |
| Promotion/release/correction/rollback | Policy + release + evidence/proof + operations review with separation of duties where required. |

Accepted policy stewardship, branch-required checks, and independent release approval remain **NEEDS VERIFICATION**.

[Back to top](#top)

---

## Related folders

| Surface | Relationship |
|---|---|
| [`contracts/policy/`](../contracts/policy/README.md) | Semantic policy-object meaning and inactive policy profiles. |
| [`schemas/contracts/v1/policy/`](../schemas/contracts/v1/policy/README.md) | Machine shape; profile maturity remains explicit. |
| [`fixtures/contracts/v1/policy/`](../fixtures/contracts/v1/policy/README.md) | Reusable synthetic contract fixtures. |
| [`fixtures/policy/release_gate_v1/`](../fixtures/policy/release_gate_v1/) | Native Pass 12 Rego input fixtures. |
| `tests/policy/` | Structural trust-boundary tests. |
| `tests/validators/` | Focused candidate-profile validator tests. |
| [`packages/policy-runtime/`](../packages/policy-runtime/README.md) | Proposed evaluator helper; currently a placeholder. |
| [`tools/validators/policy/`](../tools/validators/policy/README.md) | Deterministic policy-profile validators; not evaluators. |
| `data/registry/`, `data/receipts/`, `data/proofs/` | Source context, process memory, and proof support. |
| [`release/`](../release/README.md) | Promotion, release, correction, withdrawal, and rollback authority. |
| [`apps/governed-api/`](../apps/governed-api/README.md) | Public trust-membrane consumer boundary. |
| [Directory Rules](../docs/doctrine/directory-rules.md) | Adopted placement and README contract. |
| [`control_plane/root_registry.yaml`](../control_plane/root_registry.yaml) | Machine projection of `root.policy`; not root-creation or activation authority. |
| [`policy-test`](../.github/workflows/policy-test.yml) | Broad fail-closed readiness holds and bounded-lane wiring checks. |
| [`pass12-release-policy-v1`](../.github/workflows/pass12-release-policy-v1.yml) | Exact-head OPA execution for the inactive release-gate profile. |
| [`policy-boundary-guards`](../.github/workflows/policy-boundary-guards.yml) | Eighteen-test structural/static/API trust-boundary suite. |
| [`repository-topology`](../tools/validators/directory_governance/validate_repository_topology.py) | Exact placement-drift ratchet; not policy or migration authority. |

[Back to top](#top)

---

## Current direct-child map

Directory Rules `ROOT_FULL` requires the root README to map direct children only. The following 40-directory inventory is verified from the Git tree at `main@737dce6357d670e48df85e94ec0641aaa1a365cb`. Presence, a README, a rule stub, or a green workflow does not establish adoption, maturity, activation, or equal authority.

```text
policy/
├── README.md              # This ROOT_FULL authority, routing, and maturity contract
├── access/                # Capability-authorization policy boundary
├── ai_builder/            # AI-assisted repository-work policy boundary
├── biotopes/              # Biotopes compatibility guardrail
├── bundles/               # Bundle packaging and selection boundary
├── consent/               # Consent admissibility boundary
├── contract/              # Contract-change admissibility boundary
├── data/                  # Lifecycle and public-exposure admissibility boundary
├── decision/              # Finite outcomes and normalization candidates
├── domains/               # Domain-specific policy routing
├── evidence/              # Evidence admissibility boundary
├── fixtures/              # Held policy-local fixture-routing placeholder
├── focus/                 # Focus Mode policy scaffold boundary
├── genealogy/             # Genealogy compatibility boundary
├── geoprivacy/            # Cross-domain geoprivacy routing
├── identity/              # Identity-context policy routing
├── intake/                # Pre-RAW intake admissibility boundary
├── joins/                 # Cross-domain join admissibility boundary
├── layers/                # Layer and public-exposure admissibility boundary
├── match-scoring/         # Marker-only unresolved lane
├── opa/                   # Placeholder and convergence-hold boundary
├── promotion/             # Promotion admissibility boundary
├── proof/                 # Marker-only unresolved lane
├── redaction/             # Redaction-profile policy boundary
├── rego/                  # Reviewed Rego source lane
├── release/               # Release-admissibility rule source
├── review/                # Review-admissibility boundary
├── rights/                # Rights-admissibility boundary
├── role/                  # Marker-only unresolved lane
├── runtime/               # Runtime-policy source, not evaluator implementation
├── sensitivity/           # Sensitivity trust boundary
├── source/                # Current source-admissibility lane
├── sources/               # Marker-only parallel-name lane
├── story/                 # Story policy boundary
├── supply_chain/          # Supply-chain policy boundary
├── telemetry/             # Telemetry policy boundary
├── test/                  # Tracked lane without a README
├── tests/                 # Held policy-local test-routing boundary
├── thresholds/            # Inactive unresolved threshold candidates
├── transport/             # Marker-only unresolved lane
└── ui/                    # UI policy boundary
```

### Child-lane interpretation

| Child family | Current boundary |
|---|---|
| `rego/` | Executable declarative source lane; currently includes the bounded Pass 12 release gate and the repository's only native Rego test. The other 172 policy Rego files are not thereby tested or active. |
| `bundles/`, `decision/`, `opa/`, `runtime/` | Packaging, finite-outcome, convergence-hold, and runtime-policy boundaries. No accepted repository-wide bundle selector, general evaluator, or authoritative decision emitter is established. |
| `domains/` and named topic lanes | Policy source scoped beneath the singular policy root. The domain parent currently maps 14 direct children, 13 canonical substantive lane READMEs, and one residual marker-only `people/` path. |
| `fixtures/`, `test/`, `tests/` | Policy-local compatibility or routing lanes. Reusable executable fixtures and tests remain owned by root `fixtures/` and `tests/`; `test/` lacks its required boundary explanation. |
| `source/` and `sources/` | `source/` has a substantive boundary; `sources/` remains a one-byte marker. Parallel naming is unresolved drift, not evidence of two source-policy authorities. |
| `thresholds/` | Inactive unresolved-slot candidate registry only; no threshold value, evaluator binding, watcher binding, activation, release, or publication authority. |
| `match-scoring/`, `proof/`, `role/`, `sources/`, `transport/` | Each direct README is one byte. The path is tracked, but responsibility, writers, readers, retention, and graduation remain **NEEDS VERIFICATION**. |
| `access/`, `consent/`, `geoprivacy/`, `identity/`, `rights/`, `sensitivity/` | High-risk admissibility boundaries. Their documentation does not substitute for verified stewards, accepted semantics, negative tests, authenticated evaluation, or production enforcement. |
| All other children | Existing policy-family boundaries with mixed maturity. Review each lane's exact README, rule, fixtures, tests, validator, bundle, evaluator, consumer, receipt, correction, and rollback evidence before operational reliance. |

### README coverage

| Coverage class | Count | Current evidence |
|---|---:|---|
| Total README files under `policy/` | 73 | Root, direct-child, and deeper boundary documents in the pinned Git tree. |
| Substantive direct-child READMEs | 34 | More than one byte and independently reviewable; content maturity still varies from placeholder-routing contract to bounded executable profile. |
| One-byte direct-child README placeholders | 5 | `match-scoring/`, `proof/`, `role/`, `sources/`, and `transport/`. |
| Direct children without a README | 1 | `test/`; tracked contents do not explain its authority or compatibility relationship to `tests/`. |
| Deeper READMEs | 33 | Owned by their nearest substantive parent boundary; not expanded into this root map. |

Substantive direct-child indexes:

- **Core admissibility and context:** [`access/`](./access/) · [`consent/`](./consent/) · [`contract/`](./contract/) · [`data/`](./data/) · [`evidence/`](./evidence/) · [`geoprivacy/`](./geoprivacy/) · [`identity/`](./identity/) · [`intake/`](./intake/) · [`rights/`](./rights/) · [`sensitivity/`](./sensitivity/)
- **Composition and decisions:** [`bundles/`](./bundles/) · [`decision/`](./decision/) · [`focus/`](./focus/) · [`joins/`](./joins/) · [`layers/`](./layers/) · [`opa/`](./opa/) · [`promotion/`](./promotion/) · [`redaction/`](./redaction/) · [`rego/`](./rego/) · [`release/`](./release/) · [`review/`](./review/) · [`runtime/`](./runtime/) · [`thresholds/`](./thresholds/)
- **Domains and specialized policy:** [`biotopes/`](./biotopes/) · [`domains/`](./domains/) · [`genealogy/`](./genealogy/) · [`source/`](./source/) · [`story/`](./story/) · [`supply_chain/`](./supply_chain/) · [`telemetry/`](./telemetry/) · [`ui/`](./ui/)
- **Authoring support boundaries:** [`ai_builder/`](./ai_builder/) · [`fixtures/`](./fixtures/) · [`tests/`](./tests/)

> [!NOTE]
> The deleted `policy/living_persons_geoprivacy.md` path is not a current direct child. Commit `9d41bd04f559e25ea0cf2fc51c3e06955f9771b1` removed it on 2026-08-13. This README records the observed topology change without deciding whether another lane supersedes its former semantics or whether external consumers exist.

[Back to top](#top)

---

## ADRs

| ADR or authority | Status | Relevance |
|---|---:|---|
| [`ADR-0029 — adopt Directory Governance Standard v2`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **ACCEPTED** | Makes Directory Rules v2 effective for placement, root classes, and README contracts. |
| [`ADR-0003 — policy/ singular is canonical`](../docs/adr/ADR-0003-policy-singular-is-canonical-%28policies-is-compatibility%29.md) | **PROPOSED** | Compatibility-root and migration decision; not needed to deny a second active policy authority under adopted Directory Rules. |
| [`ADR-0001 — schema home`](../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | **PROPOSED** | Policy schema placement remains configured but not accepted by this ADR. |
| [`ADR-0002 — contracts vs schemas`](../docs/adr/ADR-0002-contracts-vs-schemas-split.md) | **DRAFT source / PROPOSED effective status** | Reconciles meaning, shape, admissibility, fixtures, tests, and validator coupling without accepting the decision. |
| [`ADR-0020 — abstain is first class`](../docs/adr/ADR-0020-abstain-is-a-first-class-decision.md) | **PROPOSED** | Closed outward outcome model. |
| General evaluator, bundle selector, normalization, activation | **NOT ACCEPTED / NEEDS VERIFICATION** | Operational policy-substrate decisions remain open. |

This README may document current bytes and open decisions. It must not accept an ADR, activate a bundle, change a required check, or grant release authority through prose.

[Back to top](#top)

---

## Last reviewed

**2026-08-13** against `main@737dce6357d670e48df85e94ec0641aaa1a365cb`.

Reviewed:

- the complete v0.3.1 root README and prior blob `6c5021f9d92778581a4e9331a9dd6ddb7efc5e35`;
- accepted ADR-0029 v1.2, exact adopted Directory Rules blob `fd49a0b83e55cef52c1124281f093e263526898d`, and the active `root.policy` machine projection;
- the complete 523-entry recursive `policy/` Git tree, all 40 direct directories, and all 73 README files;
- direct documentation coverage: 34 substantive child READMEs, five one-byte README placeholders, and one direct child without a README;
- the 173-file policy Rego inventory and exact one-file native Rego-test inventory;
- ADR-0002, ADR-0003, and ADR-0020 source and effective status boundaries;
- substantive direct child indexes, including the current 14-child domain-policy map;
- removal of `policy/living_persons_geoprivacy.md` in commit `9d41bd04f559e25ea0cf2fc51c3e06955f9771b1`;
- the Pass 12 Rego source, native tests, fixtures, bundle-profile README, and exact-head OPA workflow;
- `policy-test`, `policy-boundary-guards`, and the focused policy-profile workflows;
- explicit input, decision vocabulary/semantics, evaluation binding, obligation, reviewer-role, and enforcement-maturity contract/schema/validator slices;
- the `packages/policy-runtime` placeholder boundary.

Not established:

- branch-protection or ruleset-required check configuration;
- accepted policy steward and independent approver identities;
- repository-wide bundle manifest, selector, signing, or active evaluator;
- functional policy-runtime imports or production consumers;
- authenticated decision emission, persistence, receipts, replay, expiry, correction propagation, or cache invalidation;
- promotion-gate integration, deployment enforcement, release authorization, or public runtime behavior;
- external consumers or semantic supersession evidence for the deleted direct policy file.

[Back to top](#top)

---

## Current maturity

| Level | Evidence required | Root-wide posture |
|---|---|---:|
| M0 — Placeholder | stub README or default-only module | **CONFIRMED in five one-byte direct READMEs, one unexplained direct lane, additional scaffold lanes, and `policy-runtime`** |
| M1 — Boundary documented | responsibility, inputs, outputs, failures, authority split | **CONFIRMED for 34 direct child READMEs; completeness and exact profile compliance vary by lane** |
| M2 — Rule or profile candidate | reviewed source, contracts/schemas, synthetic fixtures, stable validator or entrypoint | **CONFIRMED in multiple inactive profiles** |
| M3 — Evaluator-backed proof | accepted evaluator/bundle, native tests, input assembly, normalization, deterministic CI | **PARTIAL only for one bounded Rego profile; general M3 not established** |
| M4 — Governed consumer and replay | consumer, authenticated decisions, receipts, replay, expiry, correction, cache invalidation | **NOT ESTABLISHED** |
| M5 — Release-significant enforcement | required checks, independent review, deployment evidence, promotion/rollback drill | **UNKNOWN / NOT ESTABLISHED** |

The fixture-only [`PolicyEnforcementMaturity`](../contracts/policy/policy_enforcement_maturity.md) profile uses a separate ordered vocabulary—`DESIGNED`, `FIXTURE_TESTED`, `MERGE_BLOCKING`, `PROMOTION_BLOCKING`, `RUNTIME_ENFORCED`. Do not infer a later stage from a workflow file or green run alone. State maturity per lane, exact revision, and evidence chain; a root with several M2 profiles is not an M2 production system.

[Back to top](#top)

---

## Outcome vocabularies

| Axis | Examples | Meaning |
|---|---|---|
| Canonical outward `PolicyDecision.outcome` | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Closed four-value candidate schema. |
| Pass 12 engine-native result | `allow: true|false`, `deny_reasons[]` | Bounded Rego profile result; deliberately not normalized into `PolicyDecision`. |
| Other engine-native terms | `ALLOW`, `RESTRICT`, `HOLD`, `DENY`, sometimes `ABSTAIN`/`ERROR` | Lower-level semantics requiring explicit accepted normalization. |
| Validation | `PASS`, `FAIL`, `DENY`, `ERROR`, validator codes | Check result; never policy permission or release state. |
| Workflow readiness | `WORKFLOW_HOLD`, `WORKFLOW_SKIPPED_EXPLICIT` | CI statement that prerequisites are intentionally absent. |
| Lifecycle/release | candidate, held, released, withdrawn, superseded | State-transition vocabulary owned elsewhere. |
| Truth labels | `CONFIRMED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION` | Evidence posture; not policy decisions. |

Do not emit native values into a closed outward schema, map abstention to denial, map evaluator failure to denial, or interpret validator pass as release approval. Preserve reasons, obligations, bundle/evaluator identity, exact input digest, and review/release references. If no accepted mapping exists, hold or error rather than invent a value.

[Back to top](#top)

---

## Policy authoring contract

Every material rule should identify:

- stable package, entrypoint, and version;
- explicit input profile and no-hidden-fetch posture;
- fail-closed defaults;
- native and outward outcomes plus accepted normalization;
- public-safe reasons and enforceable obligations;
- evidence, rights, consent, sensitivity, source-role, lifecycle, review, and release dependencies;
- pinned bundle, evaluator, and source identities;
- synthetic fixtures and positive/negative native tests;
- deterministic validator and hosted workflow;
- receipt metadata and replay requirements;
- effective time, supersession, correction, cache invalidation, and rollback.

A new module is not operationally admissible until path, package identity, evaluator version, inputs, default behavior, outcomes, reasons, obligations, tests, bundle membership, consumer, receipts, and rollback are reviewable. Fixture-first profiles must remain visibly inactive until an accepted integration closes those dependencies.

[Back to top](#top)

---

## Rights, sensitivity, consent, and public exposure

When source rights, consent, living-person or genomic data, archaeology/cultural sovereignty, rare species, critical infrastructure, harmful precision, parcel-person joins, or source-role evidence are unresolved, prefer `DENY`, `HOLD`, `ABSTAIN`, redaction, generalization, aggregation, delay, staged access, or steward review.

Client-side hiding is not a security control. Join-induced sensitivity must propagate. Rules and fixtures must not copy real protected payloads into source, tests, logs, reasons, receipts, or documentation. Public-safe reason codes must not reveal the hidden fact they are protecting.

[Back to top](#top)

---

## Runtime and public trust membrane

1. Public clients use governed APIs and released, policy-filtered artifacts.
2. Browsers, maps, exports, dashboards, and AI adapters must not load or choose bundles directly.
3. Evaluators receive explicit references and normalized context; no hidden canonical-store fetches.
4. Cache keys bind bundle digest, evaluator version, input hash, audience, purpose, expiry, and correction state.
5. Public reasons are safe; detailed reasons may require restricted review.
6. Obligations are enforced downstream or the operation fails closed.
7. Client filters never replace server-side sensitivity/access decisions.
8. AI may explain decisions with citations; it cannot grant permission or bypass denial/abstention.
9. Evaluation errors never fall back to allow.
10. Evaluator administration and bundle upload are not ordinary public routes.
11. A bounded fixture profile is not production policy merely because its dedicated CI passes.
12. Promotion, release, correction, withdrawal, and rollback remain separate governed transitions.

[Back to top](#top)

---

## Correction and rollback

Material policy changes should be versioned, preserve prior source/bundle/evaluator/test identities for replay, record supersession and effective time, reevaluate affected decisions and releases, invalidate caches, emit correction or withdrawal records through owning roots, and restore a prior accepted bundle/selector during rollback rather than copying files into an ambiguous state.

This v0.4.0 README changes no policy behavior. Before merge, close or abandon its draft PR and branch. After merge, revert the README commit and paired generated receipt together, or issue a transparent forward fix. The exact v0.3.1 baseline is blob `6c5021f9d92778581a4e9331a9dd6ddb7efc5e35`; reverting documentation must not restore the deleted `policy/living_persons_geoprivacy.md` path or roll back unrelated child-lane work by implication.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---:|
| POL-001 | Is ADR-0003 still proposed in the governing ADR index? | **CONFIRMED proposed at this snapshot** |
| POL-002 | What is the complete recursive policy inventory and per-lane maturity classification? | **PARTIAL — 523 entries, 40 direct lanes, README coverage, and Rego/native-test counts are confirmed; semantic maturity still requires per-lane review** |
| POL-003 | Which repository-wide evaluator, bundle format, manifest, selector, and activation contract are accepted? | **UNKNOWN** |
| POL-004 | Does the bounded Pass 12 native-test pattern become the general Rego test convention? | **NEEDS DECISION** |
| POL-005 | Will explicit `PolicyInputBundle` profile v1 replace, extend, or remain beside the permissive parent shape? | **NEEDS VERIFICATION / MIGRATION DECISION** |
| POL-006 | What accepted mapping joins native engine results to `ANSWER/ABSTAIN/DENY/ERROR`? | **INACTIVE CANDIDATES EXIST; ACTIVE BINDING UNKNOWN** |
| POL-007 | Which reason, obligation, and reviewer-role registries are adopted, versioned, and enforced by consumers? | **PROPOSED_INACTIVE / UNKNOWN ENFORCEMENT** |
| POL-008 | Which governed consumer is the first accepted end-to-end policy slice? | **UNKNOWN** |
| POL-009 | What decision-receipt schema, persistence, authentication, and replay contract are accepted? | **UNKNOWN** |
| POL-010 | Which policy checks are required by repository rules, and how is independent approval enforced? | **UNKNOWN / NEEDS VERIFICATION** |
| POL-011 | How does the Pass 12 native result bind into `PolicyDecision`, PromotionDecision, ReleaseManifest, correction, and rollback? | **NEEDS IMPLEMENTATION** |
| POL-012 | What rollback drill proves prior-bundle restoration and stale-decision invalidation? | **UNKNOWN** |
| POL-013 | How should `source/` versus `sources/` and `test/` versus `tests/` converge without creating parallel authority or losing references? | **DRIFT / NEEDS DIRECTORY REVIEW** |
| POL-014 | What are the intended writer, reader, retention, and graduation rules for `match-scoring/`, `proof/`, `role/`, `sources/`, `test/`, and `transport/`? | **NEEDS VERIFICATION — five one-byte READMEs and one missing README** |
| POL-015 | What process updates the OPA version and checksum while preserving reproducibility and supply-chain review? | **NEEDS VERIFICATION** |
| POL-016 | Which threshold-policy slots, values, units, operators, owners, evidence bases, consumers, and effective windows are accepted? | **PROPOSED_INACTIVE / ALL VALUES UNRESOLVED** |
| POL-017 | What semantics, if any, supersede deleted `policy/living_persons_geoprivacy.md`, and are any external consumers still unresolved? | **UNKNOWN — path absence confirmed; semantic and external-consumer closure not established** |

[Back to top](#top)

---

## No-loss and evidence ledger

| Baseline element | Disposition in v0.4.0 |
|---|---|
| Stable path, document ID, and H1 | Preserved |
| Policy-as-code plus documentation purpose | Preserved and bounded |
| Allow/deny/restrict/abstain/redaction/release/promotion/sensitivity scope | Preserved; native and outward vocabularies clarified |
| Singular policy root | Preserved; accepted ADR-0029 and `root.policy` projection reverified |
| OPA/Rego, bundles, fixtures, runtime, promotion, sensitivity, rights, release, and UI policy | Preserved and reconciled to current implementation evidence |
| Schema/source/application exclusions | Preserved and expanded |
| Inputs, outputs, validation, review, related folders, status | Preserved and refreshed |
| Maturity, authoring, sensitivity, trust membrane, rollback, open verification | Preserved and updated |
| Direct-child navigation | Repinned to 40 current directories; removed the deleted direct file; deeper detail remains delegated |
| Direct README coverage | Added exact 73-total, 34-substantive, five-one-byte, and one-missing counts |
| Prior uncertainty about Rego tests and validators | Repaired with exact counts: 173 Rego files, one native Rego test, and multiple candidate validators |
| Child-boundary modernization | Linked all 34 substantive direct child indexes without treating prose maturity as implementation |
| `source/`/`sources/` and `test/`/`tests/` drift | Preserved explicitly; no implied migration or parallel authority |
| Deleted `living_persons_geoprivacy.md` direct path | Removed from current topology; semantic supersession and external consumers remain unknown |
| Prior general evaluator, runtime, consumer, receipt, release, and publication holds | Preserved |

Evidence used includes v0.3.1 blob `6c5021f9d92778581a4e9331a9dd6ddb7efc5e35`, `main@737dce6357d670e48df85e94ec0641aaa1a365cb`, accepted ADR-0029, adopted Directory Rules blob `fd49a0b83e55cef52c1124281f093e263526898d`, the `root.policy` projection, ADR-0002/0003/0020 status records, the complete recursive policy tree, direct child metadata, Pass 12 Rego source/tests/fixtures/workflow, `policy-test`, `policy-boundary-guards`, focused policy contract/schema/validator workflows, and the policy-runtime placeholder.

[Back to top](#top)

---

## Changelog

| Version | Date | Change | Rollback |
|---|---|---|---|
| short stub | Before 2026-07-23 | Declared purpose, singular root, basic belongs/exclusions, validation/review/related pointers, and `PROPOSED` status | Historical blob recorded in v0.2 |
| v0.2 | 2026-07-23 | Same-path repository-grounded modernization with required README order, authority split, maturity evidence, workflow boundaries, outcome separation, authoring rules, sensitive/public controls, rollback, and verification register | Restore blob `fa9378a6a699d0985fd018dbdb9f27c15efcb1c3` only if paired v0.3 receipt is also removed |
| v0.3 | 2026-08-09 | Repins the root contract to current main; records ADR-0029 adoption, bounded OPA/Rego execution, inactive fixture-first policy profiles, 18 boundary tests, full direct-child inventory, preserved general readiness holds, and updated validation/rollback/open-work boundaries | Revert the v0.3 README and paired generated receipt together |
| v0.3.1 | 2026-08-10 | Adds the inactive `thresholds/` child to the direct-child map and records that every candidate slot remains value-free, unbound, and held for review. | Revert the threshold-registry candidate commit; no active rule or consumer changes |
| v0.4.0 | 2026-08-13 | Repins the root to current main; reconciles 40 direct lanes, exact README/Rego/native-test coverage, modernized child boundaries, the deleted direct file, current ADR and Root Registry evidence, and unchanged evaluator/release/publication holds. | Revert this README and its generated receipt together; do not restore deleted paths or roll back child lanes by implication. |

<p align="right"><a href="#top">Back to top</a></p>
