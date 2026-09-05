<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-examples-readme
title: configs/examples/ — Commit-Safe Configuration Examples Boundary
type: readme
version: v0.3
prior_version: v0.2
status: draft; repository-grounded; README-only; non-authoritative; no-live-binding
owners: "NEEDS VERIFICATION — configuration, security, consumer, validation, developer-experience, and documentation stewardship"
review_route: "@bartytime4life via /configs/ CODEOWNERS; routing is not independent approval"
created: 2026-06-16
updated: 2026-09-04
policy_label: public-documentation; commit-safe; non-secret; consumer-bound; no-runtime-authority; no-deployment-authority
current_path: configs/examples/README.md
owning_root: configs/
readme_profile: BOUNDARY_COMPACT
responsibility: document shared illustrative configuration inputs and their consumer, validation, safety, and correction boundaries
truth_posture: "CONFIRMED pinned tracked inventory, parent guidance, accepted Directory Rules adoption, review routing, and hook source; PROPOSED future examples and binding conventions; UNKNOWN operational consumption and enforcement; NEEDS VERIFICATION specialist ownership and consumer-specific tests"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 26c7a6aa126cb361124d15801c23824ffc03ff23
  root_tree: 1a534800b23d9702c31664f4afe879ea25f4148b
  configs_tree: 58bd56d863ec3c6298038ff5b53757d4439e5684
  examples_tree: 6142daba31066b52fc74224a3bcaee155dd2d9e0
  prior_blob: c040064e4aea09e4e87658faf37f57b4e13a96f8
  tracked_files: [README.md]
  child_directories: 0
  parent_readme_blob: a800983eac7582a84e9dd82bc7d4baf04f552ad8
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  pre_commit_blob: 6469441400941d8ecbf6cb36f98601befe6abd7b
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
related:
  - ../README.md
  - ../templates/README.md
  - ../local/README.md
  - ../dev/README.md
  - ../test/README.md
  - ../domains/README.md
  - ../maplibre/README.md
  - ../../examples/README.md
  - ../../CONTRIBUTING.md
  - ../../SECURITY.md
  - ../../.github/CODEOWNERS
  - ../../.pre-commit-config.yaml
  - ../../.gitignore
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/security/SECRETS.md
notes:
  - "v0.3 replaces the July named-probe inventory with an exact tracked-tree observation and retains the document identity and section headings."
  - "No configuration example payload or loader is introduced. Snippets are illustrative, not accepted KFM fields or consumer interfaces."
  - "Hook configuration is source evidence, not proof of execution, complete secret detection, or required-check enforcement."
  - "The former docs/runbooks/SECRET_LEAK_RUNBOOK.md reference returned Not Found at the pinned base; SECURITY.md is the verified public disclosure entrypoint, with private-channel availability still unverified."
  - "The README and its separate generated-work receipt are the only intended changed artifacts; generation does not approve either artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Commit-Safe Configuration Examples

**Explain a configuration without turning it on.** `configs/examples/` is the
shared configuration-example lane beneath [`configs/`](../README.md). It currently
contains this README only: no example payload, child directory, or verified
consumer binding.

**Status:** draft v0.3 · **Owning root:** `configs/` · **Operational use:** not established

[Inventory](#status) · [Lane distinctions](#configuration-lane-distinctions) ·
[Example contract](#proposed-example-file-contract) · [Placeholders](#placeholder-and-secret-handling) ·
[Validation](#validation) · [First example](#safe-change-pattern) · [Rollback](#rollback-and-correction-posture)

> [!IMPORTANT]
> A filename, placeholder, `example: true`, or disabled-looking setting is not an
> enforced safety boundary. Parsing is not consumer compatibility; compatibility
> is not activation, review, release, deployment, or publication approval.

> [!CAUTION]
> Never copy live configuration into an example and redact only a few values.
> Author from the documented field surface using synthetic values. Real secrets,
> private endpoints, signed URLs, personal workstation details, restricted
> identifiers, and sensitive locations do not belong here.

## Purpose

Make a named consumer's configuration understandable through small, reviewable,
non-secret illustrations. Show the fields, mock values, replacement obligations,
authority references, supported validation, and unresolved behavior. Inherit the
parent configuration contract rather than duplicate an application manual.

A proposed consumer may be named in an inactive design example, provided it is
clearly **PROPOSED**. Do not describe that example as supported, runnable, or
consumed until the actual interface and tests establish those claims.

## Authority level

**Configuration sublane, not an independent authority root.** Placement remains
under `configs/`. [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the exact [Directory Rules](../../docs/doctrine/directory-rules.md) bytes;
their retained internal draft label does not reverse adoption. Sections 10.4 and
16.3 support shared non-secret configuration and inherited lane documentation.
One application's configuration normally stays with that application.

Meaning belongs to contracts, machine shape to schemas, admissibility to policy,
implementation to its consumer, lifecycle/accountability instances to their
owning data lanes, and release decisions to release governance. An example may
reference those responsibilities but cannot manufacture any of their decisions.

Preserve `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`.
Promotion is a governed transition, not a file move. Public clients use governed
APIs and released artifacts, not this directory or internal stores. Consequential
claims still require EvidenceRef -> EvidenceBundle; AI and rendered carriers are
not substitutes for evidence, rights, sensitivity, review, or release.

## Status

### Bounded repository snapshot

Findings are pinned to `main@26c7a6aa126cb361124d15801c23824ffc03ff23`, reviewed on
2026-09-04 (America/Chicago). They are not assertions about a later `main`.

```text
configs/examples/
└── README.md
```

The direct directory response and non-truncated recursive `configs/` Git tree
agree: one tracked file, no child directories, no configuration payload. This
closes the v0.2 uncertainty about differently named **tracked** examples at this
commit. Ignored, untracked, external, and other-branch files are not inventoried.

### Current maturity

| Surface | Confirmed at the snapshot | Not established by that evidence |
|---|---|---|
| Configuration examples | README only; no payload to bind. | Runtime loader, precedence, schema binding, deployment use. |
| Parent configuration guidance | Root README v0.5 includes a pinned tracked inventory. | Currentness of every historical child-version/count claim. |
| Adjacent templates | Template README v0.3 distinguishes placeholder structures from live instances. | Template compatibility or automatic copying into this lane. |
| Review routing | CODEOWNERS maps `/configs/` to `@bartytime4life`. | Specialist appointment, independent approval, required review. |
| Repository hygiene | Pre-commit source lists syntax, private-key, conflict, and whitespace checks. | Hook installation/execution, broad credential detection, semantic config validation, CI enforcement. |
| Security guidance | `SECURITY.md` and `docs/security/SECRETS.md` are present. | Availability of a private reporting channel or a tested incident procedure. |

README-only is a finding about this directory, not a claim that all KFM examples,
configuration, or validation tooling are absent. No exhaustive consumer scan or
hosted/runtime verification is claimed.

## What belongs here

Small, shared configuration illustrations and tightly coupled explanatory notes.
Examples may show safe mock values, reference-by-name fields, expected shape,
units, path relativity, replacement requirements, and compatibility limits for a
named consumer. Future files and naming patterns below remain **PROPOSED**.

Do not add an orphan payload merely to make the directory appear implemented.
An inactive example can be drafted before production approval; supported-use
claims require the corresponding consumer evidence. Additional validation or
migration notes need a concrete purpose and established placement, not a new
parallel contract or policy home.

## What does NOT belong here

| Material | Boundary or owning responsibility |
|---|---|
| Credentials, cookies, private keys, signed URLs, private endpoints, operator values | External protected configuration/secret handling; never a committed example. |
| Schema definitions, semantic contracts, executable policy, admission decisions | Their existing schema, contract, policy, and source-governance homes. |
| Application code, runtime adapters, infrastructure, durable pipeline definitions | The named implementation, runtime, infrastructure, or pipeline-specification owner. |
| Real source data, restricted geometry, private person/DNA/land records | Governed lifecycle and sensitivity handling; synthesize rather than copy. |
| Registry instances, receipts, proofs, catalog/triplet records, release decisions | Existing accountability, identity, projection, and release lanes; no instance authority here. |
| Invalid test corpora and expected-result datasets | Explicit fixture/test ownership, not an unowned example corpus. |
| Multi-step demonstrations and walkthrough assemblies | Root `examples/`; incidental configuration does not change that responsibility. |
| Build outputs, caches, reports, public API payloads or map assets | Their reviewed output/lifecycle homes. `artifacts/` is not a general-purpose escape hatch. |

## Inputs

### Current input

Documentation and pinned repository evidence. There is no tracked example
payload or verified loading interface in this lane.

### Future admissible inputs

Use a named consumer interface, applicable contract/schema, reviewed safe
default, migration need, or clearly synthetic design scenario. Distinguish a
verified interface from a proposal. Do not infer fields from filenames or generic
framework conventions, and do not import real deployment values as examples.

### Required provenance for authoring

Record the consumer and version/commit, illustrated scope, parser, applicable
schema/contract, replacements, validation method, reviewer role, and uncertainty.
Keep model identity and final artifact hashes in the established
`data/receipts/generated/` provenance lane when required by the contribution
contract, not in a new receipt sidecar here. A receipt is process memory, not
approval or proof of consumption.

## Outputs

Reviewable illustrations, explanatory notes, and explicitly qualified validation
or migration instructions. No effective runtime configuration, resolved secret,
policy decision, lifecycle record, release decision, or public product is emitted
by this lane.

Copying an example creates a separate destination artifact. Its destination
owner, validation, access controls, and lifecycle requirements apply. Copying,
renaming, merging, or parsing does not promote the example into authority.

## Validation

### Validation matrix

| Check | Required evidence for a future supported example | Current posture |
|---|---|---|
| Syntax and types | Actual parser; explicit units, strings, dates, and format version. | No payload here. Shared syntax hooks are configured. |
| Schema and known keys | Applicable versioned schema; required/unknown/deprecated fields tested. | No lane-specific binding established. |
| Consumer compatibility | Named loader exercised with expected positive and negative outcomes. | UNKNOWN; no executed loader proof. |
| Secret and sensitive-value review | Applicable scanner plus manual review; synthetic detection cases. | `detect-private-key` is configured, not evidence of comprehensive secret scanning. |
| Side-effect isolation | No real credentials, source requests, service start, public bind, or writes outside isolated scratch storage. | Required for future example tests; not proven by a label. |
| Navigation and provenance | Resolvable links, exact source/version, final hashes, and explicit limits. | Verify for each change; not inherited from an older result. |
| Hosted enforcement | Exact-head job result and applicable required-check evidence. | NOT ESTABLISHED by this documentation review. |

The inspected [pre-commit configuration](../../.pre-commit-config.yaml) includes
`check-json`, `check-toml`, `check-yaml`, `detect-private-key`, conflict checks,
and text hygiene. It explicitly introduces no Ruff, Mypy, ESLint, or Markdownlint
profile. Its YAML hook permits multiple documents; each consumer still needs its
own supported-format and duplicate/unknown-key rules.

### Minimum manual review

Confirm the correct lane and named consumer; proposed versus verified fields;
placeholder and network behavior; version/schema references; syntax and key
handling; absence of confidential values; explicit validation limits; and a
recoverable prior version. Changes to defaults can be behavior-significant even
when only documentation changes.

### Validation is not activation

Syntax, schema, consumer compatibility, security review, operational readiness,
and release are separate claims. Report only the level actually checked. A
successful check does not prove that a source is admitted, a setting is suitable,
an endpoint is reachable, a runtime is deployed, or publication is authorized.

## Review burden

README maintenance needs configuration/documentation review. Future payloads
also need the named consumer owner; secret-reference or network changes need
security review; policy-significant defaults and sensitive-domain examples need
the appropriate policy, domain, sensitivity, and release reviewers.

[CODEOWNERS](../../.github/CODEOWNERS) confirms the repository route, not those
specialist appointments or an approval. Follow current
[contribution and delivery controls](../../CONTRIBUTING.md); authoring, validation,
draft delivery, readiness, approval, and merge remain distinct transitions.

## Related folders

| Surface | Why to use it |
|---|---|
| [Parent configuration root](../README.md) | Shared non-secret configuration boundary and responsibility split. |
| [Templates](../templates/README.md) | Replacement-oriented structures, not automatically valid instances. |
| [Local](../local/README.md), [development](../dev/README.md), [test](../test/README.md) | Environment-specific guidance; these links do not certify consumers. |
| [Domain configuration](../domains/README.md), [MapLibre configuration](../maplibre/README.md) | Their specific constraints and separately bounded maturity. |
| [Worked examples](../../examples/README.md) | Demonstrations and complete synthetic flows. |
| [Secrets guidance](../../docs/security/SECRETS.md), [security policy](../../SECURITY.md) | Secret exclusion and private-first disclosure; operational contacts remain qualified there. |

Contracts, schemas, policy, fixtures, tests, implementation, data, and release
retain the responsibilities summarized in [Authority level](#authority-level).
This README creates no additional home in those roots.

## ADRs

ADR-0029 resolves Directory Rules adoption and placement authority. It does not
create a universal example schema, a loader, or precedence rules. No such
consumer-binding decision is established by this review.

A new root or authority transfer, competing contract/schema home, material path
alias, or cross-consumer precedence change requires the applicable decision and
migration process. Routine same-path wording does not need a new ADR. This
revision changes no accepted decision and does not authorize live bindings.

## Last reviewed

**2026-09-04 (America/Chicago)**, against the commit in [Status](#status).
Review again when this directory gains a payload, a consumer changes, linked
schema/policy rules change, security guidance changes, or later source evidence
contradicts a snapshot claim. A document date is not a support window or freshness
guarantee.

## Evidence basis

All GitHub paths in this table were read or inventoried at the pinned base.
Relative links navigate the repository revision being viewed; immutable blob/tree
identities below delimit this observation.

| Evidence | Identity | Supports and limits |
|---|---|---|
| Prior target README | `c040064e4aea09e4e87658faf37f57b4e13a96f8` | v0.2 lineage and exact documentation rollback bytes. |
| `configs/examples/` Git tree | `6142daba31066b52fc74224a3bcaee155dd2d9e0` | One tracked README; no child directories or payloads. |
| Parent README | `a800983eac7582a84e9dd82bc7d4baf04f552ad8` | Configuration responsibility and existing pinned inventory; not a live census. |
| Templates / root examples READMEs | `7a0d642589a6d622929f4e67fa77b9cbb209fe2e` / `749dfd2f387589f8ef1edd639a13f066eb2d2958` | Distinct authoring responsibilities; no consumer proof inferred. |
| Directory Rules / ADR-0029 | `fd49a0b83e55cef52c1124281f093e263526898d` / `a4de0d7a96b78da59cfc499d1025e1508afd8dd9` | Adopted placement rules; not runtime behavior. |
| CODEOWNERS / pre-commit source | `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` / `6469441400941d8ecbf6cb36f98601befe6abd7b` | Review routing and configured hooks; not execution or enforcement. |
| Secrets guidance / security policy | `562b654e101ca3c52e32b85f7acdaea9f589ab5c` / `038a7d7c2b306480fc1b82aa3719d902d8105b3d` | Secret exclusion and qualified disclosure guidance; not an incident drill. |
| `.gitignore` | `50e0e0e2485e6dbd6b7e1c2767350b459335b22b` | Declared local exclusions; not access control or safe handling of tracked history. |

### Evidence conflicts and drift signals

The July v0.2 parent-inventory uncertainty is outdated: the current parent already
contains a commit-pinned inventory. Its historical counts need not be rewritten
merely to refresh this child. CODEOWNERS coverage is now confirmed, while
specialist stewardship and independent approval remain unresolved.

The old `docs/runbooks/SECRET_LEAK_RUNBOOK.md` target returned **Not Found** at
this base. It is no longer presented as a working link. Use the verified security
entrypoint above without inventing a contact, completed runbook, or reporting
capability. Existing secrets prose also contains historical proposal labels;
neither its age nor its presence establishes operational readiness.

The Drive *Directory Rules* document was read as responsibility-root lineage;
accepted GitHub doctrine governs this update. Notion search supplied coordination
context, not target implementation or approval evidence. No source document was
changed. No full checkout, native repository validator result, hosted check,
secret-scanning completeness, or runtime behavior is asserted here.

## Configuration lane distinctions

| Material or question | Appropriate responsibility |
|---|---|
| Shared illustrative values for a named configuration interface | `configs/examples/`. |
| Reusable replacement placeholders | `configs/templates/`. |
| Shared local/development/test defaults or guidance | The relevant existing `configs/` sublane. |
| One application's operational configuration | Its application owner, referencing shared defaults where appropriate. |
| Multi-step demonstration with incidental configuration | Root `examples/`. |
| Deterministic valid/invalid cases proving behavior | Existing fixture/test lanes. |
| Durable declarative pipeline run | `pipeline_specs/`, not a configuration example. |
| Deployment/exposure wiring or protected real values | Infrastructure and approved external protected systems. |

### Example versus template

An example uses concrete mock values to explain a concept; a template makes
replacement obligations prominent. Neither is automatically accepted input.
These snippets illustrate the distinction only; `service` and its keys are not
an implemented KFM interface:

```yaml
# Illustrative example only; no consumer or network enforcement is established.
service:
  mode: "mock"
  endpoint: "https://example.invalid"
```

```yaml
# Illustrative template only; interpolation is NOT established.
service:
  mode: "<REQUIRED_MODE>"
  endpoint: "${SERVICE_ENDPOINT}"
```

Do not copy the second block into a live loader and assume substitution occurs.
A mock mode or illustrative hostname is not a sandbox: the test harness must
separately prevent real egress and side effects.

## Proposed example-file contract

Prefer a short adjacent explanation naming the consumer, status, version,
validation, and replacements. The earlier header concept remains **PROPOSED**:

```yaml
# Documentation convention only, not an accepted consumer schema.
kfm_example:
  example: true
  authority: "non_authoritative_config_example"
  consumer_ref: "<VERIFIED_CONSUMER_OR_EXPLICIT_PROPOSAL>"
  consumer_version: "<COMMIT_OR_NEEDS_VERIFICATION>"
  schema_ref: "<ACCEPTED_SCHEMA_OR_EXPLICIT_GAP>"
  validation_ref: "<VERIFIED_CHECK_OR_NOT_RUN>"
  network_posture: "no_network_by_default"
  lifecycle_effect: "none"
  release_effect: "none"
```

Do not inject this extra object into a consumer's configuration unless its schema
and parser explicitly support it. For strict JSON or closed schemas, document the
same facts outside the machine payload; do not weaken the schema to fit metadata.

### Required semantic fields

Identify consumer, bounded scope, version/commit, authority references,
replacement fields, secret-reference mechanism, validation method, side effects,
reviewer role, and migration/sunset condition where applicable. Unknowns remain
explicit. These are documentation requirements, not newly adopted field names.

## Placeholder and secret handling

### Acceptable values

Use unmistakable markers such as `<REQUIRED_VALUE>`, `REPLACE_ME_NON_SECRET`,
`mock-source-id`, or `example.invalid`. A reference such as `${VARIABLE_NAME}`
illustrates a name only; actual expansion belongs to a verified consumer. Use
symbolic scratch paths rather than personal absolute paths. Public verifier
material must be intentionally public and documented, not inferred safe by shape.

### Forbidden values

Real credentials, authorization headers, private keys, usable password material,
session cookies, signed links, connection strings with credentials, internal
hosts, operator addresses, confidential bucket/tenant/project identifiers,
personal data, restricted geometry, and copied cloud/SSH/kubeconfig material.
Do not reproduce secrets or restricted details even as negative examples.

### Reference-by-name rule

A conceptual field such as `token_env: "UPSTREAM_TOKEN"` demonstrates a reference,
not the token value and not an implemented secret resolver. Never print resolved
values to validation output, logs, AI context, reports, maps, or public clients.

[`.gitignore`](../../.gitignore) excludes `.env`, `.env.*`, and `configs/local/*`,
with exceptions for `.env.example` and the local README. These source rules do
not remove already tracked content, prevent disclosure, or prove any particular
local file safe. Do not `source` an example or treat an ignore match as permission
to put confidential data in diagnostics or commits.

### Leak response

Use [Security policy](../../SECURITY.md) for private-first disclosure and the
[secrets guidance](../../docs/security/SECRETS.md) for the governing boundary.
Contain use and revoke/rotate exposed credentials through authorized channels;
preserve a redacted incident record; inspect propagation; and use reviewed
remediation. Do not repeat the secret in public issues, PRs, screenshots, or
receipts. Private-channel availability and incident-drill completion remain
**NEEDS VERIFICATION**. A normal documentation revert does not revoke a secret.

## Consumer binding and precedence

No example consumer, auto-loader, merge order, interpolation, secret resolution,
or reload behavior is established by this review. The required posture is
non-active authoring, not a claim that every possible consumer has been audited.

### Required precedence documentation

For each future supported example, identify the actual loader, relative-path
base, allowed inputs/includes, version, override sources, order, permitted keys,
secret-resolution boundary, reload behavior, and error/rollback outcome. Verify
with the consumer's tests; do not publish one speculative global ordering.
Policy, rights, sensitivity, evidence, and release constraints are not override
sources an operator or public client may weaken.

### Fail-closed posture

Missing required files, unknown or deprecated keys, duplicate keys, unsupported
versions, unresolved substitutions, unsafe endpoints, malformed values, or
conflicting inputs must produce a bounded error or disabled state under the
consumer contract. Never silently guess aliases, ignore unsafe fields, partially
apply configuration, expose unresolved secrets, or activate a permissive fallback.
These are requirements for future consumers, not proven behavior of this lane.

## File format and naming posture

### Proposed names

`<consumer>.<scope>.example.yaml`, `.example.json`, `.example.toml`, or an
explicitly justified `.env.example` / INI / CFG form are candidate conventions,
not existing files or a repository-wide naming decision. Pick only the format
actually supported by the named consumer. Keep app-only configuration with its
owner and resolve duplicate homes before adding aliases.

### File-level requirements

UTF-8, LF, final newline, parser-valid comments, no duplicate keys, explicit
units/time zones/path relativity, deterministic values where practical, and no
personal machine paths. Advanced aliases, includes, substitutions, executable
expansion, or parser-specific features require explicit interface and test
coverage; they are not harmless because a file is called an example.

### Unsafe ambiguity examples

A bare `timeout: 10` does not establish units, and YAML scalar interpretation
alone does not establish consumer semantics. A clearer illustrative form is:

```yaml
# Illustrative fields only; consumer/schema compatibility is not claimed.
enabled: false
timeout_seconds: 10
effective_date: "2026-07-13"
```

The date is an example string, not a currentness assertion. `enabled: false` is
not an enforced disable mechanism until the actual loader implements it.

## Negative examples and fixtures

Explain unsafe states in prose or unmistakably labeled synthetic snippets.
Executable rejection cases belong with their fixture/test owner. Test missing
and unknown fields, duplicate keys, unsupported versions, unresolved references,
network denial, safe logging, and invalid overrides where relevant. Synthetic
scanner patterns must be controlled fixtures, never genuine credentials or
secret-looking filler copied into a user-facing example.

## Safe change pattern

Start with one existing consumer and one bounded configuration question. Inspect
its actual interface and choose the correct lane. Author from documented shape,
not deployment copies. Validate syntax, applicable schema/keys, and isolated
consumer behavior where supported; perform sensitive-value review; preserve
compatibility and rollback; and update the tracked inventory only after the file
exists. Record `NOT RUN` and explicit design gaps rather than inventing support.

### Anti-patterns

Do not equate `.example` with exclusion from loading; a placeholder with secret
safety; parsing with operational readiness; configuration with policy; a passing
unrelated workflow with validation; a copied template with a released instance;
or a static README with evidence of a loader. Do not create additional authority
homes merely to satisfy an example's preferred path.

## Rollback and correction posture

### Exact rollback target

The documentation rollback target for v0.3 is prior README blob
`c040064e4aea09e4e87658faf37f57b4e13a96f8` at the pinned base. Restore it through a
reviewed, non-force correction if necessary, preserving the new authoring receipt
as history. The older v0.1 blob in v0.2 is lineage, not this update's rollback target.

### Rollback triggers

Correct or roll back claims of unverified inventory, consumers, ownership,
validation/enforcement, live bindings, security contacts, schema/policy authority,
or publication readiness. Also correct broken navigation, lost safety guidance,
or examples that could be mistaken for real operational inputs.

### Correction discipline

Prefer a focused forward correction when restoring v0.2 would reintroduce known
stale statements and the broken runbook reference. Preserve auditable history;
do not reset shared branches. Documentation rollback changes no runtime, secret,
source, release, or deployed environment and cannot repair an actual disclosure.

## Verification backlog

| Item | Current disposition | Next evidence needed |
|---|---|---|
| Tracked inventory | CONFIRMED: README only at the pinned tree. | Recheck when this directory changes. |
| Parent inventory and review route | CONFIRMED source evidence. | Refresh only materially stale parent claims; verify specialist assignments separately. |
| First real example | PROPOSED; none added. | Named consumer, scope, safe values, version, validation, and rollback. |
| Naming and example metadata | PROPOSED documentation conventions. | Per-consumer/per-root decision; no unsupported in-band keys. |
| Loader, precedence, substitutions, reload | UNKNOWN. | Implementation and isolated positive/negative tests. |
| Schema/key checks and no-side-effect validation | NEEDS VERIFICATION. | Exact supported interface, fixtures, commands, and results. |
| Secret scanning and hosted enforcement | PARTIAL source evidence only. | Scanner breadth, safe test cases, exact-head execution, and applicable required checks. |
| Missing secret-leak runbook / private channel | NEEDS VERIFICATION. | Reviewed current procedure and verified private reporting route; no invented replacement. |
| Correction propagation and drills | NEEDS VERIFICATION. | Consumer-specific rollback and safe operational evidence. |

## Definition of done

For this documentation update: exact tracked inventory, corrected authority and
routing claims, explicit validation limits, resolving navigation, preserved
section anchors, an exact rollback target, and hash-bound authorship provenance.

Before a future example is called **supported**, establish its consumer and
version; applicable schema or explicit absence; no secret/live/sensitive values;
syntax and key handling; isolated no-network/no-side-effect tests; reviewer
responsibility; compatibility and precedence; correction/sunset/rollback; and
truthful exact-head results. Inactive drafts may carry unresolved non-safety
questions without claiming any of those later gates passed.

**A configuration example teaches an interface. It does not authorize its use.**

[Back to top](#top)
