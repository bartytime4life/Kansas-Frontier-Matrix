# `schemas/maplibre/` — MapLibre Performance Schema Compatibility Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-maplibre-readme
title: schemas/maplibre/ — MapLibre Performance Schema Compatibility Lane
type: readme; schema-compatibility-index; migration-guardrail; performance-governance-boundary
version: v0.2
status: draft; compatibility-lane; eight-permissive-placeholders; workflow-hold; placement-conflicted; NEEDS VERIFICATION
owners: OWNER_TBD — Schema steward · Contract steward · MapLibre steward · Performance steward · Validation steward · Evidence steward · Policy steward · Release steward · Docs steward
created: NEEDS VERIFICATION — README existed before v0.1 expansion
updated: 2026-07-22
policy_label: public; schemas; maplibre; performance; compatibility; no-parallel-authority; no-publication-by-validation
current_path: schemas/maplibre/README.md
truth_posture: CONFIRMED eight individually opened accept-any-object JSON Schema 2020-12 placeholders and current static readiness workflow at the pinned snapshot / PROPOSED schema semantics and migration destinations / CONFLICTED root-topic compatibility placement versus the proposed versioned schema-home decision / UNKNOWN owners, consumers, accepted contracts, fixture coverage, runtime behavior, current CI conclusion, release use, and migration schedule / NEEDS VERIFICATION before any schema promotion or consumer binding
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 459b41d7ec91240742d8b2d3e5d9eb4dbd248df7
  prior_blob: 2dda90174ec219fd08edce155f8d151427e92ddb
related:
  - ../README.md
  - ../contracts/v1/map/README.md
  - ../contracts/v1/layers/README.md
  - ../../docs/architecture/directory-rules.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/quality/maplibre-perf-governance.md
  - ../../configs/maplibre/README.md
  - ../../packages/maplibre/README.md
  - ../../tools/validators/maplibre/README.md
  - ../../tests/maplibre/README.md
  - ../../tests/fixtures/maplibre/README.md
  - ../../.github/workflows/maplibre-perf-governance.yml
notes:
  - "v0.2 preserves the prior compatibility boundary and replaces partial inventory claims with exact per-file inspection at the pinned base."
  - "All eight direct schema files contain the same three-key accept-any-object placeholder and share blob SHA 511e7f34ca84390fd5d000326ab33c46c3050fc4."
  - "ADR-0001 is present but proposed; it does not yet prove an accepted migration destination for every MapLibre performance object family."
  - "The current MapLibre performance workflow detects placeholder and readiness drift, runs syntax checks and three scalar negative paths, then records WORKFLOW_HOLD; it does not run browser performance, render-diff, attestation, proof, release, correction, or rollback stages."
  - "This README change does not modify schemas, contracts, policy, fixtures, validators, tests, workflows, runtime behavior, artifacts, release records, or KFM publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

> [!IMPORTANT]
> `schemas/maplibre/` is a **non-authoritative compatibility lane** inside the canonical `schemas/` responsibility root. Its eight JSON files are syntactically valid, permissive placeholders. They do not establish semantic contracts, meaningful validation, evidence closure, policy approval, performance, release readiness, rollback capability, or publication safety.

> [!WARNING]
> Do not add fields, bind new consumers, or treat the current `$id`-less paths as stable contracts. The proposed repository-wide schema-home decision favors versioned families under `schemas/contracts/v1/`, but the final family for each performance envelope, receipt, report, proof, release, correction, failure, or rollback object still requires review.

## Quick navigation

[Purpose](#purpose) · [Status](#status) · [Boundary](#boundary) · [Repository fit](#repository-fit) · [Inventory](#current-inventory) · [Placeholder shape](#verified-placeholder-shape) · [Responsibilities](#object-family-and-authority-routing) · [Compatibility](#compatibility-rules) · [Consumers](#consumer-rules) · [Validation](#validation) · [Workflow](#current-workflow-boundary) · [Migration](#migration-and-promotion-gates) · [Review](#review-burden) · [Done](#definition-of-done) · [Questions](#open-questions) · [Evidence](#evidence-ledger) · [Correction](#correction-and-rollback)

---

## Purpose

`schemas/maplibre/` documents and temporarily retains eight MapLibre performance-governance schema placeholders while KFM resolves their semantic contracts, object-family ownership, canonical versioned schema placement, consumers, fixtures, validators, policy boundaries, and release relationships.

This lane exists to make unresolved compatibility visible. It must not become a second canonical schema system merely because scripts or validators currently reference its files.

The durable responsibility split is:

```text
contracts/                    semantic meaning and invariants
schemas/                      machine-checkable shape
policy/                       allow / deny / restrict / abstain
fixtures/ and tests/          examples and enforceability proof
tools/validators/             executable validation
configs/                      commit-safe thresholds and defaults
data/receipts/ and proofs/    emitted audit and proof records
release/                      promotion, correction, withdrawal, rollback
packages/ and apps/           renderer adapter and governed UI behavior
```

MapLibre remains a renderer and interaction surface downstream of those authorities. A schema in this directory cannot make a rendered result true, cited, rights-cleared, sensitive-safe, reviewed, released, or public.

[Back to top](#top)

---

## Status

| Surface | Status at the pinned snapshot | Safe conclusion |
|---|---|---|
| This README | **CONFIRMED** | Existing compatibility index; v0.2 expands its evidence and migration boundary. |
| Eight named `*.schema.json` files | **CONFIRMED** | Each was opened individually at the pinned commit. |
| JSON syntax | **CONFIRMED** | Each file parses as JSON and declares JSON Schema 2020-12. |
| Machine constraints | **CONFIRMED permissive placeholder** | Every schema accepts any JSON object and declares no fields or required keys. |
| `$id`, title, version, KFM metadata | **ABSENT in the opened files** | Identity, registry, and version posture are not established. |
| Semantic contracts | **UNKNOWN** | Filenames suggest object roles; the schema files do not define meaning. |
| Canonical placement | **PROPOSED / CONFLICTED** | ADR-0001 proposes `schemas/contracts/v1/`; it remains proposed and no versioned MapLibre README exists at the checked path. |
| Schema wrappers | **CONFIRMED present** | Eight wrappers route to the common JSON Schema runner, but permissive schemas impose no meaningful field validation. |
| Governance validators | **CONFIRMED placeholders** | The current readiness workflow deliberately checks that seven broader verifiers remain placeholders. |
| Executable MapLibre tests | **CONFIRMED narrow** | Three direct negative tests cover only invalid scalar fixture values. |
| Current workflow definition | **CONFIRMED static readiness gate** | It runs syntax and three negative paths, detects maturity drift, and records an explicit `WORKFLOW_HOLD`. |
| Current workflow run result | **UNKNOWN** | No current Actions conclusion is asserted by source inspection alone. |
| Browser performance, render diff, proof, release, correction, rollback | **NOT EXECUTED by the inspected workflow** | No operational or publication claim follows from this lane. |
| Owners and accepted migration schedule | **NEEDS VERIFICATION** | No accountable assignment or approved schedule was established. |

### Truth labels

| Label | Meaning in this README |
|---|---|
| **CONFIRMED** | Verified in the pinned repository snapshot or named attached doctrine. |
| **PROPOSED** | Intended design or future state not accepted and verified as current. |
| **UNKNOWN** | Available evidence does not establish the claim. |
| **NEEDS VERIFICATION** | A concrete repository, governance, test, or runtime check is still required. |
| **CONFLICTED** | Current surfaces point to incompatible authority or placement postures. |

[Back to top](#top)

---

## Boundary

This directory is under `schemas/`, so its only potential authority is machine-checkable shape. At the inspected snapshot, even that authority is intentionally weak because every direct schema is an accept-any-object placeholder.

### This lane may

- retain the eight existing placeholder files while migration is unresolved;
- document their exact current shape and limitations;
- point to paired contracts, policies, fixtures, validators, tests, configuration, evidence, and release surfaces;
- carry reviewed compatibility, deprecation, redirect, and migration notes; and
- expose drift without silently normalizing it.

### This lane must not

- define semantic meaning that belongs in `contracts/`;
- encode policy, rights, sensitivity, review, or release decisions;
- store configuration instances, fixtures, runtime data, screenshots, metrics, receipts, proofs, manifests, corrections, or rollback records;
- implement validators, scripts, APIs, UI, MapLibre adapters, or browser behavior;
- authorize a source, layer, style, tile, plugin, export, or public map;
- turn a valid payload into an EvidenceBundle, PolicyDecision, PromotionDecision, or PUBLISHED artifact; or
- evolve independently as a parallel schema authority.

Schema validity constrains bytes. It does not establish truth, evidence support, source role, rights, sensitivity, freshness, review state, release state, or safe presentation.

[Back to top](#top)

---

## Repository fit

```text
schemas/
├── README.md
├── maplibre/                                  # this compatibility lane
│   ├── README.md                              # this file
│   ├── perf-envelope.schema.json              # permissive placeholder
│   ├── perf-receipt.schema.json               # permissive placeholder
│   ├── render-diff-report.schema.json          # permissive placeholder
│   ├── perf-proof-pack.schema.json             # permissive placeholder
│   ├── perf-rollback-plan.schema.json           # permissive placeholder
│   ├── perf-failure-bundle.schema.json          # permissive placeholder
│   ├── perf-release-manifest.schema.json        # permissive placeholder
│   └── perf-correction-notice.schema.json       # permissive placeholder
└── contracts/
    └── v1/
        ├── map/                               # inspected versioned map family index
        └── layers/                            # inspected versioned layer family index

configs/maplibre/                              # performance-envelope instance and config boundary
tools/validators/maplibre/                     # wrappers and readiness verifiers
tests/maplibre/                                # narrow executable negative tests
tests/fixtures/maplibre/                       # documented fixture lanes; payload maturity held
packages/maplibre/                             # transitional package scaffold
docs/quality/maplibre-perf-governance.md       # design and governance lineage
.github/workflows/maplibre-perf-governance.yml # current static readiness HOLD
```

The checked path `schemas/contracts/v1/maplibre/README.md` does not exist at the pinned snapshot. The current contribution guide points to [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md) for placement preflight while the repository also retains a doctrine-path edition. That authority and placement graph remains **CONFLICTED**. Both editions describe a versioned MapLibre family as proposed architecture, and ADR-0001 proposes the general versioned schema-home rule. None of those facts authorizes a silent move or lets this README invent final destinations for the eight objects.

### Placement basis

- `schemas/` is the correct responsibility root for machine-checkable shape.
- The repository carries multiple Directory Rules artifacts; their lineage and canonical document home remain unresolved, so this README cites the current contribution-preflight target and preserves the doctrine-path companion.
- The current `schemas/maplibre/` topic lane is transitional and must not become parallel authority.
- ADR-0001 is a **proposed** schema-home decision, not accepted migration proof.
- Receipt, proof, release, correction, failure, and rollback names cross object-family boundaries; each requires semantic and lifecycle review before placement.
- Any move must preserve consumers, `$id`/identity decisions, fixtures, validator bindings, compatibility windows, correction lineage, and rollback.

[Back to top](#top)

---

## Current inventory

The eight schema paths below were individually read at the pinned evidence snapshot and verified unaffected by the later base movement to `459b41d7ec91240742d8b2d3e5d9eb4dbd248df7`. All eight contain identical bytes and share blob SHA `511e7f34ca84390fd5d000326ab33c46c3050fc4`.

| Path | Current status | Filename-level intent only |
|---|---|---|
| [`perf-envelope.schema.json`](perf-envelope.schema.json) | **CONFIRMED permissive placeholder** | Performance threshold/envelope shape is PROPOSED. |
| [`perf-receipt.schema.json`](perf-receipt.schema.json) | **CONFIRMED permissive placeholder** | Performance receipt shape and receipt-family relationship are PROPOSED. |
| [`render-diff-report.schema.json`](render-diff-report.schema.json) | **CONFIRMED permissive placeholder** | Render comparison report shape and proof relationship are PROPOSED. |
| [`perf-proof-pack.schema.json`](perf-proof-pack.schema.json) | **CONFIRMED permissive placeholder** | Proof-pack shape and proof-family relationship are PROPOSED. |
| [`perf-rollback-plan.schema.json`](perf-rollback-plan.schema.json) | **CONFIRMED permissive placeholder** | Rollback-plan shape and release-family relationship are PROPOSED. |
| [`perf-failure-bundle.schema.json`](perf-failure-bundle.schema.json) | **CONFIRMED permissive placeholder** | Failure-bundle shape, lifecycle, and evidence relationship are PROPOSED. |
| [`perf-release-manifest.schema.json`](perf-release-manifest.schema.json) | **CONFIRMED permissive placeholder** | Release-manifest shape and relation to canonical release objects are PROPOSED. |
| [`perf-correction-notice.schema.json`](perf-correction-notice.schema.json) | **CONFIRMED permissive placeholder** | Correction-notice shape and relation to canonical correction objects are PROPOSED. |

The descriptions above derive only from filenames and nearby design documentation. They do not establish accepted contracts, fields, identity, lifecycle state, consumers, or publication authority.

### Inventory completeness boundary

Exact reads confirm this README and the eight named schema files. The workflow source also treats those eight filenames as the expected exact schema set and fails its readiness inspection if the set changes. A successful current workflow run or a complete API tree listing was not inspected, so this README does not upgrade that expected set into a claim about every possible unlisted path.

[Back to top](#top)

---

## Verified placeholder shape

Every direct schema currently contains:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true
}
```

### What this proves

- the file is valid JSON;
- it declares JSON Schema draft 2020-12;
- it accepts JSON objects; and
- undeclared properties are allowed.

### What this does not prove

- stable schema identity or `$id`;
- object title, description, version, or owner;
- required fields, types, ranges, formats, enums, or references;
- compatibility with `configs/maplibre/perf-envelope.v1.json`;
- semantic agreement with a contract;
- valid and invalid fixture polarity;
- validator rejection of malformed domain content;
- evidence, policy, review, signing, provenance, integrity, release, correction, or rollback closure;
- browser performance, render stability, visual equivalence, accessibility, or public safety; or
- readiness for runtime or public consumers.

Because these schemas accept any object, a passing wrapper invocation would prove only that the input is an object. It would not prove that the object is a meaningful performance envelope, receipt, proof pack, release manifest, correction notice, failure bundle, rollback plan, or render-diff report.

[Back to top](#top)

---

## Object-family and authority routing

Final destinations remain **NEEDS VERIFICATION**. Review each object by responsibility and lifecycle rather than moving all eight together because they share a MapLibre prefix.

| Concern | Owning authority surface | Required separation |
|---|---|---|
| Performance-object meaning | accepted Markdown contract family under `contracts/` | Define semantics and invariants before hardening shape. |
| Machine shape | accepted versioned family under `schemas/contracts/v1/` or an ADR-backed exception | Do not maintain divergent canonical definitions. |
| Threshold values and commit-safe defaults | [`configs/maplibre/`](../../configs/maplibre/README.md) | Configuration instances are not schemas or policy. |
| Allow, deny, restrict, abstain, sensitivity, and public-surface decisions | `policy/` | Schema validation cannot grant admission or release. |
| Valid, invalid, boundary, stale, denied, and error examples | `fixtures/` or the accepted MapLibre fixture lane | Fixtures are proof inputs, not authority. |
| Validator implementation | [`tools/validators/maplibre/`](../../tools/validators/maplibre/README.md) | Validators consume accepted schemas; they do not define object meaning. |
| Executable proof | [`tests/maplibre/`](../../tests/maplibre/README.md) and accepted integration lanes | Tests prove only exercised behavior. |
| Emitted receipts and proofs | accepted `data/receipts/` and `data/proofs/` lanes | Never store emitted records beside schemas. |
| Release, correction, withdrawal, and rollback decisions | `release/` and accepted release contracts/schemas | Candidate objects do not publish themselves. |
| Renderer adapter and UI behavior | `packages/`, `apps/explorer-web/`, governed APIs | Standard clients consume released, policy-safe artifacts. |

### Cross-family caution

The filename prefix `perf-` does not make every object a member of one schema family. Receipt, proof, release, correction, rollback, and failure objects may need to extend or reference existing cross-cutting KFM families. Review reuse and composition before introducing MapLibre-specific duplicates.

[Back to top](#top)

---

## What belongs here

- This compatibility README.
- The eight existing placeholders while ownership and migration remain unresolved.
- Minimal, reviewed compatibility or deprecation metadata.
- Links to accepted contracts, versioned schemas, fixtures, validators, tests, policy, evidence, release, correction, and rollback surfaces.
- A migration note that preserves old-path consumers and rollback when a destination is accepted.

## What does not belong here

- New canonical schema families or a new version hierarchy.
- Semantic contracts, policy rules, threshold instances, runtime records, receipts, proofs, manifests, correction records, or rollback records.
- Source, layer, style, tile, plugin, or map data.
- Fixtures, validator code, test code, browser scripts, package code, UI components, API handlers, screenshots, baselines, or build artifacts.
- Secrets, credentials, private data, sensitive locations, or rights-restricted material.
- Claims that schema validity establishes performance, evidence, safety, approval, release, or publication.

[Back to top](#top)

---

## Compatibility rules

| Rule | Requirement |
|---|---|
| Freeze canonical growth | Do not add fields or new schema families here before contract and placement review. |
| Do not bind new production consumers | New code, APIs, pipelines, validators, or UI features must not adopt these paths as stable canonical contracts. |
| Preserve existing references | Inventory all path and prospective `$id` consumers before moving, renaming, redirecting, or deleting a file. |
| Keep identities explicit | A new `$id`, version, title, or family assignment requires collision, registry, and compatibility review. |
| Avoid copy-based migration | Do not leave independently editable old and new schema definitions. Use a reviewed compatibility strategy. |
| Keep meaning separate | Pair each meaningful schema with an accepted semantic contract. |
| Treat permissiveness as a blocker | `additionalProperties: true` with no declared properties is not an operational validation boundary. |
| Preserve finite outcomes | Validation and policy outcomes must remain distinct; schema success must not be translated into release approval. |
| Fail safely | Missing evidence, rights, sensitivity, review, or release state must narrow, hold, abstain, deny, generalize, or quarantine as appropriate. |
| Preserve auditability | Migration must record source path, destination, decision, consumers, fixtures, validation, compatibility window, correction path, and rollback target. |

[Back to top](#top)

---

## Consumer rules

### New consumers

Do not bind new production consumers to `schemas/maplibre/*.schema.json` as canonical contracts. A documentation link may identify the compatibility lane, but it must not imply accepted field semantics or runtime maturity.

### Existing consumers

For every consumer discovered:

1. record its repository path, owner, execution role, schema path, and expected object family;
2. determine whether it parses a schema, validates an instance, generates code, creates an artifact, or only links documentation;
3. identify the exact valid, invalid, boundary, and negative fixtures it exercises;
4. preserve current behavior until an accepted replacement and parity plan exist;
5. validate old and new paths during a bounded compatibility window;
6. fail closed on unresolved identity, semantics, policy, evidence, or release state; and
7. retain a transparent rollback mapping until downstream parity is proven.

### Public and runtime clients

Public and standard UI clients must use governed APIs and released projections. They must never read this schema directory as a runtime data source or treat schema presence as permission to load a source, draw a layer, expose precise geometry, export content, or answer an evidence-dependent question.

[Back to top](#top)

---

## Validation

Use repository-native checks when the full repository is available. The commands below are structural and intentionally bounded.

### JSON and meta-schema structure

```bash
find schemas/maplibre -maxdepth 1 -type f -print | sort

find schemas/maplibre -maxdepth 1 -name '*.schema.json' -print0 \
  | xargs -0 -r -n1 python -m json.tool >/dev/null

python - <<'PY'
import json
from pathlib import Path

from jsonschema import Draft202012Validator

for path in sorted(Path("schemas/maplibre").glob("*.schema.json")):
    Draft202012Validator.check_schema(json.loads(path.read_text(encoding="utf-8")))
    print(f"meta-schema valid: {path}")
PY
```

These checks prove JSON and meta-schema structure only. They do not make the placeholders meaningful.

### Narrow executable tests

```bash
python -m pytest -q tests/maplibre/test_perf_governance_negative_paths.py
```

At the pinned snapshot, those tests cover three scalar failure cases: zero frame budget, negative memory budget, and a tile-error rate outside `[0, 1]`. They do not exercise the eight schema files, a browser, MapLibre, render diffs, evidence resolution, policy, attestation, proof construction, release, correction, or rollback.

### Wrapper checks

The eight named schema wrappers use the repository's common JSON Schema runner. Do not interpret successful wrapper execution as semantic validation until the schemas declare meaningful fields and reviewed fixtures demonstrate both acceptance and rejection.

[Back to top](#top)

---

## Current workflow boundary

[`maplibre-perf-governance.yml`](../../.github/workflows/maplibre-perf-governance.yml) is path-scoped to this directory and related MapLibre surfaces. A pull request that changes this README is expected to trigger it.

### Confirmed workflow posture

| Property | Current definition |
|---|---|
| Permissions | `contents: read` only |
| Checkout credentials | `persist-credentials: false` |
| Runner | GitHub-hosted Ubuntu |
| Runtime setup | Node 22 and Python 3.12 |
| Network/runtime stage | Not run by the current workflow after action bootstrap |
| Executed checks | JavaScript syntax, Python AST parsing, three deterministic negative-path functions, and readiness-state inspection |
| Schema treatment | Confirms all eight schemas still equal the reviewed placeholder object; fails when maturity changes without deliberate wiring |
| Validator treatment | Confirms eight wrappers and seven placeholder verifiers remain in the reviewed state |
| Outputs | Job conclusion, logs, annotations, and step summary only |
| Final gate | `WORKFLOW_HOLD` with browser, performance, render, trust, and publication stages explicitly skipped |

### Held conditions recorded by the workflow

- no accepted dependency lockfile;
- no executable MapLibre fixture payloads or local runtime style fixtures;
- live-CDN dependencies remain in the dormant smoke script;
- all eight schemas remain permissive placeholders;
- broader governance verifiers remain placeholders;
- the aggregate governance command remains unwired for accepted inputs;
- attestation remains unsigned;
- proof/release builders still target an unaccepted artifact posture; and
- browser, screenshot, receipt, proof, release, correction, rollback, failure-bundle, and artifact-upload stages remain disabled.

This workflow is a readiness drift detector and explicit safety hold. It is not a performance benchmark, schema coverage suite, proof pack, release gate, or publication decision.

### Workflow-trigger safety

The inspected pull-request workflow has read-only contents permission, disables persisted checkout credentials, declares no secrets, OIDC, deployment, signing, release, comment, or repository-write authority, and emits no uploaded artifacts. That bounded definition does not prove every repository workflow or future revision is equally safe.

[Back to top](#top)

---

## Migration and promotion gates

Migration is a governed compatibility change, not a file move. Complete these gates separately for each object unless an accepted family decision explicitly groups them.

- [ ] Assign accountable schema, contract, MapLibre, performance, validation, policy, evidence, release, and documentation reviewers.
- [ ] Inventory repository path consumers, generated references, command bindings, workflow references, and any proposed `$id` consumers.
- [ ] Define or identify the accepted semantic contract and object-family relationship.
- [ ] Decide whether the object extends a cross-cutting receipt, proof, release, correction, rollback, or validation family.
- [ ] Record canonical placement in an accepted ADR, migration decision, or authority register.
- [ ] Define stable filename, title, version, `$id`, dialect, reference, and compatibility rules.
- [ ] Replace the permissive placeholder with a bounded schema whose constraints match the contract.
- [ ] Add public-safe valid, invalid, boundary, stale, denied, abstained, and error fixtures as applicable.
- [ ] Bind wrappers and aggregate validators to deterministic inputs and finite outcomes.
- [ ] Add tests that prove expected acceptance and rejection without external network dependence.
- [ ] Separate temporary QA output from trust-bearing receipts, proofs, release objects, corrections, and rollback records.
- [ ] Verify policy, evidence, source role, rights, sensitivity, review, signing, provenance, release, correction, and rollback boundaries.
- [ ] Update workflow checks only after the new maturity state is reviewed; do not bypass the intentional readiness tripwire.
- [ ] Document old-path behavior, compatibility window, correction path, and rollback target.
- [ ] Migrate consumers without leaving divergent definitions.
- [ ] Retire or freeze the compatibility file only after parity, references, and release dependencies are cleared.

Until applicable gates pass, retain the files as compatibility placeholders and keep the workflow `HOLD` visible.

[Back to top](#top)

---

## Review burden

Any edit to a JSON Schema file in this lane is outside a README-only change and should receive review proportional to its object family and consumers.

At minimum, reviewers should verify:

- [ ] semantic contract and final responsibility family;
- [ ] Directory Rules and ADR basis;
- [ ] identity, versioning, `$id`, and compatibility behavior;
- [ ] field constraints, references, and failure behavior;
- [ ] valid, invalid, boundary, and negative fixtures;
- [ ] wrapper, aggregate validator, and test wiring;
- [ ] config-instance compatibility where relevant;
- [ ] evidence, source-role, policy, rights, sensitivity, review, and stale-state handling;
- [ ] receipt, proof, release, correction, withdrawal, and rollback separation;
- [ ] consumer and generated-reference migration;
- [ ] workflow-trigger and supply-chain impact;
- [ ] proof that no public path bypasses governed APIs or released artifacts; and
- [ ] transparent correction and rollback instructions.

[Back to top](#top)

---

## Definition of done

### This README revision

- [x] Preserves the existing purpose, status, boundary, inventory, placement, validation, and open-question anchors.
- [x] Identifies the lane as non-authoritative compatibility guidance.
- [x] Records all eight individually verified schemas and their exact placeholder shape.
- [x] Separates schema shape from contracts, policy, config, fixtures, validators, evidence, runtime, release, correction, and rollback.
- [x] Documents the current workflow's executed checks and explicit `WORKFLOW_HOLD`.
- [x] Prevents wrapper presence from being mistaken for meaningful schema enforcement.
- [x] Preserves unresolved migration, consumer, correction, and rollback work.

### Executable and migration maturity

- [ ] Owners and required reviewers are assigned.
- [ ] ADR-0001 and any object-family decisions are accepted, amended, superseded, or explicitly declined.
- [ ] Consumer and prospective `$id` references are inventoried.
- [ ] Semantic contracts and final schema families are accepted.
- [ ] Non-permissive schemas, fixtures, validators, and tests are wired.
- [ ] Hermetic browser/performance and render-diff evidence exists where required.
- [ ] Evidence, policy, rights, sensitivity, review, signing, provenance, release, correction, and rollback gates are proven.
- [ ] Compatibility mappings and rollback have been exercised.
- [ ] A reviewed workflow transition replaces the readiness hold.
- [ ] Current evidence supports redirecting, migrating, freezing, or retiring each compatibility path.

Completing this README does not complete any executable, migration, performance, evidence, policy, release, correction, rollback, or publication gate.

[Back to top](#top)

---

## Open questions

| Item | Status | Evidence or decision needed |
|---|---|---|
| Accountable owners for this lane | **NEEDS VERIFICATION** | Reviewed ownership and CODEOWNERS/steward assignment. |
| Complete current directory inventory | **NEEDS VERIFICATION beyond exact named reads** | Non-truncated tree listing or successful current readiness run. |
| ADR-0001 authority | **PROPOSED** | Required steward approvals or a superseding schema-home decision. |
| Versioned MapLibre schema family | **NOT PRESENT at checked README path** | Accepted family decision and created canonical index, if approved. |
| Contract for each of the eight objects | **UNKNOWN** | Accepted semantic definitions and object-family relationships. |
| Repository path and `$id` consumers | **UNKNOWN** | Code-aware and generated-reference inventory plus owner confirmation. |
| Fixture polarity for the eight schemas | **NOT ESTABLISHED** | Valid, invalid, boundary, and negative fixture families. |
| Meaningful schema enforcement | **NOT ESTABLISHED** | Non-permissive shapes plus deterministic rejection tests. |
| Current Actions conclusion | **UNKNOWN** | Workflow run tied to the resulting commit and job conclusion. |
| Browser performance and render-diff maturity | **HELD** | Lockfile, hermetic fixtures, accepted network posture, deterministic baselines, and measured runs. |
| Receipt, proof, release, correction, and rollback placement | **CONFLICTED / NEEDS VERIFICATION** | Cross-family contract review, Directory Rules decision, and accepted output roots. |
| Runtime or public use | **UNKNOWN** | Governed route, policy enforcement, evidence resolution, release record, and audit proof. |
| Migration and deprecation window | **NOT DEFINED** | Accepted mapping, parity criteria, downstream rollout, correction path, and rollback drill. |

[Back to top](#top)

---

## Evidence ledger

Repository evidence was reviewed against `bartytime4life/Kansas-Frontier-Matrix@459b41d7ec91240742d8b2d3e5d9eb4dbd248df7`. The movement from the initial inspection commit changed only `fixtures/invalid/README.md`; it did not intersect this README's path, cited MapLibre surfaces, Directory Rules, ADR-0001, or validation configuration.

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Prior `schemas/maplibre/README.md` blob `2dda90174ec219fd08edce155f8d151427e92ddb` | **CONFIRMED** | Existing compatibility purpose, boundaries, eight named schemas, and open placement questions. | Current completeness, consumer inventory, or implementation maturity. |
| Eight direct schema files, shared blob `511e7f34ca84390fd5d000326ab33c46c3050fc4` | **CONFIRMED permissive placeholders** | Exact three-key JSON shape and absence of meaningful constraints. | Accepted semantics, identity, fixtures, performance, or release readiness. |
| [`schemas/README.md`](../README.md) | **CONFIRMED root guidance** | Machine-shape responsibility and separation from contracts, policy, fixtures, validators, data, and release. | Acceptance or completeness of this compatibility lane. |
| [Current contribution-preflight Directory Rules](../../docs/architecture/directory-rules.md) and [doctrine-path companion](../../docs/doctrine/directory-rules.md) | **CONFIRMED files / CONFLICTED authority graph** | Responsibility-root placement, compatibility discipline, schema-home direction, and renderer-as-downstream boundary. | A resolved canonical document home or accepted destination for each performance object. |
| [ADR-0001](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | **CONFIRMED file / PROPOSED decision** | Proposed versioned schema-home rule and prohibition on divergent authority. | Accepted migration or final family mapping. |
| Checked `schemas/contracts/v1/maplibre/README.md` | **NOT FOUND** | No versioned MapLibre family README exists at that exact path in the pinned snapshot. | Absence of every MapLibre-related schema elsewhere. |
| [`configs/maplibre/README.md`](../../configs/maplibre/README.md) and `perf-envelope.v1.json` | **CONFIRMED configuration lane** | Separate config responsibility and one performance-envelope instance. | Schema conformance, accepted thresholds, or runtime use. |
| [`tools/validators/maplibre/README.md`](../../tools/validators/maplibre/README.md), wrappers, and placeholder verifiers | **CONFIRMED bounded implementation** | Validator routing, eight common-runner wrappers, and held broader verifier maturity. | Meaningful validation or successful current runs. |
| [`tests/maplibre/test_perf_governance_negative_paths.py`](../../tests/maplibre/test_perf_governance_negative_paths.py) | **CONFIRMED narrow test source / not run during API-only drafting** | Three invalid scalar cases. | Schema, browser, render, evidence, policy, or release coverage. |
| [`maplibre-perf-governance.yml`](../../.github/workflows/maplibre-perf-governance.yml) | **CONFIRMED workflow definition** | Read-only static checks, placeholder drift tripwires, and explicit `WORKFLOW_HOLD`. | A current passing run or release-grade performance governance. |
| [`docs/quality/maplibre-perf-governance.md`](../../docs/quality/maplibre-perf-governance.md) | **CONFIRMED design lineage / implementation-stale** | Intended object relationships and governance concerns. | Current workflow behavior or accepted object placement. |
| Attached MapLibre operating manual, Master MapLibre report, Directory Rules, and unified implementation manual | **CONFIRMED supplied lineage/doctrine inputs** | Renderer-downstream rule, EvidenceBundle priority, proof/release separation, policy gates, and correction/rollback expectations. | Current repository implementation beyond the pinned evidence above. |

[Back to top](#top)

---

## Correction and rollback

Correct this README when:

- a Directory Rules edition or ADR resolves the schema-home or MapLibre family question;
- any placeholder gains fields, `$id`, title, version, contract pointer, or KFM metadata;
- a consumer, fixture, validator, test, policy binding, runtime route, evidence link, release role, correction role, or rollback role is added or removed;
- the readiness workflow begins running browser, performance, render-diff, attestation, proof, release, correction, rollback, or artifact-upload stages;
- the workflow's permissions, secret access, runner, network, signing, or publication posture changes;
- a compatibility path is redirected, migrated, deprecated, frozen, or retired; or
- any current-state statement no longer matches the repository.

Before merge, rollback means closing or abandoning the unmerged review branch. After merge, create a transparent revert of the documentation commit and re-run applicable Markdown, link, schema-structure, and MapLibre readiness checks. Do not force-push shared history.

Reverting this README changes documentation only. It does not restore or alter schema behavior, contracts, policy, configuration, fixtures, validators, tests, workflows, runtime behavior, evidence, receipts, proofs, release state, corrections, rollback records, deployments, public interfaces, or KFM publication state.

[Back to top](#top)
