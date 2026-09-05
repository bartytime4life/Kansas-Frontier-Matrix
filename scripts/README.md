<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/scripts-readme
title: scripts/ — Thin Operational Wrappers and Graduation Boundary
type: README
version: v0.6
status: draft; repository-grounded; mixed-maturity; legacy-performance-harness-retired; no-publication-authority
owner: "@bartytime4life — root-registry review route; independent review remains NEEDS VERIFICATION"
created: NEEDS VERIFICATION — a root stub predates v0.2
updated: 2026-09-05
supersedes: v0.5 documentation at the same path; no executable or governance behavior
policy_label: repository-facing; no-secrets; no-direct-public-path; candidate-not-proof
owning_root: scripts/
root_class: canonical
allowed_artifact_kind: thin_script
validation_profile: thin_wrapper_only
responsibility: thin non-authoritative invocation wrappers and bounded operational guidance
truth_posture: cite-or-abstain; source inspection, bounded execution, approval, and release are separate
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 8b9c52d88687986879c8f87d7e3835f6a58bbacd
  scripts_tree: c65902bea4396cc4937de406793264bc786b70ea
  prior_blob: 053cec0d3732362636970a0e38fb48544868e292
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
related:
  - ./dev/README.md
  - ./maintenance/README.md
  - ./one_off/README.md
  - ../docs/doctrine/directory-rules.md
  - ../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../control_plane/root_registry.yaml
  - ../CONTRIBUTING.md
  - ../.github/PULL_REQUEST_TEMPLATE.md
  - ../package.json
  - ../Makefile
  - ../packages/maplibre/package.json
  - ../.github/workflows/maplibre-perf-governance.yml
  - ../.github/workflows/promotion-gate.yml
  - ../schemas/contracts/v1/receipts/generated_receipt.schema.json
notes:
  - "Retains the document identity, H1, H2/H3 navigation, custom anchors, and KFM-SCR verification IDs; consolidates repeated guidance."
  - "ROOT_FULL specifies required fields, not a mandatory order of twelve literal H2 headings."
  - "Seven root-level MapLibre files now comprise six candidate writers and one retired no-write hold shim."
  - "The package-owned MapLibre dependency is separate from the held legacy performance chain."
  - "Current source and declared commands are inspected; a complete checkout, native test suite, browser performance, and hosted exact-head checks are not established by this document."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `scripts/` — Thin Operational Wrappers and Graduation Boundary

`scripts/` exposes small command interfaces to governed implementation. It is
not the owner of reusable domain logic, policy, evidence, release decisions, or
public serving. **Read a command's actual effects before running it: this
mixed-maturity directory does not uniformly implement read-only defaults.**

**Navigate:** [Status](#status) · [Inventory](#confirmed-current-inventory) ·
[Validation](#validation) · [Planners](#governed-planning-wrappers) ·
[Legacy MapLibre chain](#root-level-maplibre-performance-chain) ·
[Rollback](#correction-and-rollback) · [Open verification](#open-verification-register)

> [!IMPORTANT]
> `maplibre-smoke-perf.mjs` is retired. It prints `WORKFLOW_HOLD`, exits `3`,
> and does not launch a browser or create performance artifacts. Do not bypass
> it to complete the old command chain. The package-owned renderer dependency
> is present; that is not performance, signing, proof, or release closure.

> [!WARNING]
> Several remaining builders write files on invocation without an `--apply`
> flag. Maintenance preflight also creates outputs by default. An internal
> label is not access control: never commit secrets, private prompts, hidden
> reasoning, restricted payloads, or harmful-precision locations here.

## Purpose

Keep invocation, input adaptation, and operator guidance thin while reusable
implementation and trust responsibilities remain in their owning roots.
[Directory Rules §10.1](../docs/doctrine/directory-rules.md) and
[the root registry](../control_plane/root_registry.yaml) establish this role.

A suitable wrapper has a named purpose, bounded inputs and effects, explicit
failure behavior, a maintenance route, and a reversible lifecycle. It does not
become the only implementation of a reusable or trust-bearing rule. A temporary
script must not become a permanent dependency merely because it is convenient.

```text
governed implementation -> thin invocation -> bounded result or candidate
                       -> review and validation in the owning responsibility
```

This is the root contract, not a claim that every existing file conforms.

## Authority level

**Canonical thin-script root; non-authoritative execution surface.**

Accepted [ADR-0029](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the exact Directory Rules v2 bytes. The document's retained draft label
does not undo that adoption. The registry projects the following boundary; it
neither creates authority nor authenticates approval.

| Field | Inspected projection |
|---|---|
| Artifact kind / validation profile | `thin_script` / `thin_wrapper_only` |
| Prohibited kinds | `policy_rule`, `release_decision`, `repository_tool` |
| Owner, permitted writers, reviewers | `@bartytime4life`, through registry defaults |
| Exposure / mutation / retention | Internal role; versioned; repository lifetime |
| Physical storage | Tracked wrapper source and documentation in Git; outputs belong to their declared stores |

| Responsibility | Owning root; permitted wrapper relationship |
|---|---|
| Reusable implementation | `packages/`; call the supported interface. |
| Repository-wide validators, generators, builders, inspectors, operators | `tools/`; do not duplicate their durable implementation. |
| Lifecycle orchestration | `pipelines/`; invocation is not source admission or promotion. |
| Source acquisition and admission | `connectors/`; no silent activation. |
| Meaning, shape, admissibility | `contracts/`, `schemas/`, `policy/`; consume, do not redefine. |
| Executable assertions and synthetic inputs | `tests/`, `fixtures/`; do not treat script success as equivalent proof. |
| Lifecycle data, receipt and proof instances | The appropriate `data/` family; no parallel output authority. |
| Release, correction, withdrawal, rollback decisions and signatures | `release/`; draft or invoke only within separately granted authority. |
| Application, runtime and exposure | `apps/`, `runtime/`, `infra/`; no arbitrary public script-execution endpoint. |
| Shared non-secret configuration | `configs/`; do not hide policy or credentials in configuration. |

### Anti-collapse rules

Command availability is not successful execution. A generated JSON object is
not automatically schema-valid; schema validity is not factual truth or
admissibility. A receipt records process memory, not proof, approval, or release.
CI, signatures, screenshots, maps, tiles, graphs, and AI language cannot replace
EvidenceRef-to-EvidenceBundle resolution and the applicable policy, review,
release, correction, and rollback checks.

Production implementations must not import scripts (`DIR-EXEC-007`). Public
clients consume governed APIs and released, public-safe carriers, not internal
stores or arbitrary repository commands.

## Status

<a id="status-and-evidence-boundary"></a>

### Repository-grounded maturity summary

**Evidence base:** `main@8b9c52d88687986879c8f87d7e3835f6a58bbacd`, inspected
2026-09-05. References below are source observations at this pin unless a
bounded execution is explicitly identified. They are not live deployment claims.

| Surface | Current bounded finding |
|---|---|
| Tracked inventory | 28 files: 10 at this root, 3 in `dev/`, 14 in `maintenance/`, 1 in `one_off/`; no nested `AGENTS.md` in the inspected scripts tree. |
| Two planner CLIs | Substantive package-backed, planning-only wrappers; not backfill or resilience executors. |
| Dev helpers | Two TODO shell scripts; no implemented bootstrap or fixture regeneration. |
| Maintenance | Mixed checker, helper, orchestrator, synchronization and placeholder files; effects require command-specific review. |
| One-off lane | README only in this tracked snapshot. |
| Legacy MapLibre files | Six candidate writers plus the retired `maplibre-smoke-perf.mjs` hold shim. |
| Renderer package | `packages/maplibre/package.json` declares `maplibre-gl` exactly `6.6.0` and package-owned adapter exports; the old dependency-free description is obsolete. |
| Legacy performance workflow | Source syntax, nine direct no-network test functions, readiness inspection, and explicit HOLD; no browser or artifact upload. |
| Promotion workflow | Test-mediated doctrine checking and bounded readiness checks, not promotion. The maintenance child README's direct-caller claim is stale. |
| Approval, full-suite results and production use | Not established by this documentation update. |

### Maturity classes

`PLACEHOLDER`, `THIN_WRAPPER`, `LOCAL_HELPER`, `TEMPORARY`,
`OPERATIONAL_HELPER`, `COMMAND_EXPOSED`, `CI_CHECKED`, `CI_RUNTIME_EXECUTED`,
`TRUST_ADJACENT`, and `GRADUATION_REQUIRED` remain useful separate descriptions.
A file may have several. Add **RETIRED_HOLD_SHIM** for the legacy smoke entrypoint;
its successful containment is not a successful performance run.

Do not infer `CI_RUNTIME_EXECUTED` from a workflow definition, or universal
`thin_wrapper_only` conformance from the registry's profile name.

## What belongs here

Thin CLIs over supported package/tool/pipeline interfaces; bounded local
maintenance wrappers; read-only inspection and planning helpers; and temporary
or compatibility scripts with a task, owner, expiry or migration decision.
Script-local guidance should identify arguments, dependencies, reads, writes,
deletes, network use, secret references, outcomes, validation and rollback.

Reuse, trust burden, scheduling, or production reliance triggers a graduation
review. A stable wrapper may remain after its underlying logic moves.

## What does NOT belong here

Do not establish reusable domain implementation, a permanent validator or
builder framework, production orchestration, source admission, contracts,
schemas, policy, registries, test fixtures, public API/UI code, or deployment
configuration as independent authority in `scripts/`. Route each to the root
listed under [Authority level](#authority-level).

Do not store raw or processed datasets, published carriers, authoritative
receipts/proofs/releases, credentials, private review material, restricted
locations, living-person private data, or unclassified generated output here.
Do not use `artifacts/` to create a competing trust-object home.

## Inputs

### Permitted input classes

Explicit CLI arguments, pinned repository metadata, tracked contracts and
schemas, public-safe fixtures, non-secret configuration, and outputs from a
previous bounded step are typical inputs. Local overrides, services, injected
secret references and remote endpoints require the command's own reviewed
contract; they are not automatically admitted by this README.

### Required input controls

For consequential work, inspect argument and field closure, file type/size/
encoding, symlink and traversal handling, dependency identity, network scope,
and sensitivity before execution. Unknown rights, source role, evidence or
release state must not be replaced with permissive defaults. Record material
freshness, variability and exact source versions.

These are requirements, not a directory-wide implementation certificate. For
example, the planners check whether the supplied input path itself is a symlink;
that is not proof of a general sandbox or complete parent-path traversal defense.

### Forbidden assumptions

Presence, a registry entry, an attractive filename, a zero exit, or a familiar
`ANSWER` label does not establish authority, safety, completeness, approval,
production readiness, or permission to print credentials and sensitive context.

## Outputs

| Output | Boundary |
|---|---|
| Terminal result or plan | Operator information; not execution permission. |
| Local scratch, cache, preview, QA result | Explicit temporary storage and cleanup; not released evidence. |
| Regenerated fixture or code/configuration change | Candidate diff; deterministic comparison, tests, review and rollback required. |
| Lifecycle candidate | WORK/QUARANTINE as applicable; never an implicit PUBLISHED transition. |
| Receipt, proof or release-shaped object | Owning family, contract, integrity, evidence and review checks remain necessary. |

Durable wrapper source is versioned in Git. Output retention is independent:
temporary data may be disposable, while incident evidence and accepted audit
records require their governing retention and correction process.

### Minimum effect declaration

A **PROPOSED documentation profile**, not a registered schema, is:

```yaml
command_id: example-planner
mode: plan
outcome: PLANNED
reads: []
writes: []
deletes: []
network_profile: none
secret_refs: []
generated_objects: []
validation: []
rollback: no mutation to reverse
maintenance_route: NEEDS VERIFICATION
```

For real commands, enumerate actual effect sets and object classes rather than
copying empty arrays. Record nondeterminism and partial effects explicitly.

## Validation

### Static inventory and syntax

Run from the root of a trusted checkout with the relevant interpreters available.
These checks inspect source; they do not execute the operational scripts.

```bash
# Tracked inventory, not ignored or downloaded operator files.
git ls-files -- scripts/

# One Bash process per file: extra filenames to bash -n are not extra scripts.
find scripts -type f -name '*.sh' -print0 |
  xargs -0 -r -n1 bash -n

find scripts -type f -name '*.mjs' -print0 |
  xargs -0 -r -n1 node --check

# Parse Python without importing modules or writing __pycache__ files.
python - <<'PY'
import ast
from pathlib import Path
for path in sorted(Path('scripts').rglob('*.py')):
    ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
    print(f'parsed: {path}')
PY
```

The `find` commands also see untracked regular files in the checkout. Review that
scope before use. Syntax success proves parseability only, not safe effects,
network isolation, fixture availability, determinism, or readiness.

### Focused planner checks

The existing dependency-closed tests and fixture invocations are:

```bash
python -m pytest -q \
  tests/packages/pipelines_core/test_backfill_window.py \
  tests/packages/pipelines_core/test_pipeline_resilience.py \
  tests/packages/pipelines_core/test_pipeline_resilience_cli_projection.py

python scripts/plan_backfill_window.py \
  fixtures/contracts/v1/runtime/backfill_window_plan/valid/rebuild.request.json

python scripts/plan_pipeline_resilience.py \
  fixtures/contracts/v1/runtime/pipeline_resilience_plan/valid/allow_start.request.json
```

Use the repository's declared dependency setup; do not silently install a second
unlocked environment. These are reproducible validation instructions, **not
claims that this README update ran the planner tests**. A returned plan does not
start a pipeline, retry a job, change a queue, activate a kill switch, or publish.

### Current MapLibre CI coverage

[The performance workflow](../.github/workflows/maplibre-perf-governance.yml)
syntax-checks seven scripts, parses Python validator/test files, and invokes
nine functions covering negative budgets, legacy retirement, package-owned
acquisition, and package exports. Readiness inspection recognizes the exact
package-owned 6.x dependency boundary while retaining the legacy performance
hold. It installs no workspace packages or browser and uploads no artifacts.

Its path filters include `scripts/*maplibre*`, **not `scripts/README.md`**. Do
not promise that editing this README triggers that lane. Report actual hosted
runs and their exact heads separately.

### Current local MapLibre command surfaces

The root [package manifest](../package.json) pins `pnpm@11.17.0` and declares
Node `>=22.13 <23`. Existing `npm run` aliases are command interfaces, not a
recommendation to replace pnpm installation or weaken build-script policy.

| Existing command | Current behavior and caution |
|---|---|
| `npm run maplibre:perf` | Invokes the retired shim; nonzero hold, not performance output. |
| `npm run maplibre:perf:full` | Uses `&&`; stops at that first failure under normal execution. |
| `make maplibre-perf` | Also starts with the retired shim; normal Make failure handling stops later recipes. |
| `npm run maplibre:render-diff`, `:attest`, `:manifest`, `:proof`, `:failure-bundle`, `:correction` | The `maplibre:` prefix applies to each suffix. These expose the six legacy candidate writers; do not execute them as a validation checklist. |
| `npm run maplibre:govern`, `npm run maplibre:proof:validate`, `make maplibre-govern` | Invoke legacy validators; assess each validator's actual scope and maturity. |
| `make maplibre-proof` | Writes a proof-shaped candidate, invokes its validator, rebuilds the manifest and rechecks governance; not a read-only check. |
| `npm run maplibre:clean`, `make maplibre-clean` | Recursively remove `artifacts/perf`; preserve required incident/audit material first. |
| Root `npm run lint`, `test`, `build` | Explicit `WORKFLOW_HOLD` failures, not implemented aggregate JS checks. |
| `make validate` | Aggregate schemas and schema/contract tests; not every script or every receipt. |
| Make `policy`, `fixtures`, `proof-slice`, `catalog` | TODO readiness markers; their zero exit is not validation. |

Do not use Make's error-ignoring modes or change `&&` sequencing to bypass the
retired harness. Current package-owned browser testing belongs to its own app/
package fixtures and gates, not a recreated CDN harness in this root.

### Child-lane checks

The static commands above cover child scripts. After source review, preflight
help is available through
`python scripts/maintenance/run_doctrine_artifact_preflight.py --help`.
The test wrapper `scripts/maintenance/run_doctrine_artifact_test_suite.sh`
exists but runs a larger suite and temporary-output workflow; inspect its
commands and prerequisites before invoking it. Do not run default maintenance
preflight merely to check documentation.

### Documentation and receipt checks

For a new receipt, first set `receipt` to its actual repository-relative path;
the following assignment is an illustrative placeholder and must be replaced.

```bash
receipt='data/receipts/generated/REPLACE_WITH_ACTUAL_RECEIPT.json'
python -m json.tool "$receipt" >/dev/null
python tools/validators/validate_generated_receipt.py "$receipt"
git diff --check
```

Receipt shape and supported artifact integrity checks do not authenticate a
reviewer or approve a change. Keep human review pending until a qualifying
review occurs; preserve historical receipt bytes and use the existing replay
mechanism for historical bindings rather than rewriting old hashes.

### Claim limits for this modernization

This revision rests on current connector reads of the complete prior README,
tracked scripts tree, selected source files, manifests, workflow definitions,
and adopted placement authority. The companion GeneratedReceipt records
performed local checks and explicit skips. Session QA using source exports is
not a complete checkout or hosted execution. No full native suite, browser
performance, signing, production run, or independent approval is asserted.

## Review burden

The root registry routes review to `@bartytime4life`. Named routing does not prove
independence, required-check enforcement, or completed approval. Escalate scope
or placement uncertainty through the existing contributor/ADR process, not an
invented stewardship identity.

README-only review checks claims, navigation, effect warnings, receipt and
rollback. Script changes additionally require the relevant package/tool owner;
write-capable or trust-adjacent changes need reviewers for each affected data,
schema, policy, evidence or release responsibility. Network, secret, destructive,
archive, shell-from-input and sensitive-domain changes require the corresponding
security/rights/sensitivity review. Scheduled or CI-required behavior needs an
operations and graduation review.

The generator, validator, reviewer, signer and publisher are distinct roles.
Current [contribution controls](../CONTRIBUTING.md) also govern delivery: an
incident-quarantined PR path stops at validated branch work until its eligible
creation boundary is established. This README does not clear that hold.

## Related folders

| Entry | Use |
|---|---|
| [Dev](./dev/README.md), [maintenance](./maintenance/README.md), [one-off](./one_off/README.md) | Child contracts; source wins over stale operational descriptions. |
| [Directory Rules](../docs/doctrine/directory-rules.md), [ADR-0029](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md), [root registry](../control_plane/root_registry.yaml) | Adopted placement and its non-authoritative machine projection. |
| [Backfill wrapper](./plan_backfill_window.py), [resilience wrapper](./plan_pipeline_resilience.py) | Package-backed planner interfaces. |
| [Renderer package manifest](../packages/maplibre/package.json) | Package-owned dependency and adapter-export boundary. |
| [Package commands](../package.json), [Makefile](../Makefile) | Inspect real recipes rather than relying on help text alone. |
| [Performance workflow](../.github/workflows/maplibre-perf-governance.yml), [promotion workflow](../.github/workflows/promotion-gate.yml) | Bounded checks; neither is release approval. |
| [Contribution guide](../CONTRIBUTING.md), [PR template](../.github/PULL_REQUEST_TEMPLATE.md), [receipt schema](../schemas/contracts/v1/receipts/generated_receipt.schema.json) | Exact-head, review, provenance, validation and delivery requirements. |

Related responsibility roots remain `tools/`, `pipelines/`, `packages/`,
`connectors/`, `tests/`, `fixtures/`, `configs/`, `data/receipts/`, `data/proofs/`
and `release/`; none is replaced by this index.

## ADRs

### Governing decisions

ADR-0029 adopts Directory Rules v2; §10.1 and `DIR-EXEC-007` govern wrappers and
graduation, §§11 and 15 separate accountability instances from temporary
artifacts, and §16 defines README field coverage and direct-child maps.
`ROOT_FULL` is **not** a required sequence of twelve literal H2 headings.

### Decisions still required

This update does not choose new builder homes, accept schemas, admit performance
fixtures, establish signing authority, settle maintenance output placement, or
create an independent review body. Any migration needs accepted authority where
required, caller/consumer analysis, compatibility, validation and rollback.
The old `artifacts/perf/` conflict remains unresolved here; do not treat its
continued presence as an accepted exception to Directory Rules.

## Last reviewed

| Field | Value |
|---|---|
| Evidence review | 2026-09-05; `main@8b9c52d88687986879c8f87d7e3835f6a58bbacd` |
| Prior README | v0.5, blob `053cec0d3732362636970a0e38fb48544868e292` |
| Tracked scripts tree | `c65902bea4396cc4937de406793264bc786b70ea` |
| Scope | This README and one new generated-work receipt; no script, child README, manifest, workflow, schema or policy edit |
| Evidence boundary | Source inspection and separately recorded bounded local QA; not deployment, performance or full-suite proof |
| Review state | Proposed documentation pending human review |
| Rollback | Restore the prior README through a focused non-force change; preserve receipt history |

Re-review on changed scripts, dependencies, callers, effects, command outcomes,
validation wiring, owners, accepted decisions, public exposure, retention,
correction, or migration. Historical pins remain history, not current-main claims.

## Confirmed current inventory

The direct-child map is verified against the pinned Git tree; deeper inventory
belongs to each child guide.

```text
scripts/
├── README.md
├── attest-maplibre-perf.mjs
├── build-maplibre-perf-correction-and-rollback.mjs
├── build-maplibre-perf-failure-bundle.mjs
├── build-maplibre-perf-proof-pack.mjs
├── build-maplibre-perf-release-manifest.mjs
├── build-maplibre-render-diff.mjs
├── dev/
├── maintenance/
├── maplibre-smoke-perf.mjs
├── one_off/
├── plan_backfill_window.py
└── plan_pipeline_resilience.py
```

### Direct-child classification

The two Python files are planner wrappers. `maplibre-smoke-perf.mjs` is a retired
hold shim; the other six `.mjs` files are candidate writers. `dev/` contains
placeholder helpers, `maintenance/` contains mixed-maturity operational code,
and `one_off/` contains documentation only at this snapshot.

### Bounded inventory limits

The 28-file count covers tracked blobs only. It does not inventory ignored,
untracked, downloaded, branch-only, generated, external operator or production
copies. Root and scripts-tree inspection found no applicable `AGENTS.md`; that
observation must be repeated when the base changes.

## Child-lane contracts

### `dev/` — local development helpers

`bootstrap.sh` prints a TODO for dependency/pre-commit setup;
`regen_fixtures.sh` prints TODO. Neither implements its advertised future action.
Use this lane for small local wrappers, not shared installers or generators by
accumulation. New behavior needs explicit effects, platform/dependency tests and
rollback; placeholder success is not a setup result.

### `maintenance/` — bounded repository maintenance

The lane has 14 tracked files, including its README. Checkers, registry helpers,
synchronizers, a preflight orchestrator, strict/test shell wrappers and the
published-alias audit placeholder have different effects and maturity.

**Current default-write warning:** `run_doctrine_artifact_preflight.py` creates
its output directory and invokes output-producing child commands without an
`--apply` flag. Its default is `receipts/doctrine_artifacts/`, not a newly
approved receipt root. An explicit scratch output directory confines those
outputs but does not create receipt authority. `--stable-filenames` selects
reusable output names; assess overwrite and retention before use.

Without selected strict flags, some ordinary child-check failures can coexist
with overall exit `0`. Inspect the summary and `--strict`, `--strict-provenance`
and `--require-consumer-readiness` behavior; do not equate process completion
with all prerequisites satisfied. This update does not execute that mutator.

The child README says `promotion-gate.yml` directly runs
`check_required_doctrine_artifacts.py`. Current workflow source instead invokes
the doctrine test module. **Direct-caller wording is stale; test-mediated
execution is not evidence that the checker is unused.** Child repair and output-
home/graduation decisions remain separate work.

### `one_off/` — temporary quarantine

This is a temporary-code lane, not the data QUARANTINE lifecycle. It is README-
only in the current tree. Any admitted helper needs task, maintainer, bounded
reads/writes/network, risk, dry run, rollback, expiry and delete-or-graduate
criteria. Do not make it the normal ingestion, evidence, promotion or public path.

## Governed planning wrappers

### Dependency-closed map

| Wrapper | Package module under `packages/pipelines-core/src/pipelines_core/` | Contract under `contracts/runtime/` | Request/result schema stems under `schemas/contracts/v1/runtime/` |
|---|---|---|---|
| `plan_backfill_window.py` | `backfill_window.py` | `backfill_window_plan.md` | `backfill_window_request`, `backfill_window_plan` |
| `plan_pipeline_resilience.py` | `pipeline_resilience.py` | `pipeline_resilience_plan.md` | `pipeline_resilience_request`, `pipeline_resilience_plan` |

The schema filenames end in `.schema.json`. Fixture families and focused tests
are named in [Validation](#focused-planner-checks). The wrapper source explicitly
binds these package and schema paths; downstream adoption breadth remains a
separate verification item.

### Shared input and effect boundary

Both accept one JSON path, reject a directly supplied symlink or non-file,
limit input to 4 MiB, reject duplicate keys and non-finite numbers, and validate
request and generated-plan shapes with Draft 2020-12 and format checking.
They emit compact JSON with findings and all authority flags false. Decision
logic is delegated to `packages/pipelines-core`; no executor is called.

The resilience wrapper validates the full plan before projecting
`operator-safe-v1` output. It omits authorization/environment-gate references,
sets `write_authority` false, and declares no workflow/database mutation.
Neither wrapper performs source activation, network acquisition, artifact
publication, policy evaluation or signing. The additional CLI-projection test
checks that restricted access metadata is absent from the emitted result.

### Finite planner results

| Result | Meaning |
|---|---|
| `ANSWER`, exit `0` | The wrapper's bounded validation/planning path succeeded. |
| `DENY` or `ERROR`, exit `1` | A handled input, schema or planning failure occurred. |
| CLI usage failure | Argument parsing can exit `2` before emitting an envelope. |

Missing dependencies or schema/runtime faults are not certified as uniformly
enveloped by this README. A backfill rebuild/no-op plan or resilience
start/retry/replay/pause/quarantine/deny recommendation is planning only, not
permission to execute that action or a public evidence-backed answer.

### Placement determination

The inspected package delegation supports the thin-wrapper role; it does not
certify every implementation concern. New unique trust logic, multiple consumers,
public dependency, network access, writes, scheduling or queue/database effects
requires fresh placement and validation review.

## Root-level MapLibre performance chain

### Local candidate-builder flow

The **current first step** is terminal:

```text
maplibre:perf or make maplibre-perf
  -> retired maplibre-smoke-perf.mjs
  -> WORKFLOW_HOLD; script exit 3; no browser and no output files
```

The historical downstream sequence remains visible in command manifests:
render comparison -> unsigned envelope -> candidate manifest -> governance
validator -> proof-shaped candidate -> proof validator. Make's proof target
also rebuilds the manifest and invokes governance again. These recipes do not
restore a producer of fresh screenshots, frame times or performance receipts.
Standalone writers may encounter stale or manually supplied files; availability
is not safe chain execution.

| File | Source-observed effect / limitation |
|---|---|
| `build-maplibre-render-diff.mjs` | Reads screenshots, baselines and config; writes PNG diffs/report. `reports.every(...)` has no nonempty guard, so an empty screenshot set can satisfy that expression; this is a code-derived limitation, not visual proof. |
| `attest-maplibre-perf.mjs` | Writes an envelope and checksum; `signatures: []` and `signing_status: "unsigned"`. Hashing is not signing. |
| `build-maplibre-perf-release-manifest.mjs` | Hashes listed inputs and writes candidate/rejected status based on receipt status; does not establish policy or approval. |
| `build-maplibre-perf-proof-pack.mjs` | Hashes referenced files and writes a proof-shaped object; `validation_outcome: "ANSWER"` is a literal, not an observed validator execution. |
| `build-maplibre-perf-correction-and-rollback.mjs` | May write two draft records for a non-candidate manifest; a printed `DENY` does not itself set a nonzero exit. It does not execute rollback. |
| `build-maplibre-perf-failure-bundle.mjs` | Hashes available listed files and writes a bundle; missing inputs are skipped. `captured` does not prove complete failure evidence. |

These are bounded source findings. None is fixed by this documentation change;
reviewed implementation and tests are needed before relying on the affected
objects. Do not bootstrap trust from their output labels.

### Current CI flow

```text
checkout -> Node 22 / Python 3.12 -> syntax checks
         -> nine direct negative/retirement/export tests
         -> current package and legacy-readiness inspection
         -> HOLD summary; no browser or artifact upload
```

### Why the hold exists

The old harness and its absent slim/heavy style inputs are not an admitted
performance system. Deterministic fixtures, baselines, thresholds, supported
schemas/validators, output homes, network reproducibility, signing and review
closure still need their own evidence.

This is **not** a claim that MapLibre itself is absent: the current package
manifest has the exact 6.6.0 dependency and adapter subpaths. Package browser
smoke, legacy performance, live-source admission and public release are separate
lanes. A green containment check proves only the tested boundary.

## Safe execution contract

The intended contract is inspect -> verify prerequisites -> plan effects ->
dry run -> explicitly authorized apply -> validate -> record finite outcome ->
retain or clean outputs. **This is not uniformly implemented in existing code.**

No-argument invocations should default to inspection where possible; writes
need explicit action and destructive effects need narrower confirmation.
Unknown inputs fail rather than broadening scope. No helper silently stages,
commits, pushes, approves, merges, releases or publishes. A directly requested,
separately authorized repository operation is not permission for hidden script
side effects.

Record exact read/write/delete/network sets, dependencies, secret-reference
handling, variability, partial results and recoverable prior state. Identical
inputs should yield deterministic results where practical; repeat applies need
an explicit no-op/update contract. Do not infer these guarantees from this prose.

## Generated-artifact and trust-object boundary

### Staging is not promotion

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed transition, not a copy, command, file move or layer
toggle. Candidates need identity, rights, sensitivity, validation, provenance,
integrity, evidence, policy, review, correction and rollback appropriate to the
transition. Outputs do not approve themselves.

### `artifacts/` compatibility rule

Directory Rules §15 limits the compatibility root to approved generated-output
roles and directs durable receipts/proofs/catalogs/releases to their canonical
families. Its listed child roles are build, docs, QA and temporary. Existing
`artifacts/perf/` references do not establish a new accepted child or a trust-
object exception. Keep legacy output unrelied-on and resolve placement through
reviewed migration, not a casual move into a canonical-looking directory.

### MapLibre candidate outputs

Legacy recipes refer to performance results, frame-time CSVs, screenshots,
render comparisons, receipt-shaped JSON, unsigned envelopes, manifests,
proof-shaped JSON, correction/rollback drafts and failure bundles. The retired
shim no longer produces fresh performance inputs. None of those names conveys
canonical status, validated evidence, approval or release authority.

### Candidate handoff record

A **PROPOSED handoff profile** records candidate class/path, intended owning
family, contract/schema/version, validator and fixtures, evidence, policy and
review references, digest/tool identity, current disposition, correction/
rollback, and retention. A handoff may say held, denied or superseded; it must
not convert missing support into invented references.

## Finite outcomes and failure semantics

### Generic script execution outcomes

The retained **PROPOSED generic vocabulary** is `NOOP`, `PLANNED`, `APPLIED`,
`PARTIAL`, `HELD`, `DENIED`, `ERROR`. It is not a shared implemented enum.
Planners use `ANSWER` / `DENY` / `ERROR`; the retired smoke uses stderr
`WORKFLOW_HOLD` and exit `3`; other legacy writers have their own behavior.
Numeric exits and emitted fields must be checked command by command.

### Mandatory failure behavior

Do not convert partial, held or denied work into silent success. Report the
actual exit, structured findings, and side effects; do not infer one from a
printed word. Placeholder or failed validators cannot support a trust claim.
Missing evidence, receipts, approvals and signatures stay missing. Failure
handlers may collect diagnostics or draft corrections, but cannot authorize
rollback or publication. Preserve incident evidence, redact protected context,
and distinguish retryable failure from deterministic invalid input.

## Graduation and promotion rules

| Trigger | Required direction |
|---|---|
| Shared implementation or multiple app/domain consumers | Package-owned reusable logic; retain only a justified wrapper. |
| Permanent validator, generator, builder, inspector, proof assembler | Reviewed `tools/` implementation with contracts and tests. |
| Repeatable lifecycle work | `pipelines/`; source-specific acquisition belongs to `connectors/`. |
| Public/runtime/deployment behavior | Owning app, package, runtime or infrastructure responsibility. |
| CI-required, scheduled, monitored or production reliance | Explicit owner, effect/outcome contract, operational tests and graduation decision. |
| Trust-object writing, schema/policy/registry mutation, secrets or destructive access | Owning-root and security review, canonical placement, validation and rollback. |
| Temporary task complete or expiry exceeded | Delete or graduate under a reviewed, reversible disposition; preserve required evidence. |

Record callers, destination authority, interface compatibility, tests, output
migration, retention, deprecation, rollback and deletion criteria before moving
files. Do not bulk-move a mixed directory or adopt an ADR by implementing it.

### Current determinations

The planners retain the inspected package-backed role. The retired shim remains
a compatibility stop, not a reason to reintroduce CDN acquisition. Six legacy
writers and maintenance code need command-specific classification; new homes
are **not selected here**. Dev placeholders do not establish operational
readiness, and one-off accumulation is not a permanent architecture.

## Correction and rollback

### Documentation rollback

Leave this branch unintegrated, or restore only `scripts/README.md` from prior
blob `053cec0d3732362636970a0e38fb48544868e292` in a focused non-force change.
Preserve existing GeneratedReceipts; record a new correction receipt rather than
rewriting their historical hashes or review states. Do not revert unrelated main
advances, renderer retirement, or dependency/security work.

### Script correction triggers

Hold or correct use when effects differ from guidance; a wrapper absorbs trust
logic; output homes or evidence are invalid; dependencies/network drift;
secrets or restricted material appear; failures are suppressed; owners or
rollback targets are absent; or expiry/public reliance exceeds reviewed scope.
Documentation correction alone does not repair code behavior.

### Operational rollback expectations

Stop further affected runs, preserve redacted evidence and exact partial state,
restore the last valid files/configuration/data through authorized tooling,
invalidate affected candidates/caches, retest, and notify known consumers.
Issue correction/withdrawal/rollback decisions through their owning roots when
required. Cleanup must not erase audit history or restore revoked access.

## Open verification register

IDs are retained from v0.5. A narrower completed observation does not close the
remaining operational or authority question.

| ID | Current disposition / evidence still required |
|---|---|
| KFM-SCR-01 | Tracked tree verified: 28 files. Ignored/generated/operator inventories remain unknown. |
| KFM-SCR-02 | Independent stewardship, required review and separation evidence remain needed. |
| KFM-SCR-03 | Selected package/Make/workflow callers inspected; exhaustive and external callers unproved. |
| KFM-SCR-04 | Legacy harness retired; any replacement needs separately governed fixtures and execution prerequisites. |
| KFM-SCR-05 | Actual performance metrics, deterministic render comparisons and retained run evidence not established. |
| KFM-SCR-06 | Meaningful legacy performance schemas, nonempty fixtures and negative cases need verification. |
| KFM-SCR-07 | Legacy validator substance, finite outcomes and enforcement breadth need verification. |
| KFM-SCR-08 | Six candidate-writer destinations and retirement-wrapper disposition require reviewed decisions. |
| KFM-SCR-09 | Canonical accountability/release handoff requires contract, integrity, evidence, review and rollback closure. |
| KFM-SCR-10 | Unsigned envelope confirmed; actual signer authority, verification and revocation remain unproved. |
| KFM-SCR-11 | No acquisition in retired shim; reproducibility/network controls for future performance execution remain open. |
| KFM-SCR-12 | Perf-output retention, tracking, cleanup and incident preservation require explicit policy. |
| KFM-SCR-13 | Maintenance command-by-command responsibility, callers, effects, tests and graduation remain open. |
| KFM-SCR-14 | Default maintenance output-path conflict confirmed; no new receipt home approved. |
| KFM-SCR-15 | Maintenance child direct-caller statement remains stale; source-grounded child correction is separate. |
| KFM-SCR-16 | Dev helpers remain placeholders; future setup needs platform/dependency/effect tests. |
| KFM-SCR-17 | One-off admission, expiry and cleanup enforcement not established. |
| KFM-SCR-18 | This document does not prove the deployed public-script boundary. |
| KFM-SCR-19 | Production use, operators, schedules, logs and operational reliability unverified. |
| KFM-SCR-20 | Graduation needs inbound-consumer closure and compatibility/deletion evidence. |
| KFM-SCR-21 | Current required-check/ruleset significance not audited in this scoped update. |
| KFM-SCR-22 | Hosted exact-head results and independent review must be reported separately, not inferred. |
| KFM-SCR-23 | Complete planner consumer/caller inventory remains open. |
| KFM-SCR-24 | Planner contract/schema adoption breadth remains separate from source presence. |
| KFM-SCR-25 | Future planner integration into execution or command orchestration needs an explicit decision. |
| KFM-SCR-26 | `thin_wrapper_only` declaration is not proof of universal semantic enforcement. |
| KFM-SCR-27 | New planner network/write/scheduling/public effects require reviewed graduation thresholds. |

## No-loss ledger

| Retained surface | v0.6 treatment |
|---|---|
| Document identity, H1, H2/H3 headings and custom anchors | Preserved; repeated prose and decorative badges consolidated. |
| Root contract, owner route, prohibited kinds and dependency direction | Preserved against adopted rules and current registry. |
| Input/output, sensitivity, authority and candidate boundaries | Preserved; requirements explicitly separated from implemented defaults. |
| Child lanes, planner dependency map, finite outcomes and graduation | Preserved and qualified where source does not prove universal behavior. |
| Legacy MapLibre command names and output families | Retained as compatibility evidence; live-harness claims corrected to retirement. |
| Validation | Per-file Bash syntax checking corrected; Python parsing avoids bytecode writes; unrun checks not presented as passing. |
| Review, correction, rollback and KFM-SCR-01..27 | Preserved; rollback now identifies the actual v0.5 baseline. |
| Older evidence and changelog | Retained as lineage through the exact prior blob and Git history, not relabeled current. |
| Executables, child documents, dependencies, schemas, policies and workflow behavior | Unchanged. |

## Evidence ledger

Repository references are relative for navigation; this table binds the material
observations to the immutable evidence base stated above. A selected-file review
is not a repository-wide audit.

| Source | Observation supported |
|---|---|
| Prior README, blob `053cec0d3732362636970a0e38fb48544868e292` | Full v0.5 baseline, preserved navigation and verification IDs. |
| Scripts tree `c65902bea4396cc4937de406793264bc786b70ea` | Exact tracked inventory, file modes and child boundaries. |
| Directory Rules `fd49a0b83e55cef52c1124281f093e263526898d`; ADR-0029 `a4de0d7a96b78da59cfc499d1025e1508afd8dd9` | Adopted responsibility roots, graduation and README field requirements. |
| Root registry `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` | `thin_script` projection, default owner/review route; no approval. |
| Planner wrapper blobs `6b3927af11756db011699cf093a9c85a264b39b0`, `0e4f0265ddc91a2b05958099d405cd78658e0c93` | Actual parsing, package delegation, schema paths, projections and outcomes. |
| Retired smoke blob `ac2522686546b7428ad0cc5c8cd76860ab285998` | No browser/acquisition/write logic; stderr hold and exit `3`. |
| Six adjacent `.mjs` source files | Candidate-writing effects, unsigned/literal/vacuous-output limitations. |
| Renderer manifest `f6d450af19c33011e159e123c8a07ca2bca6dfd3` | Exact 6.6.0 runtime dependency and package exports, not deployed runtime proof. |
| Root package `5cba790c88c40b885cc65fe2d585f3205aa1ef9d`; Makefile `304145dd0f674dda759f9097a747c4c7f0b9269d` | Command sequencing, explicit failures, TODO markers and destructive cleanup. |
| `maplibre-perf-governance.yml`, `promotion-gate.yml` | Current declared workflow/test scope and non-effects, not run results. |
| Maintenance preflight `649ff460db0dc2b3e23882d1828f6a4c842d4b6d`; child README `bd4ef697d7118074be44d00e6e77a8a311afe5f4` | Default writes/output conflict, selected strict gates, stale direct-caller wording. |
| `CONTRIBUTING.md` and PR template | Exact-head, proportional validation, review, receipt and eligible delivery boundaries. |

Google Drive's unversioned *Directory Rules* was consulted as placement lineage;
Notion's Repository Workbench as coordination. Neither supersedes adopted repo
authority or supplies missing runtime, review or delivery-control proof.

## Changelog

| Version | Date | Change / historical rollback |
|---|---|---|
| v0.2 | 2026-07-16 or earlier lineage | Root helper/graduation guide; prior bytes retained in Git history. |
| v0.3 | 2026-07-16 | Child lanes, legacy MapLibre chain and operational boundaries; rollback recorded in that edition. |
| v0.4 | 2026-07-23 | README profile and workflow reconciliation; prior rollback recorded in that edition. |
| v0.5 | 2026-08-09 | Adopted placement, two planner wrappers and pnpm-aware legacy hold; prior blob `8ab7b3f740f21822310fa8bf40a18527bf2057a1`. |
| v0.6 | 2026-09-05 | Current inventory, retired harness/package distinction, source-derived effect warnings and corrected validation examples; prior blob `053cec0d3732362636970a0e38fb48544868e292`. No executable change. |

[Back to top](#top)
