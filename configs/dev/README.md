<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-dev-readme
title: configs/dev/ — Governed Development Configuration Boundary
type: readme
version: v0.3
status: draft
owners: OWNER_TBD — Config steward · Security steward · Developer-experience steward · Consumer owner(s) · Validation steward · Ops steward · Docs steward
created: 2026-06-16
updated: 2026-07-13
policy_label: public; config-sublane; development; commit-safe; non-secret; non-authoritative; no-live-binding; no-runtime-authority; no-deployment-authority
current_path: configs/dev/README.md
truth_posture: CONFIRMED repository-present README lane at the pinned base, parent configs root contract, sibling examples/local/templates/test boundaries, Directory Rules placement doctrine, repository secrets doctrine, current CODEOWNERS fallback, prior README lineage, repository search result scoped by returned path, and named conventional-path probes / PROPOSED development-config file contract, precedence documentation contract, naming convention, validation matrix, review workflow, and minimum safe development slice / UNKNOWN exhaustive recursive inventory, differently named files, consumer loaders, merge order, environment substitution, schema bindings, validators, secret-scanning enforcement, CI requirements, deployment integration, accepted owners, and runtime behavior
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: b6bcc4cd27dc8c0fa1f74aa5b989cb3240e90aa8
  prior_blob: d9b6a87289fe60370f9e849954c9cccb6ece57b1
  path_search_result: README.md only
  named_absence_probes:
    - configs/dev/dev.yaml
    - configs/dev/.env.example
    - configs/dev/local.template.yaml
    - configs/dev/validation.md
related:
  - ../README.md
  - ../examples/README.md
  - ../local/README.md
  - ../templates/README.md
  - ../test/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/security/SECRETS.md
  - ../../docs/runbooks/FIRST_GOVERNED_PR_RUNBOOK.md
  - ../../schemas/contracts/v1/
  - ../../contracts/
  - ../../policy/
  - ../../apps/
  - ../../packages/
  - ../../pipelines/
  - ../../pipeline_specs/
  - ../../runtime/
  - ../../infra/
  - ../../tests/
  - ../../fixtures/
  - ../../tools/
  - ../../.github/CODEOWNERS
  - ../../.github/PULL_REQUEST_TEMPLATE.md
tags: [kfm, configs, dev, development, local-defaults, templates, placeholders, non-secret, commit-safe, config-validation, consumer-binding, precedence, portability, governance]
notes:
  - "At the pinned base, a repository search for `configs/dev` returned this README as the only result located inside that directory; other results were references from outside the lane. Exact probes for dev.yaml, .env.example, local.template.yaml, and validation.md returned Not Found. These are bounded findings, not an exhaustive recursive tree receipt."
  - "configs/dev/ is distinct from configs/examples/, configs/local/, configs/templates/, configs/test/, root examples/, fixtures/, runtime/, and infra/."
  - "A development config is candidate input for a named local-development consumer. It is not a schema, policy, contract, deployment binding, secret store, runtime state, release decision, lifecycle object, test fixture, generated artifact, or proof of consumption."
  - "The repository secrets standard forbids real secrets even when labeled test or local. Only references-by-name, public verifier material, obvious placeholders, and clearly mock values are acceptable."
  - "The repository secrets standard references a secret-leak runbook path that was not present at the pinned base. Incident-response procedure therefore remains NEEDS VERIFICATION; do not invent a path or delay credential rotation."
  - "Only this README and its required GENERATED_RECEIPT are changed. No development config payload, consumer, loader, schema, contract, policy, validator, test, workflow, secret-scanning rule, deployment binding, runtime behavior, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Development Configuration

> `configs/dev/` is the development-configuration sublane under `configs/`. It may provide safe, reviewable defaults and templates for local development, but it does not create runtime behavior, deployment authority, schema authority, policy authority, secret material, release state, or operational truth.

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.3`  
> **Observed lane maturity:** README-only at the inspected repository search and named conventional-path probes  
> **Owning responsibility root:** `configs/` — safe, non-secret configuration defaults and templates  
> **Authority:** development-configuration documentation and candidate defaults only  
> **Default posture:** safe to review, not safe to assume consumed  
> **Public-path posture:** no public client, search index, export, map surface, or AI surface should read this lane as a truth source

> [!CAUTION]
> Never commit a real credential, token, password, private key, cookie, signed URL, private endpoint, restricted identifier, operator-specific path, production hostname, sensitive source detail, or deployment-only value here. A development file that contains a real secret is a security incident, not a harmless local convenience.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Lane distinctions](#configuration-lane-distinctions) · [Allowed](#what-belongs-here) · [Forbidden](#what-does-not-belong-here) · [File contract](#proposed-development-config-file-contract) · [Secrets](#placeholder-and-secret-handling) · [Consumers](#consumer-binding-and-precedence) · [Naming](#file-format-and-naming-posture) · [Overrides](#local-override-and-portability-posture) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Change pattern](#safe-change-pattern) · [Migration](#migration-and-drift-posture) · [Rollback](#rollback-and-correction-posture) · [Evidence](#evidence-basis) · [Backlog](#verification-backlog) · [Done](#definition-of-done)

---

## Purpose

`configs/dev/` exists to reduce local-development ambiguity without weakening KFM's responsibility roots or trust membrane.

A useful development config should make it easier to:

- start or inspect a local development workflow;
- understand which values are configurable;
- see safe development defaults and explicit placeholders;
- identify the intended app, package, pipeline, pipeline spec, runtime adapter, test, or tool;
- find the owning schema or semantic contract when one exists;
- find a validation command or an explicit `NEEDS VERIFICATION`;
- understand which values must be supplied outside the repository;
- understand failure behavior when required values are missing;
- remove or supersede the config without creating hidden runtime drift.

A file in this lane is only a **candidate input** until a current consumer, loader, schema, test, and precedence rule establish how it is used.

[Back to top](#top)

---

## Authority level

**Configuration sublane / non-authoritative development input.**

| Concern | Authority status | Determination |
|---|---:|---|
| Folder placement | **CONFIRMED** | The path exists under `configs/`, whose parent README identifies that root as the home for safe non-secret defaults and templates. |
| Development defaults | **PROPOSED UNTIL CONSUMED** | A committed default may be documented here, but current code or pipeline evidence must establish that a consumer actually reads it. |
| Current inventory | **BOUNDED README-ONLY FINDING** | The returned search results contained this README as the only file located inside `configs/dev/`; four common candidate paths were absent at named probes. Differently named or unindexed files remain `UNKNOWN`. |
| Consumer behavior | **UNKNOWN** | No loader, import, merge order, environment substitution, or runtime precedence is established by this README. |
| Machine shape | **NOT OWNED HERE** | Machine-checkable shape belongs under the accepted `schemas/` authority. |
| Semantic meaning | **NOT OWNED HERE** | Object and field meaning belongs under `contracts/` or the verified consumer contract. |
| Policy | **NOT OWNED HERE** | Allow, deny, restrict, redact, or abstain behavior belongs under `policy/`. |
| Deployment binding | **NOT AUTHORIZED** | Production, staging, private-network, and operator-specific binding belongs outside this lane. |
| Secret safety | **CONFIRMED DOCTRINE / ENFORCEMENT UNKNOWN** | Real secrets are forbidden in the repository; automated enforcement coverage remains `NEEDS VERIFICATION`. |
| Runtime truth | **NOT ESTABLISHED** | Parsing a file does not prove that a runtime uses it correctly. |
| Release/publication | **NOT APPLICABLE** | This lane cannot authorize KFM publication or become a public data surface. |

A development config can point to authority. It cannot become authority by convenience, repetition, or successful parsing.

[Back to top](#top)

---

## Status

### Bounded repository snapshot

At base commit `b6bcc4cd27dc8c0fa1f74aa5b989cb3240e90aa8`, the directly verified lane is:

```text
configs/dev/
└── README.md
```

A repository search for `configs/dev` returned this README as the only result located inside the directory; other returned files referenced the lane from elsewhere. Exact probes returned `Not Found` for:

```text
configs/dev/dev.yaml
configs/dev/.env.example
configs/dev/local.template.yaml
configs/dev/validation.md
```

These are bounded absence statements for named paths and indexed search results—not a recursive filesystem receipt. Differently named files, ignored files, generated files, branch-only work, or unindexed content remain `UNKNOWN`.

### Current maturity

| Capability | Status | Safe conclusion |
|---|---:|---|
| README boundary | **CONFIRMED** | The lane has a documented responsibility boundary. |
| Development config payloads | **NOT ESTABLISHED** | No actual dev configuration payload was verified in the inspected evidence. |
| Named consumers | **NOT ESTABLISHED** | No app, package, pipeline, runtime, test, or tool is bound here by current evidence. |
| Config loader | **NOT ESTABLISHED** | Do not infer auto-loading, discovery, imports, overlay order, or environment expansion. |
| Schema validation | **NOT ESTABLISHED** | No lane-specific schema binding or validator was verified. |
| Secret scanning | **NEEDS VERIFICATION** | Doctrine forbids secrets; repository automation coverage was not established. |
| Test/CI enforcement | **NEEDS VERIFICATION** | No lane-specific executable check or passing proof was verified. |
| Deployment integration | **UNKNOWN** | Nothing here establishes production, staging, review, or operator binding. |
| Accepted ownership | **OWNER_TBD** | Current CODEOWNERS provides a repository-wide fallback, not a verified config-specific steward. |
| Publication impact | **NONE BY DESIGN** | This README update does not create or promote a published artifact. |

[Back to top](#top)

---

## Configuration lane distinctions

The `configs/` sublanes should remain distinguishable by responsibility.

| Lane | Primary responsibility | Must not silently become |
|---|---|---|
| `configs/dev/` | Safe defaults and templates intended for development workflows | Local override store, test fixture home, deployment binding, or runtime authority |
| `configs/local/` | Commit-safe local configuration templates and setup notes | Personal workstation state or committed local override values |
| `configs/templates/` | Reusable, consumer-neutral or consumer-named configuration templates | Schema authority, implementation code, or deployment state |
| `configs/examples/` | Illustrative configuration examples for a named consumer | Automatically loaded defaults, fixtures, or proof of supported behavior |
| `configs/test/` | Test-runner and test-environment configuration defaults/templates | Test suite, fixture corpus, policy tests, or CI authority |
| `fixtures/` | Valid, invalid, and golden machine-test inputs | Human setup examples or runtime defaults |
| root `examples/` | Worked examples, walkthroughs, and runnable assemblies | Automatically loaded configuration authority |
| `runtime/` | Local adapters and harnesses | Config-template storage or public model surface |
| `infra/` | Deployment, host, network, exposure, and access-control definitions | General development defaults or secret values |
| `pipeline_specs/` | Durable declarative pipeline definitions | Merely illustrative or local-only config snippets |

When a file could fit more than one lane, classify it by its **primary responsibility**, split mixed responsibilities, and record migration impact rather than creating a duplicate.

[Back to top](#top)

---

## What belongs here

This lane may contain only development configuration and tightly coupled explanatory notes that are safe to commit.

| Accepted material | Purpose | Required posture |
|---|---|---|
| `*.dev.yaml` / `*.dev.yml` | Development defaults for a named consumer | Parseable, non-secret, consumer named, precedence documented or `NEEDS VERIFICATION` |
| `*.dev.json` | Strict JSON development configuration | Valid JSON; schema reference or `NEEDS VERIFICATION`; no comments disguised as JSON |
| `*.dev.toml` | TOML development defaults | Consumer and parser named; portability reviewed |
| `*.dev.ini` / `*.dev.cfg` | Tool-specific development settings | Consumer and format version named |
| `.env.example` | Environment-variable names and obvious placeholder/reference values | No real values; never automatically treated as a secret source |
| `*.template.*` | Placeholder-based development template | Replacement requirements and local-only handling documented |
| `README.md` | Lane contract, evidence boundary, review guidance, and inventory | Truth-labeled and current |
| `validation.md` | Human validation instructions | Commands verified or labeled `PROPOSED`; no false CI claims |
| `MIGRATION.md` | Temporary key/path compatibility guidance | Review-linked, reversible, and retired when migration closes |
| Small public-safe mock values | Explain one development configuration concern | Synthetic, non-sensitive, and not a source payload or fixture authority |

Each non-trivial config should be self-describing enough that a reviewer can determine the consumer, authority references, override method, validation path, and safe failure posture without guessing.

[Back to top](#top)

---

## What does NOT belong here

| Prohibited material | Why prohibited | Correct home or action |
|---|---|---|
| Real secrets, tokens, keys, passwords, cookies, signed URLs, or private endpoints | Repository is not a secret store | External secret manager or approved deployment system; rotate and invoke incident response if committed |
| Production, staging, or operator-specific live values | Creates accidental deployment authority and exposure risk | Environment-specific deployment controls outside this lane |
| Personal workstation paths, usernames, home directories, drive letters, device IDs | Leaks local identity and creates non-portable config | Uncommitted local override or symbolic placeholder |
| Schema definitions | Config defaults cannot own machine shape | `schemas/contracts/v1/` or accepted schema home |
| Semantic contracts | Config defaults cannot own object meaning | `contracts/` |
| Policy rules or allow/deny decisions | Config cannot authorize behavior | `policy/` |
| Application or package source code | Config lane is not implementation | `apps/` or `packages/` |
| Pipeline implementation | Config lane is not executable processing | `pipelines/` |
| Durable pipeline specifications | Reusable pipeline definitions are not dev defaults | `pipeline_specs/` |
| Runtime adapters, model adapters, harnesses, service definitions | Config lane cannot become runtime authority | `runtime/` |
| Deployment, network, firewall, proxy, or access-control definitions | Config lane cannot own operational exposure | `infra/` |
| Source payloads, API responses, rasters, vectors, scans, exports | Config lane is not a lifecycle data lane | Governed `data/raw/`, `data/work/`, or `data/quarantine/` as applicable |
| Registry rows, `SourceDescriptor`s, receipts, proofs, catalog/triplet records | Config defaults cannot become canonical trust objects | Their owning `data/` or `control_plane/` homes |
| Release manifests, promotion decisions, correction notices, rollback cards | Config cannot approve or record release | `release/` |
| Generated reports, screenshots, exports, caches, build products | Config lane is not an artifact home | `artifacts/` or ignored workspace as appropriate |
| Valid/invalid machine-test corpora | Test inputs require deterministic expected outcomes | `fixtures/` and `tests/` |
| Sensitive locations, living-person data, DNA, private parcel joins, proprietary identifiers | Unnecessary for development configuration and may cause harm | Synthesize, generalize, redact, quarantine, restrict, or deny |
| Public UI or AI content | Config files are not public claims | Governed API and released evidence surfaces only |

This lane must not become a quiet parallel home for any trust-bearing object family.

[Back to top](#top)

---

## Proposed development-config file contract

Every substantive future file in `configs/dev/` should carry the following information in a header, adjacent README table, or verified manifest.

| Field | Requirement | Example posture |
|---|---|---|
| `config_id` | Stable identifier or path-derived name | `kfm-dev-governed-api` |
| `status` | `PROPOSED`, `NEEDS VERIFICATION`, or verified lifecycle state | Do not label `active` without consumer evidence |
| `intended_consumer` | Exact app/package/pipeline/runtime/test/tool path or identifier | `apps/governed-api` |
| `consumer_version` | Commit, package version, or `NEEDS VERIFICATION` | Prevents stale examples from looking current |
| `format` | YAML, JSON, TOML, dotenv example, INI, or other parser format | Name the parser when non-obvious |
| `schema_ref` | Owning schema path/URI or `NEEDS VERIFICATION` | Reference; do not copy schema authority |
| `contract_ref` | Semantic contract path when one exists | Reference; do not redefine meaning |
| `policy_ref` | Relevant policy path when configuration can affect exposure or access | Reference; config cannot authorize |
| `precedence` | Where this file sits in a verified merge/load order | Otherwise say `NEEDS VERIFICATION` |
| `required_overrides` | Values that must be supplied outside the repository | Prefer references-by-name |
| `safe_defaults` | Why committed values are harmless and development-only | No live endpoint or credential |
| `validation` | Verified command/test or `NEEDS VERIFICATION` | Distinguish syntax from consumer compatibility |
| `failure_mode` | Behavior when values are absent, invalid, or unresolved | Fail closed where risk matters |
| `owner` | Config steward plus consumer owner | `OWNER_TBD` until accepted |
| `last_verified` | Date and evidence reference | Not merely last edited |
| `supersedes` | Replaced file/key/version when applicable | Preserve migration lineage |
| `removal_condition` | When the file can be deleted or archived | Prevents indefinite compatibility residue |

A file that cannot identify a consumer and safe failure posture should remain a proposal or move to `configs/examples/` rather than pretending to be an operational default.

[Back to top](#top)

---

## Placeholder and secret handling

### Allowed representation patterns

| Pattern | Use | Example |
|---|---|---|
| Reference-by-name | Consumer resolves a secret outside the repository | `${KFM_SOURCE_API_KEY}` |
| Obvious placeholder | Human must replace locally | `<REPLACE_WITH_LOCAL_VALUE>` |
| Clearly mock value | Parser/demo needs a harmless value | `example.invalid`, `00000000-0000-0000-0000-000000000000` |
| Public verifier material | Public key or non-secret verification identifier | Only when publication is intentional and documented |
| Loopback binding | Local-only endpoint where safe | `127.0.0.1:<LOCAL_PORT>` with consumer review |
| Relative repo path | Portable non-sensitive file reference | Avoid personal absolute paths |

### Forbidden representation patterns

- copied production or staging values;
- realistic-looking tokens or credentials;
- signed URLs, cookies, bearer headers, private keys, certificates with private material;
- private DNS names, private IP addresses, internal dashboards, or privileged connection strings;
- personal home-directory paths, usernames, synced-drive paths, or device identifiers;
- sensitive source records disguised as config examples;
- commented-out secrets retained “for convenience”;
- encrypted secret blobs without an accepted encrypted-secret workflow and ADR;
- values that a browser bundle can expose as public environment variables.

### Leak response

When credential-like material is discovered:

1. stop treating the file as a harmless documentation change;
2. remove the value from the candidate diff;
3. notify the security/credential owner through the repository's approved process;
4. rotate or revoke the credential immediately when exposure is plausible;
5. assess Git history, forks, logs, caches, artifacts, and downstream copies;
6. record the correction and follow the verified incident-response procedure;
7. do not wait for documentation-path cleanup before rotation.

The current secrets standard references a dedicated secret-leak runbook, but that named path was not present at the pinned base. The procedure path is therefore `NEEDS VERIFICATION`; the duty to rotate, contain, and audit is not.

[Back to top](#top)

---

## Consumer binding and precedence

A committed development config must not imply a loading mechanism that current code does not prove.

### Required questions

- Which exact consumer reads the file?
- Does the consumer discover the file automatically or receive an explicit path?
- Is the file parsed directly, imported by another config, or converted first?
- Which environment variables may override it?
- Are overrides replacement, deep merge, shallow merge, or append?
- What is the deterministic order when multiple files define the same key?
- Are unknown keys rejected, ignored, logged, or passed through?
- Are missing required values an `ERROR`, an `ABSTAIN`, a local-only fallback, or a safe refusal?
- Can any value change exposure, rights, sensitivity, policy, publication, or public paths?
- Which test proves the documented behavior?

### Precedence rule

Until consumer evidence establishes an actual merge order, use this documentation posture:

```text
repository development config
  -> candidate defaults only
local uncommitted override
  -> operator/developer-specific values
environment or secret reference
  -> externally supplied value
deployment binding
  -> outside configs/dev/
```

This diagram is a responsibility model, not proof of a current loader or merge algorithm.

### Anti-bypass rules

| Bypass risk | Required response |
|---|---|
| Consumer silently auto-loads every file in `configs/dev/` | Document exact discovery and reject unexpected files |
| Dev config overrides policy or release state | Reject; move authority to `policy/` or `release/` |
| Browser bundle receives secret-bearing environment variables | Reject and move resolution server-side behind the trust membrane |
| Public client reads this folder directly | Reject; use governed APIs and released artifacts |
| Pipeline uses a dev default in a production run | Require explicit environment profile and deployment review |
| Missing values cause permissive behavior | Fail closed where exposure, rights, sensitivity, or publication is affected |
| Unknown keys are silently ignored | Prefer validation failure or explicit compatibility policy |
| Config key is duplicated across files without deterministic order | Define one owner and one tested precedence rule |
| Runtime behavior differs from README | Treat implementation as current behavior evidence and correct the documentation or code through review |

[Back to top](#top)

---

## File format and naming posture

Use names that communicate environment and role without implying authority.

### Preferred patterns

```text
<consumer>.dev.yaml
<consumer>.dev.json
<consumer>.dev.toml
<consumer>.template.yaml
<consumer>.env.example
validation.md
MIGRATION.md
```

### Naming rules

- Include the consumer or bounded purpose when practical.
- Use `.dev.` for a development default intended to be consumed.
- Use `.template.` or `.example` when the file is not intended for direct loading.
- Do not use names such as `production.*`, `prod.*`, `release.*`, `canonical.*`, or `approved.*` in this lane.
- Avoid ambiguous names such as `config.yaml`, `settings.json`, `default.env`, or `local.yaml` without a consumer prefix.
- Keep one format authoritative for a consumer unless compatibility requirements are documented.
- Record renamed keys and files in `MIGRATION.md` or the consumer's migration notes.
- Do not create generated copies of one config format unless a canonical source and synchronization rule are defined.

### Format rules

| Format | Minimum review |
|---|---|
| YAML | Parse test; duplicate-key policy; anchor/merge behavior; scalar coercion review |
| JSON | Strict parse; no comments; schema validation where available |
| TOML | Parse test; table/key collision review |
| dotenv example | Names only or obvious placeholders; no shell execution assumptions |
| INI/CFG | Parser and case-sensitivity behavior documented |
| Custom format | Parser, version, escaping, and validation explicitly documented |

[Back to top](#top)

---

## Local override and portability posture

Development defaults should be portable across contributor machines.

### Requirements

- Prefer relative paths, repository anchors, or explicit placeholders.
- Keep personal and machine-specific values in ignored local files or external environment variables.
- Document the expected local override filename without committing the override.
- Verify `.gitignore` behavior before instructing contributors to store local values in a named path.
- Do not assume Windows, Linux, macOS, container, or CI path semantics are interchangeable.
- Do not hard-code ports that may expose services externally; use loopback and explicit local-only notes where safe.
- Do not make privileged ports, host networking, disabled TLS, wildcard CORS, or `0.0.0.0` the default.
- Mark container-only, GPU-only, or platform-specific settings clearly.
- Keep source credentials and restricted-data paths outside the repository.
- Treat local model endpoints as runtime-adapter concerns behind governed APIs, not as browser configuration.

### Proposed override pattern

```text
configs/dev/<consumer>.dev.yaml          # commit-safe candidate defaults
<ignored-local-path>                     # real local values; path NEEDS VERIFICATION
environment references                   # secret/value injection outside repository
consumer validation                      # rejects unknown or unsafe values
```

The ignored-local path and precedence are intentionally not named here until `.gitignore` and consumer behavior are verified.

[Back to top](#top)

---

## Inputs

### Current input

The current lane consumes documentation and repository evidence only. No development payload or supported loading interface is established by the inspected repository evidence.

### Future admissible inputs

A proposed development config may be authored from:

- an existing, verified consumer's configuration interface;
- a semantic contract describing configuration meaning;
- a machine schema describing configuration shape;
- current safe defaults from code or a pipeline specification;
- a reviewed migration from an older configuration key or file;
- a minimal synthetic local-development need;
- a test or validator interface, provided the config remains outside fixture/test authority;
- an accepted ADR when the configuration affects architecture or exposure.

Do not copy a real deployment configuration and “redact a few values.” Build a clean development config from the accepted field surface and unmistakably safe values.

[Back to top](#top)

---

## Outputs

A future file in this lane may produce only:

- a commit-safe development configuration candidate;
- a human-readable description of configurable values;
- a validated syntax result;
- a consumer-compatibility result when a verified test exists;
- a migration note for development configuration;
- a local setup instruction that keeps real values uncommitted.

It must not produce or imply:

- a `SourceDescriptor`, `EvidenceBundle`, policy decision, receipt, proof, catalog record, release manifest, correction notice, or rollback card;
- a deployment, public endpoint, public client path, or released map layer;
- a secret, credential, access grant, or source activation;
- a runtime guarantee unsupported by tests;
- a KFM `PUBLISHED` state.

[Back to top](#top)

---

## Validation

Validation should be layered. Passing a lower layer does not imply a higher layer passed.

| Gate | What it checks | Current state |
|---|---|---:|
| Markdown structure | README headings, tables, fences, relative references, no truncation | **Performed for this revision** |
| Syntax parse | YAML/JSON/TOML/dotenv/custom format parses as intended | **NOT APPLICABLE — no payload changed** |
| Secret/live-binding scan | No credential-like or private operational value is introduced | **Performed on changed text; repository-wide enforcement `NEEDS VERIFICATION`** |
| Named-path probes | Common candidate files and related evidence paths checked | **Performed, bounded** |
| Schema validation | Fields satisfy the owning schema | **NOT ESTABLISHED for this lane** |
| Consumer compatibility | Current consumer accepts the file and rejects unsafe/unknown values | **NOT ESTABLISHED** |
| Precedence test | Merge/load order is deterministic and documented | **NOT ESTABLISHED** |
| Negative tests | Missing, malformed, unknown, and unsafe values fail as documented | **NOT ESTABLISHED** |
| Portability check | Paths, ports, environment references, and platform assumptions are safe | **NOT APPLICABLE — no payload changed** |
| CI enforcement | Required workflow runs and protects merge | **NEEDS VERIFICATION** |
| Runtime smoke test | Local consumer starts or safely refuses with the config | **NOT APPLICABLE — no payload changed** |
| Deployment test | Environment-specific binding works | **OUT OF SCOPE** |
| Publication gate | KFM release/promotion checks | **NOT APPLICABLE** |

### Minimum validation for a future payload

1. parse the file with the actual parser;
2. validate against the owning schema when one exists;
3. scan for secrets, private endpoints, personal paths, and live bindings;
4. run the verified consumer/config-loader test;
5. run negative tests for unknown keys, missing required values, and unsafe exposure;
6. confirm documented precedence matches implementation;
7. confirm real local values remain ignored and uncommitted;
8. document all skipped checks and why.

[Back to top](#top)

---

## Review burden

### Current routing

At the pinned base, `.github/CODEOWNERS` provides a repository-wide fallback but no config-specific path rule. Config-specific accepted owners therefore remain `NEEDS VERIFICATION`.

### Review matrix

| Change type | Minimum review |
|---|---|
| README-only clarification | Config/docs maintainer; security review when secret or exposure language changes |
| New development config payload | Config steward + exact consumer owner + validation reviewer |
| New environment variable name | Consumer owner + security review when credential or exposure related |
| New external endpoint or source binding | Security + infra + source/rights owner; likely move outside this lane |
| Config affecting public exposure, CORS, auth, data sensitivity, or location precision | Security + policy + affected domain owner; fail closed |
| Config affecting pipeline publication or release | Pipeline + release + policy owners; config cannot authorize |
| New schema or semantic meaning | Move to `schemas/` or `contracts/`; review there |
| New loader, merge order, or auto-discovery behavior | Consumer implementation review plus tests and migration notes |
| Secret discovered | Immediate security response; do not wait for ordinary docs review |

### Workflow-trigger preflight

This revision changes one README and one required generated receipt. No workflow file, executable config, policy, schema, runtime, or deployment file is changed. Repository-level push or pull-request workflows may still run. Their required-check status and branch-protection enforcement remain `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Safe change pattern

For a future change under `configs/dev/`:

1. identify the exact consumer and primary responsibility;
2. verify the path against Directory Rules and sibling config-lane boundaries;
3. confirm the file is safe development configuration rather than an example, fixture, schema, contract, policy, runtime adapter, pipeline spec, infra definition, lifecycle record, release record, or artifact;
4. start from accepted fields, not a copied live configuration;
5. replace all local/deployment values with references-by-name or obvious placeholders;
6. document consumer, parser, schema/contract references, precedence, failure mode, and override method;
7. validate syntax and consumer compatibility;
8. run secret, private-endpoint, personal-path, and unsafe-exposure review;
9. add negative tests where behavior can affect exposure or data handling;
10. update migration notes when keys or paths change;
11. emit the required generated-work receipt for AI-authored changes;
12. open a scoped review branch and draft PR;
13. keep publication, deployment, and source activation outside the change unless separately authorized.

[Back to top](#top)

---

## Migration and drift posture

If misplaced material is found under `configs/dev/`:

1. do not treat it as authoritative merely because a consumer reads it;
2. classify its primary responsibility;
3. quarantine the change from release or deployment when secret, rights, sensitivity, or exposure risk exists;
4. move schema shape to `schemas/`;
5. move semantic meaning to `contracts/`;
6. move policy/admissibility to `policy/`;
7. move app/package/runtime/pipeline/tool code to its implementation root;
8. move durable pipeline definitions to `pipeline_specs/`;
9. move deployment and exposure controls to `infra/` or approved external systems;
10. move source/lifecycle/catalog/triplet/receipt/proof/published material to the owning `data/` lane;
11. move release, correction, and rollback records to `release/`;
12. move test corpora to `fixtures/` and enforceability to `tests/`;
13. move generated outputs to `artifacts/` or the governed output home;
14. preserve consumer compatibility, provenance, migration notes, and rollback instructions;
15. add a drift-register entry when the misplaced path has become an established dependency or contradicts Directory Rules;
16. require an ADR before creating a parallel authority home or changing root responsibilities.

### Drift triggers

- consumer reads a config from multiple authority-equivalent paths;
- same key has conflicting defaults across files;
- dev config contains policy-like allow/deny logic;
- dev config starts carrying release or publication state;
- local overrides are committed;
- production references appear in a development file;
- config examples and direct-load defaults are indistinguishable;
- generated copies drift from a canonical source;
- README claims a loader or validator that current code no longer supports.

[Back to top](#top)

---

## Rollback and correction posture

### Documentation-only rollback

Revert the commit that changed this README and its generated receipt, then re-run documentation and receipt validation. Do not rewrite shared history.

### Future config-payload rollback

A payload rollback should:

1. restore the prior reviewed config or remove the new file;
2. restore prior consumer key names and precedence when compatibility requires;
3. invalidate or remove stale generated copies;
4. update migration notes and consumer documentation;
5. re-run syntax, schema, consumer, negative, and secret checks;
6. confirm no local, CI, artifact, or deployment copy still carries the superseded value;
7. record correction impact when the config was already used;
8. preserve review history rather than force-pushing it away.

### Security correction

If a secret or live binding was exposed, reverting the file is insufficient. Rotate/revoke, inspect history and downstream copies, and follow the verified incident process.

[Back to top](#top)

---

## ADRs

No ADR is required for this README-only boundary refresh because it does not add, remove, or rename a canonical root; change schema-home authority; create a parallel authority home; change lifecycle stages; or authorize a public path.

An ADR is required before a future config change:

- creates a new canonical or compatibility root;
- changes `configs/` responsibility;
- creates a parallel schema, contract, policy, registry, source, release, receipt, proof, or catalog home;
- makes dev config a deployment or publication authority;
- introduces a cross-repository or generated synchronization authority;
- changes the trust membrane or public-client access model.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| `configs/` | Parent responsibility root for safe non-secret defaults and templates |
| `configs/examples/` | Illustrative examples; should not be assumed loaded |
| `configs/local/` | Commit-safe local templates and setup notes; not personal overrides |
| `configs/templates/` | Reusable configuration templates |
| `configs/test/` | Test configuration defaults/templates; tests and fixtures remain elsewhere |
| `apps/` / `packages/` | Possible consumers; implementation authority |
| `pipelines/` / `pipeline_specs/` | Executable logic and durable pipeline definitions |
| `runtime/` | Local adapters and harnesses |
| `infra/` | Deployment, network, exposure, and access controls |
| `schemas/` | Machine-checkable shape |
| `contracts/` | Semantic meaning |
| `policy/` | Admissibility and safe-exposure decisions |
| `tests/` / `fixtures/` | Enforceability and deterministic test inputs |
| `data/` | Lifecycle data and trust objects |
| `release/` | Release decisions, correction, and rollback |
| `artifacts/` | Generated outputs subject to its own governance |

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| `configs/dev/README.md` at prior blob `d9b6a872…` | **CONFIRMED** | Existing lane and v0.2 boundary; this is a revision, not a new path | Current payload inventory or consumer behavior |
| `configs/README.md` | **CONFIRMED** | Parent root owns safe non-secret defaults/templates | Complete current config inventory or enforcement |
| `configs/examples/README.md` | **CONFIRMED** | Example lane is illustrative and non-authoritative | Dev loader behavior |
| `configs/local/README.md` | **CONFIRMED** | Local lane is for commit-safe templates/notes, not personal values | Ignored override mechanism |
| `configs/templates/README.md` | **CONFIRMED** | Template lane owns reusable templates | Current template consumers |
| `configs/test/README.md` | **CONFIRMED** | Test config lane is distinct from tests/fixtures | CI enforcement |
| `docs/doctrine/directory-rules.md` | **CONFIRMED doctrine** | Placement by responsibility root; `configs/` is non-secret configuration | Current runtime or deployment behavior |
| `docs/security/SECRETS.md` | **CONFIRMED repository standard** | No real secrets in repository, including test/local material | Tooling coverage, store choice, or current leak-response path |
| `.github/CODEOWNERS` | **CONFIRMED at pinned base** | Repository-wide fallback owner exists | Accepted config-specific owner or team resolvability |
| `.github/PULL_REQUEST_TEMPLATE.md` | **CONFIRMED at pinned base** | PR requires evidence, Directory Rules basis, validation, rollback, and generated receipt disclosure | Branch protection or required-check enforcement |
| Repository search for `configs/dev` | **BOUNDED** | Returned this README as the only result located inside the directory | Exhaustive recursive absence |
| Named probes for `dev.yaml`, `.env.example`, `local.template.yaml`, `validation.md` | **CONFIRMED ABSENT AT NAMED PATHS** | Those exact conventional files were not present | Differently named files or branch-only work |
| Root/configs/configs-dev `AGENTS.md` probes | **CONFIRMED ABSENT AT NAMED PATHS** | No path-scoped agent instruction file was found at those exact locations | Other instruction mechanisms |
| Uploaded documentation operating prompt v3.1 | **CONFIRMED task input** | Implementation, evidence, concurrency, PR, and no-truncation requirements | Repository behavior by itself |

### Evidence limitations

- No recursive Git tree receipt was available through the selected connector surface.
- No config loader, consumer implementation, validator, workflow log, branch-protection setting, deployment, or runtime trace was inspected.
- No external source activation or version-sensitive product fact is needed for this README.
- The failed anonymous local clone attempt made no repository mutation and provided no additional evidence.

[Back to top](#top)

---

## Verification backlog

| Item | Why it matters | Evidence needed |
|---|---|---|
| Obtain recursive `configs/dev/` tree inventory | Replaces bounded search/probe finding with complete inventory | Git tree or mounted checkout receipt |
| Confirm config-specific owner(s) | Establishes maintenance and review routing | Accepted CODEOWNERS/team evidence |
| Confirm intended consumers | Required before any payload is called active | Current code/import/loader evidence |
| Confirm config discovery and precedence | Prevents hidden override drift | Loader tests and documented merge algorithm |
| Confirm schema bindings | Prevents malformed or stale fields | Schema refs and passing validation |
| Confirm secret scanning | Doctrine alone does not prove enforcement | Workflow/tool configuration and run evidence |
| Confirm negative tests | Unsafe values must fail predictably | Test files and passing runs |
| Confirm ignored local override path | Prevents accidental commits and false instructions | `.gitignore`, setup docs, and consumer behavior |
| Confirm CI required checks | A workflow file does not prove merge protection | GitHub branch/ruleset settings |
| Confirm incident-response runbook path | Secrets standard references a path not present at pinned base | Accepted runbook or corrected reference |
| Confirm generated/mirrored config policy | Prevents hand-edited drift | Generator, canonical source, and sync tests |
| Confirm platform portability | Avoids Windows/Linux/container divergence | Cross-platform tests or support statement |
| Confirm stale-config review cadence | Prevents obsolete defaults from looking supported | Ownership and scheduled validation evidence |

[Back to top](#top)

---

## Definition of done

### This README revision

- [x] Existing strong no-secrets, no-live-binding, and no-authority boundaries are preserved.
- [x] Parent and sibling config-lane responsibilities are distinguished.
- [x] Current evidence is pinned to repository, ref, commit, and prior blob.
- [x] Bounded search and named absence probes are stated without claiming exhaustive inventory.
- [x] Development-config file contract, precedence questions, naming, portability, validation, review, migration, and rollback are documented.
- [x] Secret-leak response duty is stated without inventing a missing runbook path.
- [x] No config payload, consumer, schema, contract, policy, test, workflow, runtime, deployment, or publication behavior is claimed as implemented.
- [x] AI-authored change is paired with a generated-work receipt.
- [ ] Human review approves the README and receipt.
- [ ] Repository-native checks complete successfully.

### Future `configs/dev/` maturity

- [ ] Accepted owners replace `OWNER_TBD`.
- [ ] Recursive lane inventory is recorded.
- [ ] Every payload names a verified consumer.
- [ ] Every payload documents parser, schema/contract references, precedence, safe failure, and override method.
- [ ] Secret and private-binding enforcement is verified.
- [ ] Syntax, schema, consumer, negative, and portability tests pass.
- [ ] Stale or duplicate config is removed or migrated.
- [ ] No public path, policy, release, lifecycle, or deployment authority bypasses its owning root.

[Back to top](#top)

---

<details>
<summary>Appendix A — no-loss preservation and v0.2 → v0.3 delta</summary>

The prior README established these durable boundaries:

- `configs/dev/` is a development-only sublane under `configs/`;
- committed material must be safe, non-secret, and development-focused;
- no live credentials, private endpoints, workstation state, lifecycle data, release records, schemas, contracts, policy, source code, runtime adapters, infra definitions, receipts, proofs, registry rows, or generated artifacts belong here;
- consumer, validator, CI, deployment, secret-scanning, and ownership maturity must not be overclaimed;
- misplaced material should migrate to its responsibility root through a reversible change;
- rollback and safe-language rules are part of the lane contract.

v0.3 preserves those points and adds:

- a pinned evidence snapshot and bounded README-only finding;
- explicit sibling-lane distinctions;
- a per-file development-config contract;
- placeholder, secret, portability, naming, and override rules;
- consumer-binding and precedence questions;
- layered validation and review matrices;
- workflow-trigger threat preflight;
- current CODEOWNERS and PR-template posture;
- the missing secret-leak-runbook verification gap;
- ADR triggers, drift triggers, migration, rollback, and correction detail;
- a required generated-work receipt for the AI-authored revision.

No previous substantive protection is intentionally removed.

</details>

## Status summary

`configs/dev/` is for commit-safe development configuration candidates, defaults, and tightly coupled documentation. It is not a secret store, local override store, schema or contract authority, policy engine, deployment binding, runtime implementation, lifecycle data lane, release record home, test fixture corpus, generated-artifact home, public data surface, or proof that any consumer works.

<p align="right"><a href="#top">Back to top</a></p>
