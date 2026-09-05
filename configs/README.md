<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-readme
title: configs/ — Canonical Commit-Safe Configuration Root
type: README
subtype: canonical-root-landing-page
version: v0.6
prior_version: v0.5
status: repository-grounded; draft; canonical-root; mixed-maturity; non-authoritative
owner: "@bartytime4life — CONFIRMED CODEOWNERS route and root-registry default; accepted specialist stewardship and independent approval remain NEEDS VERIFICATION"
created: 2026-06-16
updated: 2026-09-04
review_date_timezone: America/Chicago
policy_label: public-documentation; non-secret; consumer-bound; fail-closed; non-publisher
current_path: configs/README.md
owning_root: configs/
root_class: canonical
readme_profile: ROOT_FULL
responsibility: explain shared commit-safe configuration, current lane inventory, verified reader boundaries, validation limits, and reversible maintenance without owning policy, evidence, lifecycle, runtime, infrastructure, or release authority
truth_posture: CONFIRMED pinned tree and inspected declarations; PROPOSED documentation revision and future per-file guidance; UNKNOWN general loading, deployment, and runtime state; NEEDS VERIFICATION consumer closure, enforcement, and independent stewardship
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 26c7a6aa126cb361124d15801c23824ffc03ff23
  configs_tree: 58bd56d863ec3c6298038ff5b53757d4439e5684
  prior_blob: a800983eac7582a84e9dd82bc7d4baf04f552ad8
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  directory_rules_tombstone_blob: 9f70679c61dba2df46fd85d780f115fee6b59007
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  gitignore_blob: 50e0e0e2485e6dbd6b7e1c2767350b459335b22b
  direct_child_directories: 7
  tracked_directories_including_root: 21
  tracked_blobs: 28
  tracked_readmes: 21
  tracked_templates: 5
  tracked_json_config_payloads: 1
  tracked_gitkeeps: 1
related:
  - ../CONTRIBUTING.md
  - ../.github/CODEOWNERS
  - ../.gitignore
  - ../docs/doctrine/directory-rules.md
  - ../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../docs/architecture/directory-rules.md
  - ../control_plane/root_registry.yaml
  - ../docs/security/INCIDENT_RESPONSE.md
  - dev/README.md
  - domains/README.md
  - examples/README.md
  - local/README.md
  - maplibre/README.md
  - templates/README.md
  - test/README.md
  - ../data/receipts/generated/README.md
notes:
  - "Counts close the non-truncated tracked configs tree at the pinned base, not ignored workstation files, external stores, other branches, or operational consumers."
  - "Directory Rules section 16 defines required ROOT_FULL fields, not mandatory literal H2 titles or an exact first-twelve-heading order. Existing H2 navigation is retained."
  - "The displayed tree is direct-child only; deeper detail belongs to the child READMEs."
  - "The legacy architecture Directory Rules path is already a read-only tombstone; consumer closure and physical retirement remain separate."
  - "The MapLibre workflow reads envelope identity and threshold-object shape; its separate fixture tests do not prove enforcement of the envelope budgets."
  - "This revision changes root documentation and its required authorship receipt only. It changes no child README, configuration payload, dependency, consumer, validator, workflow, policy, registry, runtime, or release state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `configs/` — Canonical Commit-Safe Configuration Root

**Find the right configuration lane, identify its reader, and keep authority out
of configuration.** This root holds shared, non-secret defaults, templates,
examples, and configuration guidance. A file here is input to a named consumer;
it is not proof that the consumer loads it or that a system is running safely.

**Start here:** [Lane index](#configuration-lane-index) ·
[Current inventory](#status) · [Reader evidence](#validation) ·
[Local overrides](#local-overrides) · [Change checklist](#safe-change-pattern) ·
[Open verification](#open-verification-register)

> [!IMPORTANT]
> **Current tracked shape: 28 files, seven direct child directories.** Most of
> this root is documentation: 21 READMEs, five placeholder templates, one
> MapLibre performance-envelope JSON file, and one empty `.gitkeep`.
> These counts describe the pinned Git tree, not installed services, complete
> validation, active domain profiles, or deployment readiness.

> [!CAUTION]
> **No secrets and no authority overrides.** Real credentials, private endpoints,
> signed URLs, living-person or DNA records, protected locations, and sensitive
> source details do not belong here, including files called `local`, `test`,
> `example`, or `template`. A setting cannot approve evidence, consent, rights,
> source admission, review, release, or public access.

<a id="1-purpose"></a>

## Purpose

Make shared configuration reviewable: what can vary, which consumer reads it,
what values are safe, which checks run, and how a change is corrected or rolled
back. Configuration follows its consumer unless genuinely shared; centralizing
one application's settings merely for directory symmetry is not the goal.

The [lane index](#configuration-lane-index) routes development, local, testing,
example, template, MapLibre, and domain work. Deeper domain semantics, consumers,
and commands stay in their owning child or implementation documentation.

KFM's trust path remains:

```text
RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED
```

Public clients use governed APIs and released artifacts, never internal or
unreleased stores or this root as a public data interface. Consequential claims
resolve through `EvidenceRef -> EvidenceBundle`; maps, tiles, graphs, indexes,
scenes, summaries, and AI remain carriers or interpretations. Promotion is a
governed transition, not a config switch, passing test, or file move.

<a id="2-authority"></a>
<a id="3-directory-rules-basis"></a>
<a id="4-authority-boundary"></a>

## Authority level

**Canonical responsibility for shared non-secret configuration; no independent
truth, policy, release, or deployment authority.** [ADR-0029](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../docs/doctrine/directory-rules.md). Section 10.4
routes configuration by its consumer; section 16 defines README fields and
direct-child maps. The adopted bytes retain an internal draft label; that does
not undo the accepted decision.

| Root field | Current declaration and limit |
|---|---|
| Identity / class / status | `root.configs` / `canonical` / inherited `ACTIVE` in the Root Registry |
| Allowed artifact kind | `configuration`; its local README explains the boundary |
| Prohibited artifact kinds | `data_instance`, `policy_rule`, `release_decision`; other responsibilities are routed below |
| Exposure | `internal` configuration responsibility; the repository and this documentation are public |
| Mutation / retention | Versioned / repository lifetime; not an ephemeral cache or generated-output store |
| Owner / permitted writer / reviewer | Registry defaults name `@bartytime4life`; CODEOWNERS routes `/configs/` to that account |
| Validation profile | `non_secret_configuration` is a declared profile, not proof of a comprehensive executable check |

These are inspected declarations from the
[Root Registry](../control_plane/root_registry.yaml) and
[CODEOWNERS](../.github/CODEOWNERS). They do not authenticate specialist roles,
independent approval, access-control enforcement, or a particular write's authority.
Authorized agents contribute through isolated branches under current delivery
controls; the register does not permit direct-main or release writes.

### Responsibility split

| Question | Owning responsibility | Configuration's limit |
|---|---|---|
| What does an object or field mean? | [contracts/](../contracts/) | Reference meaning, never redefine it |
| What machine shape is valid? | [schemas/](../schemas/) | Reference the actual parser/schema |
| Is an operation allowed? | [policy/](../policy/) | Select permitted behavior, never forge a decision |
| What acquires a source? | [connectors/](../connectors/) | No source admission by filename or selector |
| What transforms or schedules a run? | [pipelines/](../pipelines/) / [pipeline_specs/](../pipeline_specs/) | Keep executable stages and durable run graphs separate |
| What implements or composes a consumer? | [apps/](../apps/), [packages/](../packages/), [runtime/](../runtime/) | No disguised application, adapter, or model code |
| What deploys, networks, exposes, or hardens it? | [infra/](../infra/) | Local overrides are not host or public-ingress authority |
| What owns lifecycle and accountability instances? | [data/](../data/) | No source records, EvidenceBundles, receipts, proofs, or catalogs here |
| What authorizes release, correction, or rollback? | [release/](../release/) | No release decision by configuration |
| What tests behavior or supplies reusable test inputs? | [tests/](../tests/) / [fixtures/](../fixtures/) | Configuration is neither test implementation nor fixture corpus |

Tracked defaults and documentation are authored, versioned files. Their logical
home does not imply a secret store, database, production mount, or installed
workstation layout. Generated results belong in the existing scoped
[artifacts/](../artifacts/) compatibility surface or approved external CI storage,
not in `configs/`. Restricted bytes remain outside public Git even when another
logical responsibility root is involved.

## Status

### Repository snapshot

| Evidence | Immutable identity |
|---|---|
| Inspected base | `main@26c7a6aa126cb361124d15801c23824ffc03ff23` |
| Complete recursive `configs/` tree | `58bd56d863ec3c6298038ff5b53757d4439e5684`; response `truncated: false` |
| Prior root README | `a800983eac7582a84e9dd82bc7d4baf04f552ad8` (`v0.5`) |
| Adopted Directory Rules | `fd49a0b83e55cef52c1124281f093e263526898d` |
| ADR-0029 | `a4de0d7a96b78da59cfc499d1025e1508afd8dd9` |
| Existing compatibility tombstone | `9f70679c61dba2df46fd85d780f115fee6b59007` |
| Root Registry | `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` |

The snapshot is reproducible at the recorded commit. Later merges, corrected
children, ignored local files, and other branches require a new read; they must
not be silently incorporated into this historical pin.

### Material corrections from v0.4

The `v0.5` revision replaced older root-registry and adoption uncertainty with
accepted placement evidence. That remains historical progress. This `v0.6`
refresh advances the evidence pin, incorporates newer direct-child guidance,
replaces the recursive display with a direct-child map, and recognizes the
already-present legacy Directory Rules tombstone. It does not enact a migration.

<a id="7-current-tracked-directory-shape"></a>

### Exact tracked tree

The display shows **this directory and direct children only**, as required by
`DIR-README-003`. Child READMEs own deeper maps.

```text
configs/
├── README.md     # shared configuration boundary and navigation
├── dev/          # development guidance; no tracked payload
├── domains/      # domain configuration guidance; no tracked profile
├── examples/     # configuration-example guidance; no tracked example payload
├── local/        # README tracked; local overrides ignored
├── maplibre/     # configuration guidance and one performance envelope
├── templates/    # guidance and five placeholder templates
└── test/         # test-configuration guidance; no tracked profile
```

### Inventory closure

| Tracked class | Count | What this establishes |
|---|---:|---|
| Direct child directories | 7 | The seven lanes above |
| Nested directories / including root | 20 / 21 | Recursive tracked directory structure |
| README files | 21 | Root, seven lane READMEs, and thirteen domain READMEs |
| Templates | 5 | Four YAML templates and one JSON template |
| Other JSON configuration payloads | 1 | `maplibre/perf-envelope.v1.json` |
| Empty placeholders | 1 | `domains/habitat/.gitkeep`, zero bytes |
| Total blobs / other blobs | 28 / 0 | Complete tracked inventory at this pin |

The thirteen domain directories contain documentation and the one placeholder,
not executable domain configurations. `dev/`, `examples/`, `local/`, and `test/`
are each README-only. The JSON template is counted among templates, not again
as the separate JSON configuration payload.

### Maturity matrix

| Claim | Status | Limit |
|---|---|---|
| Root placement and machine projection | **CONFIRMED** declarations | Not proof of enforcement or independent stewardship |
| Tracked inventory and child document identities | **CONFIRMED** at the pin | Not an audit of every claim in every child README |
| Five templates and one envelope exist | **CONFIRMED** bytes/identity inventory | Not operational adoption or semantic adequacy |
| MapLibre envelope readers | **CONFIRMED, BOUNDED** source inspection below | Not complete consumer coverage or measured browser performance |
| Generic loading, overlays, and semantic validation | **UNKNOWN / NEEDS VERIFICATION** | Do not infer a root-wide loader from the directory names |
| Secret-scanning and required-check enforcement | **NEEDS VERIFICATION** | No scanner/control audit in this documentation change |
| Local installation, runtime parity, and public self-hosting | **UNKNOWN** | No host, network, deployment, or public-service probe |
| Release/publication authority in this root | **NONE** | Independent governed transitions remain required |

<a id="5-allowed-contents"></a>

## What belongs here

Small, genuinely shared non-secret defaults, templates, examples, thresholds,
profile selectors, and their explanatory or migration guidance. Every payload
needs a named consumer or an explicit non-operational template purpose. A
single-consumer operational file normally stays with its owner under §10.4.

### Admission test

Establish responsibility, public-commit safety, consumer or illustrative purpose,
field meaning, parser/schema where applicable, environment scope, precedence,
failure behavior, ownership, and rollback. Unknown non-critical details may
travel with a visibly non-operational draft; missing safety-critical bindings
block the operational transition that needs them.

Templates may reference source, dataset, layer, or release shapes; they are not
instances of those objects. Reviewed public verification material is permissible
only under the applicable security contract. Any compatibility alias needs its
own accepted scope, one-way ownership, migration, and exit evidence; none is
created here. A README or `.gitkeep` reserves no implementation authority.

<a id="6-forbidden-contents"></a>

## What does NOT belong here

No resolved secret, credential, cookie, signing key, private endpoint, live signed
URL, protected identity, exact sensitive location, production snapshot, or source
export. This includes material labeled local, mock, example, or test.

No schema, semantic contract, executable policy, source-registry instance,
EvidenceBundle, receipt, proof, catalog, lifecycle record, release decision,
application/adapter code, pipeline implementation, durable run graph, deployment
configuration, generated report, screenshot, cache, or log. Route these by the
[responsibility split](#responsibility-split), not by their filenames.

Do not create parallel configuration, schema, contract, policy, source, registry,
proof, receipt, or release authority. Living-person/DNA, person–parcel, rare-species,
archaeology, cultural/sovereignty, infrastructure, and private-land uncertainty
requires applicable denial, restriction, quarantine, or reviewed transformation;
configuration cannot clear it.

## Inputs

A proposed configuration derives from a verified consumer interface and version,
its load mechanism, field semantics, parser/schema, safe defaults and units,
policy constraints, environment contract, fixtures/tests, and reviewed migration
requirements. Build examples from that interface, not by copying production data
and replacing a few values.

A filename, planning document, vendor example, parser success, unrelated green
workflow, merged PR, operator-local file, or AI-generated explanation is not
sufficient evidence of consumer binding or safe operation.

<a id="8-diagram"></a>

## Outputs

The root directly supplies authored configuration inputs and guidance. A consumer
may produce runtime behavior, but this root does not itself emit evidence,
PolicyDecisions, lifecycle promotion, release approval, public responses, or
published artifacts. Its required authorship receipt belongs in the separate
[generated-work receipt lane](../data/receipts/generated/README.md).

```text
contracts / schemas / policy constraints
                    |
                    v
       shared non-secret configuration
                    |
                    v
       named bounded consumer or adapter <--- external values by reference
                    |
                    v
       behavior requiring its own execution evidence

validation != human approval != release != deployment != publication
```

This is a responsibility sketch, not a deployed topology. Config changes do not
configure an Ubuntu host, firewall, router, domain, public IP, or local model
endpoint. Runtime composition and public exposure retain separate owners and
authorization gates.

<a id="9-validation-expectations"></a>

## Validation

### Current evidence boundary

The root inventory is exact; implementation inspection is deliberately bounded.
The following source reads narrow the old generic consumer-unknown statement
without claiming a complete configuration audit.

| Surface | Inspected behavior or declaration | What it does not prove |
|---|---|---|
| [MapLibre envelope schema](../schemas/maplibre/perf-envelope.schema.json) | Requires a JSON object and permits additional properties; no budget fields or numerical bounds are required | Meaningful validation of the envelope's declared budgets |
| [Envelope validator wrapper](../tools/validators/maplibre/validate_perf_envelope.py) | Delegates to the shared JSON-schema runner with the schema above | A dedicated numerical or browser-performance gate |
| [MapLibre performance workflow](../.github/workflows/maplibre-perf-governance.yml) | Explicitly reads `configs/maplibre/perf-envelope.v1.json`; requires `object_type == PerfEnvelope` and a dictionary-valued `thresholds` | Enforcement of the five numerical envelope budgets, general runtime loading, or release readiness |
| [Fixture negative tests](../tests/maplibre/test_perf_governance_negative_paths.py) and [builder](../tests/maplibre/perf_fixture_builder.py) | Three tests exercise a separate in-memory fixture's frame, memory, and tile-error constraints; neither file reads the envelope | Validation of the committed envelope or actual browser measurements |
| [Template guide](templates/README.md) | Records five placeholder payloads and unresolved consumers | Template consumption, accepted schema conformance, source admission, or release closure |
| [Ignore rules](../.gitignore) | Ignore `configs/local/*`, except `configs/local/README.md` | Safety, existence, encryption, or runtime use of local files |

These statements report source inspection, **not test execution in this revision**.
The MapLibre child owns the deeper reader analysis. This root does not admit a
renderer version, plugin, source, protocol, worker, or operational profile.

| Documentation workflow | Inspected coverage | Interpretation |
|---|---|---|
| [link-check](../.github/workflows/link-check.yml) | Local targets in changed Markdown; no external URL requests | The definition covers this README; exact-head hosted success is separate |
| [docs-meta-block](../.github/workflows/docs-meta-block.yml) | Its command's explicit roots are `README.md docs tools/validators/docs` | `configs/` is outside that command's explicit scan roots |
| [docs-stale-scan](../.github/workflows/docs-stale-scan.yml) | The same explicit roots, with an advisory freshness profile | Same coverage gap; freshness is not semantic correctness |

No workflow is changed by this revision. A workflow running after a Markdown
change does not by itself mean it inspected this file. Complete checker behavior,
required-check coupling, and later hosted results require their own evidence.

### Minimum checks for a configuration change

Run checks proportionate to the actual diff. For payloads: syntax; duplicate keys
and non-finite values; accepted schema and known-key behavior; ranges, units, and
cross-field semantics; consumer loading and precedence; secret/sensitivity safety;
policy and release boundaries; deterministic failures; positive and negative
fixtures; compatibility; and rollback of the configuration/consumer pair.

For a README-only change: review placement and claims, preserve identity and
navigation, validate metadata and Markdown targets, inspect the complete diff,
record exact source/head identities, and check the authorship receipt. Report
unavailable native checks rather than converting them to a pass.

### Safe inspection examples

Run from a real repository checkout. These are **inspection examples**, not a
root-wide validation command or a record of this session's execution:

```bash
git ls-tree -r --name-only HEAD -- configs/
python -m json.tool configs/maplibre/perf-envelope.v1.json >/dev/null
git check-ignore -v configs/local/example.local.yaml
git diff --check
```

`json.tool` checks syntax, not duplicate-key rejection, schema, numerical budgets,
consumer use, or release safety. The ignore probe tests a synthetic path without
creating a local file. Use the consumer-supported safe YAML/TOML parser and
explicit duplicate-key handling when those formats actually change; do not add
dependencies merely to validate documentation examples.

### Interpretation rule

A green check supports only its checked assertion, inputs, environment, and
revision. It is not evidence sufficiency, policy approval, human review, release,
deployment, publication, or proof that every test ran. Record failures as
introduced, inherited, external, or unattributed only to the extent the evidence
supports; an old failure is not a current base-versus-head comparison.

## Review burden

### Confirmed routing

CODEOWNERS routes this path to `@bartytime4life`. Specialist configuration,
security, domain, operational, and independent-review assignments remain
**NEEDS VERIFICATION**. Routing and registry defaults do not prove that review
occurred or that separation of duties is enforced.

### Review by change class

| Change | Additional review burden |
|---|---|
| Root or child README | Source accuracy, currentness, placement, navigation, preserved boundaries |
| Template or example | Placeholder safety, illustrative status, consumer/schema references |
| Shared default or threshold | Consumer owner, units/ranges, compatibility, negative tests, rollback |
| Loader or precedence | Every affected consumer; migration and override ceilings |
| Domain or security-sensitive selector | Rights, privacy, sovereignty, sensitivity, consent, and policy specialists as applicable |
| Runtime, map, or deployment-adjacent setting | Owning implementation/operations team; accessibility, performance, and exposure boundaries |
| Release-dependent setting | Independent evidence, policy, review, release, correction, and rollback duties |

Escalate a placement conflict through the owning root and accepted ADR process.
For potentially leaked values, use the repository security reporting guidance and
[incident-response document](../docs/security/INCIDENT_RESPONSE.md); that document
still carries draft ownership and must not be represented as an exercised
operational service. Never reproduce secrets or protected details in an issue.

## Related folders

The [lane index](#configuration-lane-index) is the local navigation surface. The
[responsibility split](#responsibility-split) routes contracts, schemas, policy,
implementation, tests, fixtures, infrastructure, lifecycle, and release work.
Root [examples/](../examples/) is distinct from `configs/examples/`: a supported
runnable demonstration is not merely a configuration snippet.

Existing `tests/fixtures/` support is not a second automatically accepted reusable
fixture authority. The [test-configuration guide](test/README.md) preserves that
placement conflict; this root neither migrates existing fixtures nor approves a
new home. Generated outputs likewise retain the scoped `artifacts/` compatibility
boundary rather than becoming config, receipt, proof, or release objects.

## ADRs

### Accepted governing decision

ADR-0029 adopts the canonical doctrine bytes. The legacy
[architecture-path document](../docs/architecture/directory-rules.md) is **already
a read-only compatibility tombstone**, not a live duplicate awaiting replacement.
Its consumer closure remains open and physical deletion held. This update
corrects root documentation to that observed state without changing doctrine,
the ADR, the alias register, or any migration/deletion authority.

### Configuration-specific decision posture

This bounded review did not establish a new root-wide configuration-loader ADR.
A cross-root loader/precedence contract, new root, authority transfer, lane
rename/split/retirement, or changed public/secret boundary requires the applicable
accepted decision and migration evidence. Routine truthful same-path authoring
must not be blocked merely because a later operational or release gate is open.

## Last reviewed

**2026-09-04 America/Chicago** (inspection continued into September 5 UTC), against
`main@26c7a6aa126cb361124d15801c23824ffc03ff23`.

Reviewed: full prior root README; exact non-truncated tracked configuration tree;
seven direct-child README metadata/current-boundary sections; accepted placement
and registry declarations; legacy tombstone; CODEOWNERS/ignore rules; selected
MapLibre reader/schema/test source; documentation workflow commands; receipt
schema/lane; and current delivery controls. Domain child payload/README identities
were inventoried, not exhaustively re-audited for semantics.

Not established: whole-repository test results, complete consumer inventory,
application installation, runtime or host behavior, enforcement of network/write
isolation, branch protection, independent approval, or release readiness.

Re-review when a child inventory or boundary changes, a consumer or validation
surface changes, an ADR is accepted/superseded, an exposure/secret/storage rule
changes, or drift/correction/rollback occurs. Child evidence pins remain their
own historical records. Do not label every child current solely because this
root has a newer review date.

## Configuration lane index

Versions below are **document versions observed at the root's evidence pin**,
not package versions, acceptance decisions, or maturity scores.

| Lane | README edition / update | Exact tracked contents | Reader and ownership limit |
|---|---|---|---|
| [dev/](dev/README.md) | `v0.4` / 2026-09-04 | README only | Shared development guidance, not installed defaults or a generic loader |
| [domains/](domains/README.md) | `v0.6` / 2026-09-04 | Parent README, thirteen domain READMEs, habitat placeholder | Domain configuration boundaries, not live profiles or domain truth |
| [examples/](examples/README.md) | `v0.2` / 2026-07-13 | README only | Illustrative guidance; older child currentness claims remain bounded |
| [local/](local/README.md) | `v0.3` / 2026-09-04 | README only; other paths ignored | Uncommitted local overrides, never the only undocumented shared prerequisite |
| [maplibre/](maplibre/README.md) | `v0.5` / 2026-09-04 | README and `perf-envelope.v1.json` | Bounded readers described above; no operational map or measured performance implied |
| [templates/](templates/README.md) | `v0.3` / 2026-09-04 | README and five templates | Placeholder inputs; named consumers and semantic validation remain unverified |
| [test/](test/README.md) | `v0.4.0` / 2026-09-04 | README only | Test-configuration guidance; not tests, fixtures, a runner, or a loaded profile |

### Domain lanes

The exact directory set is agriculture, archaeology, atmosphere, fauna, flora,
geology, habitat, hazards, hydrology, people-dna-land, roads-rail-trade,
settlements-infrastructure, and soil. Use the [domain index](domains/README.md)
and its children for local boundaries; its older child-version totals are a
snapshot, not a live roll-up. No domain profile, source, renderer, API, or release
is activated by the existence or recent update of a README.

## Minimum per-file configuration contract

**PROPOSED documentation guidance**, unless an accepted consumer contract already
specifies these concerns. This is not a new envelope schema or mandatory wrapper
for every existing file.

| Concern | Required before claiming operational use |
|---|---|
| Identity and class | Stable config ID/version; default, template, example, selector, threshold, override, or compatibility role |
| Consumer | Exact implementation owner, version/ref, loader, invocation, and supported environment |
| Meaning and shape | Contract/schema references where applicable; parser/version, duplicate and unknown-key behavior |
| Defaults | Explicit units, bounds, required values, empty/null/sentinel behavior, and unresolved-placeholder rejection |
| Precedence | Deterministic merge/replacement order, source selection, conflict and override behavior |
| Trust boundary | No secrets; references-by-name only; no policy, source, rights, sensitivity, review, or release override |
| Validation | Actual commands, positive/negative and consumer-loading cases, scope, revision, and known gaps |
| Governance | Accountable owner, review expectations, change trigger, compatible prior state, migration, and rollback |

Do not replace an accepted consumer interface with this illustrative checklist.
A future machine schema belongs to `schemas/`, meaning to `contracts/`, and
admissibility to `policy/`.

## Consumer binding, precedence, and overrides

### Current posture

No repository-wide loader or precedence contract is established here. The
specific MapLibre workflow reader does not establish automatic discovery of
other files, template rendering, local override loading, application consumption,
or shared unknown-key behavior.

### Required consumer binding

Bind config identity to a named bounded loader, version, field semantics,
parser/schema, explicit environment and precedence, policy constraints, tests,
and migration/rollback target. Direct scattered imports must not create hidden
consumer-specific authorities. Record source and loaded-value digests where
appropriate without leaking secret or sensitive values.

### Precedence discipline

Each consumer declares its actual order; this README invents no universal one.
Use one documented default source, explicit overlays, ignored local overrides
where supported, conflict/cycle detection, stable unknown-key behavior, and
rejection of unresolved required placeholders. Do not silently substitute a
weaker parser or a production environment when a configured source fails.

### Override ceiling

No overlay may replace source authority, evidence support, consent, rights,
sensitivity, policy decisions, required review, release state, correction or
rollback lineage, access class, or protections for restricted locations and
private data. A client-side toggle cannot lift those restrictions.

## Secrets, sensitive values, endpoints, and local overrides

### Commit-safe representations

Use unmistakable placeholders, synthetic identifiers, variable/secret-store
references by name, or reviewed public values permitted by the consumer and
policy. Even localhost values need an explicitly local purpose; they do not
establish access control or deployment readiness. Public verification material
requires its own approved security contract.

### Forbidden representations

No credentials, private keys, cookies, signed URLs, authorization headers,
confidential host/bucket/account/database identifiers, reconstructable protected
coordinates, restricted source metadata, operator home paths, or browser-exposed
model/source/admin credentials. Names and hashes may themselves be sensitive;
minimize public diagnostics and identifiers rather than assuming hashing makes
them safe.

### Local overrides

The exact [ignore rules](../.gitignore) exclude `configs/local/*` and re-include
only `configs/local/README.md`. This is a tracking rule, not a security boundary.
Ignored files can still leak through logs, screenshots, archives, backups,
support bundles, container contexts, caches, or force-adds. No such workstation
files were inspected here.

Shared non-secret templates belong in a tracked shared lane. Actual secrets stay
external; local installation/runtime setup and later public self-hosting/network
exposure remain separate. Nothing here authorizes firewall, DNS, router, public-IP,
reverse-proxy, cloud-hosting, or direct-model exposure changes.

### Incident posture

Stop unsafe use; revoke or rotate an exposed credential; preserve appropriately
restricted evidence; assess history and downstream copies; follow the applicable
security response; correct the repository without publishing the value; and add
bounded prevention tests. Removing a string alone is not revocation or cleanup.
Shared-history rewriting requires separate explicit incident authority.

## Formats, placeholders, and versioning

### Format guidance

| Format | Use and required caution |
|---|---|
| JSON | Strict machine input; syntax alone does not reject every ambiguous or semantically unsafe value |
| YAML | Safe consumer-supported parser, explicit type/duplicate/tag/anchor controls |
| TOML | Bind supported parser and consumer version |
| Environment example | Variable names and obvious fake/reference values only; review browser-exposed prefixes |
| Markdown | Boundary and validation guidance, never a substitute for implementation or policy |

### Naming

A future name should expose consumer, role, and version when material, for
example `<consumer>.<class>.v<major>.json` or
`<consumer>.<environment>.example.toml`. These are patterns, not new paths.
Existing names remain unchanged until a reviewed compatibility migration.

### Placeholder rules

Values such as `<REQUIRED_OUTSIDE_REPOSITORY>`, `${SECRET_REFERENCE_NAME}`, and
`example.invalid` are illustrative. `TBD`, empty strings, nulls, arrays, or objects
are incomplete values, not proof of failure safety. The actual consumer must
reject unresolved safety-critical placeholders before an operation proceeds.

### Versioning and deprecation

Version changes to interpretation, defaults, units, enums, required fields,
precedence, security posture, or failures. Record prior/new identities, compatible
consumer range, migration, deprecation/exit condition, correction implications,
and rollback. A permitted compatibility alias remains one-way and cannot evolve
as a second writer.

## Failure semantics and negative cases

| Negative case | Required design response |
|---|---|
| Missing file/key or unresolved required placeholder | Error or hold, not unsafe fallback |
| Duplicate key, non-finite number, invalid range/unit, cross-field conflict | Reject before action with bounded diagnostics |
| Unknown field or schema/version mismatch | Apply the declared consumer rule; no silent trust-significant drift |
| Missing consumer, ambiguous precedence, cycle, unavailable loader/parser | Hold or error; no guessed behavior or weaker substitute |
| Secret-like value or protected precision in tracked input | Stop, redact diagnostics, invoke restricted review/incident handling |
| Policy, consent, rights, review, access, or release override | Deny |
| Unsafe endpoint or public credential | Deny; do not probe or disclose the value |
| Deprecated profile beyond its supported window | Reject or require reviewed migration |
| Incompatible rollback pair | Hold rollback until compatibility is restored |
| Validator echoes raw sensitive values | Treat as a defect; retain only safe path/code context |

These are requirements for future consumer validation, not a new global enum or
proof that all consumers enforce them. Test positive, negative, denial, stale,
correction, and rollback cases. Distinguish workflow HOLD from runtime outcomes;
normalization and obligation enforcement remain owned by the relevant contract.

<a id="10-migration-posture"></a>

## Migration, correction, and rollback

### Misplaced material

Inventory the actual object and its producers/consumers before moving it. Resolve
responsibility through adopted rules, classify the needed decision, preserve
identity and history, update consumers and references in a bounded migration,
validate parity/negative behavior, and record correction and rollback. Physical
retirement requires the relevant writer/consumer closure; a file move is not it.

### Common routing

Meaning goes to contracts, shape to schemas, admissibility to policy, operational
code to its implementation owner, host exposure to infrastructure, and source,
lifecycle, receipt/proof, or release instances to their existing object-family
homes. See the [responsibility table](#responsibility-split). Do not select a
new path from a filename or copied illustrative tree.

### Documentation rollback

Prior root README blob: `a800983eac7582a84e9dd82bc7d4baf04f552ad8`.
Before integration, leave the proposal unmerged or apply a non-force corrective
commit on its task branch. After separately authorized integration, use a
reviewed focused revert or transparent forward correction. Preserve the
historical authorship receipt; it describes authored bytes at its own revision,
not an evergreen hash of current main. No child file needs restoration for this
root-only content update.

### Configuration rollback

Restore a **reviewed configuration/consumer pair**, not just old bytes. Check
parser/schema compatibility, precedence, environment, secret references, policy
and release constraints, caches/derivatives, and correction notices where public
behavior changed. Rollback must not recreate parallel writable authorities or
restore a revoked permission.

<a id="11-safe-change-pattern"></a>

## Safe change pattern

Pin base and target; read authority and adjacent boundaries; check active overlap;
classify the artifact; identify the consumer or explicit example-only purpose;
keep values non-secret and public-safe; document actual semantics, precedence,
failure, and rollback; implement the smallest useful review unit; validate the
changed area; preserve receipt/provenance; and deliver through the currently
permitted branch or draft-review path. An unresolved later operational gate does
not prohibit safe reversible authoring, but a concrete delivery control still
applies to the affected transition.

### Change-impact crosswalk

| Changed concern | Dependency to inspect or update |
|---|---|
| Meaning / machine shape | Contract / schema plus applicable valid and invalid fixtures |
| Policy, exposure, consent, rights, sensitivity | Owning policy checks and qualified review |
| Loading, precedence, or selection | Consumer code, integration tests, compatibility and migration |
| Source or provider selection | Source-admission or runtime-adapter boundary; no activation by config |
| Rendering or thresholds | Actual map reader, accessibility/performance evidence, correction and rollback |
| Release-dependent behavior | Evidence, proofs, review, release, cache invalidation, correction |
| Secret references | Restricted security review and non-echoing negative tests |
| Names or paths | Links/imports, alias ownership, migration, identity and rollback |

No ready transition, approval, merge, repository setting, source activation,
release, deployment, promotion, or publication is implied by this guide.

<a id="12-definition-of-done"></a>

## Definition of done

### Root README update

A root update preserves identity/navigation; provides a pinned inventory; maps
required ROOT_FULL fields; retains exposure, writer, storage, trust, review,
validation, and rollback boundaries; and reports exact performed/not-run checks.
This edition's results belong in its authorship receipt and delivery handoff,
not in a permanent claim that the README passes every repository gate.

Section 16 requires **fields**, not an exact first-twelve-H2 order. Coverage here:

| Required ROOT_FULL concern | Section providing it |
|---|---|
| Purpose | Purpose |
| Root class and authority owner | Authority level |
| Adoption and conformance | Authority level; Status; ADRs |
| Belongs and prohibited | What belongs here; What does NOT belong here |
| Inputs, outputs, permitted writers | Inputs; Outputs; Authority level |
| Exposure and sensitivity | Authority level; Secrets, sensitive values, endpoints, and local overrides |
| Mutation, retention, generation, physical storage | Authority level; Outputs; Local overrides |
| Validation and negative checks | Validation; Failure semantics and negative cases |
| Owner, reviewers, escalation | Review burden; Incident posture |
| ADRs, migrations, aliases, targets | ADRs; Migration, correction, and rollback |
| Direct-child directory map | Status / Exact tracked tree |
| Evidence review and trigger | Last reviewed |

### Consequential configuration payload

Operational completion additionally requires a verified consumer/loader;
deterministic precedence; accepted meaning/shape where applicable; safe defaults,
units, ranges, and unknown-key behavior; no secrets or harmful precision;
positive/negative/compatibility/loading tests; preserved policy and release
boundaries; qualified review; and a tested compatible rollback. This documentation
update does not mark those requirements complete for an unseen payload.

<a id="13-open-verification-items"></a>

## Open verification register

| Open item | Status | First affected transition / closure evidence |
|---|---|---|
| Accountable specialist stewardship and independent review | NEEDS VERIFICATION | Approval; assignment and qualifying review/control evidence |
| Complete payload/template consumer map | NEEDS VERIFICATION | Operational use; pinned reads/imports/loaders and tests |
| Root-wide identity, precedence, unknown-key or semantic contract | PROPOSED / UNKNOWN | Adoption or shared loading; accepted scope and executable cases |
| MapLibre envelope numerical enforcement | NEEDS VERIFICATION | Performance assurance; real payload-bound checks and measured evidence |
| Template schema/semantic adequacy | NEEDS VERIFICATION | Consumption; per-template consumer and valid/invalid cases |
| Metadata/freshness coverage for configs | CONFIRMED command-scope gap | Hosted documentation assurance; explicit inclusion or accepted equivalent |
| Child README semantic freshness | PARTIAL | Reliance on child claims; targeted reviews, not root-date inheritance |
| Ignored local state and external secret integration | UNKNOWN | Local/runtime use; authorized workstation and environment evidence |
| Secret-scanner and required-check coverage | NEEDS VERIFICATION | Enforcement claims; exact scanner and server-side results |
| Correction and rollback propagation | NEEDS VERIFICATION | Operational change; consumer/cache/derivative drill |
| Legacy Directory Rules consumer closure / deletion | OPEN / HOLD | Retirement only; alias-consumer and retirement evidence |
| PR-delivery incident controls | NEEDS VERIFICATION before affected delivery | Current incident disposition and proven permitted delivery boundary |

Missing evidence narrows the claim; it does not admit secrets, invent a loader,
weaken policy, or freeze unrelated safe authoring.

<details>
<summary>Appendix A — no-loss and anchor-preservation ledger</summary>

### Retained

The same root, document ID, H1, all 23 H2 headings, and legacy section anchors;
shared non-secret configuration; all seven lanes; template/envelope context;
consumer/precedence discipline; sensitivity, source, evidence, policy, lifecycle,
review and release separation; failure, migration, correction, and rollback.

### Corrected or narrowed

The evidence snapshot and rollback blob; already-present tombstone versus pending
migration language; recursive map versus direct-child law; required fields versus
mandatory heading-order claim; bounded MapLibre readers versus unspecified
consumer maturity; documentation-check scope; and root review versus inherited
child-currentness claims. Detailed child prose is linked, not copied as a second
configuration manual. Child files and all six payload/template files are unchanged.

### Legacy anchor map

`#1-purpose` maps to Purpose; `#2-authority`, `#3-directory-rules-basis`, and
`#4-authority-boundary` to Authority level; `#5-allowed-contents` and
`#6-forbidden-contents` to their original sections; `#7-current-tracked-directory-shape`
to Exact tracked tree; `#8-diagram` to Outputs; `#9-validation-expectations` to
Validation; `#10-migration-posture` to Migration, correction, and rollback;
`#11-safe-change-pattern`, `#12-definition-of-done`, and
`#13-open-verification-items` to their original sections. `#status-summary` and
`#top` remain available. Historical source bytes remain in Git history.

</details>

## Status summary

At the pinned base, `configs/` is a canonical, versioned non-secret configuration
root containing **28 tracked files**. The current documentation, inventory,
registry/ignore declarations, and selected MapLibre reader limits are inspectable.
General loading, independent approval, complete validation, deployed behavior,
and operational enforcement remain unproved unless named evidence closes them.

**A configuration file is an input, not permission, evidence, deployment, or
publication.** Keep future work consumer-bound, default-safe, reviewable,
traceable, and reversible.

[Back to top](#top)
