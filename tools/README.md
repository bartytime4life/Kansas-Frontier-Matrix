<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-readme
title: tools README
type: README
version: v0.2
status: draft
owner: TODO-tooling-qa-owner-plus-validator-steward-plus-watcher-steward-plus-schema-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: NEEDS VERIFICATION — file existed before this repo-aware update
updated: 2026-07-08
policy_label: repository-facing; tools-root; canonical-root; trust-tooling; validators; watchers; generators; catalog-builders; proof-pack; release-tooling; qa; fail-closed; no-publication-by-tool; non-authoritative
owning_root: tools/
responsibility: parent README for the tools responsibility root; documents placement boundaries for long-lived trust-bearing tooling including validators, watchers, generators, catalog builders, proof-pack helpers, release helpers, QA tooling, attestation helpers, and CI helpers while preserving authority boundaries with docs, contracts, schemas, policy, data lifecycle roots, source registries, evidence/proofs, receipts, release records, fixtures, tests, pipelines, packages, scripts, and public runtime surfaces
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - validators/README.md
  - watchers/README.md
  - ../docs/doctrine/directory-rules.md
  - ../docs/adr/ADR-0001-schema-home.md
  - ../contracts/
  - ../schemas/contracts/v1/
  - ../policy/
  - ../data/registry/sources/
  - ../data/proofs/
  - ../data/receipts/
  - ../release/
  - ../fixtures/
  - ../tests/
  - ../scripts/
  - ../packages/
  - ../pipelines/
notes:
  - "This README is updated from a previously pasted tools-root scaffold and current repo evidence. It no longer claims current tools-root presence is UNKNOWN: tools/README.md, tools/validators/README.md, and tools/watchers/README.md are confirmed README surfaces in this session."
  - "Executable behavior is still not confirmed merely because a README exists. Validator scripts, watcher scripts, registry wiring, package entrypoints, scheduler wiring, generated reports, receipt emission, runtime behavior, and CI behavior remain NEEDS VERIFICATION unless separately verified."
  - "tools/ owns executable trust tooling. It does not define domain meaning, create canonical schemas, admit sources, create EvidenceBundles as truth authority, decide policy, approve release, publish artifacts, or authorize public API/UI/map/AI surfaces."
  - "Validators check readiness; watchers detect change and emit candidates. Neither role is a publisher. Publication remains a governed state transition through evidence, policy, review, release, correction, and rollback controls."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-trust--tooling-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![authority](https://img.shields.io/badge/authority-tooling--not--truth-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/` is the repo-wide home for long-lived, trust-bearing tooling: validators, watchers, generators, catalog builders, proof-pack helpers, release helpers, QA tools, attestation helpers, and CI helpers that enforce KFM governance without becoming doctrine, schema, policy, evidence, release, data, or public-runtime authority.

---

## Purpose

`tools/` owns KFM's durable executable trust tooling.

The durable KFM question for this root is:

> Which reusable command-line or workflow-invoked tooling checks, builds, detects, summarizes, signs, packages, or reports on governed KFM artifacts while preserving the authority of contracts, schemas, policy, source registries, evidence, receipts, lifecycle data, release records, fixtures, tests, pipelines, packages, and public runtime roots?

`tools/` is where long-lived scripts graduate when they become trust-bearing. It is not a convenience bucket, not a domain root, and not a place to hide schemas, policy decisions, source registry records, evidence records, receipts, release records, fixtures, tests, or public-facing runtime logic.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/README.md` | **CONFIRMED README** | This file is updated from the earlier tools-root scaffold. |
| `tools/validators/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Parent validator index exists and defines validator lanes as fail-closed checker routing, not truth or publication authority. |
| `tools/watchers/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Parent watcher index exists and defines watchers as candidate-producing non-publishers. |
| `tools/watchers/plants_watch/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Child watcher lane for Flora plant-source drift and PLANTS taxa drift posture. |
| `tools/generators/`, `tools/catalog_builders/`, `tools/proof_pack/`, `tools/release/`, `tools/qa/`, `tools/attest/`, `tools/ci/` | **NEEDS VERIFICATION** | Mentioned as responsibility-root families or proposed lanes; directory/file presence and behavior were not verified in this update. |
| Executable tooling, registry ids, CLI/package entrypoints, scheduler wiring, fixtures, tests, CI jobs, generated reports, receipts, runtime behavior, and end-to-end enforcement | **NEEDS VERIFICATION** | README presence is not implementation proof. |

[Back to top](#top)

---

## Root invariants

| Invariant | Required posture | Anti-pattern |
|---|---|---|
| Tools enforce; they do not govern by themselves. | Tools check or produce governed artifacts for other roots. | Tool output is treated as policy, evidence, release, or public truth. |
| Contracts, schemas, and policy stay separate. | Tools read `contracts/`, `schemas/`, and `policy/` as authority inputs. | Tool-local schema, contract, or policy copy becomes canonical. |
| Validators are fail-closed. | Missing or unresolved evidence, rights, sensitivity, source, policy, release, correction, or rollback support produces fail/hold/deny/restrict/abstain/review. | Silent pass, skipped validator returning success, or best-effort allow. |
| Watchers are non-publishers. | Watchers detect drift and emit reviewable candidates. | Watcher writes directly to `processed/`, `catalog/`, `triplets/`, `published/`, `release/`, public maps, public APIs, or AI answer surfaces. |
| Lifecycle boundaries are preserved. | RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED remain governed states. | Tool turns promotion into a file move. |
| Source roles do not collapse. | Observed, modeled, aggregate, candidate, administrative, synthetic, regulatory, and contextual roles remain distinct. | AI, map rendering, publication, or derivative tooling upgrades a source role. |
| Most restrictive wins. | Rights, sensitivity, geoprivacy, redaction, consent, cultural sensitivity, infrastructure risk, and living-person constraints propagate downstream. | Public-safe status is assumed from a single weak input. |
| Public runtime is downstream. | API/UI/map/tile/graph/search/export/Focus Mode/AI surfaces consume released public-safe artifacts. | Public runtime reads internal stores, validator output, watcher candidates, or model output as truth. |

[Back to top](#top)

---

## Responsibility map

| Tooling family | Preferred home | Status | Responsibility boundary |
|---|---|---|---|
| Validators | [`tools/validators/`](validators/README.md) | **CONFIRMED README / behavior NEEDS VERIFICATION** | Check readiness and fail-closed conditions; do not own schemas, policy, evidence, or release. |
| Watchers | [`tools/watchers/`](watchers/README.md) | **CONFIRMED README / behavior NEEDS VERIFICATION** | Detect source/head/drift signals and emit candidates; do not publish. |
| Generators | `tools/generators/` | **NEEDS VERIFICATION** | Deterministic scaffolds, ids, templates, or generated helper artifacts; must not invent truth. |
| Catalog builders | `tools/catalog_builders/` | **NEEDS VERIFICATION** | Build proposed catalog records from validated processed outputs; final publication remains governed. |
| Proof-pack tooling | `tools/proof_pack/` | **NEEDS VERIFICATION** | Assemble evidence/proof/receipt bundles for promotion/release checks; proof records live in accepted data/proof homes. |
| Release tooling | `tools/release/` | **NEEDS VERIFICATION** | Dry-runs, manifest checks, rollback/correction helpers; release authority remains in `release/`. |
| QA tooling | `tools/qa/` | **NEEDS VERIFICATION** | Link checks, drift scans, coverage reports, review summaries; does not replace tests or release gates. |
| Attestation helpers | `tools/attest/` | **PROPOSED / NEEDS VERIFICATION** | Signing and verification helpers if accepted; signing keys and trust records do not live here by default. |
| CI helpers | `tools/ci/` | **PROPOSED / NEEDS VERIFICATION** | CI-only rendering/report helpers; CI workflows remain outside this root. |

[Back to top](#top)

---

## Directory tree

The tree below is a **repo-aware target map**, not a claim that every folder exists.

```text
tools/
├── README.md                              # CONFIRMED README
├── validators/                            # CONFIRMED README; executable behavior NEEDS VERIFICATION
│   ├── README.md
│   ├── domains/                           # per-domain validator index
│   ├── policy/                            # policy-facing validation routing
│   ├── source/                            # source-admission validation routing
│   ├── source_descriptor/                 # SourceDescriptor underscore lane
│   ├── source-descriptor/                 # SourceDescriptor hyphenated lane
│   ├── source_role/                       # source-role anti-collapse lane
│   ├── sources/                           # plural compatibility lane
│   ├── sensitivity/                       # sensitivity posture lane
│   ├── rights/                            # rights posture lane
│   ├── release/                           # release-readiness validation lane
│   ├── promotion_gate/                    # promotion-gate lane
│   ├── taxonomy_resolver/                 # taxonomy/crosswalk resolution checks
│   ├── suitability/                       # broad suitability checks
│   ├── soil-suitability/                  # soil suitability derivative checks
│   ├── transport-facility-topology/        # transport topology checks
│   └── vegetation_community/              # Flora vegetation community checks
├── watchers/                              # CONFIRMED README; executable behavior NEEDS VERIFICATION
│   ├── README.md
│   └── plants_watch/                      # Flora plant-source drift watcher lane
├── generators/                            # NEEDS VERIFICATION
├── catalog_builders/                      # NEEDS VERIFICATION
├── proof_pack/                            # NEEDS VERIFICATION
├── release/                               # NEEDS VERIFICATION
├── qa/                                    # NEEDS VERIFICATION
├── attest/                                # PROPOSED / NEEDS VERIFICATION
└── ci/                                    # PROPOSED / NEEDS VERIFICATION
```

[Back to top](#top)

---

## What belongs here

Good fits for `tools/` include:

- long-lived validators that check declared contracts, schemas, policy posture, evidence closure, lifecycle state, source roles, sensitivity, release references, corrections, rollback, and public-surface eligibility;
- side-effect-limited watchers that detect source/head/drift signals and emit reviewable candidates;
- deterministic generators that scaffold governed objects without becoming their authority;
- catalog-building helpers that prepare proposed catalog records from validated data;
- proof-pack helpers that assemble references to evidence, receipts, manifests, and signatures;
- release-support helpers that validate release readiness, dry runs, rollback cards, and correction notices without approving release;
- QA tools that help maintainers inspect coverage, links, drift, and review readiness;
- CI helpers that render summaries or normalize deterministic reports.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/` | Correct home |
|---|---|
| Canonical schemas, enums, DTOs, OpenAPI contracts | `schemas/` and accepted API/schema homes |
| Semantic object contracts | `contracts/` |
| Policy rules, allowlists, denylists, sensitivity thresholds, release decisions | `policy/`, `release/`, accepted governance homes |
| Source descriptors, source activation decisions, source registry records | `data/registry/sources/` and accepted source registry/control-plane homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads | governed `data/` lifecycle roots |
| EvidenceBundles, proof packs, receipts, signed attestations as records | `data/proofs/`, `data/receipts/`, accepted trust-artifact homes |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawals | `release/` and accepted release/correction homes |
| Golden, valid, invalid, synthetic, or no-network fixture payloads | `fixtures/` or accepted fixture homes |
| Test suites | `tests/` |
| Shared libraries imported by multiple deployables | `packages/` |
| Pipeline orchestration | `pipelines/` and `pipeline_specs/` |
| Small one-off operational helpers | `scripts/` until they graduate |
| Public API, UI, MapLibre runtime, tile service, graph/search/export/Focus Mode/AI runtime code | governed app/runtime roots |
| Secrets, credentials, private source data, exact sensitive locations, hidden policy values, signing keys, reconstruction hints | denied from repository-facing tooling docs and code |

[Back to top](#top)

---

## `tools/` vs nearby roots

| Root | Owns | Use `tools/` instead when |
|---|---|---|
| `scripts/` | Small operational helpers, dev utilities, one-offs. | The script becomes long-lived, trust-bearing, CI-invoked, promotion-related, or release-related. |
| `packages/` | Shared importable libraries used by deployables. | The code is invoked as a tool/CLI/workflow step rather than imported as application logic. |
| `pipelines/` | Orchestration of lifecycle flows. | The code is a reusable checker/builder/helper step invoked by multiple flows. |
| `pipeline_specs/` | Declarative specs for what should run. | The artifact is executable implementation rather than configuration. |
| `tests/` | Tests proving behavior. | The logic is the validator/checker being tested; tests should call tools, not contain the canonical validator. |
| `fixtures/` | Golden/valid/invalid/no-network sample payloads. | The file is a generator or checker for fixtures rather than fixture data. |

[Back to top](#top)

---

## Inputs and outputs

### Inputs

Tools may read, when authorized by the task and placement rules:

- semantic contracts from `contracts/`;
- machine schemas from `schemas/contracts/v1/` and accepted schema homes;
- policy bundles and policy decisions from `policy/` and accepted decision homes;
- source descriptors and source registry records from `data/registry/sources/`;
- lifecycle records from governed `data/` roots;
- fixtures from `fixtures/` and tests from `tests/`;
- release records from `release/`;
- CI metadata from accepted workflow/artifact surfaces.

### Outputs

Tools may emit only to accepted destinations for their role:

- validation reports to accepted report/artifact homes;
- watcher candidates or summaries to accepted candidate/report/quarantine/review homes;
- receipts to accepted receipt homes;
- proof references or proof packs to accepted proof homes;
- proposed catalog records only through accepted catalog-building flows;
- release dry-run artifacts, rollback drafts, or correction helpers only through accepted release-support routes.

Tool output is not public by default. Public use still requires evidence, policy, review, release, correction, and rollback closure.

[Back to top](#top)

---

## Standard outcome posture

Validator and watcher families may define narrower vocabularies, but the root posture stays finite and fail-closed.

| Outcome family | Meaning |
|---|---|
| `PASS` / `NO_CHANGE` | Configured checks ran and did not find a blocker for the declared scope. |
| `CHANGE_CANDIDATE` / `ROUTE` | A candidate or routing decision was produced for downstream review. |
| `FAIL` | Configured checks found a defect. |
| `DENY` | Candidate must not proceed for the requested use. |
| `RESTRICT` | Candidate may proceed only in constrained/steward-gated contexts. |
| `HOLD` | Candidate must remain held pending source, rights, sensitivity, evidence, policy, review, release, correction, or rollback closure. |
| `ABSTAIN` | Tool lacks enough support to make the requested assertion. |
| `NEEDS_REVIEW` | Steward review is required before downstream use. |
| `PUBLIC_SURFACE_DENIED` | Candidate is not eligible for public API/UI/map/tile/export/search/graph/Focus Mode/AI surfaces. |
| `SYSTEM_ERROR` | Tool could not complete because of malformed input, missing dependency, missing registry entry, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Negative-state rule

Every trust-bearing tool should test negative states, not only happy paths.

Minimum negative cases for tool families:

- missing schema, contract, source descriptor, policy decision, evidence reference, receipt, release reference, correction path, or rollback target;
- stale source, missing source-head, unresolved cadence, or unactivated watcher source;
- rights unknown, license restricted, attribution missing, consent revoked, or source terms drifted;
- sensitivity unresolved, exact sensitive geometry exposed, redaction receipt missing, or most-restrictive propagation broken;
- source-role collapse, modeled-to-observed upgrade, aggregate-to-place overclaim, or AI-inferred authority;
- tool attempts to publish, mutate lifecycle state outside its role, or write to public/runtime surfaces;
- missing fixture or skipped validation returning success.

[Back to top](#top)

---

## Review burden

| Change | Review expectation |
|---|---|
| New top-level tooling family under `tools/` | Tooling owner plus affected subsystem owner; ADR or migration note if it changes an authority boundary. |
| New validator lane | Tooling/validator owner plus domain/source/policy/evidence/release steward as applicable. |
| New watcher lane | Tooling/watcher owner plus source/domain steward, rights/sensitivity reviewer, and policy/evidence/release steward as applicable. |
| Tool that writes receipts, proofs, catalog records, or release-support artifacts | Evidence/release steward review and tests for output destination. |
| Tool that handles sensitive data, rights-limited data, living-person data, infrastructure, rare species, archaeology, cultural material, or exact locations | Sensitivity/policy review and fail-closed fixtures. |
| Move from `scripts/` to `tools/` | Graduation review with tests, fixtures, outcome contract, docs, and CI/update plan. |
| Documentation-only update | Docs steward or owning root maintainer. |

[Back to top](#top)

---

## Minimal future layout

```text
tools/
├── README.md
├── validators/
├── watchers/
├── generators/
├── catalog_builders/
├── proof_pack/
├── release/
├── qa/
├── attest/
└── ci/
```

Future folders should be added only when the owning responsibility is clear, the authority boundary is documented, outputs route to accepted homes, and tests prove fail-closed behavior.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the earlier scaffold with current repo-aware `tools/` root documentation.
- [x] It marks `tools/README.md`, `tools/validators/README.md`, and `tools/watchers/README.md` as confirmed README surfaces.
- [x] It keeps executable behavior, registry wiring, scheduler wiring, package entrypoints, generated reports, receipts, runtime behavior, and CI behavior as **NEEDS VERIFICATION**.
- [x] It distinguishes validators from watchers and keeps both non-authoritative.
- [x] It routes schemas to `schemas/`, contracts to `contracts/`, policy to `policy/`, source registries to `data/registry/sources/`, evidence/proofs/receipts to `data/`, release records to `release/`, fixtures to `fixtures/`, tests to `tests/`, shared libraries to `packages/`, orchestration to `pipelines/`, one-offs to `scripts/`, and public runtime to governed app/runtime roots.
- [x] It preserves cite-or-abstain, fail-closed, lifecycle, source-role, sensitivity/rights, no-publication, correction, and rollback posture.

Future implementation is not complete until:

- [ ] Tool registry, CLI entrypoints, scheduler references, and CI workflows are searched and classified.
- [ ] Existing `tools/` subdirectories are inventoried and reconciled against this README.
- [ ] Validator and watcher outcome vocabularies are tied to tests and fixtures.
- [ ] Generated reports, receipts, proof packs, release helpers, and catalog-builder outputs are verified to write only to accepted homes.
- [ ] Sensitive and rights-limited negative fixtures are added without leaking restricted details.
- [ ] CI invokes trust-bearing tools in deterministic, no-network-by-default lanes unless a governed exception exists.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Updated tools root README from pasted scaffold to repo-aware root contract that reflects confirmed validator and watcher README surfaces. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
