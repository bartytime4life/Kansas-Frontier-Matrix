<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-readme
title: tools README
type: README
version: v0.3
status: draft
owner: NEEDS VERIFICATION — GitHub review routing currently resolves to @bartytime4life; separate tooling stewardship is not verified
created: NEEDS VERIFICATION — file existed before this repo-aware update
updated: 2026-07-23
policy_label: repository-facing; tools-root; canonical-root; implementation-bearing; trust-tooling; fail-closed; no-publication-by-tool; non-authoritative
owning_root: tools/
responsibility: canonical implementation root for reusable repo-wide validators, generators, builders, checkers, comparators, diagnostic probes, bounded source-review helpers, QA helpers, attestation helpers, release-support helpers, and thin durable tooling entrypoints
truth_posture: cite-or-abstain; implementation claims require current repository evidence
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 20c8a98beee2219fa8ae673981f9bc41c586fdb9
  prior_blob: 02c9e71420af8afe029e7ce25829d86a59696cc1
  directory_rules_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  sampled_orchestrator_blobs:
    - tools/validate_all.py@5f01ac208c46f4ee98750af4fc1032604b670e9b
    - tools/validators/validate_all.py@2f04d2dcbae2f5f2c5657a15559b005c61ed3598
related:
  - ../docs/architecture/directory-rules.md
  - ../CONTRIBUTING.md
  - ../.github/CODEOWNERS
  - validators/README.md
  - watchers/README.md
  - ingest/README.md
  - generators/README.md
  - catalog_builders/README.md
  - proof_pack/README.md
  - release/README.md
  - qa/README.md
  - attest/README.md
  - ci/README.md
notes:
  - "v0.3 is a same-path, documentation-only modernization of the tools root README."
  - "The required canonical-root README contract follows Directory Rules §15."
  - "Confirmed child README presence establishes documentation surfaces only; it does not prove executable behavior, CI wiring, runtime use, or release authority."
  - "Both validate_all.py paths sampled in this review are docstring-only PROPOSED placeholders. No operational root validator command is claimed."
  - "Watcher placement remains CONFLICTED across tools/watchers/, tools/ingest/, pipelines/watchers/, and pipeline_specs/watchers/; do not create another implementation lane without reconciliation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools

[![Status: draft](https://img.shields.io/badge/status-draft-f59e0b?style=flat-square)](#status)
[![Authority: canonical implementation root](https://img.shields.io/badge/authority-canonical%20implementation%20root-1f6feb?style=flat-square)](#authority-level)
[![Truth posture: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](../CONTRIBUTING.md#evidence-and-truth-labels)
[![Publication: not an authority](https://img.shields.io/badge/publication-not%20an%20authority-6e7781?style=flat-square)](#authority-level)
[![Validation: placeholder aware](https://img.shields.io/badge/validation-placeholder%20aware-8250df?style=flat-square)](#validation)

> **One-line purpose.** `tools/` is the canonical implementation root for reusable, trust-bearing repository tooling that checks, builds, compares, packages, probes, or reports on governed KFM artifacts without becoming doctrine, schema, policy, evidence, lifecycle, release, or public-runtime authority.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related roots](#related-folders) · [ADRs](#adrs) · [Lane index](#verified-lane-index) · [Outcomes](#standard-outcome-posture) · [Backlog](#maintenance-and-verification-backlog)

> [!IMPORTANT]
> A tool result is a **review signal or governed input**, not sovereign truth. A successful check does not by itself establish evidence closure, policy approval, release readiness, publication, public safety, or KFM `PUBLISHED` state.

> [!CAUTION]
> No operational root validator command is confirmed in this review. Both [`tools/validate_all.py`](validate_all.py) and [`tools/validators/validate_all.py`](validators/validate_all.py) are currently docstring-only `PROPOSED` placeholders. Watcher placement is also unresolved across `tools/watchers/`, `tools/ingest/`, `pipelines/watchers/`, and `pipeline_specs/watchers/`.

---

## Purpose

`tools/` owns durable executable support used across the repository: validators, generators, builders, checkers, comparators, diagnostic probes, bounded source-review helpers, QA helpers, attestation helpers, release-support helpers, and thin tooling entrypoints.

The durable question for this root is:

> Which reusable repository tool can inspect or derive a governed artifact deterministically, expose its assumptions and outcomes, route outputs to the correct responsibility root, and fail closed without claiming authority it does not have?

`tools/` is where long-lived helpers graduate when they become reusable, trust-bearing, reviewable, and testable. It is not a convenience bucket, a domain root, or a substitute for the responsibility roots that own meaning, shape, policy, evidence, lifecycle data, release records, tests, fixtures, pipelines, packages, or public runtime behavior.

[Back to top](#top)

---

## Authority level

| Field | Authority |
|---|---|
| **Directory class** | **Canonical, implementation-bearing root** |
| **Primary responsibility** | Repo-wide validators, generators, builders, checkers, comparators, probes, and reusable trust-support helpers |
| **May do** | Read governed inputs; perform deterministic checks or transformations; emit bounded reports, candidates, drafts, summaries, or support artifacts to accepted destinations |
| **Must not do** | Define domain meaning, own machine schemas, decide policy, admit sources, create evidence authority, approve release, publish artifacts, or serve public clients |
| **Public-path posture** | **DENY direct public use.** Public API, UI, map, tile, graph, search, export, Focus Mode, and AI surfaces consume released public-safe artifacts through governed interfaces |
| **Promotion posture** | Tool output may support a promotion decision; it is never the promotion decision by itself |
| **Truth posture** | Cite or abstain; preserve source roles, uncertainty, rights, sensitivity, correction lineage, and rollback requirements |

The canonical lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Tools may support checks at lifecycle boundaries. They must not collapse promotion into a file move, a passing exit code, a generated report, a commit, or a pull request.

[Back to top](#top)

---

## Status

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| `tools/README.md` | **CONFIRMED** at the pinned base; this revision is v0.3 | Canonical-root documentation exists and is being modernized in place |
| Direct child README lanes listed in the [verified lane index](#verified-lane-index) | **CONFIRMED README presence** | Documentation boundaries exist; executable maturity varies and remains separately bounded |
| `tools/validators/` | **CONFIRMED extensive README index; sampled scripts are placeholders** | Validator documentation is broad; implementation and enforcement must be verified file by file |
| `tools/watchers/` | **CONFIRMED README-only parent plus one direct child README in its bounded inventory** | No active watcher framework is established by this path; placement is **CONFLICTED** |
| `tools/validate_all.py` | **CONFIRMED file; docstring-only `PROPOSED` placeholder** | Not an operational orchestrator |
| `tools/validators/validate_all.py` | **CONFIRMED file; docstring-only `PROPOSED` placeholder** | Not an operational orchestrator |
| Tool registry, stable CLI entrypoints, test coverage, workflow wiring, generated reports, receipts, proof outputs, runtime use, and end-to-end enforcement | **UNKNOWN / NEEDS VERIFICATION** | README and path presence are not implementation proof |
| Review routing | **CONFIRMED** default CODEOWNERS route to `@bartytime4life`; explicit routes exist for `tools/validators/` and `tools/watchers/` | GitHub routing exists; separate stewardship roles and enforced independent review remain **NEEDS VERIFICATION** |

> [!NOTE]
> `CONFIRMED README` means the documentation file exists at the pinned repository snapshot. It does not mean the described executable, registry, scheduler, workflow, test, or runtime behavior exists or passes.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/` include:

- long-lived validators that check declared contracts, schemas, source roles, evidence closure, lifecycle state, rights, sensitivity, policy posture, release references, correction paths, rollback targets, and public-surface eligibility;
- deterministic generators that scaffold candidate files or derive reviewable outputs from explicit governed inputs;
- catalog builders that compose catalog-stage candidate records from validated processed inputs;
- comparison and diff helpers that produce deterministic, machine-readable review reports;
- diagnostic probes that exercise a bounded rule or fixture without claiming production behavior;
- bounded ingest-adjacent helpers that inspect source changes, freshness, or sidecars and emit review signals without acting as source-of-record connectors;
- join helpers that compute derived candidate links while preserving source roles, evidence references, sensitivity inheritance, and review requirements;
- proof-pack, attestation, and release-support helpers that build, verify, summarize, or dry-run candidate support objects without storing canonical trust records or approving release;
- documentation, QA, and CI helpers that check or render repository signals without becoming documentation, workflow, test, or policy authority;
- stable script-shaped wrappers around durable tool behavior when the wrapper remains thin and the underlying tool keeps responsibility.

A tool should be deterministic where practical, explicit about inputs and outputs, bounded in side effects, testable with local fixtures, no-network by default unless a governed exception exists, and honest about finite negative outcomes.

[Back to top](#top)

---

## What does NOT belong here

| Do not put in `tools/` | Correct home or boundary |
|---|---|
| Canonical schemas, enums, DTOs, or OpenAPI definitions | `schemas/` and verified API/schema homes |
| Semantic object-family meaning | `contracts/` |
| Policy rules, allowlists, denylists, hidden thresholds, or admissibility decisions | `policy/` and accepted decision homes |
| Source descriptors, source activation decisions, or source-registry records | `data/registry/sources/` and accepted control-plane homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads | The correct governed `data/` lifecycle phase |
| Canonical `EvidenceBundle`, `ProofPack`, receipt, or signed-attestation records | `data/proofs/`, `data/receipts/`, and accepted trust-artifact homes |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawals, or signatures as governance records | `release/` |
| Golden, valid, invalid, denied, abstain, or no-network fixture payloads | `fixtures/` or the repository's verified fixture lane |
| Test suites | `tests/` |
| Shared importable libraries used by deployables | `packages/` |
| Pipeline orchestration or declarative pipeline configuration | `pipelines/` and `pipeline_specs/` |
| Named external-source fetching or admission as source-of-record behavior | `connectors/` plus governed source admission |
| Small one-off operational helpers | Top-level `scripts/` until they graduate |
| Public API, UI, MapLibre, tile, graph, search, export, Focus Mode, or AI runtime code | Governed `apps/`, `packages/`, and `runtime/` homes |
| Secrets, credentials, private source terms, exact sensitive locations, signing keys, restricted data, or reconstruction hints | **Denied from repository-facing tooling and documentation** |

[Back to top](#top)

---

<a id="inputs-and-outputs"></a>

## Inputs

Tools may read, when the caller is authorized and placement rules permit:

- semantic contracts from `contracts/`;
- machine schemas from `schemas/` and verified schema homes;
- policy bundles and policy decisions from `policy/` and accepted decision homes;
- source descriptors and source-registry records from `data/registry/sources/`;
- lifecycle records from governed `data/` phases;
- fixtures from `fixtures/` and tests from `tests/`;
- release records from `release/`;
- workflow metadata and non-secret configuration from accepted repository surfaces;
- explicit caller-supplied local paths, identifiers, and output destinations.

Inputs must be pinned or otherwise reproducible where the governing contract requires it. A tool must not silently widen its source scope, enable network access, read secrets, or substitute an inferred path for a missing governed input.

[Back to top](#top)

---

## Outputs

Tools may emit only to caller-authorized and responsibility-correct destinations, such as:

- validation, diff, probe, QA, or reviewer-summary reports to accepted report or artifact homes;
- watcher or source-change candidates to accepted work, quarantine, candidate, or review surfaces;
- receipts to accepted receipt homes;
- proof candidates or proof references to accepted proof homes;
- catalog candidates through accepted catalog-building flows;
- release dry-run reports, rollback drafts, correction drafts, or attestation verification reports through accepted release-support routes;
- generated candidate files to an explicit destination controlled by the owning root.

Every output must identify its role. A report, candidate, draft, receipt, proof candidate, or generated file must not be mislabeled as source truth, policy approval, review approval, release approval, or publication.

Tool output is not public by default. Public use still requires evidence, rights, sensitivity, validation, policy, review, release, correction, and rollback closure appropriate to the claim.

[Back to top](#top)

---

## Validation

### README validation

This root README is checked against the folder-level contract in [Directory Rules §15](../docs/architecture/directory-rules.md#15-required-readme-contract):

- the required H2 sections appear in the required order;
- the `kfm://doc/tools-readme` identity and same repository path are preserved;
- repository-relative links and maintained custom anchors resolve;
- badges represent static, visible document facts and link to useful evidence;
- no workflow, runtime, test-pass, coverage, security, compliance, release, or publication claim is inferred from documentation;
- confirmed child lanes are separated from unverified executable behavior.

### Tool implementation validation

A trust-bearing tool is not implementation-complete until evidence appropriate to its role exists:

1. **Deterministic contract** — documented inputs, outputs, side effects, finite outcomes, reason codes, and error behavior.
2. **Fixtures** — representative positive and negative cases, no-network by default.
3. **Tests** — import/CLI behavior, malformed input, missing dependency, denied or held states, and output-destination boundaries.
4. **Authority checks** — contracts, schemas, policy, source roles, evidence, lifecycle, release, correction, and rollback remain in their owning roots.
5. **Security and sensitivity checks** — secrets are excluded; logs and reports minimize rights-limited or sensitive detail.
6. **Workflow evidence** — any CI or scheduler wiring is inspected directly; a README or workflow filename is not enough.
7. **Output verification** — emitted bytes, hashes, paths, and receipts are checked against the declared contract.

### Current orchestrator limitation

Both candidate orchestrator paths exist, but both sampled files are only `PROPOSED` docstring placeholders:

- [`tools/validate_all.py`](validate_all.py)
- [`tools/validators/validate_all.py`](validators/validate_all.py)

Directory Rules record the location conflict as **OPEN-DR-07**. Until an accepted implementation and contract are verified, this README intentionally publishes **no root validation quickstart command** and makes no exit-code claim.

> [!WARNING]
> A passing tool check proves only that the configured check passed for its declared inputs and version. It does not prove the underlying claim is true, policy-safe, reviewed, released, public-safe, or KFM-published.

[Back to top](#top)

---

## Review burden

[`.github/CODEOWNERS`](../.github/CODEOWNERS) currently routes all repository paths to `@bartytime4life` by default and explicitly routes `tools/validators/` and `tools/watchers/` to that account. This is verified GitHub review routing, not proof that review occurred and not a substitute for stewardship, policy, or release approval.

| Change | Minimum review posture |
|---|---|
| Documentation-only root or lane update | Owning root maintainer or verified docs review route |
| New top-level tooling family under `tools/` | Tooling review plus affected subsystem review; ADR or migration note if an authority boundary changes |
| New or materially changed validator | Validator/tooling review plus affected contract, schema, domain, source, policy, evidence, or release review |
| New or materially changed watcher or ingest-adjacent helper | Tooling review plus source/domain review and rights, sensitivity, policy, evidence, and release review as applicable |
| Tool that writes receipts, proofs, catalog candidates, attestations, or release-support artifacts | Review by the owning trust-artifact or release surface; output-destination tests required |
| Tool that handles living-person data, DNA/genomics, archaeology, rare species, infrastructure, cultural/sovereignty material, private land, or precise locations | Sensitivity/policy review and fail-closed fixtures before use |
| Move from top-level `scripts/` into `tools/` | Graduation review covering ownership, contracts, tests, fixtures, outcomes, docs, CI, and rollback |
| Change that creates a new root or parallel authority | Stop and follow Directory Rules, ADR, migration, and drift procedures |

Named steward roles above describe review burden, not verified GitHub identities. Branch protection, required code-owner review, and author/approver separation remain **NEEDS VERIFICATION**.

[Back to top](#top)

---

## Related folders

| Responsibility | Related location | Boundary |
|---|---|---|
| Placement doctrine | [Directory Rules](../docs/architecture/directory-rules.md) | Decides where files belong; does not prove implementation |
| Contribution workflow | [CONTRIBUTING.md](../CONTRIBUTING.md) | Defines repository contribution and validation posture |
| GitHub review routing | [`.github/CODEOWNERS`](../.github/CODEOWNERS) | Routes review requests; does not prove approval |
| Semantic meaning | [`contracts/`](../contracts/) | Object-family meaning and invariants |
| Machine shape | [`schemas/`](../schemas/) | Machine-checkable schema authority |
| Admissibility | [`policy/`](../policy/) | Allow, deny, restrict, hold, and abstain decisions |
| Source authority | [`data/registry/sources/`](../data/registry/sources/) | Source descriptors, roles, rights, cadence, and activation records |
| Receipts and proofs | [`data/receipts/`](../data/receipts/) · [`data/proofs/`](../data/proofs/) | Process memory and evidence/proof records |
| Lifecycle data | [`data/`](../data/) | RAW through PUBLISHED plus registries, receipts, proofs, and rollback lanes |
| Release governance | [`release/`](../release/) | Manifests, decisions, corrections, withdrawals, and rollback records |
| Tests and fixtures | [`tests/`](../tests/) · [`fixtures/`](../fixtures/) | Enforceability and deterministic examples |
| Orchestration | [`pipelines/`](../pipelines/) · [`pipeline_specs/`](../pipeline_specs/) | Executable flows and declarative configuration |
| Shared libraries | [`packages/`](../packages/) | Importable implementation shared by deployables |
| One-off helpers | [`scripts/`](../scripts/) | Small operational helpers before graduation |
| Public/runtime systems | [`apps/`](../apps/) · [`runtime/`](../runtime/) | Governed deployables and local adapters; downstream of trust |

[Back to top](#top)

---

## ADRs

| Decision or open question | Status in the pinned repository | Effect on `tools/` |
|---|---|---|
| [ADR-0001 — Schema Home](../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | **PROPOSED** | Tools consume canonical schemas; they do not create a parallel schema home |
| [ADR-0011 — Receipts vs Proofs vs Manifests vs Catalog Separation](../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | **PROPOSED** | Tool outputs must route to the correct receipt, proof, catalog, or release home |
| [ADR-0017 — Source Descriptor Admission Process](../docs/adr/ADR-0017-source-descriptor-admission-process.md) | **PROPOSED** | Source-review helpers and watchers must not activate or admit sources by themselves |
| Directory Rules **OPEN-DR-07** | **UNRESOLVED** | `tools/validate_all.py` versus `tools/validators/validate_all.py`; both sampled files are placeholders |
| Watcher helper placement | **CONFLICTED / no accepted resolution verified** | Reconcile `tools/watchers/`, `tools/ingest/`, `pipelines/watchers/`, and `pipeline_specs/watchers/` before adding another implementation lane |

No accepted `tools/`-specific ADR that resolves the orchestrator or watcher-placement conflicts was verified in this review. Proposed ADRs provide review context; they do not grant release, publication, or implementation authority.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| **Review date** | `2026-07-23` |
| **Evidence scope** | Pinned `main` commit, complete prior `tools/README.md`, current Directory Rules §15, CODEOWNERS, CONTRIBUTING, selected tool-lane READMEs, both orchestrator candidates, and representative validator placeholders |
| **Review type** | Documentation structure, placement, link, authority-boundary, and claim audit |
| **Not established** | Exhaustive recursive executable inventory, package entrypoints, workflow runs, test results, branch protection, scheduler behavior, generated outputs, receipts, runtime use, or production enforcement |
| **Next review trigger** | Accepted orchestrator decision, watcher-placement decision, new top-level tooling family, material authority-boundary change, or six months after this review |

[Back to top](#top)

---

## Root invariants

| Invariant | Required posture | Anti-pattern |
|---|---|---|
| Tools enforce or support; they do not govern by themselves. | Tools check or derive governed artifacts for other roots. | Tool output is treated as policy, evidence, release, or public truth. |
| Contracts, schemas, and policy stay separate. | Tools read `contracts/`, `schemas/`, and `policy/` as authority inputs. | Tool-local schema, contract, or policy copy becomes canonical. |
| Validators fail closed. | Missing or unresolved evidence, rights, sensitivity, source role, policy, release, correction, or rollback support produces fail, hold, deny, restrict, abstain, or review. | Silent pass, skipped validator returning success, or best-effort allow. |
| Watchers are non-publishers. | Watchers detect drift and emit reviewable candidates. | Watcher writes directly to PROCESSED, CATALOG, TRIPLET, PUBLISHED, release, or public surfaces. |
| Lifecycle boundaries are preserved. | Tools check governed transitions. | Tool turns promotion into a file move or a passing exit code. |
| Source roles do not collapse. | Observed, modeled, aggregate, candidate, administrative, synthetic, regulatory, and contextual roles remain distinct. | AI, rendering, publication, or derived tooling upgrades a source role. |
| Most restrictive wins. | Rights, sensitivity, geoprivacy, consent, cultural/sovereignty, infrastructure, and living-person constraints propagate downstream. | Public-safe status is inferred from a weaker input. |
| Public runtime is downstream. | Public clients consume governed APIs and released public-safe artifacts. | Public runtime reads internal stores, validator output, watcher candidates, or model output as truth. |
| Corrections remain visible. | Tools preserve supersession, withdrawal, correction, and rollback references where relevant. | In-place mutation erases prior public state or audit history. |

[Back to top](#top)

---

<a id="responsibility-map"></a>
<a id="directory-tree"></a>
<a id="minimal-future-layout"></a>

## Verified lane index

Every lane below has a README at the pinned repository snapshot. A confirmed README is documentation evidence, not proof that scripts, packages, tests, workflows, or runtime behavior exist.

| Lane | Documented role | Current maturity boundary |
|---|---|---|
| [`attest/`](attest/README.md) | Attestation packaging and verification helpers | README confirmed; executable inventory and signing backend **NEEDS VERIFICATION** |
| [`catalog_builders/`](catalog_builders/README.md) | Catalog candidate and index builders | README confirmed; CLI, schemas, tests, receipts, and CI **NEEDS VERIFICATION** |
| [`ci/`](ci/README.md) | CI-support renderers and normalizers | README confirmed; workflow wiring and pass rates **NEEDS VERIFICATION** |
| [`diff/`](diff/README.md) | Deterministic machine-readable comparison helpers | README confirmed; executable thin slice **NEEDS VERIFICATION** |
| [`docs/`](docs/README.md) | Documentation hygiene, normalization, rendering, and report helpers | README confirmed; helper inventory and CI behavior **NEEDS VERIFICATION** |
| [`generators/`](generators/README.md) | Deterministic candidate-file and derived-output generators | README confirmed; executable inventory **NEEDS VERIFICATION** |
| [`ingest/`](ingest/README.md) | Ingest-adjacent preflight, drift, and review-signal helpers | README confirmed; child implementations and watcher overlap **NEEDS VERIFICATION / CONFLICTED** |
| [`joins/`](joins/README.md) | Deterministic candidate-join and anti-collapse helpers | README confirmed; implementation and policy integration **NEEDS VERIFICATION** |
| [`probes/`](probes/README.md) | Bounded diagnostic probes | README confirmed; executable probes mostly **PROPOSED / NEEDS VERIFICATION** |
| [`proof_pack/`](proof_pack/README.md) | ProofPack candidate assembly, checking, and summaries | README confirmed; canonical ProofPack records remain under `data/proofs/` |
| [`qa/`](qa/README.md) | README coverage, links, drift, placeholders, and reviewer summaries | README confirmed; executable inventory **NEEDS VERIFICATION** |
| [`release/`](release/README.md) | Release dry-runs, manifest checks, rollback/correction support | README confirmed; no release authority; executables **NEEDS VERIFICATION** |
| [`scripts/`](scripts/README.md) | Thin durable wrappers and compatibility entrypoints | README confirmed; relationship to top-level `scripts/` **NEEDS VERIFICATION** |
| [`validators/`](validators/README.md) | Parent routing surface for fail-closed validators | README confirmed; broad index; implementation must be verified per validator |
| [`watchers/`](watchers/README.md) | Reusable watcher-tooling routing and compatibility boundary | README confirmed; direct tree documentation-only; placement **CONFLICTED** |

[Back to top](#top)

---

## `tools/` vs nearby roots

| Root | Owns | Use `tools/` instead when |
|---|---|---|
| `scripts/` | Small operational helpers and one-offs. | The helper becomes durable, reusable, trust-bearing, fixture-tested, or workflow-invoked. |
| `packages/` | Shared importable libraries used by deployables. | The implementation is primarily invoked as a CLI, checker, builder, probe, or workflow step. |
| `connectors/` | Named external-source access and governed admission edge. | The helper only inspects, validates, compares, or reports on already supplied inputs. |
| `pipelines/` | Executable lifecycle orchestration. | The code is a reusable checker, builder, comparator, or helper invoked by multiple flows. |
| `pipeline_specs/` | Declarative statements of what should run. | The artifact is executable implementation rather than configuration. |
| `tests/` | Tests that prove behavior. | The logic is the tool being tested; tests call tools rather than contain the canonical tool. |
| `fixtures/` | Stable positive, negative, denied, abstain, and no-network examples. | The file generates or checks fixtures rather than being fixture data. |
| `apps/` / `runtime/` | Deployable or local runtime behavior. | The code is repository support and must not serve public clients. |

[Back to top](#top)

---

## Standard outcome posture

Individual tool contracts may define narrower vocabularies. At the root, outcomes remain finite, explicit, and fail-closed.

| Outcome family | Meaning |
|---|---|
| `PASS` / `NO_CHANGE` | Configured checks ran and found no blocker for the declared scope. |
| `CHANGE_CANDIDATE` / `ROUTE` | A candidate or routing decision was produced for downstream review. |
| `FAIL` | Configured checks found a defect. |
| `DENY` | The candidate must not proceed for the requested use. |
| `RESTRICT` | The candidate may proceed only in constrained, steward-gated contexts. |
| `HOLD` | The candidate remains held pending source, rights, sensitivity, evidence, policy, review, release, correction, or rollback closure. |
| `ABSTAIN` | The tool lacks enough support to make the requested assertion. |
| `NEEDS_REVIEW` | Steward review is required before downstream use. |
| `PUBLIC_SURFACE_DENIED` | The candidate is not eligible for public API, UI, map, tile, graph, search, export, Focus Mode, or AI surfaces. |
| `SYSTEM_ERROR` | The tool could not complete because of malformed input, missing dependency, missing registry entry, timeout, or unexpected runtime failure. |

A tool-specific schema or contract controls exact enum spelling. This root README does not standardize conflicting downstream vocabularies by prose alone.

[Back to top](#top)

---

## Negative-state rule

Every trust-bearing tool should test negative states, not only happy paths.

Minimum negative cases, when applicable:

- missing schema, contract, source descriptor, policy decision, evidence reference, receipt, release reference, correction path, or rollback target;
- stale source, missing source head, unresolved cadence, or unactivated source;
- rights unknown, license restricted, attribution missing, consent revoked, or source terms drifted;
- sensitivity unresolved, exact sensitive geometry exposed, redaction receipt missing, or most-restrictive propagation broken;
- source-role collapse, modeled-to-observed upgrade, aggregate-to-place overclaim, or AI-inferred authority;
- tool attempts to publish, promote, mutate lifecycle state outside its role, or write to public/runtime surfaces;
- missing fixture, skipped validation, or unavailable dependency incorrectly returning success;
- logs or reports exposing secrets, private terms, precise restricted locations, or reconstruction hints.

[Back to top](#top)

---

<a id="acceptance-checklist"></a>

## Maintenance and verification backlog

- [ ] Inventory executable files under each top-level tool lane and classify implemented, placeholder, generated, compatibility, or dead surfaces.
- [ ] Resolve **OPEN-DR-07** and establish one tested orchestrator path, versioned contract, exit-code vocabulary, and rollback plan.
- [ ] Reconcile watcher responsibilities across `tools/watchers/`, `tools/ingest/`, `pipelines/watchers/`, and `pipeline_specs/watchers/`; retire or mark compatibility lanes rather than adding another implementation.
- [ ] Verify stable CLI or package entrypoints and document only commands that run successfully in a safe environment.
- [ ] Tie validator, generator, diff, probe, ingest, join, QA, attestation, proof-pack, and release-support behavior to deterministic tests and fixtures.
- [ ] Verify workflow triggers, network posture, secret handling, artifact destinations, and generated report retention before making CI claims.
- [ ] Verify receipts, proof candidates, catalog candidates, and release-support outputs write only to accepted responsibility roots.
- [ ] Assign and verify stewardship identities beyond the current default CODEOWNERS route where governance maturity requires separation of duties.
- [ ] Add sensitive and rights-limited negative fixtures without exposing restricted values or precise locations.
- [ ] Re-review this root README when a top-level lane is added, retired, reclassified, or promoted from documentation-only to implemented.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-23 | Modernized the canonical-root README in place; aligned H2 order with Directory Rules §15; replaced the speculative future tree with a verified README-lane index; surfaced placeholder orchestrators and watcher-placement conflict; repaired owner, review, validation, ADR, related-root, badge, and last-reviewed guidance. | **CONFIRMED documentation change / implementation maturity bounded** |
| 2026-07-08 | Updated tools root README from pasted scaffold to repo-aware root contract that reflects confirmed validator and watcher README surfaces. | **CONFIRMED README / implementation NEEDS VERIFICATION** |

[Back to top](#top)
