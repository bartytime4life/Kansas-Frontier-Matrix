<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-readme
title: tools README
type: README
version: v0.4
status: draft; directory-rules-v2-aligned; root-orchestrator-confirmed; direct-child-inventory-refreshed
owner: "@bartytime4life — verified CODEOWNERS and root-registry route; independent tooling stewardship remains NEEDS VERIFICATION"
created: NEEDS VERIFICATION — file existed before the repo-aware v0.3 update
updated: 2026-08-09
policy_label: repository-facing; tools-root; canonical-root; implementation-bearing; trust-tooling; fail-closed; no-publication-by-tool; non-authoritative
owning_root: tools/
responsibility: canonical repository-tool root for validators, generators, builders, inspectors, comparators, diagnostic probes, bounded operators, and stable repository-facing tooling entrypoints
truth_posture: cite-or-abstain; current-behavior claims require pinned repository evidence; tool output never upgrades itself to evidence, policy, review, release, or publication authority
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 3793c4fd72fecb189e38e39fed17220606120e49
  prior_blob: df9aad984076894d4a9e4aac13cd667995b6700a
  accepted_directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  root_entrypoint_blob: c308015da780d7b72f56277b521fb0e42317651e
  orchestrator_blob: 728cf1404839a5b95e03d70d44567863a6f9b6df
  validator_registry_blob: 12517f368cb1c8b850d3a7138a968cee889875ba
  makefile_blob: 7edd58ecb847a6b911f5eb71c7945247860a7ec4
related:
  - ../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../docs/doctrine/directory-rules.md
  - ../control_plane/root_registry.yaml
  - ../CONTRIBUTING.md
  - ../.github/CODEOWNERS
  - validators/README.md
  - validators/validator_registry.json
  - validate_all.py
  - validators/validate_all.py
  - validators/_common/run_all.py
  - ../Makefile
notes:
  - "v0.4 is a same-path ROOT_FULL documentation modernization; it changes no executable, schema, contract, policy, fixture, test, workflow, dependency, lifecycle, release, runtime, or public behavior."
  - "The first twelve H2 sections implement the accepted Directory Rules v2 ROOT_FULL field order."
  - "tools/validate_all.py is now the confirmed canonical thin entrypoint; it delegates to the registry-driven tools/validators/validate_all.py implementation."
  - "The current registry contains eight validators and four selection profiles; profile success remains bounded validation evidence, not truth or release authority."
  - "The direct-child map records nineteen directories plus README.md and validate_all.py at the pinned base."
  - "tools/experiments/ has an executable file but no boundary README at the pinned base; its ownership and graduation posture remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/`

[![Status: draft](https://img.shields.io/badge/status-draft-f59e0b?style=flat-square)](#adoption-and-conformance-status)
[![Root: canonical](https://img.shields.io/badge/root-canonical-1f6feb?style=flat-square)](#root-class-and-authority-owner)
[![Orchestrator: confirmed](https://img.shields.io/badge/orchestrator-confirmed-1a7f37?style=flat-square)](#validation-and-negative-checks)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](../CONTRIBUTING.md#evidence-and-truth-labels)
[![Publication: none](https://img.shields.io/badge/publication-authority%20none-6e7781?style=flat-square)](#public-exposure-and-sensitivity-posture)

> **One-line purpose.** `tools/` owns reusable repository-wide validators, generators, builders, inspectors, comparators, probes, and operators that support governed KFM work without becoming the authority for doctrine, contracts, schemas, policy, evidence, lifecycle state, release decisions, or public truth.

**Quick navigation:** [Purpose](#purpose) · [Authority](#root-class-and-authority-owner) · [Status](#adoption-and-conformance-status) · [Belongs and prohibited](#what-belongs-and-what-is-prohibited) · [I/O and writers](#inputs-outputs-and-permitted-writers) · [Exposure](#public-exposure-and-sensitivity-posture) · [Storage](#mutability-retention-generation-and-physical-storage) · [Validation](#validation-and-negative-checks) · [Review](#owner-reviewers-and-escalation-path) · [Decisions](#governing-adrs-migrations-aliases-and-canonical-target-if-noncanonical) · [Direct children](#direct-child-directory-map) · [Evidence review](#last-evidence-review-and-review-trigger) · [Invariants](#root-invariants) · [Nearby roots](#tools-vs-nearby-roots) · [Backlog](#maintenance-and-verification-backlog)

> [!IMPORTANT]
> A tool result is a bounded process result. It may support review, evidence resolution, policy evaluation, catalog closure, or release preparation, but it is never sovereign truth, approval, promotion, release, deployment, or publication by itself.

> [!NOTE]
> The canonical repository entrypoint is now [`tools/validate_all.py`](validate_all.py). It delegates to [`tools/validators/validate_all.py`](validators/validate_all.py), which loads the bounded registry at [`tools/validators/validator_registry.json`](validators/validator_registry.json). The historical Make compatibility entrypoint remains [`tools/validators/_common/run_all.py`](validators/_common/run_all.py).

---

## Purpose

`tools/` is the canonical home for durable repository tooling whose primary job is to validate, generate, inspect, compare, package, probe, or operate on governed KFM artifacts. A tool belongs here when it is repository-wide or cross-cutting, has a stable responsibility, is useful beyond one transient maintenance command, and can be reviewed and tested independently.

The root answers this question:

> Which bounded repository tool can perform a declared operation deterministically, expose its inputs and finite outcomes, preserve KFM authority boundaries, and route every output to the responsibility root that owns it?

`tools/` is not a convenience bucket and not a domain root. Domain names may appear below a tooling family when a real validator or operator requires domain scope, but the domain does not gain tooling, schema, policy, evidence, or release authority from that placement.

The canonical lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

Tools may inspect or support transitions in that lifecycle. They may not infer promotion from a file copy, command exit, generated report, commit, pull request, workflow result, or map/UI state.

[Back to top](#top)

---

<a id="authority-level"></a>

## Root class and authority owner

| Field | Current contract |
|---|---|
| **Root ID** | `root.tools` |
| **Root class** | `canonical` |
| **Authority owner** | Repository tooling implementation |
| **Registry responsibility** | Repository-wide validators, generators, builders, inspectors, and operators |
| **Allowed artifact kind** | `repository_tool` |
| **Prohibited artifact kinds** | `data_instance`, `deployable_application`, `release_decision` |
| **Exposure** | `internal` implementation; human-facing README content may be public |
| **Mutation** | `versioned` |
| **Retention** | `repository_lifetime` |
| **Validation profile** | `repository_tooling` |
| **Verified owner/reviewer route** | `@bartytime4life` in the active root registry and CODEOWNERS |

The active [`control_plane/root_registry.yaml`](../control_plane/root_registry.yaml) is a machine projection of adopted placement law. It confirms the current `tools/` root class and responsibility; it does not grant runtime credentials, approve a tool's output, or replace human doctrine.

`tools/` may implement checks and bounded operations. It must not:

- define the semantic meaning of an object family;
- become machine-schema authority;
- decide policy or source admission;
- create evidence or review authority from its own output;
- own canonical lifecycle, receipt, proof, catalog, or published instances;
- make a release, correction, withdrawal, rollback, or publication decision;
- serve public clients as the normal trust path.

[Back to top](#top)

---

<a id="status"></a>

## Adoption and conformance status

| Surface | Status | Evidence-bounded conclusion |
|---|---|---|
| Directory Rules v2 | **ACCEPTED** through [`ADR-0029`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | The exact pinned bytes at [`docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md) govern this README's placement and ROOT_FULL profile. |
| `root.tools` registry entry | **ACTIVE** | `tools/` is the canonical `repository_tool` root with internal exposure and versioned mutation. |
| `tools/README.md` | **CONFIRMED existing / draft documentation** | This v0.4 update is same-path and does not change root authority. |
| [`tools/validate_all.py`](validate_all.py) | **CONFIRMED implemented thin entrypoint** | It imports and returns the orchestrator's `main()` result. |
| [`tools/validators/validate_all.py`](validators/validate_all.py) | **CONFIRMED implemented orchestrator** | It validates a bounded registry, selects validators, executes them no-network, and emits deterministic JSON unless timing is requested. |
| [`validator_registry.json`](validators/validator_registry.json) | **CONFIRMED v1 registry** | Eight validators are registered under `focused`, `changed-area`, `release-dry-run`, and `full` profiles. |
| [`_common/run_all.py`](validators/_common/run_all.py) | **CONFIRMED compatibility entrypoint** | It preserves the historical aggregate fixture runner while delegating to the full orchestrator profile. |
| Root direct-child inventory | **CONFIRMED at the pinned base** | Nineteen directories, this README, and the root validator entrypoint are present. |
| Tool-family implementation maturity | **MIXED** | Some lanes are executable and fixture-tested; others remain documentation-only, proposed, compatibility-bound, or insufficiently reviewed. |
| Public or release authority | **NONE** | No tool path, validator pass, report, receipt, workflow, or badge upgrades an artifact to PUBLISHED state. |
| Independent tooling stewardship | **NEEDS VERIFICATION** | GitHub routing is verified; independent role assignment and enforced separation of duties are not. |

> [!CAUTION]
> The implemented root orchestrator resolves the former placeholder limitation, but it does not make every validator lane implemented. Maturity remains a per-tool claim that must be supported by source, fixtures, tests, workflow evidence, or emitted artifacts tied to a known revision.

[Back to top](#top)

---

<a id="what-belongs-here"></a>
<a id="what-does-not-belong-here"></a>

## What belongs and what is prohibited

### What belongs

Good fits include:

- fail-closed validators for declared contracts, schemas, source roles, evidence closure, rights, sensitivity, policy posture, lifecycle state, release references, correction paths, rollback targets, and public-surface eligibility;
- deterministic generators that create candidate files or derived review outputs from explicit inputs;
- catalog builders that derive catalog candidates from validated processed inputs without authoring release approval;
- comparison, diff, crosswalk, and join helpers that preserve identity, source role, evidence references, temporal scope, and sensitivity inheritance;
- bounded diagnostic probes and no-network verification helpers;
- attestation, proof-pack, source-artifact, spec-hash, QA, and release-support operators that verify or package candidate support objects without owning canonical trust records;
- repository documentation and CI helpers that normalize or report on repository state without becoming platform policy or test authority;
- stable repository-facing wrappers whose implementation responsibility remains here or delegates to an accepted reusable package.

### What is prohibited

| Prohibited in `tools/` | Owning root or boundary |
|---|---|
| Semantic meaning and invariants | [`contracts/`](../contracts/) |
| Canonical machine shapes, contexts, DTOs, or OpenAPI | [`schemas/`](../schemas/) |
| Normative allow, deny, hold, restrict, or abstain rules | [`policy/`](../policy/) |
| Source descriptors, source activation, rights, cadence, or registry identity | [`data/registry/`](../data/registry/) and governed source admission |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED instances | The corresponding [`data/`](../data/) lane |
| Canonical receipts, proofs, and released carriers | [`data/receipts/`](../data/receipts/), [`data/proofs/`](../data/proofs/), and [`data/published/`](../data/published/) |
| Release manifests, promotion decisions, corrections, withdrawals, rollback cards, or signatures | [`release/`](../release/) |
| Reusable synthetic fixtures and executable tests | [`fixtures/`](../fixtures/) and [`tests/`](../tests/) |
| Shared importable library implementation | [`packages/`](../packages/) |
| External-source acquisition and admission | [`connectors/`](../connectors/) |
| Lifecycle orchestration or declarative run graphs | [`pipelines/`](../pipelines/) and [`pipeline_specs/`](../pipeline_specs/) |
| Thin one-off wrappers with no unique trust logic | Top-level [`scripts/`](../scripts/) |
| Deployable APIs, UIs, workers, or runtime services | [`apps/`](../apps/) and [`runtime/`](../runtime/) |
| Secrets, credentials, private terms, signing keys, protected exact locations, or restricted payloads | Denied from tracked repository tooling and public documentation |

A tool must not create a parallel contract, schema, policy, registry, receipt, proof, release, catalog, or canonical data home merely because writing beside the executable is convenient.

[Back to top](#top)

---

<a id="inputs-and-outputs"></a>
<a id="inputs"></a>
<a id="outputs"></a>

## Inputs, outputs, and permitted writers

### Inputs

A tool may read only inputs that its own contract and the caller's authority permit, including:

- contracts, schemas, policy bundles, and machine governance projections;
- source, dataset, layer, rights, sensitivity, or crosswalk registry records;
- lifecycle instances from an allowed phase;
- synthetic fixtures and executable tests;
- release, correction, withdrawal, or rollback records when a tool is checking them;
- explicit repository-relative paths, identifiers, and output destinations;
- non-secret configuration and workflow metadata.

Inputs should be pinned, bounded, or reproducible where the governing object contract requires it. A tool must not silently widen scope, infer a missing authority object, read secrets, follow unsafe symlinks, or enable network access as a fallback.

### Outputs

Permitted outputs are role-labeled and destination-bound:

| Output class | Required destination posture |
|---|---|
| Validation, diff, probe, QA, or reviewer report | Caller-selected local path, CI artifact, or accepted report lane; never truth authority |
| Generated candidate | Explicit path under the root that owns the candidate's meaning |
| Receipt | Canonical receipt family under `data/receipts/`; process memory only |
| Proof candidate | Canonical proof family under `data/proofs/`; support only |
| Catalog candidate | Governed catalog-building flow into `data/catalog/` |
| Release-support report or draft | Accepted candidate/support path; never a release decision |
| Temporary build or QA output | Ignored local storage, external CI artifact, or the bounded `artifacts/` compatibility lanes permitted by Directory Rules |

Every output must distinguish report, candidate, receipt, proof, catalog projection, release-support draft, and released artifact. A tool must not relabel a lower-authority output as a higher-authority object.

### Permitted writers

- Repository contributors and automation may modify tool source only through the repository's reviewed contribution path and applicable platform controls.
- The active root registry and CODEOWNERS currently route ownership and review to `@bartytime4life`; that routing is not runtime authorization or proof of review.
- Tool processes may write only to explicit, caller-authorized destinations allowed by the tool contract.
- Public clients, renderers, model runtimes, watchers, and ordinary UI surfaces have no canonical write capability through this root.
- A tool that needs broader write authority must stop, declare the target object family, and use the owning root's policy and review path rather than expanding itself silently.

[Back to top](#top)

---

## Public exposure and sensitivity posture

`tools/` implementation is repository-internal. This README and other public documentation may describe bounded behavior, but tools are not public service endpoints and their raw outputs are not public by default.

| Concern | Required posture |
|---|---|
| Public API/UI/map/AI use | **DENY direct use.** Public surfaces consume governed APIs and released public-safe artifacts. |
| Sensitive or rights-limited input | Use synthetic fixtures, redaction, generalization, quarantine, staged access, or denial as required by the owning policy. |
| Logs and reports | Minimize values; prefer reason codes, safe identifiers, hashes, and bounded paths. Do not echo secrets, private terms, precise protected coordinates, or reconstruction hints. |
| Network access | No-network by default for validation and test paths; any exception must be explicit, reviewed, bounded, and separately testable. |
| Model output | Interpretive input only. Generated language cannot replace EvidenceBundle, policy, review, or release state. |
| Failure detail | Public-facing output must not reveal restricted reason data; route sensitive diagnostics to authorized review surfaces. |

When rights, sovereignty, cultural sensitivity, living-person or genomic data, rare-species locations, archaeology, infrastructure, land/title data, or harmful precision are unresolved, the safe tooling outcome is `HOLD`, `DENY`, `RESTRICT`, `ABSTAIN`, or quarantine—not best-effort publication.

[Back to top](#top)

---

## Mutability, retention, generation, and physical storage

| Property | Root contract |
|---|---|
| Source and documentation mutability | Versioned in Git; ordinary changes use reviewable commits and preserve history. |
| Retention | Repository lifetime unless a child contract defines a narrower deprecation or compatibility window. |
| Generated code or documentation | Must declare source, generator identity, digest, edit policy, and regeneration command. |
| Temporary outputs | Ignored local storage, external CI artifacts, or permitted `artifacts/build`, `artifacts/docs`, `artifacts/qa`, and `artifacts/temporary` compatibility lanes. |
| Durable accountability objects | Written only to canonical receipt, proof, catalog, release, or published families—not left in `tools/` or `artifacts/`. |
| Caches, virtual environments, and dependency installs | Local or CI cache only; never tracked as authority. |
| External physical storage | A tool may emit or verify locators only through a governed manifest/registry record; the locator itself is not authority. |

Tool source should be side-effect bounded. Write-capable tools must document overwrite behavior, atomicity, symlink handling, path traversal controls, partial-failure cleanup, idempotency, and rollback or forward-correction behavior.

`tools/experiments/` is present in the current tree but lacks a boundary README at the pinned base. Its `temporal_slice_store.py` implementation does not receive permanent authority from the folder name. Placement, owner, consumers, test evidence, graduation target, and retention remain **NEEDS VERIFICATION**.

[Back to top](#top)

---

<a id="validation"></a>

## Validation and negative checks

### Canonical orchestrator

The current root validation surface is registry-driven:

```bash
# Inspect available profiles and validator IDs.
python tools/validate_all.py --list

# Validate registry structure and referenced scripts without running validators.
python tools/validate_all.py --validate-registry

# Run the default full profile.
python tools/validate_all.py --profile full

# Run one named validator.
python tools/validate_all.py --validator evidence-bundle

# Select validators whose declared globs match changed paths.
python tools/validate_all.py \
  --profile changed-area \
  --changed-path schemas/contracts/v1/evidence/evidence_bundle.schema.json

# Preserve the historical aggregate Make surface.
make schemas
```

The orchestrator's confirmed contract is:

| Surface | Current behavior |
|---|---|
| Registry | `tools/validators/validator_registry.json`; bounded JSON, duplicate-key denial, normalized repository-relative paths, referenced-script existence checks |
| Profiles | `focused` (4), `changed-area` (path-selected), `release-dry-run` (5), `full` (8) |
| Execution environment | `KFM_NO_NETWORK=1`, deterministic hash seed, UTC, no bytecode writes, captured output, per-validator timeout |
| Default report | Stable, sorted JSON without timing; optional `--include-timing` is explicitly nondeterministic |
| Validator result mapping | Return `0` -> `PASS`; `1` -> `FAIL`; other return or timeout -> `ERROR` |
| Orchestrator exits | `0` for `PASS` or no-match `ABSTAIN`; `1` for validation failure; `2` for orchestrator/configuration/I/O error |
| No-match changed-area result | `ABSTAIN` with reason `NO_MATCHING_VALIDATORS`; this is not proof that an unselected area is valid |
| Output write | Optional caller-supplied path, temporary-file replacement, symlink denial |

The root entrypoint is canonical for new callers. [`tools/validators/_common/run_all.py`](validators/_common/run_all.py) is retained as the historical aggregate compatibility surface used by `make schemas` and existing workflow expectations.

### README source checks

A documentation-only update to this file should verify at least:

1. one H1 and the exact first-twelve-H2 ROOT_FULL field order;
2. balanced fenced code blocks and no heading-level jumps;
3. unique explicit anchors and valid same-document fragments;
4. repository-relative links to verified paths;
5. no tabs, trailing whitespace, hidden control characters, or missing final newline;
6. a direct-child map matching the pinned repository tree;
7. claims about implementation, tests, workflows, and authority remain bounded to inspected evidence;
8. no secret, restricted source content, precise protected location, or private review material is present.

### Tool negative checks

A trust-bearing tool should fail closed on applicable cases:

- missing, malformed, duplicate-key, oversized, unsafe, or unsupported inputs;
- symlinks, path traversal, repository escape, unsafe output replacement, or ambiguous destinations;
- absent contract, schema, source identity, evidence reference, policy decision, review state, release reference, correction path, or rollback target;
- unknown rights, stale source, unresolved sensitivity, over-precise geometry, source-role collapse, or unsupported temporal/spatial scope;
- network access introduced where the declared profile is no-network;
- validator timeout, dependency failure, unexpected return code, or partial write;
- a skipped or unselected check being misreported as `PASS`;
- a report, receipt, proof candidate, catalog candidate, or workflow result being treated as publication authority.

> [!WARNING]
> `PASS` means only that the selected validator contract passed for the declared inputs and version. It does not prove the underlying real-world claim, evidence completeness, rights clearance, policy approval, human review, release readiness, public safety, or KFM publication.

[Back to top](#top)

---

<a id="review-burden"></a>

## Owner, reviewers, and escalation path

[`.github/CODEOWNERS`](../.github/CODEOWNERS) routes all repository paths to `@bartytime4life` by default and explicitly routes `tools/validators/` and `tools/watchers/` to that account. The active root registry names the same owner, permitted writer, and reviewer. These are verified repository routing facts, not proof that review occurred or that independent separation of duties is enforced.

| Change | Minimum review posture |
|---|---|
| README-only correction with no changed meaning | Root owner or verified documentation review route |
| New direct child or reclassification under `tools/` | Root owner plus affected consumer; Directory Rules/ADR review if authority, identity, compatibility, or dependency direction changes |
| Validator or generator behavior | Tooling review plus the owners of affected contracts, schemas, fixtures, tests, policy, source/evidence, or release surfaces |
| Write-capable operator | Owning output-family review plus negative path, atomicity, and rollback evidence |
| Watcher or ingest-adjacent helper | Source/domain review; rights, sensitivity, policy, and non-publisher boundary review as applicable |
| Sensitive-domain handling | Appropriate sensitivity, sovereignty, privacy, security, or domain review before use |
| Release-support or attestation tooling | Release and integrity review; the tool cannot self-approve its output |
| Security defect | Follow [`SECURITY.md`](../SECURITY.md) and keep exploit or credential details out of public issues and PRs |

Escalate to `HOLD` rather than choosing a convenient path when:

- root or object-family ownership is ambiguous;
- a proposed tool would duplicate another writable authority;
- a child lane changes from experimental or compatibility status to durable authority;
- network, credential, sensitive-data, public-surface, or release effects are unclear;
- a tool's output would be consumed as evidence, policy, review, release, or publication state without an accepted contract.

Independent tooling stewardship and author/approver separation remain **NEEDS VERIFICATION**. A future stewardship assignment should update the root registry, CODEOWNERS, this README, and affected child contracts together without inventing an identity.

[Back to top](#top)

---

<a id="related-folders"></a>
<a id="adrs"></a>

## Governing ADRs, migrations, aliases, and canonical target if noncanonical

| Item | State | Effect on `tools/` |
|---|---|---|
| [`ADR-0029`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **ACCEPTED** | Adopts the exact Directory Rules v2 bytes and makes [`docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md) the writable human placement authority. |
| Directory Rules v2 `DIR-EXEC-006` | **ADOPTED rule** | `tools/validate_all.py` may be a thin repository entrypoint while implementation lives under `tools/validators/`. |
| `root.tools` projection | **ACTIVE** | Confirms canonical root class, allowed/prohibited artifacts, exposure, mutation, retention, ownership, and validation profile. |
| Root validator entrypoint | **CONFIRMED current implementation** | New callers use `python tools/validate_all.py`; implementation lives in `tools/validators/validate_all.py`. |
| Historical aggregate runner | **CONFIRMED compatibility surface** | `tools/validators/_common/run_all.py` and `make schemas` delegate to the full profile; they are not a second validator registry. |
| `tools/crosswalks/` lane | **EXISTING / lane contract NEEDS VERIFICATION** | Its README still carries a July placement hold. This root README records the existing child without granting a new crosswalk registry, contract, schema, or policy authority. |
| `tools/experiments/` lane | **EXISTING / boundary NEEDS VERIFICATION** | No README is present at the pinned base; classify and graduate, move, or constrain the implementation through a separate reviewed change. |
| Watcher/tooling overlap | **NEEDS VERIFICATION / previously recorded as CONFLICTED** | Reconcile `tools/watchers/`, `tools/ingest/`, `pipelines/watchers/`, and `pipeline_specs/watchers/` before adding another writer or scheduler. |
| Root canonical target | **N/A** | `tools/` is canonical, not a compatibility or deprecated root. |
| Root aliases | **None verified** | Child compatibility entrypoints are documented locally; no root alias is created here. |

### Related responsibility roots

| Responsibility | Canonical location | Boundary |
|---|---|---|
| Human doctrine and guidance | [`docs/`](../docs/) | Explains; does not implement repository tooling |
| Machine governance projection | [`control_plane/`](../control_plane/) | Projects adopted authority; cannot amend it |
| Meaning, shape, and admissibility | [`contracts/`](../contracts/) · [`schemas/`](../schemas/) · [`policy/`](../policy/) | Tools consume; they do not own these authorities |
| Source identity and lifecycle instances | [`data/registry/`](../data/registry/) · [`data/`](../data/) | Tools inspect or derive under explicit authority; they do not own the data |
| Receipts, proofs, and published carriers | [`data/receipts/`](../data/receipts/) · [`data/proofs/`](../data/proofs/) · [`data/published/`](../data/published/) | Durable objects leave the tooling root |
| Release decisions | [`release/`](../release/) | Tool output may support but never replace release authority |
| Tests and fixtures | [`tests/`](../tests/) · [`fixtures/`](../fixtures/) | Prove bounded behavior and provide synthetic inputs |
| Shared libraries | [`packages/`](../packages/) | Reused implementation belongs here rather than in a CLI wrapper |
| Source acquisition and lifecycle orchestration | [`connectors/`](../connectors/) · [`pipelines/`](../pipelines/) · [`pipeline_specs/`](../pipeline_specs/) | Tools must not become a second connector or pipeline authority |
| Thin one-off wrappers | [`scripts/`](../scripts/) | Graduate only when durable repository-tool responsibility is proven |
| Deployables and runtime composition | [`apps/`](../apps/) · [`runtime/`](../runtime/) | Public and running systems remain downstream of trust |

[Back to top](#top)

---

<a id="responsibility-map"></a>
<a id="directory-tree"></a>
<a id="minimal-future-layout"></a>
<a id="verified-lane-index"></a>

## Direct-child directory map

The following map is **CONFIRMED** from the pinned `main` tree and intentionally stops at direct children, as required by `DIR-README-003` and `DIR-README-004`.

```text
tools/
├── README.md                 # this ROOT_FULL authority and routing document
├── attest/                   # attestation packaging and verification helpers
├── catalog_builders/         # catalog-candidate builders and index helpers
├── ci/                       # CI-facing repository support helpers
├── crosswalks/               # crosswalk comparison and candidate-preparation helpers
├── diff/                     # deterministic comparison helpers
├── docs/                     # documentation QA, normalization, and rendering helpers
├── experiments/              # existing experimental implementation; boundary review required
├── generators/               # deterministic candidate and derived-output generators
├── ingest/                   # ingest-adjacent preflight and review-signal helpers
├── joins/                    # candidate join and anti-collapse helpers
├── probes/                   # bounded diagnostics
├── proof_pack/               # proof-pack candidate assembly and checking helpers
├── qa/                       # repository QA and reviewer-summary helpers
├── release/                  # release dry-run and release-support tooling; no release authority
├── scripts/                  # tool-local thin/compatibility entrypoints
├── source_artifacts/         # local content-addressed SourceArtifact verification helpers
├── spec_hash/                # deterministic spec-hash CLI boundary
├── validate_all.py           # canonical thin root validator entrypoint
├── validators/               # validator implementation, registry, and family routing
└── watchers/                 # watcher-tooling routing; non-publisher boundary
```

### Direct-child evidence ledger

| Entry | Documented responsibility | Current evidence boundary |
|---|---|---|
| [`attest/`](attest/README.md) | Attestation packaging and verification | README confirmed; signing backend and full execution matrix remain per-tool claims. |
| [`catalog_builders/`](catalog_builders/README.md) | Catalog candidate and index building | README confirmed; no catalog or release authority. |
| [`ci/`](ci/README.md) | CI-support helpers | README confirmed; workflow wiring must be inspected separately. |
| [`crosswalks/`](crosswalks/README.md) | Crosswalk comparison, reconciliation, and candidate preparation | README confirmed; lane-specific placement and executable inventory need renewed review. |
| [`diff/`](diff/README.md) | Deterministic machine-readable comparison | README confirmed; implementation maturity is per helper. |
| [`docs/`](docs/README.md) | Documentation normalization, rendering, and QA helpers | README confirmed; generated previews are not docs authority. |
| [`experiments/`](experiments/) | Current `temporal_slice_store.py` experiment | Executable presence confirmed; boundary README, owner, tests, consumers, and graduation target are not verified here. |
| [`generators/`](generators/README.md) | Deterministic candidate generation | README confirmed; outputs remain owned by destination roots. |
| [`ingest/`](ingest/README.md) | Ingest-adjacent preflight and drift signals | README confirmed; must not become a connector or publisher. |
| [`joins/`](joins/README.md) | Candidate joins and source-role anti-collapse | README confirmed; policy and evidence closure remain external authority. |
| [`probes/`](probes/README.md) | Bounded diagnostics | README confirmed; production behavior is not inferred. |
| [`proof_pack/`](proof_pack/README.md) | Proof-pack candidate support | README confirmed; canonical proof objects live under `data/proofs/`. |
| [`qa/`](qa/README.md) | Repository QA and reviewer summaries | README confirmed; QA result is not release proof. |
| [`release/`](release/README.md) | Release dry-run, manifest, correction, and rollback support | README confirmed; current implementation is mixed and creates no release authority. |
| [`scripts/`](scripts/README.md) | Tool-local wrappers and compatibility entrypoints | README confirmed; relationship to top-level `scripts/` remains a review boundary. |
| [`source_artifacts/`](source_artifacts/README.md) | Local deterministic content-addressed storage/verification helper | README and helper boundary confirmed; no production storage, retention, or evidence authority. |
| [`spec_hash/`](spec_hash/README.md) | Thin repository CLI over reusable canonicalization/hashing logic | README and implemented slice confirmed; hash equality is integrity evidence only. |
| [`validators/`](validators/README.md) | Validator implementation, registry, and routing | README plus implemented root orchestrator and bounded registry confirmed; lane maturity varies. |
| [`watchers/`](watchers/README.md) | Watcher-tooling routing | README confirmed; watchers remain non-publishers and placement overlap needs review. |
| [`README.md`](README.md) | Root authority, routing, and evidence boundary | This document. |
| [`validate_all.py`](validate_all.py) | Canonical thin validator entrypoint | Implemented; delegates to the registry-driven orchestrator. |

A child README owns deeper detail. This root map does not duplicate recursive trees or convert a documented lane into implemented authority.

[Back to top](#top)

---

<a id="last-reviewed"></a>

## Last evidence review and review trigger

| Field | Value |
|---|---|
| **Review date** | `2026-08-09` |
| **Pinned base** | `main@3793c4fd72fecb189e38e39fed17220606120e49` |
| **Target baseline** | Complete `tools/README.md` v0.3 at blob `df9aad984076894d4a9e4aac13cd667995b6700a` |
| **Authority evidence** | Accepted ADR-0029, exact Directory Rules v2 bytes, active root registry, and CODEOWNERS |
| **Implementation evidence** | Current direct-child tree, root entrypoint, orchestrator, validator registry, historical compatibility runner, Makefile, validators README, crosswalk/source-artifact/spec-hash READMEs, and experiments inventory |
| **Review type** | Same-path README reconciliation, ROOT_FULL conformance, direct-child inventory, command/exit-boundary verification, link/anchor audit, and claim-boundary review |
| **Not established** | Exhaustive recursive tool inventory; every child tool's test or hosted-CI result; branch-protection enforcement; production scheduling; external storage; signing; live network behavior; runtime use; release, deployment, or publication |
| **Risk-based maximum interval** | No calendar interval is asserted by this README; event-based triggers below control re-review. |

Re-review this README when any of the following occurs:

- a direct child is added, removed, renamed, reclassified, or given a new writer;
- the root registry, Directory Rules, ADR-0029 status, CODEOWNERS, or validation profile changes;
- the root entrypoint, validator registry schema, profile membership, exit code, deterministic-report contract, or Make compatibility path changes;
- `tools/experiments/`, `tools/crosswalks/`, `tools/watchers/`, `tools/ingest/`, or `tools/scripts/` is migrated, graduated, or retired;
- a tool gains network, secret, sensitive-data, public-surface, lifecycle-write, proof, catalog, or release-support capability;
- a security incident, correction, rollback, path-drift finding, or compatibility deadline affects this root.

[Back to top](#top)

---

## Root invariants

| Invariant | Required behavior | Denied shortcut |
|---|---|---|
| Tools support; they do not self-authorize. | Results remain bounded inputs to governed review and downstream decisions. | A report or exit code is treated as truth, policy, approval, or publication. |
| One authority per object family. | Meaning, shape, admissibility, instances, and decisions remain in their owning roots. | Tool-local parallel schema, contract, policy, registry, receipt, proof, or release home. |
| Validators fail closed. | Missing or unresolved support returns finite failure, hold, deny, restrict, abstain, or error. | Skip, timeout, or missing dependency reported as success. |
| Watchers are non-publishers. | Watchers detect and propose; promotion remains separate. | Direct writes to PROCESSED, CATALOG, TRIPLETS, PUBLISHED, or release state. |
| Source roles remain explicit. | Observed, modeled, aggregate, candidate, regulatory, administrative, contextual, and synthetic support stays distinct. | Publication, rendering, AI, or tooling silently upgrades source authority. |
| Most restrictive posture propagates. | Rights, sensitivity, consent, sovereignty, geoprivacy, infrastructure, and living-person constraints follow derivatives. | A weaker downstream surface drops upstream restrictions. |
| Public clients stay downstream. | Public surfaces use governed APIs and released public-safe carriers. | Direct public reads from tool output, internal stores, watcher candidates, or model runtimes. |
| Corrections remain visible. | Supersession, withdrawal, correction, rollback, and prior-state identity remain auditable. | In-place mutation erases public lineage. |
| Deterministic identity is preferred. | Inputs, registry, tool version, output hash, and finite result are recordable where practical. | Unpinned or irreproducible output is presented as settled evidence. |

[Back to top](#top)

---

## `tools/` vs nearby roots

| Root | Owns | Use `tools/` instead when |
|---|---|---|
| [`scripts/`](../scripts/) | Thin one-off or routine invocation wrappers with no unique trust logic. | Behavior becomes durable, reusable, repository-wide, trust-bearing, fixture-tested, or workflow-invoked. |
| [`packages/`](../packages/) | Reusable importable library implementation. | The primary product is a repository CLI, checker, builder, inspector, probe, or operator; reusable internals may still live in a package. |
| [`connectors/`](../connectors/) | External-source acquisition and admission edge. | Inputs are already supplied and the helper only validates, compares, hashes, packages, or reports. |
| [`pipelines/`](../pipelines/) | Executable lifecycle transformation and orchestration. | Logic is a reusable validator or support operator invoked by multiple flows. |
| [`pipeline_specs/`](../pipeline_specs/) | Declarative run graphs, schedules, inputs, outputs, and resource envelopes. | The artifact executes rather than declares behavior. |
| [`tests/`](../tests/) | Executable proof of behavior. | The code is the implementation being tested. |
| [`fixtures/`](../fixtures/) | Synthetic positive, negative, denied, abstain, and golden examples. | The file generates, validates, or inspects fixtures. |
| [`apps/`](../apps/) / [`runtime/`](../runtime/) | Deployable processes and bounded runtime composition. | The code is repository support and must never serve public clients directly. |

[Back to top](#top)

---

<a id="standard-outcome-posture"></a>

## Finite outcome posture

Exact enums belong to each tool's contract. The root-level vocabulary is guidance for compatible, fail-closed behavior—not a prose override of machine schemas.

| Outcome family | Meaning |
|---|---|
| `PASS` / `NO_CHANGE` | The selected operation completed and found no blocker for its declared scope. |
| `CHANGE_CANDIDATE` / `ROUTE` | A candidate or routing result was produced for downstream review. |
| `FAIL` | A configured check rejected the input. |
| `DENY` | The requested use is not allowed. |
| `RESTRICT` | Use is permitted only under stated constraints and review. |
| `HOLD` | Required authority, evidence, rights, sensitivity, review, release, correction, or rollback support is unresolved. |
| `ABSTAIN` | The tool lacks sufficient support to make the requested assertion; no-match selection may be one bounded case. |
| `NEEDS_REVIEW` | Human or steward review is required before further use. |
| `PUBLIC_SURFACE_DENIED` | The candidate cannot enter public API, UI, map, tile, graph, search, export, Focus Mode, or AI surfaces. |
| `ERROR` / `SYSTEM_ERROR` | Configuration, I/O, dependency, timeout, malformed input, or unexpected execution prevented completion. |

A process may exit zero for a documented no-op or `ABSTAIN`; callers must inspect the structured outcome rather than equating zero with substantive validation.

[Back to top](#top)

---

## Negative-state checklist

Every trust-bearing tool should test applicable negative states:

- missing or malformed contract, schema, registry, source, evidence, policy, review, release, correction, or rollback input;
- stale source head, unresolved cadence, withdrawn consent, unknown rights, or attribution omission;
- sensitivity mismatch, precise restricted geometry, missing redaction/generalization record, or downstream restriction loss;
- source-role collapse, modeled-to-observed upgrade, aggregate-to-place overclaim, or generated-text authority;
- direct public/runtime access to internal data or tool output;
- tool attempt to promote, publish, mutate another authority root, or silently widen its write scope;
- registry drift, duplicate IDs or keys, unsafe path, symlink, path escape, oversized input, timeout, or partial output;
- missing fixture or skipped/unselected validation incorrectly reported as `PASS`;
- logs, reports, or errors exposing credentials, private terms, protected coordinates, or reconstruction hints.

[Back to top](#top)

---

<a id="acceptance-checklist"></a>
<a id="maintenance-and-verification-backlog"></a>

## Maintenance and verification backlog

- [ ] Inventory every executable below the nineteen direct-child directories and classify it as implemented, placeholder, experimental, generated, compatibility, deprecated, or dead.
- [ ] Add or adopt a bounded `tools/experiments/` boundary contract, then graduate, relocate, or explicitly constrain `temporal_slice_store.py` with tests and consumers identified.
- [ ] Reconcile the stale placement hold in `tools/crosswalks/README.md` against the accepted v2 responsibility model and current executable inventory.
- [ ] Reconcile watcher responsibilities and writers across tooling, pipeline implementation, and pipeline specifications before adding another watcher lane.
- [ ] Decide whether `tools/scripts/` remains a compatibility family or should converge on top-level `scripts/` and other owning roots.
- [ ] Keep validator registry profile membership, path globs, timeouts, artifact references, exit codes, and Make compatibility behavior synchronized with tests and workflow expectations.
- [ ] Verify each documented command in a safe environment when its implementation changes; do not copy old pass counts or workflow conclusions into this root README.
- [ ] Verify write-capable tools route durable receipts, proofs, catalogs, release-support objects, and published carriers only to canonical families.
- [ ] Add sensitive, rights-limited, stale, denied, abstain, timeout, unsafe-path, and partial-write fixtures where tool risk warrants them without exposing protected content.
- [ ] Establish independently reviewable tooling stewardship when repository maturity and policy-significant release duties require separation of duties.

[Back to top](#top)

---

## Changelog

| Date | Version | Change | Status |
|---|---|---|---|
| 2026-08-09 | v0.4 | Aligned the root README with accepted Directory Rules v2 and the active root registry; replaced stale placeholder-orchestrator claims with the implemented registry-driven contract; added the current direct-child map and newly observed lanes; refreshed validation, writer, exposure, storage, review, migration, outcome, negative-state, and review-trigger guidance while preserving stable identity and legacy anchors. | **CONFIRMED documentation update / executable behavior unchanged** |
| 2026-07-23 | v0.3 | Modernized the canonical-root README in place; aligned the prior H2 order; replaced a speculative future tree with a verified README-lane index; surfaced placeholder orchestrators and watcher-placement conflict; repaired owner, review, validation, ADR, related-root, badge, and evidence-review guidance. | **CONFIRMED historical documentation change** |
| 2026-07-08 | v0.2 | Updated the tools root README from pasted scaffold to a repo-aware root contract reflecting then-confirmed validator and watcher README surfaces. | **CONFIRMED historical documentation change** |

[Back to top](#top)
