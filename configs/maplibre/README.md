<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-maplibre-readme
title: configs/maplibre/ — MapLibre Configuration, Drift, and Consumer-Binding Boundary
type: readme
version: v0.5
status: draft; repository-grounded; bounded-config-lane; runtime-HOLD; performance-HOLD; non-release; non-publication
owners: OWNER_TBD — configuration and MapLibre specialist stewardship
review_route: "@bartytime4life; repository routing is not independent approval"
created: 2026-06-16
updated: 2026-09-04
policy_label: public-documentation; commit-safe; non-secret; non-authoritative
current_path: configs/maplibre/README.md
owning_root: configs/
root_class: canonical
readme_profile: BOUNDARY_COMPACT
responsibility: explain shared non-secret MapLibre configuration inputs, their actual readers, and their validation limits
truth_posture: CONFIRMED pinned inventory and inspected source; PROPOSED documentation revision and future contract; UNKNOWN operational readiness and general config loading
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: bb3eb695e6068b38453ca3ded8f1394a8fdebc20
  root_tree: b17f061592f3da0b1903c5252bc1d12437fe3575
  prior_readme_blob: 9b24a8d51013e06401cce7a02f06941feecf37e7
  payload_blob: 2833f99b5316df91e71c0f8913bb06d70917abcf
  package_manifest_blob: f6d450af19c33011e159e123c8a07ca2bca6dfd3
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  perf_workflow_blob: 8e4c3b801fe6dbaac5e6645b054768859e84fa1e
  method: pinned connector reads; exact-byte materialized subset for bounded offline checks; no full checkout
related:
  - ../README.md
  - ./perf-envelope.v1.json
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - "../../docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - ../../packages/maplibre/package.json
  - ../../schemas/maplibre/perf-envelope.schema.json
  - ../../tools/validators/maplibre/validate_perf_envelope.py
  - ../../.github/workflows/maplibre-perf-governance.yml
  - ../../tests/maplibre/test_perf_governance_negative_paths.py
  - ../../tests/maplibre/perf_fixture_builder.py
  - ../../data/receipts/generated/README.md
notes:
  - "v0.5 consolidates repeated guidance while retaining the document identity and legacy heading anchors."
  - "ADR-0006 and ADR-0007 are accepted architecture decisions, not proposed decisions or runtime-readiness proofs."
  - "The three fixture budget tests do not load or validate perf-envelope.v1.json."
  - "The workflow reads envelope identity and threshold-object shape, not the five numerical budgets."
  - "Literal ANSWER in a candidate builder is not evidence that its named validation command ran."
  - "No configuration payload, schema, dependency, workflow, renderer, source, release, or deployment is changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MapLibre Configuration, Drift, and Consumer-Binding Boundary

**This lane supplies shared, non-secret configuration inputs. It does not turn on a map.**

Start with [the tracked performance envelope](./perf-envelope.v1.json) to inspect
its declared thresholds, or the [consumer table](#consumer-binding-contract) to
see which code actually reads it. The lane inherits the
[`configs/` boundary](../README.md).

| Question | Evidence-bounded answer |
|---|---|
| What is tracked here? | This README and `perf-envelope.v1.json`; no child directories at the recorded snapshot. |
| Is MapLibre architecture accepted? | Yes: ADR-0006 owns the package seam; ADR-0007 selects the renderer family. |
| Is a renderer version declared? | `packages/maplibre/package.json` declares exact `maplibre-gl` `6.6.0`. That is repository dependency state, not a latest-version or readiness claim. |
| Are these thresholds fully enforced? | No. The schema accepts any JSON object; workflow shape checks and separate fixture tests do not establish numerical enforcement. |
| Does this configure a running Explorer? | No general application loader, override model, or deployed binding was established by this review. |
| Does a successful check permit release? | No. Runtime, performance, source admission, review, release, and publication remain separate gates. |

> [!IMPORTANT]
> **Configuration is an input, not permission.** A `public_safe` string, a layer
> toggle, a manifest path, a generated `ANSWER`, or a green static check cannot
> approve a source, plugin, sensitive geometry, release, or public endpoint.

> [!NOTE]
> All repository findings below are pinned to
> `bb3eb695e6068b38453ca3ded8f1394a8fdebc20`, inspected on 2026-09-04. They are not
> assertions about later `main`. See [evidence](#evidence-basis) and
> [validation](#validation) for source identities and execution limits.

**Navigate:** [Inventory](#current-repository-state) ·
[Readers](#consumer-binding-contract) · [Thresholds](#payload-and-consumer-path) ·
[Checks](#validation) · [Next slice](#smallest-safe-implementation-sequence) ·
[Rollback](#rollback)

## Purpose

Own small, reviewable, shared defaults or templates for a named MapLibre-related
consumer. Explain what is configurable, who reads it, what validates it, what
remains held, and how to reverse a change. This README is not a replacement map
architecture, API contract, style catalog, source registry, or release manual.

## Authority level

**Canonical configuration root; bounded local responsibility; no independent
renderer, evidence, policy, or publication authority.**

[Directory Rules](../../docs/doctrine/directory-rules.md), adopted by
[ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md),
place genuinely shared non-secret profiles in `configs/`. One application's
configuration normally stays with that application; executable admissibility
rules belong to policy, and deployment configuration belongs to infrastructure.
The adopted file's preserved internal draft label does not undo ADR-0029.

The parent README identifies `@bartytime4life` as the repository review route.
Configuration, map, security, and release specialist assignments and independent
approval remain **NEEDS VERIFICATION**. No owner or approval is created here.

## Current repository state

### Bounded snapshot

The pinned directory listing contains exactly:

```text
configs/maplibre/
├── README.md                 # configuration boundary and reader guidance
└── perf-envelope.v1.json      # existing threshold declaration; not a release
```

The payload is 487 bytes with Git blob
`2833f99b5316df91e71c0f8913bb06d70917abcf`. No additional config, style, layer,
probe-results file, or subdirectory is tracked **inside this lane** at the pin.
This does not inventory ignored files, external stores, other branches, or apps.

### Adjacent MapLibre surfaces

The [package manifest](../../packages/maplibre/package.json) declares
`@kfm/maplibre`, private version `0.0.0`, exact `maplibre-gl` `6.6.0`, and the
root, `./adapter`, and `./vite-adapter` exports. This review verifies those
**declarations**, not successful construction, browser rendering, or deployment.

The [performance workflow](../../.github/workflows/maplibre-perf-governance.yml)
expects readiness to remain `HOLD` with `RUNTIME_PROBES_PENDING`. That is a
source-defined guard, not this revision's full readiness execution. Previously
reported bounded browser results and the remaining twelve-probe matrix must be
re-read at their exact heads; do not infer either universal readiness or that no
browser test has ever run.

## Repository fit

| Responsibility | Owning root or inspected surface |
|---|---|
| Shared non-secret configuration | `configs/`; this existing sublane |
| App behavior and app-only configuration | `apps/`, with the relevant consumer |
| Reusable browser-renderer dependency seam | `packages/maplibre/`, under accepted ADR-0006 |
| Meaning / machine shape / admissibility | `contracts/` / `schemas/` / `policy/`, respectively |
| Pipeline run definitions / deployment | `pipeline_specs/` / `infra/`, respectively |
| Lifecycle, registries, receipts, proofs, released carriers | Their governed `data/` lanes |
| Release, correction, withdrawal, rollback decisions | `release/`, not this config lane |
| Synthetic inputs and verification | Existing responsibility-owning fixture, test, and validator lanes |

### Configuration is not a release artifact

A style, tile set, manifest, or scene intended for public delivery requires its
own governed artifact identity and release state. Calling it JSON configuration
does not relocate that authority into `configs/`. This lane may reference an
approved object; it cannot approve or duplicate the authoritative object.

## `config/` versus `configs/` path migration

### Current decision

Use the existing plural path `configs/maplibre/perf-envelope.v1.json` for the
inspected tooling. This revision does not repeat the historical singular-path
migration or create an alias.

### Current consumers and guards

The workflow and the three candidate builders listed below name the plural path.
The retired smoke harness does not read an envelope. Workflow filters for
`apps/web/**`, `packages/maplibre-runtime/**`, and
`schemas/contracts/v1/maplibre/**` are **drift guards**, not proof those paths are
active consumers or permission to create them.

### Safe posture

Do not add a second payload, silent singular-path fallback, or symlink merely to
satisfy a stale reference. A bounded source inspection is not a repository-wide
or external-consumer zero-reference proof.

### Migration decision requirements

A later migration must bind old/new paths and identities, readers/writers,
contract/schema versions, explicit compatibility and expiry, workflow coverage,
negative tests, review, and rollback. Follow the owning roots; do not create a
parallel config, schema, or runtime home through this README.

## What belongs here

The existing threshold declaration and its boundary documentation belong here.
Additional shared defaults, templates, examples, or conservative diagnostics
settings require a named consumer, safe values, a declared class/version,
validation, and a reversible review boundary. Camera, accessibility, cache, or
released-asset reference settings are **possible future inputs**, not an
inventory of implemented files.

## What does not belong here

Do not store secrets, signed URLs, operator-specific endpoints, sensitive
geometry, source payloads, tiles, screenshots, evidence objects, normative
policies, schemas, renderer code, runtime services, release decisions, or public
artifacts here. Keep process receipts and proofs in their separate owning lanes.
A template must remain unmistakably non-live; a filename cannot confer authority.

## Configuration classes

The following is explanatory vocabulary, **not an implemented enum or schema**:

| Class | Meaning and loading boundary |
|---|---|
| Default | Conservative input read by a verified consumer, with explicit fallback rules. |
| Template / example | Starting point or illustration; never implicitly auto-loaded. |
| Local / test / review | Explicitly selected non-production input; still secret-free. |
| Threshold | Declared limits for named verification tooling; validation is not release. |
| Compatibility alias | Time-bounded reviewed mapping; not a second writable authority. |
| Released reference / deployment template | Public-safe handles or placeholders only; no approval or live binding. |

### No hidden promotion

Changing an example into a default, enabling automatic loading, or binding a
local value to production is a behavior change. It needs the corresponding
consumer, security, policy, test, and rollback review; it is not cosmetic editing.

## Consumer-binding contract

### Minimum binding evidence

A reader is confirmed by code that opens the file, not proximity or a matching
name. The inspected set is deliberately bounded:

| Source | What it actually does | What it does not establish |
|---|---|---|
| [Performance workflow](../../.github/workflows/maplibre-perf-governance.yml) | Parses the envelope; checks `object_type == "PerfEnvelope"` and that `thresholds` is an object. | Does not validate all five keys, their types, units, ranges, or measured results. |
| [Render-diff builder](../../scripts/build-maplibre-render-diff.mjs) | Parses the envelope and reads `thresholds.render_pixel_delta_ratio` for screenshot comparison. | Not an active benchmark; does not consume the four time budgets. |
| [Proof-pack builder](../../scripts/build-maplibre-perf-proof-pack.mjs) | Hashes the envelope bytes and records their path/digest. | Hashing is not threshold validation; its literal `validation_outcome: "ANSWER"` does not execute the named command. |
| [Release-manifest builder](../../scripts/build-maplibre-perf-release-manifest.mjs) | Includes the envelope as an artifact and hashes its bytes. | Does not decide release or validate threshold semantics; output is candidate/rejected. |
| [Envelope validator](../../tools/validators/maplibre/validate_perf_envelope.py) | Delegates supplied inputs to the existing JSON Schema runner. | The referenced schema only constrains the top level to an object. |
| [Three budget-negative tests](../../tests/maplibre/test_perf_governance_negative_paths.py) | Exercise a separate [dataclass fixture](../../tests/maplibre/perf_fixture_builder.py). | Do **not** load `perf-envelope.v1.json` or test its five threshold fields. |
| [Retired smoke harness](../../scripts/maplibre-smoke-perf.mjs) | Prints a finite retirement/hold message and sets exit code `3`. | Does not load the config, launch a browser, measure performance, or emit evidence. |

### Proposed metadata fields

A future contract should bind a stable config ID/version/class to the exact
consumer interface, schema and semantic contract, environment, allowed override
sources, network policy, relevant release references, owner/reviewer, deprecation,
and rollback. No general metadata schema or effective-config object is introduced
by this documentation update.

### Binding by convention is forbidden

A path filter, README link, environment-variable name, source constant, receipt
hash, or unrelated green check is not proof of effective runtime loading. Claims
of supported loading additionally need parser/validation behavior, precedence,
negative tests, and the appropriate execution evidence.

## Precedence, overrides, and environments

### Required rules

No general loader or precedence implementation was established in this scope.
Before adding one, declare every input source and deterministic merge order;
shallow/deep/field-specific behavior; duplicate/unknown keys; null semantics;
immutable fields; substitutions; path resolution; version compatibility; and
rejection behavior. Do not prescribe an imagined current loading sequence.

### Fail-closed defaults

Missing or conflicting trust-significant values must not choose the most
permissive result. Endpoint access, plugin enablement, public visibility,
sensitivity, evidence, and release state remain governed outside config.

### Environment separation

Keep local, test, review, and deployment-template selection explicit. Actual
operator values and secrets stay outside Git. The same parseable file must not
silently become both a fixture and production configuration.

## Secrets, endpoints, and network posture

### Secret prohibition

No keys, passwords, cookies, tokens, signed/presigned URLs, private hostnames,
restricted identifiers, precise protected locations, or private filesystem paths.
Use obvious placeholders or references-by-name only; even a file called `local`
or `example` is subject to the repository's disclosure boundary.

### Endpoint rules

A future endpoint binding needs a known owner, purpose, access class, allowed
hosts/redirects, transport requirements, request/response limits, timeout/retry
rules, attribution, and authorization. Merely recording a URL does not permit a
fetch or transmission of location, identity, or evidence context.

### Current performance-script network finding

The retired harness executes no browser or network acquisition. The workflow is
no-network **after GitHub Action bootstrap**, not proof that bootstrap or all
future browser work is offline. Future asset fetching requires separately
reviewed dependencies, fixtures, network constraints, and rights.

### Logging and telemetry

Log stable IDs, versions, digests, finite reason codes, and redacted diagnostics.
Do not log substituted secrets, private endpoints, feature payloads, sensitive
coordinates, EvidenceBundle contents, living-person/DNA information, or restricted
infrastructure detail.

## Map trust, release, and sensitive-geometry boundaries

Preserve `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`.
Promotion is a governed transition, never a config merge or layer toggle.

### Released-artifact references only

Ordinary public clients use governed APIs and released, public-safe carriers;
they do not read raw, candidate, internal, canonical, or direct model stores.
Where consequential, references must resolve identity/digest, source role,
space/time scope, EvidenceRef -> EvidenceBundle, rights, policy, review, release,
correction, withdrawal, and rollback. Configuration cannot invent those records.

### Sensitive geometry

Generalization, aggregation, omission, delay, or denial occurs upstream under
policy and review. Client-side opacity or style filtering is not geoprivacy:
underlying geometry must not be delivered merely because it is hidden visually.
Unclear rights, sovereignty, archaeology, rare species, infrastructure, private
land, or living-person/DNA scope requires restrictive handling, not guessed defaults.

### Negative states must remain visible

Keep invalid config, denial, unavailability, stale/degraded state, evidence
abstention, correction, withdrawal, and rollback mismatch visible. Use each
consumer's actual finite vocabulary; this prose does not introduce a new enum.
Maps, tiles, graphs, scenes, summaries, and AI remain carriers, not root truth.

## Styles, layers, tiles, sprites, and glyphs

### Style configuration

Preferences may reference approved styles, attribution, legends, or color/motion
settings. They must not duplicate released style authority or hide trust status.

### Layer configuration

Visibility is a preference after admission and release, not permission. Preserve
stable feature/layer identities, time and scale scope, source roles, evidence,
rights, sensitivity transforms, correction, and rollback.

### Tile and raster references

PMTiles, COG, MVT/MLT, raster, terrain, and other source references remain proposed
capabilities here. A consumer must validate the actual format, bounds, zoom,
manifest/digest, policy, attribution, and released state before binding them.

### Sprites and glyphs

External asset locations require integrity, supply-chain, rights, availability,
and request-disclosure review. Do not copy mutable demo URLs into shared defaults.

### Camera and viewport defaults

Any future center, bounds, zoom, pitch, bearing, projection, or animation setting
must be finite, bounded, public-safe, and accessibility-aware. Do not expose a
protected location or remove a non-map fallback through a camera preference.

## Plugins, protocols, and renderer capabilities

A plugin/protocol preference is not dependency admission. Enabling PMTiles, COG,
terrain/globe, 3D Tiles, glTF, point clouds, deck.gl, or custom rendering needs its
own exact dependency/rights/integrity, resource, compatibility, fallback, and
rollback evidence. This README enables none of them.

### Renderer-boundary compatibility

[ADR-0006](../../docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md)
is **accepted**: `packages/maplibre/` owns the reusable acquisition seam and
consumers use the KFM-shaped `MapRuntimePort` / `MapLibreAdapter` boundary.
[ADR-0007](<../../docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>)
is **accepted**: MapLibre GL JS is the sole normal production browser renderer
family; subordinate integrations and any peer-renderer exception remain governed.

These decisions accepted architecture, not a specific version or operational
readiness. Their historical dependency-free acceptance snapshots must not be
mistaken for current package inventory: the inspected manifest now declares
`6.6.0`. Conversely, that declaration does not prove that later admission,
browser, release, or deployment obligations are closed.

## MapLibre performance configuration drift

### Payload and consumer path

The tracked envelope declares exactly these five values; this update changes none:

| Threshold key | Value | Current interpretation limit |
|---|---:|---|
| `avg_frame_ms` | 22 | Millisecond-labelled declaration; measurement methodology and enforced consumer are not established here. |
| `p95_frame_ms` | 40 | Same limit; do not substitute the separate fixture's `frame_budget_ms`. |
| `idle_ms` | 3000 | Named time budget; not a measured stable-idle result. |
| `load_ms` | 4000 | Named time budget; not a measured page/tile load result. |
| `render_pixel_delta_ratio` | 0.01 | Read by the candidate render-diff builder as the allowed changed-pixel fraction. |

The render-diff script's separate `pixelmatch` option `threshold: 0.1` is not the
same parameter as the envelope's `0.01` ratio. A comparison pass also does not
prove expected-scenario coverage: the current builder evaluates the screenshots
it discovers, and an empty report list satisfies its `every(...)` expression.
Require nonempty expected-scenario coverage before interpreting a future result.

### Current command-bearing workflow

The workflow performs syntax checks, nine directly invoked negative/retirement/
export tests, dependency-state checks, limited envelope shape inspection, and
readiness/placeholder guards. It deliberately leaves browser, performance,
render-diff, attestation, proof, release, correction, and rollback execution held.

It also expects the eight performance schemas to retain their placeholder shape.
Therefore strengthening an envelope schema requires a dependency-closed review of
the schema, consumers, fixtures/tests, and workflow assumptions; editing the
schema alone is not a complete implementation slice.

### Current holds

The permissive schema, numerical enforcement, benchmark methodology, deterministic
baselines, expected-scenario coverage, output placement, and release-grade
verification remain unresolved. The candidate builders name outputs beneath
`artifacts/perf/`; those **source-coded destinations** are not proof that files
exist, and their trust-shaped content is not canonical receipt/proof/release state.

### Current safe conclusion

`policy_posture: "public_safe"` and the envelope's publication-blocking note are
claims in configuration, not authenticated policy or preventive enforcement.
The proof builder's literal `ANSWER` is another declaration, not a validator run.
Do not run these builders to manufacture closure or weaken a gate to make it green.

## Formats, naming, and versioning

### Supported format posture

JSON is the only machine payload format in the inspected lane. YAML/TOML defaults,
viewer configs, or environment templates remain future choices for real consumers;
no format is admitted simply because it is mentioned here.

### Proposed naming pattern

Names should communicate consumer, purpose, class, and version. This is guidance,
not a newly accepted filename grammar. Preserve the existing plural path until a
reviewed migration changes it.

### Versioning

Keep file/schema version, semantic configuration version, consumer compatibility,
renderer dependency version, and release version distinct. A `v1` filename does
not establish compatibility or permit a silent change of meaning.

### Deterministic identity

Where replay matters, bind the final effective config and references to a digest.
Identity enables inspection and rollback; it does not authenticate truth, rights,
policy, review, or release. The generation receipt for this README is process
provenance, not an effective runtime-config receipt.

## Validation

### Current evidence result

Source reads establish the inventory and consumer table. Bounded local execution
uses an exact-byte materialized subset, **not a complete Git checkout**. The
small-source Git blobs are checked before execution. Full repository checks and
browser/runtime tests are not implied by that subset.

Read-only inspection from an actual checkout, with Git available:

```bash
REF=bb3eb695e6068b38453ca3ded8f1394a8fdebc20

git rev-parse --verify "${REF}^{commit}"
git ls-tree --long "$REF" -- configs/maplibre/
git show "${REF}:configs/maplibre/perf-envelope.v1.json"
git show "${REF}:schemas/maplibre/perf-envelope.schema.json"
```

These commands inspect the pinned commit; they do not launch an application or
prove loading. They were syntax-checked, not executed against a full checkout in
this revision. A missing commit or Git error is not an empty inventory.

### Validation matrix

| Check | Evidence / interpretation |
|---|---|
| Exact target directory listing | Confirms two tracked files at the pin, not ignored/external content. |
| JSON parsing and schema evaluation on materialized payload | Confirms the existing object passes the **open** schema; not numerical validity. |
| Schema gap probes | `{}` and an object with invalid threshold types still pass; a non-object fails. This demonstrates an inherited validation gap, not its repair. |
| Three existing fixture-budget negative tests | Validate their separate dataclass fields; not the tracked envelope. |
| Retired harness invocation | Expected exit `3` / `WORKFLOW_HOLD`; not a performance pass. |
| README and generated receipt | Check metadata, links, anchors, fenced examples, exact artifact hash, schema, and pending review. |
| Full workflow, native aggregate validators, topology, browser, release | Not run for this source-subset revision; no success claimed. |

Record exact executed commands and outcomes in the review handoff and generation
receipt. Do not rename `NOT_RUN`, skipped work, or an expected hold as readiness.

### Effective-config receipt

A future consumer may record config/version/hash, resolved sources and precedence,
consumer/schema versions, redacted reasons, outcome, and rollback linkage. Define
its family and owning receipt lane before emission; do not put a trust object
beside the config or pretend this proposed record already exists.

## Required negative cases

The following are **future acceptance requirements**, not a claim that tests exist:

| Failure family | Required behavior |
|---|---|
| Missing, malformed, duplicate-key, unknown-field, or wrong-version config | Deterministic rejection or explicitly permitted conservative fallback. |
| Wrong type, non-finite number, negative/zero/out-of-range budget | Field-specific finite rejection under the actual contract. |
| Conflicting sources, nulls, substitutions, or unsafe path resolution | Explicit precedence or error; no permissive guessing. |
| Unapproved endpoint/redirect, secret, sensitive log, or unadmitted plugin | Deny and provide redacted diagnostics. |
| Internal-store reference, unreleased/withdrawn asset, missing/mismatched digest | Do not bind the public source; retain a visible reason. |
| Sensitive geometry hidden only by style, absent attribution, inaccessible fallback | Block the unsafe exposure; repair upstream or in the owning consumer. |
| No scenarios, missing baseline, incompatible image dimensions, stale result | Fail coverage/integrity rather than infer performance success. |

Keep these tests distinct from the three already implemented fixture-budget tests.
The latter are useful but are not substitutes for the table above.

## Tests, workflows, and CI

### Current state

The inspected workflow triggers for path-scoped pull requests, qualifying pushes
**to `main`**, and explicit dispatch. `configs/maplibre/**` is included. A task
branch push alone is not proof this workflow ran. The job has read-only contents
permission and no declared deployment, signing, OIDC, or artifact-upload step.

### Required test layers

An eventual config consumer needs parser/schema, loading/precedence, negative
security/network, version/migration, and trust-boundary checks. Performance,
accessibility, visual, and long-session claims additionally need their own actual
fixtures, environments, commands, and results. This update installs nothing.

### CI claims

Distinguish a source-defined check, a local subset result, an exact-head hosted
result, and a synthetic merge result. Check name and successful execution do not
prove server-side required-check enforcement or human approval. The performance
workflow explicitly reports `WORKFLOW_HOLD` and `WORKFLOW_SKIPPED_EXPLICIT` for
its unexecuted stages; successful preservation of that hold is not readiness.

## Review burden

| Change | Appropriate review |
|---|---|
| This documentation/provenance update | Configuration and documentation review; verify evidence and limits. |
| Payload or effective loading | Consumer, configuration, contract/schema, and test review. |
| Endpoint, telemetry, plugin, or dependency | Security/supply-chain and affected consumer review. |
| Public style/layer or sensitive data | Map, domain/sensitivity, policy, and release review. |
| Thresholds, benchmark, output family, migration | Performance/validation and the affected responsibility-root owners. |

### Separation of duties

Repository routing is not an approval. Keep generation, validation, review,
ready/merge decisions, source admission, release, and publication separate.
Apply current contributor and PR-delivery controls before creating a review
surface; documentation cannot clear an active delivery incident.

## Safe change pattern

Pin the target and authority; verify the named reader and overlapping work;
classify the change; keep secrets and live effects out; update only direct
dependencies; validate positive/negative paths; record actual failures and limits;
then preserve a reviewable branch and explicit rollback. Re-pin before remote
mutation. A proposed README or passing test does not authorize later transitions.

## Smallest safe implementation sequence

### Phase 0 — reconcile authority and paths

**Do not repeat resolved decisions.** Retain the plural payload and accepted
`packages/maplibre/` boundary. Recheck current readers, workflow guards, and
owners. No new runtime package or second config home is needed.

### Phase 1 — accept a config contract

**PROPOSED next slice:** define the existing five threshold fields' meaning,
units, bounds, finite-number rules, missing/unknown-key behavior, and version
compatibility for a named no-network consumer. Determine the schema's accepted
placement without creating a parallel schema authority.

### Phase 2 — implement one bounded consumer

Add substantive envelope validation and tests using the actual JSON shape. Keep
it no-network and non-publishing. Prove missing/wrong/extra fields and numerical
bounds; do not claim the dataclass fixture covers those requirements.

### Phase 3 — migrate workflow paths

The inspected readers already use `configs/`; no path migration is requested.
In the future contract slice, reconcile the workflow's placeholder-schema and
validator-inventory assumptions with the new validator and negative fixtures.
Keep unrelated guards and named jobs unchanged unless the reviewed scope requires
otherwise. Schema tightening must not be made to pass by suppressing its checks.

### Phase 4 — make performance runs hermetic or explicitly admitted

Only after the contract/consumer slice: define deterministic expected scenarios,
baselines, metrics, browser/toolchain, asset/network constraints, and independently
reviewable results. Restore neither the retired CDN/global loader nor live source
acquisition through configuration.

### Phase 5 — integrate trust and release gates

Resolve candidate output-family placement, actual validator execution, identity
and coverage, policy/review, correction, and rollback before using performance
results for any release decision. This sequence proposes work; it activates none.

## Definition of done

### Ownership and placement

The existing lane and parent responsibility are verified. Specialist ownership
and independent review remain open; no new authority or config path is created.

### Inventory

The pinned two-file inventory is known. General loaders, external storage, and
runtime consumers are not inferred from it.

### Contracts and schemas

A documentation correction is complete only when it accurately states that the
current schema is permissive. A production config contract remains separate work.

### Consumer binding

Named readers and byte-hash references are distinguished; complete effective
loading and override behavior remain unproved.

### Security

No new endpoint, credential, sensitive geometry, or real source data is added.
The upstream sensitivity and deny-by-default network requirements are retained.

### Trust and release

Configuration, evidence, policy, review, and release remain distinct. No generated
record or successful check is promoted into authority by this text.

### Tests and CI

The review packet records executed checks and their limits. Pending hosted or
full-repository validation is not marked passed.

### Documentation and operations

The README preserves its document ID, original heading anchors, canonical pointer,
and rollback lineage. This does not graduate the lane to runtime, performance,
release, or publication readiness.

## Evidence basis

All repository paths in this table were read at the snapshot above. The original
README was read in full through bounded line ranges before consolidation.

| Evidence | Exact Git blob | What it supports |
|---|---|---|
| Prior README | `9b24a8d51013e06401cce7a02f06941feecf37e7` | v0.4 baseline and retained navigation. |
| Parent `configs/README.md` | `a800983eac7582a84e9dd82bc7d4baf04f552ad8` | Shared non-secret configuration responsibility. |
| Directory Rules | `fd49a0b83e55cef52c1124281f093e263526898d` | Adopted placement law; configuration ownership and compact boundary profile. |
| ADR-0029 | `a4de0d7a96b78da59cfc499d1025e1508afd8dd9` | Accepted adoption of the exact Directory Rules bytes. |
| ADR-0006 / ADR-0007 | `4bf4292dc05a85fd4cd829c491808b13894bc223` / `2482eea382fd97e68544bb04bc2e2ea1e1cedebe` | Accepted package seam / renderer-family decisions, not current execution proof. |
| Package manifest | `f6d450af19c33011e159e123c8a07ca2bca6dfd3` | Exact dependency and export declarations; repairs the prior truncated blob reference. |
| Envelope / schema | `2833f99b5316df91e71c0f8913bb06d70917abcf` / `511e7f34ca84390fd5d000326ab33c46c3050fc4` | Current values and accept-any-object schema. |
| Envelope wrapper | `1f9e0f785a701da2a2b8f52bf73f4e97866d951d` | Existing schema-runner delegation. |
| Performance workflow | `8e4c3b801fe6dbaac5e6645b054768859e84fa1e` | Shape check, nine direct tests, triggers, and explicit execution holds. |
| Fixture helper / negative tests | `f5d42f75b671e0fa07767f52fdda9661d0d721ab` / `886543d63184ff5f7fc6f14b6944eb6000ff5a10` | Separate dataclass validation, not envelope loading. |
| Retired harness | `ac2522686546b7428ad0cc5c8cd76860ab285998` | Finite exit-3 hold. |
| Render-diff builder | `ee24890c0e06bd941e0f1ead919e9e7b9bc37460` | Ratio reader and discovered-scenario coverage limit. |
| Proof / release-manifest builders | `8396c912a75c803baf8a92abe7a2f8cad582ba41` / `566731bd6ad1510ecd1e01e0275ffa04b3993a86` | Byte hashing and candidate-output limitations. |

Drive's *Directory Rules* was consulted as lineage. Notion's *Close governed
MapLibre runtime probe matrix* was consulted as coordination: it retains earlier
bounded results and unresolved wider probes. Neither replaces current GitHub
source, authenticates a browser run here, or overrides accepted decisions.

### Evidence limits

This revision does not audit every consumer, import, package, schema, deployment,
source, policy, or hosted run. It does not resolve EvidenceBundles, run a complete
probe matrix, measure performance, or establish required-check enforcement.
Code-defined destinations are not inventories of emitted objects.

**No-loss record:** v0.5 preserves all original H1/H2/H3 anchors and the existing
identity while consolidating repetitive lists. It corrects contradictory proposed
ADR language, replaces already-resolved roadmap questions, makes reader/test
coverage explicit, and narrows unverified runtime/absence claims. Prior content
remains available at the recorded blob; no payload or normative authority changes.

## Open decisions and ADR triggers

### ADR or migration discipline

The immediate unresolved decision is the substantive envelope contract and its
consumer/validator/workflow closure. New authority homes, package ownership,
public access, policy, source admission, lifecycle semantics, or meaningful alias
migrations require their own applicable decisions. This README makes none.

### No decision by convenience

Do not treat an open schema, convenient endpoint, generated hash, existing
filename, screenshot, or model recommendation as adoption. The correct next
step is the bounded contract/consumer slice, not a second renderer or live map.

## Rollback

### Before merge

Keep the task branch unmerged or append a focused revert to that branch. Preserve
the new [generated-work receipt](../../data/receipts/generated/README.md) as
historical process memory rather than editing it to describe different bytes.

### After merge

After any separately authorized integration, restore only this README from prior
blob `9b24a8d51013e06401cce7a02f06941feecf37e7` through reviewed history, or make a
forward correction. Restoring v0.4 also restores its contradictory ADR language;
a reviewed forward fix is often preferable. Do not force-reset shared history.

### Rollback triggers

Correct unsupported reader, schema, value, runtime, ownership, or validation
claims; broken anchors/links; introduced disclosure; or conflict with accepted
placement and trust boundaries. Re-pin actual implementation before reversal.

### Documentation rollback is not operational rollback

The change affects this README and its authoring receipt only. Reverting prose
does not revert configuration, workflows, dependencies, applications, deployments,
policy, data, or release state. Those require their own bounded rollback records.

## Verification backlog

| Item | State / first affected transition |
|---|---|
| Full five-field contract, numerical limits, and validator | **NEEDS VERIFICATION** before substantive config-validity claims. |
| All readers, effective loading, precedence, and overrides | **UNKNOWN** beyond the inspected set; blocks general runtime-config claims. |
| Actual performance scenarios, baselines, metrics, and coverage | **HOLD** before benchmark or regression claims. |
| Candidate trust-output homes and real command/result binding | **HOLD** before treating outputs as proof or release support. |
| Wider browser/source/plugin/accessibility/long-session evidence | **NOT RUN HERE**; remains separate from this documentation task. |
| Specialist stewardship, human review, and hosted exact-head results | **NEEDS VERIFICATION** before readiness or integration claims. |
| External endpoints, rights, sensitive-data handling, and public serving | **NOT INSPECTED**; no activation or publication authority. |

## Maintainer checklist

- Preserve the plural path, named consumer, exact version, and non-secret scope.
- Separate architecture acceptance, dependency declarations, config checks, and runtime proof.
- Check the actual envelope shape; do not substitute unrelated fixture fields.
- Keep policy, evidence, release, correction, and rollback outside configuration authority.
- Record exact checks, failures, gaps, and provenance; preserve current delivery controls.

[Back to top](#top)
