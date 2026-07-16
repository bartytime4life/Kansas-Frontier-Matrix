<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/scripts-readme
title: scripts/ — Governed Operational Helper and Graduation Root
type: readme; root-readme; operational-helper-root; trust-adjacent-script-index; graduation-boundary
version: v0.3
status: draft; repository-grounded; mixed-maturity; active-ci-helper-chain-confirmed; placement-drift-visible; non-authoritative
owners: OWNER_TBD — Developer tooling steward · Maintenance tooling steward · MapLibre quality steward · CI steward · Security steward · Evidence steward · Receipt and proof steward · Release steward · Migration steward · Docs steward
created: NEEDS VERIFICATION — short root stub existed before v0.2
updated: 2026-07-16
supersedes: v0.2 operational script root guide
policy_label: "public; scripts; operational-helpers; local-dev; maintenance; one-off; maplibre-perf; no-hidden-authority; no-direct-public-path; no-secrets; dry-run-first; graduation-required; rollback-aware"
current_path: scripts/README.md
truth_posture: >
  CONFIRMED target v0.2 README and prior blob; current dev v0.2 placeholder-only lane;
  current one_off v0.2 README-only empty-by-default lane; maintenance v0.3 mixed-maturity
  doctrine tooling; current package.json MapLibre commands; current MapLibre performance
  workflow invoking root-level scripts and validators; selected root-level MapLibre script
  implementations and artifact write paths; draft MapLibre performance governance document /
  PROPOSED root script admission contract, risk classes, execution modes, finite outcomes,
  graduation ledger, mutation disclosure, generated-artifact handoff, correction and rollback /
  CONFLICTED trust-adjacent MapLibre receipts, ProofPack, ReleaseManifest, correction, rollback,
  and failure objects being written under artifacts/perf while doctrine identifies data/receipts/,
  data/proofs/, and release/ as the trust-bearing homes; substantive release-adjacent behavior
  remaining under scripts/ despite the root graduation rule /
  UNKNOWN exhaustive script inventory beyond inspected and indexed surfaces, all workflow callers,
  production use, operator-local copies, generated artifact retention, signing, release adoption,
  correction propagation, and downstream consumers /
  NEEDS VERIFICATION accepted owners, CODEOWNERS, graduation destination for MapLibre helpers,
  canonical artifact migration, CI branch-protection significance, receipt/proof/release schemas,
  network policy, cleanup automation, and rollback tests
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 15d88fceced7050abac4493b9cf66f5bc288c1e6
  prior_blob: 4000b70a60af0d0656a4343ac6ae7f951b5327e3
  dev_readme_blob: 390687c80912d52def5909b66bec7bb08b9d0bfa
  maintenance_readme_blob: bd4ef697d7118074be44d00e6e77a8a311afe5f4
  promotion_gate_workflow_blob: f335521df78940390d22d7e359d50f6c8591a451
  one_off_readme_blob: 46e85d9b2e9bba3dd48c697dfc020b456e4cae18
  package_json_blob: 62f45306aef7376a2d68042b0c9e7f556edf0e78
  maplibre_workflow_blob: 49374af01e92973b54f690e4ab0af9e5e1e577f3
  maplibre_governance_doc_blob: 67f57a9a0878801f83a13f3b1c6d80be3174036e
  maplibre_smoke_blob: 699dd4cf42d355dd2ed7620852b7fd1f3000bbe2
  maplibre_render_diff_blob: ee24890c0e06bd941e0f1ead919e9e7b9bc37460
  maplibre_attest_blob: 0c8187e0c4d88926a7cd2de413564d2d942dd9b3
  maplibre_manifest_blob: 566731bd6ad1510ecd1e01e0275ffa04b3993a86
  maplibre_proof_pack_blob: 8396c912a75c803baf8a92abe7a2f8cad582ba41
  maplibre_correction_blob: dc75786fbc0343dba17eef8f122eb1d67728f541
  maplibre_failure_bundle_blob: f22f248084bc231212915b4e40a653faef566b64
related:
  - ./dev/README.md
  - ./maintenance/README.md
  - ./one_off/README.md
  - ../tools/README.md
  - ../tools/validators/README.md
  - ../pipelines/README.md
  - ../packages/README.md
  - ../tests/README.md
  - ../fixtures/README.md
  - ../configs/README.md
  - ../artifacts/README.md
  - ../data/README.md
  - ../data/receipts/README.md
  - ../data/proofs/README.md
  - ../release/README.md
  - ../package.json
  - ../.github/workflows/maplibre-perf-governance.yml
  - ../docs/quality/maplibre-perf-governance.md
  - ../docs/doctrine/directory-rules.md
  - ../docs/security/SECRETS.md
  - ../docs/registers/DRIFT_REGISTER.md
tags: [kfm, scripts, operational-helpers, dev, maintenance, one-off, maplibre, performance, ci, artifacts, receipts, proofs, release, graduation, dry-run, rollback]
notes:
  - "This revision changes only scripts/README.md."
  - "No script, workflow, package command, validator, artifact, receipt, proof, release record, configuration, fixture, test, or deployment behavior is changed."
  - "The root graduation rule remains controlling: long-lived or trust-bearing behavior belongs in tools/, pipelines/, packages/, tests/, or another accepted responsibility lane."
  - "Current MapLibre helper execution is confirmed through package.json and a dedicated workflow; artifact placement and long-term implementation ownership remain governance issues."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `scripts/` — Governed Operational Helper and Graduation Root

> **One-line purpose.** Hold small, explicit, inspectable operational wrappers while enforcing a visible graduation boundary so convenience scripts cannot become hidden validators, pipelines, policy engines, evidence authorities, release systems, or public execution paths.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.3" src="https://img.shields.io/badge/version-v0.3-informational">
  <img alt="Root: scripts" src="https://img.shields.io/badge/root-scripts%2F-blue">
  <img alt="Maturity: mixed" src="https://img.shields.io/badge/maturity-mixed-orange">
  <img alt="CI: MapLibre chain confirmed" src="https://img.shields.io/badge/CI-MapLibre__confirmed-success">
  <img alt="Authority: none" src="https://img.shields.io/badge/authority-none-red">
  <img alt="Rule: graduate trust logic" src="https://img.shields.io/badge/rule-graduate__trust__logic-critical">
</p>

> [!IMPORTANT]
> **A script may execute work, but successful execution grants no authority.** Script output is not automatically evidence, proof, policy approval, lifecycle promotion, release approval, correction authority, rollback authorization, or public truth.

> [!CAUTION]
> **Trust-adjacent behavior must not hide in convenience wrappers.** When a script becomes repeatedly relied upon, CI-critical, write-capable against governed roots, or responsible for receipts, proofs, release manifests, correction records, or publication gates, maintainers must review its graduation into the responsibility root that owns that behavior.

> [!WARNING]
> **Scripts must not become secret, network, or mutation shortcuts.** Every write set, delete set, network endpoint, secret reference, generated artifact, retention rule, validation command, and rollback path must be explicit before a script is admitted for consequential use.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Inventory](#confirmed-current-inventory) · [Child lanes](#child-lane-contracts) · [MapLibre](#root-level-maplibre-performance-chain) · [Execution](#safe-execution-contract) · [Artifacts](#generated-artifact-and-trust-object-boundary) · [Failures](#finite-outcomes-and-failure-semantics) · [Graduation](#graduation-and-promotion-rules) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Rollback](#correction-and-rollback) · [Open](#open-verification-register) · [Last reviewed](#last-reviewed)

---

## Purpose

`scripts/` is the KFM responsibility root for **small operational wrappers and bounded repository helpers** that are useful but have not earned a durable home as a validator, generator, package, pipeline, test harness, deployment unit, or release tool.

A script belongs here only while all of these remain true:

1. its purpose is narrow and explicit;
2. its inputs, outputs, side effects, and failure states are inspectable;
3. its logic is not the sole source of trust-bearing behavior;
4. it can be disabled, deleted, or graduated without changing public contracts;
5. its outputs remain candidates until validated and routed to their owning roots;
6. it does not bypass evidence, policy, rights, sensitivity, review, release, correction, or rollback gates.

The controlling rule is:

```text
small bounded helper
  -> repeated or trust-bearing use detected
  -> responsibility and risk review
  -> graduate logic to tools/, pipelines/, packages/, tests/, infra/, release/,
     or another accepted authority root
  -> optionally retain a thin script wrapper
```

This is a **PROPOSED operating discipline** grounded in the current parent and child documentation. It does not claim automated graduation enforcement.

[Back to top](#top)

---

## Authority level

**Operational helper root / non-authoritative execution surface.**

| Concern | Authority home | `scripts/` role |
|---|---|---|
| Small local or operational wrapper | `scripts/` | Owns the thin command wrapper and bounded usage notes. |
| Long-lived validator, generator, builder, proof assembler, or QA tool | `tools/` | Scripts may call it; they must not replace its accepted contract and tests. |
| Repeatable lifecycle or production orchestration | `pipelines/` | Scripts may launch a pipeline; orchestration authority stays with the pipeline. |
| Reusable implementation | `packages/` | Shared logic belongs in importable, versioned, tested code. |
| Executable proof | `tests/` | A script exit code is not a substitute for tests. |
| Fixtures and golden/negative cases | `fixtures/` | Scripts may read or regenerate through accepted generators; fixture authority remains separate. |
| Semantic meaning | `contracts/` | Scripts consume contracts and cannot redefine object meaning. |
| Machine-checkable shape | `schemas/` | Scripts may invoke validators; they cannot create parallel schema authority. |
| Policy, rights, sensitivity, consent, access | `policy/` and governed review | Scripts obey decisions and cannot grant permission. |
| Source identity and activation | registry/source-governance roots | Scripts cannot activate sources by writing files. |
| Lifecycle data | `data/raw`, `work`, `quarantine`, `processed`, `catalog`, `triplet`, `published` | Scripts may produce candidates only through governed transitions. |
| Receipts and proofs | governed `data/receipts/` and `data/proofs/` lanes | Scripts may emit through accepted contracts; output location alone grants no status. |
| Release, correction, withdrawal, rollback | `release/` | Scripts may draft or assist; authority remains with governed records and reviewers. |
| Deployment and network exposure | `infra/`, runtime, and app roots | Scripts cannot authorize a service or public route. |
| Public API/UI behavior | accepted app/API/UI roots | Public clients never execute arbitrary repository scripts. |
| Secrets | approved external mechanism | Scripts use references or injected values, never committed secrets. |

### Anti-collapse rules

`scripts/` must not collapse:

- command convenience into canonical implementation;
- generated JSON into accepted contract conformance;
- validator invocation into validator authority;
- CI success into release approval;
- artifact upload into publication;
- a receipt-shaped object into a governed receipt;
- a proof-shaped object into accepted proof;
- a release-manifest-shaped object into a release;
- a draft correction or rollback object into an authorized state transition;
- developer-local success into production readiness;
- a one-off mutation into a durable system dependency.

[Back to top](#top)

---

## Status

### Repository-grounded maturity summary

| Surface | Status at the pinned snapshot | Safe conclusion |
|---|---:|---|
| `scripts/README.md` | **CONFIRMED v0.2** | Root guidance exists but predates the current child-lane revisions and verified CI wiring. |
| `scripts/dev/` | **CONFIRMED v0.2; placeholder-only** | `bootstrap.sh` and `regen_fixtures.sh` print TODO messages and do not implement their advertised future behavior. |
| `scripts/maintenance/` | **CONFIRMED v0.3; mixed maturity** | Substantive doctrine preflight, registry, readiness, synchronization, and test-bundle scripts exist beside at least one placeholder. |
| `scripts/one_off/` | **CONFIRMED v0.2; README-only in bounded evidence** | Empty-by-default temporary quarantine lane; direct executable scripts were not established. |
| Root-level MapLibre scripts | **CONFIRMED present and substantive** | They run smoke performance, render-diff, attestation-shaped, manifest-shaped, proof-shaped, correction/rollback, and failure-bundle work. |
| Root `package.json` commands | **CONFIRMED** | Named `maplibre:*` commands invoke the helper chain and validators. |
| MapLibre performance workflow | **CONFIRMED executable workflow definition** | A dedicated workflow installs dependencies, runs scripts and validators, handles failures, and uploads artifacts. |
| Workflow run success or branch-protection requirement | **UNKNOWN in this edit** | Workflow definition is not proof of current run success or merge-gate significance. |
| Canonical trust-object placement | **CONFLICTED** | Scripts write receipt/proof/release-shaped objects under `artifacts/perf`; doctrine identifies governed data/release homes for accepted objects. |
| MapLibre helper long-term home | **NEEDS VERIFICATION** | Draft governance recommends graduation from `scripts/` to a tools-oriented lane. |
| Ownership and CODEOWNERS | **OWNER_TBD / NEEDS VERIFICATION** | Current accepted owners and enforcement are not established here. |
| Production/public use | **DENIED unless separately proven** | Repository scripts are not public or production interfaces. |

### Maturity classes

| Class | Meaning | Current examples |
|---|---|---|
| `PLACEHOLDER` | File exists but does not perform the advertised future action. | `dev/bootstrap.sh`, `dev/regen_fixtures.sh`, documented maintenance placeholders. |
| `LOCAL_HELPER` | Bounded developer or operator convenience; non-authoritative. | Future reviewed scripts under `dev/`. |
| `TEMPORARY` | Ticket-bound, expiry-bound helper that must be deleted or promoted. | `one_off/` lane. |
| `OPERATIONAL_HELPER` | Substantive bounded maintenance or QA behavior with explicit contract. | Doctrine maintenance scripts. |
| `CI_INVOKED` | Called by a verified workflow. | Root-level MapLibre helper chain. |
| `TRUST_ADJACENT` | Writes or gates receipts, proofs, release-shaped records, correction, rollback, or publication-support artifacts. | MapLibre performance chain. |
| `GRADUATION_REQUIRED` | Reliance or authority burden exceeds the script root's intended role. | **PROPOSED current posture for the MapLibre helper chain.** |

A file may occupy more than one class. `CI_INVOKED` does not mean canonical, and `TRUST_ADJACENT` does not mean accepted authority.

[Back to top](#top)

---

## What belongs here

- This root README and child-lane indexes.
- Small shell, Python, Node, or other wrappers with bounded contracts.
- Local-development helpers under `dev/`.
- Bounded maintenance CLIs and wrappers under `maintenance/`.
- Temporary, expiry-bound one-off scripts under `one_off/`.
- Thin launchers around accepted tools, validators, tests, or pipelines.
- Read-only inspection and report-generation helpers.
- Transitional trust-adjacent wrappers while a documented graduation decision is active.
- Explicit migration, deprecation, cleanup, and rollback notes for scripts.
- Script-local usage documentation that states exact inputs, outputs, side effects, exit codes, network behavior, secret posture, validation, and rollback.

Every consequential script should carry or link:

- stable command identity;
- owner and reviewers;
- purpose and bounded scope;
- input and output paths;
- read, write, and delete sets;
- network and secret profile;
- deterministic or recorded variability;
- finite outcomes and exit-code mapping;
- validation command;
- generated-artifact classification;
- retention and cleanup;
- rollback or restoration procedure;
- graduation trigger and target.

[Back to top](#top)

---

## What does not belong here

| Do not place or retain here | Correct home or action |
|---|---|
| Long-lived validators, generators, builders, proof assemblers, release tools, or QA frameworks | `tools/` with accepted contracts and tests |
| Repeatable lifecycle or production orchestration | `pipelines/` |
| Shared or domain implementation logic | `packages/` |
| Test cases, assertions, test harness authority | `tests/` |
| Fixture payloads, baselines, golden outputs, invalid examples | `fixtures/` |
| Semantic contracts or JSON Schema | `contracts/`, `schemas/` |
| Policy rules, access grants, rights decisions, sensitivity decisions, consent approvals | `policy/` and governed review roots |
| Source descriptors, source activation, or identity registries | accepted source/registry roots |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads | governed `data/` lifecycle roots |
| Governed receipt and proof instances retained as canonical records | accepted `data/receipts/` and `data/proofs/` lanes |
| Release manifests, PromotionDecisions, CorrectionNotices, WithdrawalNotices, RollbackCards, or signatures as authoritative records | `release/` |
| Shared configuration defaults or templates | `configs/` |
| Deployment definitions, service units, firewall/proxy rules, production schedules | `infra/`, runtime, or app roots |
| Credentials, tokens, private keys, passwords, private endpoints, secret-bearing `.env` files | approved external secret system |
| Public API routes, UI components, browser bundles, or arbitrary script execution endpoints | accepted app/API/UI roots |
| Unowned experiments or forgotten temporary scripts | delete, quarantine in a reviewed branch, or assign an explicit one-off contract |
| Generated artifacts committed without classification, review, or rollback | classify, validate, route, or delete before merge |

[Back to top](#top)

---

## Inputs

A script may consume only inputs appropriate to its declared scope.

### Permitted input classes

- explicit CLI arguments;
- tracked manifests, lockfiles, schemas, contracts, configuration examples, and fixtures;
- accepted tool, validator, package, pipeline, and test entry points;
- ignored workstation-local overrides where the consumer contract permits them;
- non-secret environment variables;
- approved secret references or injected values;
- local services or reviewed remote endpoints;
- artifacts generated earlier in the same bounded run;
- repository metadata such as commit SHA, branch, or changed paths.

### Required input controls

A consequential script must:

1. reject unknown arguments;
2. validate required paths and versions;
3. distinguish tracked, ignored, generated, and external inputs;
4. pin or record dependency and tool versions;
5. avoid broad scans of secrets or protected data;
6. deny unreviewed network sources;
7. resolve symlinks and path traversal safely before writes;
8. record when input freshness, policy, rights, sensitivity, or release state affects execution;
9. stop rather than invent defaults when authority-bearing inputs are missing;
10. avoid reading public clients directly from internal or canonical stores outside accepted interfaces.

### Forbidden assumptions

A script must not assume that:

- path presence means an object is accepted;
- schema validity means a claim is true;
- a registry row means a source is active;
- a receipt exists because a JSON file is named like one;
- a release is approved because a manifest status says `candidate`;
- a local or CI environment reflects production;
- credentials exist or may be printed;
- network access is harmless;
- generated content is safe to commit or publish.

[Back to top](#top)

---

## Outputs

Script outputs remain **candidates or operational results** until the owning root validates and accepts them.

### Output classes

| Class | Examples | Required handling |
|---|---|---|
| Terminal-only | status, plan, warning, finite outcome | No secret or protected content; stable exit mapping. |
| Local temporary | cache, scratch report, preview | Ignored or deleted; not evidence or release material. |
| Build/QA artifact | screenshots, diffs, perf results, failure bundle | `artifacts/` may carry temporary QA output; classify retention and sensitivity. |
| Fixture candidate | regenerated examples | Compare deterministically; validate; review before replacing fixture authority. |
| Lifecycle candidate | transformed or derived data | Route to WORK/QUARANTINE and governed promotion, never directly to PUBLISHED. |
| Receipt candidate | run or validation receipt-shaped object | Validate and route to accepted receipt lane before treating as process memory. |
| Proof candidate | ProofPack or integrity object | Validate and route to accepted proof lane before treating as proof. |
| Release candidate | manifest, correction, withdrawal, rollback object | Route to `release/` and governed review; scripts cannot approve it. |
| Code/config mutation | source, docs, config, registry changes | Dry run, exact diff, tests, owner review, rollback. |

### Minimum output declaration

```yaml
command_id: <stable-id>
mode: inspect | plan | apply | verify
outcome: NOOP | PLANNED | APPLIED | PARTIAL | HELD | DENIED | ERROR
reads: []
writes: []
deletes: []
network_profile: none | reviewed-profile
secret_refs: []
generated_objects:
  - path: <path>
    class: terminal | temporary | artifact | fixture_candidate | lifecycle_candidate | receipt_candidate | proof_candidate | release_candidate | mutation
validation:
  - <command or check>
rollback: <mechanical restoration>
owner: <owner>
```

This is a **PROPOSED declaration profile**, not a confirmed schema.

[Back to top](#top)

---

## Confirmed current inventory

### Child lanes

```text
scripts/
├── README.md
├── dev/
│   ├── README.md
│   ├── bootstrap.sh
│   └── regen_fixtures.sh
├── maintenance/
│   ├── README.md
│   ├── Python maintenance CLIs and helpers
│   └── shell wrappers and test bundle
└── one_off/
    └── README.md
```

### Root-level MapLibre performance helpers

```text
scripts/
├── maplibre-smoke-perf.mjs
├── build-maplibre-render-diff.mjs
├── attest-maplibre-perf.mjs
├── build-maplibre-perf-release-manifest.mjs
├── build-maplibre-perf-proof-pack.mjs
├── build-maplibre-perf-correction-and-rollback.mjs
└── build-maplibre-perf-failure-bundle.mjs
```

### Supporting entry points and workflow

- `package.json` exposes `maplibre:perf`, `maplibre:render-diff`, `maplibre:attest`, `maplibre:manifest`, `maplibre:proof`, `maplibre:govern`, `maplibre:proof:validate`, `maplibre:failure-bundle`, `maplibre:correction`, `maplibre:perf:full`, and `maplibre:clean`.
- `.github/workflows/maplibre-perf-governance.yml` installs Node, Python, browser, and validator dependencies; starts a fixture server; runs the scripts and validators; builds failure artifacts on failure; and uploads the generated artifact tree.
- The workflow definition is **CONFIRMED**. Current run success, required-check status, production use, signing, and release adoption are **UNKNOWN** unless separately verified.

### Inventory limitations

This is not a complete proof against:

- ignored or untracked scripts;
- branch-only or historical scripts;
- local operator copies;
- dynamically downloaded scripts;
- generated executables;
- workflow commands outside the inspected surfaces;
- scripts nested deeper than the inspected and documented inventory.

[Back to top](#top)

---

## Child-lane contracts

### `dev/` — local development helpers

Current posture:

- two six-line Bash placeholders;
- no dependency installation;
- no fixture regeneration;
- no confirmed CI use;
- no production authority;
- no secret store;
- future mutation must be inspectable, dry-run capable, tested, and reversible.

Use `dev/` for small workstation-oriented wrappers only. Graduate implementation when it becomes reliable infrastructure, a shared tool, a generator, or a test harness.

### `maintenance/` — bounded repository maintenance

Current posture:

- substantive doctrine-artifact preflight, registry, provenance, readiness, synchronization, and test-bundle behavior;
- mixed maturity;
- direct invocation by the repository promotion-gate workflow;
- release- and promotion-adjacent use;
- some scripts emit or write receipt/summary-shaped objects;
- long-term placement and accepted receipt home remain unresolved.

Maintenance scripts may support gates but cannot become doctrine, policy, validator, receipt, or release authority. Release-critical logic requires stronger ownership, tests, output contracts, CI evidence, and likely graduation.

### `one_off/` — temporary quarantine

Current posture:

- README-only in bounded evidence;
- empty by default;
- deletion-first;
- dry-run first;
- network denied by default;
- every temporary script requires task, owner, risk, inputs, outputs, rollback, expiry, and delete-or-promote decision.

One-off scripts must never become the normal path for ingestion, validation, evidence resolution, policy enforcement, promotion, publication, correction, or rollback.

[Back to top](#top)

---

## Root-level MapLibre performance chain

### Confirmed execution chain

```text
configs/maplibre/perf-envelope.v1.json
  -> maplibre-smoke-perf.mjs
  -> build-maplibre-render-diff.mjs
  -> attest-maplibre-perf.mjs
  -> build-maplibre-perf-release-manifest.mjs
  -> tools/validators/maplibre/validate_perf_governance.py
  -> build-maplibre-perf-proof-pack.mjs
  -> tools/validators/maplibre/validate_perf_proof_pack.py
  -> release-manifest rebuild
  -> final governance validation
```

On workflow failure:

```text
failure
  -> build-maplibre-perf-correction-and-rollback.mjs
  -> build-maplibre-perf-failure-bundle.mjs
  -> failure-bundle validator
  -> artifact upload
```

### Confirmed generated paths

The inspected scripts write under `artifacts/perf/`, including:

- performance results;
- frame-time CSV files;
- screenshots;
- render-diff reports and images;
- run-receipt-shaped JSON;
- unsigned DSSE-shaped envelope and checksum;
- release-manifest-shaped JSON;
- ProofPack-shaped JSON;
- draft correction notice;
- draft rollback plan;
- failure bundle.

### Boundary determination

**CONFIRMED:** the code and workflow implement a substantive CI-oriented artifact chain.

**CONFLICTED:** trust-bearing object families are represented under `artifacts/perf/`, while KFM doctrine treats `artifacts/` as build/docs/QA/temporary and assigns accepted receipts, proofs, and release records to governed data and release roots.

**PROPOSED:** retain `artifacts/perf/` as an ephemeral CI staging area only, then validate and deliberately promote accepted receipt/proof/release records to their owning roots through a governed process.

**NEEDS VERIFICATION:** whether the root scripts should graduate to a structure such as `tools/maplibre/perf/`, whether the workflow should call a package or pipeline, and whether any generated object is currently consumed outside CI.

> [!IMPORTANT]
> A `RunReceipt`, `ProofPack`, `ReleaseManifest`, `CorrectionNotice`, or rollback object name inside `artifacts/perf/` does not make that file the canonical governed object. Placement, schema, validator, evidence, review, signature, release state, correction path, and rollback authority still apply.

### Network posture

The smoke script loads MapLibre assets and glyphs from public URLs while also reading local fixture-server content. The workflow installs package and browser dependencies from external sources. This is **CONFIRMED network use**, not a no-network test lane.

The final governance contract should specify:

- allowed hosts;
- dependency lock and integrity behavior;
- cache and outage handling;
- reproducibility limits;
- data-exfiltration safeguards;
- whether release-grade runs require vendored or mirrored assets;
- how remote-version drift is represented in receipts.

[Back to top](#top)

---

## Safe execution contract

Every consequential script should support a visible sequence:

```text
inspect
  -> validate prerequisites
  -> plan exact reads/writes/deletes/network calls
  -> dry run
  -> explicit apply
  -> validate outputs
  -> emit finite outcome
  -> preserve review evidence
  -> clean up or route outputs
```

### Default rules

- No-argument mode should be read-only unless the command is inherently read-only.
- Write mode should require `--apply`, `--write`, or an equally explicit action.
- Destructive operations should require a narrower confirmation.
- Unknown arguments and fields should fail.
- Scripts should not automatically stage, commit, push, merge, release, or publish.
- Scripts should not modify canonical records when the precondition state is stale or conflicted.
- Partial writes should return `PARTIAL` or `ERROR`, not success.
- Temporary output should be cleaned or retained under an explicit policy.
- Governed output should be validated and routed through its owning root.
- CI mode and local mode should declare any behavioral differences.
- Network access should be denied unless the command contract lists approved endpoints.
- Secrets should be injected through an approved mechanism and redacted from output.

### Idempotence and replay

Where practical:

- the same inputs and pinned versions should yield the same plan;
- file ordering, locale, time, random identifiers, and environment should be controlled or recorded;
- repeated apply after success should produce `NOOP` or a declared update;
- generated object hashes should be stable when semantic inputs are unchanged;
- a receipt or run record should identify the tool version, commit, parameters, and input digests;
- rollback should identify the exact prior state or restoration target.

[Back to top](#top)

---

## Generated-artifact and trust-object boundary

### Staging is not promotion

```text
script output
  -> temporary or WORK candidate
  -> schema/contract validation
  -> policy, rights, sensitivity, and evidence checks
  -> receipt/proof assembly in the correct authority root
  -> steward review
  -> PromotionDecision and ReleaseManifest where applicable
  -> PUBLISHED
```

A script must never shortcut this flow by writing directly to a path and treating the path as approval.

### `artifacts/` compatibility rule

`artifacts/` may hold:

- temporary QA output;
- screenshots and render diffs;
- build reports;
- CI upload bundles;
- disposable evidence candidates;
- preview or diagnostic material.

It must not silently become the sovereign home for:

- canonical receipts;
- accepted proofs;
- release manifests;
- policy decisions;
- correction or withdrawal records;
- rollback authority;
- published material.

### Required handoff record

When a script produces a trust-adjacent candidate, record:

| Field | Purpose |
|---|---|
| Candidate path | Where the temporary object was written. |
| Candidate class | Receipt, proof, release, correction, rollback, lifecycle, or other. |
| Owning root | Canonical destination if admitted. |
| Schema and contract | Shape and semantic authority. |
| Validator | Executable check and version. |
| Evidence refs | Support used by the object. |
| Policy/review refs | Decisions and reviewers required. |
| Digest | Integrity of the candidate. |
| Promotion status | `staged`, `held`, `denied`, `accepted`, or `superseded`. |
| Correction/rollback | What invalidates or reverses the candidate. |
| Retention | Cleanup or preservation period. |

This handoff profile is **PROPOSED**.

[Back to top](#top)

---

## Finite outcomes and failure semantics

### Script execution outcomes

| Outcome | Meaning |
|---|---|
| `NOOP` | Preconditions were valid and no change was needed. |
| `PLANNED` | A dry-run or review plan was produced; no mutation occurred. |
| `APPLIED` | The declared bounded mutation completed and passed required verification. |
| `PARTIAL` | Some effects occurred; reconciliation and review are required. |
| `HELD` | Execution or output is held pending evidence, dependency, freshness, review, or placement. |
| `DENIED` | Policy, rights, sensitivity, consent, access, release, or scope forbids the action. |
| `ERROR` | Technical execution failed. |

### Mandatory failure behavior

- `PARTIAL`, `HELD`, `DENIED`, and `ERROR` must not be converted to zero-success without an explicit wrapper contract.
- A failed validator must block downstream trust claims.
- Missing receipts, proofs, review, signatures, or release records must not be invented.
- A failure handler may capture diagnostics and draft correction/rollback candidates, but it cannot authorize correction or rollback.
- Scripts must avoid printing secrets, protected context, exact sensitive locations, living-person data, or private reasoning in failures.
- Cleanup must not destroy incident evidence or the prior recoverable state.
- Retry behavior must distinguish transient failures from deterministic invalid input.
- A stale or superseded candidate must not be silently reused.

### Exit-code posture

Exact numeric codes remain script-specific until accepted command contracts exist. Each script should document:

- success/no-op;
- planned/no-write;
- validation or governance failure;
- denied/held;
- partial mutation;
- technical error;
- invalid invocation.

[Back to top](#top)

---

## Graduation and promotion rules

A script must be reviewed for graduation when any of these becomes true:

| Trigger | Expected destination or action |
|---|---|
| Reused by multiple apps, packages, or domains | Move reusable logic to `packages/`; keep a thin CLI if useful. |
| Becomes a long-lived validator, generator, builder, or proof assembler | Move to `tools/` with tests, contracts, schemas, and ownership. |
| Orchestrates repeatable lifecycle or production work | Move to `pipelines/`. |
| Defines or enforces public/runtime behavior | Move to the owning app, package, runtime, or infra lane. |
| Is required by CI or branch protection | Add command contract, tests, ownership, failure semantics, and decide whether `tools/` or pipeline placement is required. |
| Writes or validates receipts, proofs, release records, corrections, or rollback objects | Establish canonical object homes, validators, reviews, receipts, and likely graduate implementation. |
| Mutates schemas, contracts, policy, registries, fixtures, or release records | Require dry run, owner review, rollback, and move logic to the owning tool/pipeline when repeated. |
| Requires secrets, broad network access, or production credentials | Normally graduate to governed infra/runtime/tooling; deny casual script use. |
| Becomes scheduled or operationally monitored | Move to a durable service, pipeline, or maintenance tool. |
| One-off task finishes | Delete the script or promote the useful logic. |
| Script and documentation disagree | Hold use, correct docs/code, and preserve rollback. |

### Graduation record

A graduation PR should state:

- source script and callers;
- destination responsibility root;
- reason for graduation;
- stable command/interface contract;
- compatibility wrapper plan;
- input/output and artifact migration;
- tests and CI;
- ownership;
- deprecation window;
- correction and rollback;
- deletion date for obsolete wrappers.

### Current MapLibre determination

The MapLibre chain is **PROPOSED for graduation review now** because it is:

- CI-invoked;
- multi-step;
- networked;
- artifact-generating;
- validator-integrated;
- receipt/proof/release/correction/rollback adjacent;
- relied upon by a named governance workflow.

This README does not select the final destination or move any file.

[Back to top](#top)

---

## Validation

### Root inventory and syntax

```bash
find scripts -maxdepth 3 -type f | sort

find scripts -name '*.sh' -print0 |
  xargs -0 -r bash -n

find scripts -name '*.py' -print0 |
  xargs -0 -r python -m py_compile

find scripts -name '*.mjs' -print0 |
  xargs -0 -r -n1 node --check
```

### Development lane

```bash
bash -n scripts/dev/bootstrap.sh
bash -n scripts/dev/regen_fixtures.sh
bash scripts/dev/bootstrap.sh
bash scripts/dev/regen_fixtures.sh
```

Expected current behavior is TODO output only.

### Maintenance lane

```bash
python -m py_compile scripts/maintenance/*.py
bash -n scripts/maintenance/*.sh
python scripts/maintenance/run_doctrine_artifact_preflight.py --help
bash scripts/maintenance/run_doctrine_artifact_test_suite.sh
```

Review help and write options before executing reconciliation commands.

### MapLibre helper chain

```bash
npm run maplibre:perf:full
```

Or inspect syntax and individual steps first:

```bash
node --check scripts/maplibre-smoke-perf.mjs
node --check scripts/build-maplibre-render-diff.mjs
node --check scripts/attest-maplibre-perf.mjs
node --check scripts/build-maplibre-perf-release-manifest.mjs
node --check scripts/build-maplibre-perf-proof-pack.mjs
node --check scripts/build-maplibre-perf-correction-and-rollback.mjs
node --check scripts/build-maplibre-perf-failure-bundle.mjs
```

### Documentation and mutation review

```bash
git status --short
git diff -- scripts package.json .github/workflows/maplibre-perf-governance.yml
git diff -- artifacts data release configs fixtures tests tools
```

### Validation limitations

For this README revision:

- commands were not executed;
- workflow runs were not evaluated;
- no generated artifacts were inspected;
- no production behavior was verified;
- no migration or graduation test was performed.

File and workflow presence is not runtime success.

[Back to top](#top)

---

## Review burden

### Ordinary maintainer review

Required for:

- README-only changes;
- comments;
- non-mutating local helpers;
- typo or help-text corrections;
- narrow wrappers with no trust-adjacent output.

### Owning steward review

Required when a script touches:

- schemas, contracts, policy, rights, sensitivity, consent, or access;
- source activation, registries, identity, or provenance;
- fixtures, tests, validators, or golden baselines;
- lifecycle data;
- receipts, proofs, catalogs, or release objects;
- correction, withdrawal, rollback, or signatures;
- sensitive domains or protected locations;
- secret references or external services;
- CI merge gates or scheduled operations.

### Security review

Required for:

- credentials or secret injection;
- remote mutation;
- downloads or unpinned network content;
- shell execution from external input;
- path traversal or archive extraction;
- deletion or recursive writes;
- production endpoints;
- logs or artifacts containing protected context.

### Release and separation-of-duty review

Required when a script or workflow:

- generates a release candidate;
- evaluates promotion eligibility;
- produces or validates release manifests;
- signs artifacts;
- drafts correction, withdrawal, or rollback records;
- can alter what public clients consume.

The same script must not become generator, validator, approver, and publisher without an explicit accepted design and compensating controls.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| [`scripts/dev/`](./dev/) | Placeholder and future local-development wrappers. |
| [`scripts/maintenance/`](./maintenance/) | Mixed-maturity repository maintenance and doctrine preflight. |
| [`scripts/one_off/`](./one_off/) | Temporary deletion-first quarantine lane. |
| [`tools/`](../tools/) | Long-lived validators, generators, builders, proof assemblers, and governed tooling. |
| [`tools/validators/`](../tools/validators/) | Validator implementation authority. |
| [`pipelines/`](../pipelines/) | Repeatable lifecycle and production orchestration. |
| [`packages/`](../packages/) | Reusable implementation. |
| [`tests/`](../tests/) | Executable proof of behavior. |
| [`fixtures/`](../fixtures/) | Valid, invalid, negative, and golden examples. |
| [`configs/`](../configs/) | Shared safe defaults and configuration templates. |
| [`artifacts/`](../artifacts/) | Build, docs, QA, preview, and temporary outputs; not sovereign truth. |
| [`data/receipts/`](../data/receipts/) | Governed process-memory records. |
| [`data/proofs/`](../data/proofs/) | Governed proof objects. |
| [`release/`](../release/) | Promotion, release, correction, withdrawal, and rollback authority. |
| [MapLibre workflow](../.github/workflows/maplibre-perf-governance.yml) | Confirmed CI caller for root-level MapLibre scripts. |
| [MapLibre governance](../docs/quality/maplibre-perf-governance.md) | Draft architecture and migration guidance. |
| [Directory Rules](../docs/doctrine/directory-rules.md) | Placement and authority-boundary doctrine. |

[Back to top](#top)

---

## ADRs

### Existing related decisions and doctrine

- Directory Rules — responsibility-root placement, compatibility, migration, and trust-bearing artifact boundaries.
- Lifecycle law — promotion is a governed state transition, not a file move.
- Receipt/proof/catalog/release separation doctrine.
- MapLibre performance governance draft — proposes graduated tooling and canonical trust-object placement.
- Telemetry, signing, security, and rollback standards where scripts emit operational or trust-adjacent material.

### ADRs or decisions still needed

| Decision | Status |
|---|---|
| Confirm `scripts/` root and child-lane ownership model. | NEEDS VERIFICATION |
| Decide the final home for MapLibre performance scripts. | ADR or explicit placement decision recommended |
| Decide whether MapLibre CI artifacts remain ephemeral only or are promoted to canonical receipt/proof/release roots. | NEEDS VERIFICATION |
| Pin accepted schemas/contracts for MapLibre RunReceipt, ProofPack, ReleaseManifest, correction, rollback, and failure bundles. | NEEDS VERIFICATION |
| Define a generic script command-effect declaration profile. | PROPOSED |
| Define risk classification and review thresholds for scripts. | PROPOSED |
| Define CI-required script graduation policy. | PROPOSED |
| Define allowed network and dependency-integrity posture for release-grade script runs. | NEEDS VERIFICATION |
| Define canonical receipt home for maintenance doctrine-artifact preflight output. | NEEDS VERIFICATION |
| Define automated expiry enforcement for `one_off/`. | NEEDS VERIFICATION |
| Define deprecation, compatibility-wrapper, and cleanup rules after graduation. | PROPOSED |

No path is moved and no ADR is accepted by this README revision.

[Back to top](#top)

---

## Correction and rollback

### Documentation rollback

This README change is documentation-only. Roll back by reverting the update commit or restoring prior blob `4000b70a60af0d0656a4343ac6ae7f951b5327e3`.

### Script correction triggers

Correct or hold a script when:

- documented and actual side effects differ;
- an output uses the wrong authority root;
- a generated object fails schema, contract, policy, or integrity checks;
- secrets or protected context appear in output;
- network dependencies drift;
- a workflow silently ignores failure;
- a script is relied upon beyond its reviewed maturity;
- an owner or rollback target is missing;
- a temporary script passes its expiry;
- public clients or production systems depend directly on it;
- generated receipt/proof/release claims overstate their authority.

### Operational rollback expectations

For a mutating script:

1. stop further runs;
2. preserve logs and bounded incident evidence without exposing secrets;
3. record the exact partial state;
4. restore prior files, registry rows, configuration, fixtures, or artifacts;
5. invalidate candidate outputs and caches;
6. rerun validators and tests;
7. notify downstream consumers;
8. issue correction, withdrawal, or rollback records through the owning authority root when required;
9. document the cause and fix;
10. decide whether to retire, restrict, or graduate the script.

### MapLibre artifact rollback posture

Until canonical promotion is defined:

- treat `artifacts/perf/` as temporary CI staging;
- do not infer that a manifest, proof, receipt, correction, or rollback object there is authoritative;
- retain or upload failure evidence according to workflow policy;
- prevent failed candidates from promotion;
- restore the prior released renderer or artifact set through release authority;
- migrate accepted trust objects only through a reviewed governed process.

[Back to top](#top)

---

## Open verification register

| Item | Evidence needed |
|---|---|
| Exact recursive script inventory | Commit-pinned tree listing and classification. |
| Accepted owners and CODEOWNERS | Current ownership rules plus steward confirmation. |
| All workflow and Makefile callers | Search plus workflow execution evidence. |
| MapLibre workflow health | Current runs, artifacts, failures, branch-protection status. |
| MapLibre helper destination | Directory Rules review and accepted ADR or migration decision. |
| Canonical MapLibre artifact homes | Accepted contracts, schemas, validators, receipts/proofs/release layouts. |
| Artifact staging-to-promotion process | Implementation, receipts, reviews, correction, rollback tests. |
| Signing posture | Accepted signer, keyless/keyed policy, verification, revocation, CI environment. |
| Network reproducibility | Allowed hosts, locks, mirrors, caching, outage behavior, remote version receipts. |
| Maintenance receipt home | Accepted data/receipt layout and migration from compatibility paths. |
| Maintenance CI significance | Verified workflow callers, strict gates, current test results. |
| Dev helper future behavior | Dependency manager, platforms, test harness, network and secret profile. |
| One-off expiry enforcement | Schema/profile, CI check, cleanup cadence, owner. |
| Generic script command contract | Contract/schema or documented standard. |
| Generic risk classes | Accepted policy or ADR and reviewer matrix. |
| Generated artifact retention | Retention, sensitivity, deletion, audit, and storage controls. |
| Production use | Deployment, schedules, operators, logs, incidents, SLOs. |
| Public boundary | Tests proving no normal public client invokes repository scripts. |
| Graduation cleanup | Inbound-link inventory, compatibility wrappers, deletion and rollback plan. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-16 |
| Evidence base | `main@15d88fceced7050abac4493b9cf66f5bc288c1e6` |
| Target prior blob | `4000b70a60af0d0656a4343ac6ae7f951b5327e3` |
| Review mode | Repository-grounded documentation revision; one-file scope |
| Implementation effect | None — documentation only |
| Rollback | Revert the update commit or restore the prior blob |
| Runtime/CI effect | None; no script or workflow changed |

### Maintenance triggers

Re-review when:

- a script is added, removed, moved, renamed, or made executable;
- a child-lane README changes;
- a placeholder gains real behavior;
- a one-off script is admitted;
- a script is added to CI or branch protection;
- a script becomes scheduled or production-used;
- a script writes a new artifact family;
- a trust-adjacent object gains an accepted schema or canonical home;
- MapLibre scripts graduate or artifact paths migrate;
- maintenance preflight output homes or gates change;
- network, dependency, secret, logging, or retention posture changes;
- correction or rollback automation changes;
- Directory Rules or an accepted ADR changes placement.

### v0.2 → v0.3 change summary

- Grounds the root against the merged `dev/` and `one_off/` v0.2 boundaries.
- Preserves the maintenance lane's substantive mixed-maturity posture.
- Confirms package and workflow wiring for the MapLibre performance chain.
- Records selected root-level script implementations and generated paths.
- Upgrades CI invocation from UNKNOWN to CONFIRMED workflow-definition evidence.
- Makes the `artifacts/perf/` trust-object placement conflict explicit.
- Adds authority routing, bounded inputs and outputs, finite outcomes, network and secret controls, artifact handoffs, graduation triggers, review burdens, correction, and rollback.
- Proposes immediate graduation review for the CI-invoked MapLibre chain without moving files.
- Preserves the controlling rule: scripts support governance but never replace it.

<p align="right"><a href="#top">Back to top</a></p>
