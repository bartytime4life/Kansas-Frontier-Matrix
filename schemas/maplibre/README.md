<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-maplibre-readme
title: schemas/maplibre/ — MapLibre Performance-Schema Compatibility and Readiness Boundary
type: README
version: v0.4
status: draft; repository-grounded; transitional-compatibility-lane; eight-permissive-placeholders; performance-workflow-held; migration-unresolved
owner: "NEEDS VERIFICATION — schema stewardship and independent review; CODEOWNERS routing is not approval"
created: 2026-07-05
updated: 2026-09-05
policy_label: public
owning_root: schemas/
current_path: schemas/maplibre/README.md
responsibility: "Index the eight retained performance-schema placeholders, explain their actual validation limits, and preserve reviewed versioned-family migration and renderer boundaries."
truth_posture: "CONFIRMED pinned source and bounded local checks; PROPOSED migration and future constraints; UNKNOWN complete consumers, operational performance, and release readiness"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 8b9c52d88687986879c8f87d7e3835f6a58bbacd
  prior_readme_blob: 9560ed016077964b56988d7fb4c02fe34e42fb28
  shared_placeholder_blob: 511e7f34ca84390fd5d000326ab33c46c3050fc4
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  performance_workflow_blob: 8e4c3b801fe6dbaac5e6645b054768859e84fa1e
  common_runner_blob: 88fd21279ebd71b3f65918ae13889846cec1d6ae
related:
  - ../README.md
  - ../contracts/v1/map/README.md
  - ../contracts/v1/layers/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - ../../packages/maplibre/package.json
  - ../../tools/validators/maplibre/validate_perf_envelope.py
  - ../../tools/validators/maplibre/validate_perf_governance.py
  - ../../tools/validators/_common/jsonschema_runner.py
  - ../../tests/maplibre/test_perf_governance_negative_paths.py
  - ../../.github/workflows/maplibre-perf-governance.yml
  - ../../CONTRIBUTING.md
  - ../../data/receipts/generated/README.md
tags: [kfm, schemas, maplibre, performance, compatibility, validation, migration]
notes:
  - "All eight schema files remain byte-identical object-only placeholders; this revision changes none of them."
  - "ADR-0006 and ADR-0007 are accepted architecture decisions. Package-owned renderer implementation is separate from the still-held performance-schema family."
  - "Workflow definitions, local source-subset execution, historical hosted runs, and current-head CI are separate evidence classes."
  - "This same-path documentation update creates no schema family, consumer binding, migration, approval, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `schemas/maplibre/` — MapLibre Performance-Schema Compatibility and Readiness Boundary

**This is the retained performance-schema compatibility lane, not the MapLibre
Style Specification or the renderer package.** Its eight schemas accept any JSON
object. They must not be used to certify performance, evidence, policy, or release.

**Source checkpoint:** `main@8b9c52d88687986879c8f87d7e3835f6a58bbacd`, reviewed
2026-09-05. **Document:** v0.4, pending review. **Schema maturity:** placeholders.

[Purpose](#purpose) · [Authority](#authority-and-inheritance) ·
[Inventory](#complete-placeholder-inventory) · [Validation](#validation-and-negative-checks) ·
[CI](#current-ci-and-readiness-boundary) · [Migration](#compatibility-migration-and-retirement) ·
[Open items](#open-verification-register) · [Rollback](#correction-and-rollback)

> [!IMPORTANT]
> The renderer package has advanced; these schemas have not. The current
> `@kfm/maplibre` manifest pins `maplibre-gl@6.6.0` and exports a concrete adapter
> and Vite adapter. That source evidence does not make these eight placeholders
> meaningful or establish a completed browser benchmark, live layer admission,
> deployment, or publication.

> [!CAUTION]
> Do not extend these unversioned placeholders or add new trust-bearing consumers.
> Use a reviewed versioned object family. Compatibility migration and performance
> graduation require their own scope; a README update does not authorize either.

## Purpose

Retain discoverable historical filenames while distinguishing machine shape from
meaning, evidence, policy, configuration, renderer behavior, and release state.
The lane records compatibility debt and the evidence needed to resolve it. It is
not a payload store, package API, benchmark runner, or retention decision.

The inherited responsibility split remains: `contracts/` owns meaning;
`schemas/` owns shape; `policy/` owns admissibility; `configs/` owns safe defaults;
`tools/`, tests, and fixtures establish bounded behavior; `data/` owns lifecycle
and accountability instances; `release/` owns release/correction decisions;
packages and applications implement downstream behavior.

## Authority and inheritance

### Governing authority

| Source | Verified status | Effect here |
|---|---|---|
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted | Adopts exact Directory Rules v2 bytes; establishes placement authority, not a migration of these files |
| [Directory Rules](../../docs/doctrine/directory-rules.md) | Adopted through ADR-0029 | `DIR-AUTHROOT-001` defaults machine schemas to `schemas/contracts/v1/<family>/` unless an accepted ADR establishes another versioned profile |
| [Schema-root README](../README.md) | Existing parent guidance | Classifies unversioned MapLibre schemas as compatibility debt; does not make them a parallel authority |
| [ADR-0001](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Proposed | More specific schema-home/migration proposal; not an adopted migration decision |
| [ADR-0006](../../docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md) and [ADR-0007](../../docs/adr/ADR-0007%20%E2%80%94%20MapLibre%20GL%20JS%20Is%20the%20Sole%20Browser-Side%20Renderer.md) | Accepted architecture | Package-owned renderer seam and sole normal browser renderer family; neither changes this schema inventory |

The doctrine's retained `PROPOSED_FOR_ADOPTION` header is part of the exact bytes
adopted by ADR-0029. The older architecture-path rules copy remains read-only
compatibility. Neither its age nor a source header reverses the accepted decision.

### Local authority statement

This README may explain, index, and identify unresolved work. It cannot accept an
ADR, assign a new canonical schema family, approve a consumer, manufacture a
PolicyDecision, authorize exposure, or execute migration/retirement. Review routing
is not stewardship assignment, independent approval, or required-check enforcement.

### Authority precedence

Preserve KFM trust and lifecycle invariants, then apply accepted decisions and
adopted Directory Rules, non-conflicting parent guidance, and current implementation
evidence within each source's scope. Drive and uploaded manuals supply lineage;
Notion supplies coordination. Neither substitutes for current repository evidence.

## Status and evidence

| Surface | CONFIRMED at the source checkpoint | Limit |
|---|---|---|
| Directory | One README and eight regular schema files; no child directories in the complete target listing | Tracked snapshot only |
| Schema bytes | All eight share blob `511e7f34ca84390fd5d000326ab33c46c3050fc4` | Object-type constraint only |
| Identity and constraints | No `$id`, properties, required keys, or family-specific constraints | No meaningful performance or release validation |
| Representative wrapper | `validate_perf_envelope.py` passes this schema and `fixtures_dir=None` to the shared runner | No configured fixture suite for that wrapper |
| Shared runner | Rejects duplicate JSON keys and non-finite parsed numbers; format checking is opt-in | Parser checks are not constraints supplied by these schemas |
| Governance placeholder | `validate_perf_governance.py` checks path existence only | `OK` is not JSON, metric, integrity, or policy validation |
| Scalar tests | Three tests exercise a separate Python fixture helper | They do not validate payloads against these eight schemas |
| Performance workflow | Defines static checks, nine directly invoked test functions, and explicit readiness HOLD | Source definition, not a current-head hosted result |
| Renderer package | Exact MapLibre dependency, concrete adapter source, and Vite worker wiring exist | Separate maturity axis; no performance-schema graduation |
| Consumers and migration | No complete accepted consumer/retirement packet established in this review | UNKNOWN; rename, deletion, and new reliance remain held |

### Truth labels used here

**CONFIRMED** means verified at the stated checkpoint or in a separately identified
execution. **PROPOSED** marks design and routing recommendations. **UNKNOWN** marks
insufficient evidence. **NEEDS VERIFICATION** marks a checkable open item.
`HOLD` is a work/transition outcome, not an extra truth label; inference is a
qualification, not an accepted decision.

## Current directory map

```text
schemas/maplibre/
├── README.md
├── perf-correction-notice.schema.json
├── perf-envelope.schema.json
├── perf-failure-bundle.schema.json
├── perf-proof-pack.schema.json
├── perf-receipt.schema.json
├── perf-release-manifest.schema.json
├── perf-rollback-plan.schema.json
└── render-diff-report.schema.json
```

This direct-child map follows `DIR-README-003`. No file is added to this lane by
this revision; the new authoring receipt belongs in the existing accountability
lane, not beside these schemas.

## Complete placeholder inventory

| Retained schema | Filename-implied concern, not accepted semantics |
|---|---|
| [perf-envelope.schema.json](./perf-envelope.schema.json) | Performance configuration or observation envelope |
| [perf-receipt.schema.json](./perf-receipt.schema.json) | Evaluation/execution receipt |
| [render-diff-report.schema.json](./render-diff-report.schema.json) | Render comparison report |
| [perf-proof-pack.schema.json](./perf-proof-pack.schema.json) | Proof/evidence aggregation |
| [perf-rollback-plan.schema.json](./perf-rollback-plan.schema.json) | Rollback planning |
| [perf-failure-bundle.schema.json](./perf-failure-bundle.schema.json) | Failure diagnostics |
| [perf-release-manifest.schema.json](./perf-release-manifest.schema.json) | Release manifest |
| [perf-correction-notice.schema.json](./perf-correction-notice.schema.json) | Correction or withdrawal notice |

**Every row:** accepts any JSON object; canonical destination remains
**NEEDS VERIFICATION**. A filename is not a contract or permission to bind a new
consumer to the placeholder.

## Verified placeholder shape

Every schema contains exactly:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true
}
```

### What this proves

The schema declares Draft 2020-12, permits empty and populated objects, and rejects
non-object JSON values. All eight copies are identical at the checkpoint.

### What this does not prove

It does not constrain identity, versions, units, time, environments, measurements,
baselines, tolerances, hashes, citations, rights, sensitivity, review, or release.
For example, an object containing a negative frame budget is schema-valid here.
The separate scalar helper can reject that budget; the placeholder cannot.
Malformed JSON rejection and duplicate/non-finite checks belong to the parser,
not to this schema's semantic coverage.

## Object-family and authority routing

### Adjacent versioned families

[Map](../contracts/v1/map/README.md) and [layers](../contracts/v1/layers/README.md)
are existing versioned-family indexes with mixed maturity. The map index describes
a machine-backed, proposed MapReleaseManifest fixture profile alongside other
scaffolds. These are navigation and overlap leads, not proof that all performance,
receipt, proof, correction, or rollback objects belong in either family.

### Required routing questions

Before replacement or migration, identify each object's semantic aggregate,
contract, versioned schema and stable identity, writer, readers, existing consumers,
mutability, policy/rights/sensitivity obligations, fixtures, validator, correction
model, retention, migration compatibility, and rollback. Configuration, observation,
receipt, proof, and release decision must remain distinguishable.

### Cross-family caution

**PROPOSED routing consideration:** choose ownership by responsibility, not the
`perf-` prefix or renderer name. Receipt/proof and release/correction families may
need different owners. Do not create `schemas/contracts/v1/maplibre/` merely
because a workflow watches that potential path; a watched path is not adopted
placement authority.

## Governed responsibility flow

```text
contracts + reviewed schemas + fixtures/tests + policy/review
  -> governed release and public-safe delivery
  -> MapLibre / Evidence Drawer / bounded AI interpretation

schemas/maplibre/ -> compatibility inventory and migration evidence only
```

This is a responsibility model, not a claim that the full flow is operational.
Keep `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED` and
`EvidenceRef -> EvidenceBundle` intact. Promotion is not a file move or layer toggle.

### Renderer boundary

The [package manifest](../../packages/maplibre/package.json) pins `maplibre-gl@6.6.0`.
The [concrete adapter](../../packages/maplibre/src/maplibre-adapter.ts) implements
the KFM port; the [Vite adapter](../../packages/maplibre/src/maplibre-vite-adapter.ts)
configures the package-owned worker. These are verified source facts, not a fresh
browser run. This corrects v0.3's dependency-free/placeholder package description.
Renderer, source/layer admission, performance, evidence, and release maturity are
separate. The renderer and AI remain downstream carriers, never approval authorities.

## Source, layer, style, and performance separation

| Concern | Distinction to preserve |
|---|---|
| Source | Identity, role, rights, freshness, and acquisition authority |
| Layer | Geographic/thematic meaning, coverage, scale, precision, and evidence |
| Style | Presentation and interaction; not a performance receipt or data source |
| Tile/artifact | Derived carrier with provenance/integrity and released-delivery obligations |
| Performance | Measured environment, method, samples, baselines, tolerances, and limitations |
| Render diff | Identified images/states and comparison method; not semantic equivalence by itself |
| Receipt/proof | What ran versus what supports a claim; neither approves itself |
| Release/correction | Authorized state change, invalidation, withdrawal, and reversal |

This directory does not vendor or validate the upstream MapLibre Style Specification.
A map that looks correct, a successful import, or a passing schema check cannot
substitute for any other concern in this table.

## What belongs here

The retained files, accurate compatibility documentation, and only separately
reviewed migration/deprecation mechanisms. Safe, reversible authoring may proceed
without pretending a later migration or release gate has passed. Do not establish
independent writable authority or new consumer reliance here.

## What does not belong here

No payload instances, fixtures, screenshots, logs, metrics, validators, policies,
contracts, configuration secrets, renderer code, receipt/proof instances, signatures,
release decisions, or published artifacts. Similar filenames do not make this an
instance store. Route implementation and accountability to their existing owners.

## Compatibility rules

Preserve single-write authority; forbid new trust-bearing bindings to these files;
use approved, time-bounded dual-read only when necessary; reject ambiguous legacy
coercion; establish identity before `$ref` redirects; avoid independently edited
schema copies; and prove consumer closure before retirement. Renaming or adding
metadata does not improve semantic maturity by itself.

## Consumer rules

### New consumers

Bind to a reviewed versioned contract/schema pair with defined unknown-field
behavior, valid/invalid fixtures, executable validation, policy and evidence
relationships, and an accountable review route. These placeholders are unsuitable
as acceptance or release gates.

### Existing consumers

The complete consumer set is **UNKNOWN**, not empty. Inspect dynamic path building,
imports, wrappers, scripts, workflow path filters/commands, fixtures, configuration,
docs, registries, builders, and external integrations before changing bytes or paths.
A text hit can be documentation rather than runtime consumption; a missing search
hit does not prove no consumer exists.

### Public and runtime clients

Public clients use governed APIs and released public-safe artifacts, never internal
lifecycle stores, direct model endpoints, or schema repositories as truth stores.
No parser/schema success permits exposure of a denied or unreleased payload.

## Inputs, outputs, writers, and consumers

This is a Git-managed schema/documentation lane, not an event processor. Its outputs
are the schema bytes and this index. Repository contributors are writers under the
current contribution contract; readers include the retained validation and readiness
surfaces. The complete reader graph and independent stewardship remain unverified.

### Non-effects contract

No schema or README result establishes factual truth, benchmark execution,
render parity, evidence closure, policy approval, rights/sensitivity clearance,
human review, signing, release, publication, correction, or operational rollback.
No external side effect is authorized by a local check.

## Security, privacy, exposure, and retention

Do not commit credentials, private endpoints, sensitive locations, living-person/DNA
material, restricted screenshots, or production traces. Future performance records
must consider device/environment fingerprints, location reconstruction, source rights,
retention, redaction, signer references, and public versus restricted projections.
For ambiguous rights or sensitivity, hold, redact, generalize, quarantine, or deny
through the owning process; do not encode an approval default in a schema.

## Validation and negative checks

### Documentation checks for this README

From repository root, after using the repository's declared Python environment:

```bash
git diff --check
python -m pytest -q tests/maplibre/test_perf_governance_negative_paths.py
```

The second command runs three existing scalar-helper tests, not a schema fixture
suite, complete MapLibre test suite, or browser benchmark. Also check metadata,
anchors, relative links, exact inventory, and receipt binding. Command definitions
are not execution receipts; report environment and actual results separately.

### Schema and wrapper checks

For an existing local candidate JSON file, the representative wrapper is:

```bash
python tools/validators/maplibre/validate_perf_envelope.py /path/to/candidate.json
```

The path is an operator-supplied example, not a tracked fixture. Run at repository
root: the wrapper's schema path is relative to the working directory. The shared
runner also builds its registry from `schemas/contracts/v1/`; it can fail on an
incomplete or invalid repository registry before checking this local schema.

| Invocation or layer | Source-defined behavior | What it does not establish |
|---|---|---|
| Wrapper with no arguments | Exit 2, `No files provided` | No validation occurred |
| Wrapper with object JSON | `OK` and exit 0 if parsing and registry setup succeed | No field-level metric, evidence, or release check |
| Wrapper with non-object JSON | Schema rejection, exit 1 after setup | No richer semantic rejection |
| Wrapper with malformed/duplicate-key/non-finite JSON | Shared parser rejects the input | Not a constraint contributed by the placeholder |
| Wrapper with `--fixtures` | After registry setup, exit 1: `FAIL fixture configuration: no fixture directory configured` | No configured valid/invalid suite; do not advertise a passing fixture command |
| `validate_perf_governance.py` with no arguments | Exit 2 | Root no-argument governance entrypoint is not usable proof |
| Same governance script with an existing path | Prints `OK`; checks existence only | Does not parse JSON or recompute metrics/hashes, and does not require a regular file |

The last script is a different implementation from the schema wrapper. Neither
should be confused with the three tests' scalar helper or a meaningful governance
verifier. A future schema needs a reviewed contract, identity/version rules,
constraints, valid/invalid and boundary/privacy/migration cases, deterministic
validators, consumer compatibility, and separate policy/release checks.

## Current CI and readiness boundary

### MapLibre performance-governance workflow

The [current workflow](../../.github/workflows/maplibre-perf-governance.yml) retains
name `MapLibre Perf Governance`, job ID `maplibre-perf-governance`, and job name
`MapLibre perf governance`. Its PR and push-to-main path filters include
`schemas/maplibre/**`; it also supports manual dispatch.

The inspected definition uses read-only contents permission, Node 22 and Python
3.12, checks seven JavaScript scripts and Python syntax, then directly invokes
nine Python test functions: three scalar negative cases, three legacy-harness
retirement/acquisition cases, and three package-export cases. It installs no
workspace packages or browsers. This is not `pytest tests/maplibre`.

Readiness inspection expects the eight permissive schemas, eight schema wrappers,
seven placeholder verifiers, and separately governed acquisition/source-metadata/
readiness surfaces. It checks exact package/lock compatibility and expects `HOLD`
with `RUNTIME_PROBES_PENDING`. The package is no longer expected to be dependency-free.

It does not run the retired browser performance harness, measure frame/memory
behavior, capture/diff screenshots, authenticate receipts/proofs, sign, upload
release artifacts, promote, publish, correct, or execute rollback. Passing the
static readiness guard preserves the hold; it does not graduate the held stages.
The inspection's own JSON parsing is not a Draft meta-schema validation run.

### Latest applicable hosted run

**No new latest-run or current-head hosted result is claimed by this edition.**
The previous v0.3 review cited main run `31654973078` and job `94307343990` as
success plus `WORKFLOW_HOLD`. That is historical evidence, not the result for this
README revision. Check the actual candidate head and tested merge ref separately.

### Adjacent workflows

The source-metadata, acquisition, package, Explorer, schema, and topology lanes
have different inputs and acceptance boundaries. v0.3's source-metadata run
`30958539690` and schema/validator runs `31758530911` / `31758530894` remain
historical references, not current-main health claims. Attribute a failure using
exact commands, environment, tested SHA, logs, and a comparable base execution;
do not call an unchanged-path failure proven inherited without that comparison.

## Safe change workflow

Pin main and target bytes; inspect instructions/authority and overlapping work;
make the smallest useful documentation change with its hash-bound authoring receipt;
validate the changed area; compare final remote bytes and scope; then use only an
eligible draft-PR path. Follow [CONTRIBUTING](../../CONTRIBUTING.md): an
incident-quarantined PR-state path stops at validated branch-only delivery until
the independent draft-creation boundary is proven. A new request, green check,
closed issue, or new branch name is not evidence that containment has ended.

Carry bounded unknowns with the draft/branch. Hold the particular unsafe transition,
not unrelated reversible authoring. Do not mark ready, self-approve, merge, change
settings, activate sources, deploy, or publish under a README-update request.

## Compatibility, migration, and retirement

### Required migration sequence

Inventory exact consumers and bytes; establish the semantic contract and versioned
owner; author constrained schemas and tests; prove intended consumers; introduce
approved compatibility where needed; obtain separate policy/release decisions;
then redirect/tombstone and retire only after closure. A branch-local proposal may
be written before acceptance, but must not be treated as adopted or activated.

### Promotion gates

Before reliance: accepted meaning and placement, stable identity/version strategy,
accountable review, constraints or justified extension points, positive/negative
fixtures, meaningful validators, security/rights/sensitivity/retention review,
consumer evidence, non-self-attesting accountability, and applicable release,
correction, and rollback support. Schema success alone satisfies none of the
non-shape gates.

### Retirement gates

Require an accepted migration decision, no unauthorized writers, migrated or
intentionally retired consumers, reference and external-compatibility closure,
appropriate redirects/expiry, documentation repair, and tested reversal. No file
is moved, redirected, or removed by this README revision.

## Review burden and escalation

README changes need source/claim, navigation, receipt, and no-loss review. Schema
identity/constraint changes additionally need contract and compatibility review;
receipt/proof changes need evidence/security review; release/correction objects
need release-duty separation; runtime/CI changes need their owning validation.
Escalate disputed ownership, public exposure, self-approval, legacy writer creation,
skipped-stage laundering, or a weakened fail-closed result. Do not invent reviewers.

## Definition of done

### This README revision

The document preserves identity, inventory, original section anchors, compatibility
warnings, migration gates, open-item IDs, and historical evidence boundaries;
corrects renderer/ADR/CI currentness; and makes parser, wrapper, placeholder, and
scalar-helper coverage distinct. Human review and integration remain separate.

### Executable and migration maturity

Still open: accepted per-object meaning/destination, real consumers, schema
constraints and fixtures, meaningful performance/proof/release verifiers, browser
measurement evidence, independent review, approved compatibility, and retirement.
Source presence and documentation completion do not close these gates.

## Open verification register

| ID | Open question / first dependent transition |
|---|---|
| MAPLIBRE-SCHEMA-001 | Accountable compatibility/family owners and independent review before authority claims |
| MAPLIBRE-SCHEMA-002 | Accepted semantic contract per object before semantic reliance |
| MAPLIBRE-SCHEMA-003 | Versioned destination and identity before migration |
| MAPLIBRE-SCHEMA-004 | Complete code/workflow/tool/doc/external consumer graph before rename/deletion |
| MAPLIBRE-SCHEMA-005 | Config/observation/receipt/proof/decision distinctions before trust-bearing use |
| MAPLIBRE-SCHEMA-006 | Measured environment, baseline, tolerance, and sampling before performance claims |
| MAPLIBRE-SCHEMA-007 | Capture/diff protocol and reviewed baselines before parity claims |
| MAPLIBRE-SCHEMA-008 | Rights, consent, sensitivity, privacy, and public projection before exposure |
| MAPLIBRE-SCHEMA-009 | Integrity and signer/reviewer separation before proof/receipt trust claims |
| MAPLIBRE-SCHEMA-010 | Operational release/correction/withdrawal/rollback closure before release |
| MAPLIBRE-SCHEMA-011 | Consumer closure, expiry, redirects, and reversal before retirement |
| MAPLIBRE-SCHEMA-012 | Exact candidate/base validation and eligible PR delivery before integration |

These are retained verification items, not a claim that no related implementation
exists elsewhere. Resolve them with current object-specific evidence, not a broad
renderer or workflow badge.

## Review checklist

- [ ] Re-pin base, head, prior blob, eight schema blobs, and overlap before integration.
- [ ] Verify claims, metadata, links, anchors, and exact two-file change scope.
- [ ] Keep source facts, local execution, historical runs, and current-head CI separate.
- [ ] Confirm no schema, validator, workflow, policy, dependency, or release behavior changed.
- [ ] Complete qualified review and verify actual GitHub lifecycle state through an eligible path.

## No-loss ledger

| Prior concern | v0.4 treatment |
|---|---|
| Stable identity, section anchors, inventory and object names | Retained |
| Placeholder bytes and semantic limits | Retained; parser, fixture-mode and path-existence distinctions added |
| Renderer/package maturity and ADR status | Superseded stale source claims with current accepted decisions and package evidence |
| Source/layer/style/performance and truth boundaries | Retained; upstream-style distinction made explicit |
| Compatibility, ownership, migration, review, retirement, correction | Retained without authorizing a transition |
| Workflow scope and historical runs | Updated source-defined checks; prior run IDs retained as history, not current results |
| Open verification register | All twelve IDs retained; holds narrowed to their dependent transitions |
| Repeated checklists and broad neighboring inventories | Condensed; adjacent family indexes remain linked instead of repeating stale counts |

The preceding v0.3 bytes remain in Git at the pinned prior blob; historical receipts
are not rewritten to bind the new document. This edition removes no executable
capability and adopts no new schema or renderer decision.

## Evidence ledger

All repository source references below use the checkpoint in metadata.

| Evidence | Observation / boundary |
|---|---|
| `schemas/maplibre/` complete listing and blob `511e7f34ca84390fd5d000326ab33c46c3050fc4` | Exact eight-schema inventory and shared bytes |
| Parent index and ADR-0029 / adopted doctrine | Existing compatibility classification and responsibility-root placement |
| ADR-0001 / ADR-0006 / ADR-0007 | Proposed schema-home decision versus accepted renderer architecture |
| `packages/maplibre/package.json` and adapter source | Declared dependency and implementation presence, not fresh browser execution |
| `tools/validators/_common/jsonschema_runner.py` and `local_resolver.py` | Parser, optional format checking, registry setup, fixture and exit behavior |
| `tools/validators/maplibre/validate_perf_envelope.py` | Representative wrapper with no configured fixture directory |
| `tools/validators/maplibre/validate_perf_governance.py` | Existence-only placeholder, not a semantic verifier |
| `tests/maplibre/perf_fixture_builder.py` and its three negative tests | Independent scalar helper, not enforcement by these schemas |
| Performance workflow blob `8e4c3b801fe6dbaac5e6645b054768859e84fa1e` | Current static/test/readiness definition with held browser/release stages |
| New GeneratedReceipt in the existing receipt lane | Actual authoring checks and limits; process memory, not approval |

Drive Directory Rules and the Notion Workbench were consulted as lineage and
coordination. No private source text, prompts, or hidden reasoning is copied into
this document or its receipt. No live public map, source, or model was exercised.

## Correction and rollback

For a mistaken claim, identify the affected statement and exact evidence, stop
reliance on it, and prepare a focused forward correction or reviewed non-force
revert. Preserve old receipts, logs, and Git history; add later correction evidence
rather than silently rewriting an earlier result. Recheck navigation, metadata,
byte binding, and any consumer that relied on the claim.

The pre-update README is blob `9560ed016077964b56988d7fb4c02fe34e42fb28` at the
source checkpoint. Reverting this documentation change does not alter schema
bytes, dependencies, validators, runtime, datasets, releases, or public artifacts.
Treat any future schema migration or operational rollback as a separate change.

---

**Last source review:** 2026-09-05 · **Version:** v0.4 ·
**Performance schemas:** eight placeholders; semantic reliance and migration held.

[Back to top](#top)
