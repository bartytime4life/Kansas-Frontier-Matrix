<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-examples-readme
title: configs/examples/ — Commit-Safe Configuration Examples Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Security steward · Consumer owner(s) · Validation steward · Developer-experience steward · Docs steward
created: 2026-06-16
updated: 2026-07-13
policy_label: public; config-sublane; examples; commit-safe; non-secret; non-authoritative; no-live-binding; no-runtime-authority; no-deployment-authority
current_path: configs/examples/README.md
truth_posture: CONFIRMED repository-present README-only lane at the inspected search and named conventional probes, parent configs root contract, root examples distinction, sibling local/templates/domain config boundaries, secrets doctrine, and v0.1 introduction lineage / PROPOSED example-file contract, naming convention, metadata header, validation matrix, review workflow, and minimum safe example slice / UNKNOWN exhaustive recursive inventory, differently named example files, consumers, config loaders, precedence rules, schema bindings, validators, secret scanning, CI enforcement, deployment integration, owner assignments, and runtime behavior
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: b2db8a4f84754c111b28d756cbaac145fa0fcd84
  prior_blob: c1308ae4518ad3a8b852ecf0bafcc74eb4e926f3
  introduction_commit: df73db648805f5bbbe885d334cfbf492e6592404
related:
  - ../README.md
  - ../templates/README.md
  - ../local/README.md
  - ../dev/README.md
  - ../test/README.md
  - ../domains/README.md
  - ../maplibre/README.md
  - ../../examples/README.md
  - ../../fixtures/README.md
  - ../../tests/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/security/SECRETS.md
  - ../../docs/runbooks/SECRET_LEAK_RUNBOOK.md
  - ../../schemas/contracts/v1/
  - ../../contracts/
  - ../../policy/
  - ../../apps/
  - ../../packages/
  - ../../pipelines/
  - ../../pipeline_specs/
  - ../../runtime/
  - ../../infra/
  - ../../tools/
  - ../../.github/CODEOWNERS
  - ../../.github/PULL_REQUEST_TEMPLATE.md
tags: [kfm, configs, examples, samples, templates, placeholders, non-secret, commit-safe, config-validation, consumer-binding, non-authoritative, no-live-binding, governance]
notes:
  - "At the pinned base, a path-scoped repository search returned this README but no additional configs/examples files. Exact probes for default.example.yaml, config.example.yaml, .env.example, and validation.md returned Not Found. These are bounded findings, not an exhaustive recursive tree receipt."
  - "configs/examples/ is distinct from configs/templates/, configs/local/, configs/dev/, configs/test/, configs/domains/, and the root examples/ and fixtures/ responsibilities."
  - "A config example is illustrative input for a named consumer. It is not a schema, policy, contract, deployment binding, secret store, runtime state, release decision, lifecycle object, test fixture, or proof of consumption."
  - "The repository secrets standard states that no real secret may be committed, including material labeled test or local; only references-by-name, public verifier material, obvious placeholders, and clearly mock example values are acceptable."
  - "Only this Markdown file changes. No example config, consumer, schema, contract, policy, validator, test, workflow, secret-scanning rule, deployment binding, runtime behavior, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Commit-Safe Configuration Examples

> `configs/examples/` is the configuration-example sublane under `configs/`. It may teach safe configuration shape for a named consumer, but it does not create runtime behavior, deployment binding, schema authority, policy authority, secret material, release state, or operational truth.

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.2`  
> **Observed lane maturity:** README-only at the inspected repository search and named conventional probes  
> **Owning responsibility root:** `configs/` — safe, non-secret defaults and templates  
> **Authority:** configuration-example documentation only; no consumer, schema, policy, deployment, runtime, lifecycle, release, or publication authority  
> **Default posture:** safe to review, not safe to assume consumed

> [!CAUTION]
> Never place a real token, credential, private key, password, cookie, signed URL, private endpoint, restricted identifier, operator-specific path, production hostname, or sensitive source detail in a configuration example. An example that contains a real secret is a security incident, not documentation.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [What belongs](#what-belongs-here) · [What does not](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Evidence](#evidence-basis) · [Lane distinctions](#configuration-lane-distinctions) · [Example contract](#proposed-example-file-contract) · [Placeholders](#placeholder-and-secret-handling) · [Consumers](#consumer-binding-and-precedence) · [Formats](#file-format-and-naming-posture) · [Negative states](#negative-examples-and-fixtures) · [Change pattern](#safe-change-pattern) · [Rollback](#rollback-and-correction-posture) · [Backlog](#verification-backlog) · [Done](#definition-of-done)

---

## Purpose

`configs/examples/` is for small, commit-safe configuration examples that make a configuration surface understandable without creating a live binding.

A good example answers:

- which app, package, pipeline, pipeline spec, runtime adapter, tool, test, or review workflow it illustrates;
- which configuration fields are being demonstrated;
- which values are placeholders, mock values, or safe illustrative defaults;
- which contract or schema owns meaning and machine shape, when one exists;
- how a maintainer can validate syntax and compatibility;
- what must be replaced outside the repository before any real operation;
- which behavior remains `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`.

This lane should reduce setup ambiguity while preserving KFM's trust membrane. It must never turn documentation convenience into an operational shortcut.

[Back to top](#top)

---

## Authority level

**Configuration sublane / non-authoritative examples.**

| Concern | Authority status | Determination |
|---|---:|---|
| Folder placement | **CONFIRMED** | The path exists under `configs/`, whose parent README identifies that root as the home for safe non-secret defaults and templates. |
| Example content | **NON-AUTHORITATIVE** | An example may illustrate config shape but cannot define schema, policy, contract meaning, deployment state, runtime state, or release state. |
| Current inventory | **BOUNDED README-ONLY FINDING** | Search returned this README only; common candidate filenames were absent at named probes. Differently named or unindexed files remain `UNKNOWN`. |
| Consumer behavior | **UNKNOWN** | No consumer, config loader, import, merge order, or precedence behavior is established by this README. |
| Validation | **PROPOSED / NEEDS VERIFICATION** | Validation expectations are defined here; executable validators and CI bindings were not established in the inspected evidence. |
| Secret safety | **CONFIRMED DOCTRINE / ENFORCEMENT UNKNOWN** | Real secrets are forbidden in the repository; automated enforcement coverage remains `NEEDS VERIFICATION`. |
| Production use | **NOT AUTHORIZED** | No file in this lane may be treated as production-ready merely because it parses or resembles a real configuration. |

An example can point to an authority surface. It cannot become that authority surface.

[Back to top](#top)

---

## Status

### Bounded repository snapshot

At base commit `b2db8a4f84754c111b28d756cbaac145fa0fcd84`, the directly verified lane is:

```text
configs/examples/
└── README.md
```

A path-scoped repository search returned no other file in this lane. Exact probes returned `Not Found` for:

```text
configs/examples/default.example.yaml
configs/examples/config.example.yaml
configs/examples/.env.example
configs/examples/validation.md
```

These are bounded absence statements for named paths and indexed search results—not a recursive filesystem receipt. Differently named files, ignored files, generated files, branch-only work, or unindexed content remain `UNKNOWN`.

### Current maturity

| Capability | Status | Safe conclusion |
|---|---:|---|
| README boundary | **CONFIRMED** | The lane has documentation. |
| Example configuration files | **NOT ESTABLISHED** | No actual example payload was verified in the inspected lane. |
| Named consumers | **NOT ESTABLISHED** | No app/package/pipeline/runtime consumer was bound here. |
| Config loader or precedence | **NOT ESTABLISHED** | Do not infer auto-loading, overlay order, environment substitution, or merge behavior. |
| Schema validation | **NOT ESTABLISHED** | The lane does not prove schema references or validators. |
| Secret scanning | **NEEDS VERIFICATION** | Doctrine forbids secrets; repository automation coverage was not established by the inspected evidence. |
| Test/CI enforcement | **NEEDS VERIFICATION** | No lane-specific executable check or passing proof was verified. |
| Deployment integration | **UNKNOWN** | Nothing here establishes production, staging, review, or local runtime binding. |
| Ownership | **OWNER_TBD** | The current metadata does not identify accepted owners. |

[Back to top](#top)

---

## What belongs here

This lane may contain only configuration examples and tightly coupled explanatory notes that are safe to commit.

| Accepted material | Purpose | Required posture |
|---|---|---|
| `*.example.yaml` / `*.example.yml` | Human-readable YAML example for a named consumer. | Parseable, non-secret, consumer identified, authority references explicit. |
| `*.example.json` | Strict JSON example. | Valid JSON; no comments disguised as JSON; schema reference or `NEEDS VERIFICATION`. |
| `*.example.toml` | TOML example for a named consumer. | Parseable; consumer and version documented. |
| `.env.example` | Environment-variable names and obvious mock/reference values. | Never contain real values; use references-by-name or unmistakable placeholders. |
| `*.example.ini` / `*.example.cfg` | Legacy or tool-specific config examples where the consumer requires them. | Consumer and parser named; compatibility status explicit. |
| `README.md` | Lane contract, inventory, review guidance, and evidence boundary. | Truth-labeled and current. |
| `validation.md` | Human validation instructions. | Commands must be verified or labeled `PROPOSED`; no false CI claims. |
| `MIGRATION.md` | Temporary field/path compatibility guidance. | Review-linked, reversible, and removed or archived when migration closes. |
| Small public-safe snippets | Illustrate one configuration concern. | Synthetic or mock values; not a source payload or operational artifact. |

Each non-trivial example should be self-describing enough that a reviewer can determine the consumer, authority references, replacement requirements, and safe failure posture without guessing.

[Back to top](#top)

---

## What does NOT belong here

| Prohibited material | Why prohibited | Correct home or action |
|---|---|---|
| Real secrets, tokens, keys, passwords, cookies, signed URLs, private endpoints | Repository is not a secret store. | External secret manager / deployment system; rotate and invoke leak response if committed. |
| Production, staging, or operator-specific live values | Creates accidental deployment binding and exposure risk. | Environment-specific deployment controls outside the repository or under governed `infra/` references. |
| Personal workstation paths, usernames, home directories, device IDs | Leaks local identity and creates non-portable config. | Use symbolic placeholders or local uncommitted overrides. |
| Schema definitions | Examples cannot own machine shape. | `schemas/contracts/v1/` or accepted schema home. |
| Semantic contracts | Examples cannot own object meaning. | `contracts/`. |
| Policy rules or allow/deny decisions | Examples cannot authorize behavior. | `policy/`. |
| Application or package code | Config lane is not implementation. | `apps/` or `packages/`. |
| Pipeline implementation | Config lane is not executable processing. | `pipelines/`. |
| Durable declarative pipeline specs | A reusable pipeline definition is not merely an example. | `pipeline_specs/`. |
| Runtime adapters, harnesses, or service definitions | Examples cannot become runtime authority. | `runtime/`. |
| Deployment/network/access-control definitions | Examples cannot own operational exposure. | `infra/`. |
| Source data, API responses, rasters, vectors, scans, exports | Configuration examples are not data lanes. | Governed `data/raw/`, `data/work/`, or `data/quarantine/` as applicable. |
| Registry rows, SourceDescriptors, receipts, proofs, catalog/triplet records | Examples cannot become canonical trust objects. | Their owning `data/` or `control_plane/` homes. |
| Release manifests, promotion decisions, correction notices, rollback cards | Examples cannot approve or record release. | `release/`. |
| Generated outputs or reports | Examples lane is not a build-output home. | `artifacts/` or governed published/release homes as applicable. |
| Walkthrough projects, story flows, or multi-file demonstrations | Root `examples/` owns worked examples and walkthrough assemblies. | `examples/`. |
| Valid/invalid machine-test corpora | Tests and fixtures need deterministic ownership and expected outcomes. | `fixtures/` and `tests/`. |
| Sensitive locations, living-person data, proprietary identifiers, private parcel joins | Not needed to explain config shape and may cause harm. | Synthesize, generalize, redact, quarantine, or deny. |

A configuration example must not become a quiet parallel home for any trust-bearing object family.

[Back to top](#top)

---

## Inputs

### Current input

The current lane consumes documentation and repository evidence only. No example payload or supported loading interface is established by the inspected repository evidence.

### Future admissible inputs

A proposed configuration example may be authored from:

- an existing, verified consumer's configuration interface;
- a semantic contract describing configuration meaning;
- a machine schema describing configuration shape;
- current safe defaults from code or a pipeline specification;
- a reviewed migration from an older configuration name or field;
- a minimal synthetic use case needed for documentation;
- a test or validator interface, provided the example itself remains outside fixture/test authority.

The author must not copy a real deployment configuration and “redact a few values.” Create a clean example from the accepted field surface and obvious mock values.

### Required provenance for authoring

Before adding a new example, record or link:

```text
consumer
consumer version or commit
config loader or parser
schema/contract reference, if any
required replacement fields
safe default rationale
validation method
owner/reviewer
```

Unknown fields should remain explicitly unknown rather than being guessed from generic conventions.

[Back to top](#top)

---

## Outputs

This lane may produce:

- human-readable configuration examples;
- copyable but non-operational starting points;
- references-by-name for external secret injection;
- validation instructions;
- migration notes;
- reviewer guidance about consumers and authority boundaries.

This lane does **not** emit:

- effective runtime configuration;
- resolved secrets;
- deployment configuration;
- policy decisions;
- validation reports;
- receipts or proofs;
- lifecycle state;
- release decisions;
- public API or UI payloads.

Copying an example into another location is a new governed act. The copied file inherits the authority and review requirements of its destination; it does not inherit approval from this lane.

[Back to top](#top)

---

## Validation

### Validation matrix

Every new or changed example should be checked at the strongest applicable level.

| Check | Requirement | Current lane status |
|---|---|---:|
| Syntax parse | Parse with the consumer's real parser or a compatible standard parser. | **PROPOSED / NEEDS VERIFICATION** |
| Schema conformance | Validate against the accepted schema when one exists. | **PROPOSED / NEEDS VERIFICATION** |
| Known-key check | Detect unknown, misspelled, deprecated, or ignored keys. | **PROPOSED** |
| Consumer compatibility | Load through the verified consumer in a no-side-effect mode where possible. | **PROPOSED** |
| Secret scan | Detect private keys, tokens, credentials, signed URLs, cookies, and suspicious high-entropy values. | **REQUIRED; ENFORCEMENT NEEDS VERIFICATION** |
| Placeholder review | Confirm replacement fields are obvious and cannot be mistaken for real credentials or hosts. | **REQUIRED** |
| Network safety | Validation should not contact real services unless an explicit governed test permits it. | **DEFAULT NO NETWORK** |
| Filesystem safety | No writes outside an isolated temporary directory; no absolute operator paths. | **REQUIRED** |
| Lifecycle isolation | Example validation must not write RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, PUBLISHED, receipt, proof, or release objects. | **REQUIRED** |
| Determinism | Repeated validation should yield the same result absent an intentional version change. | **REQUIRED** |
| Documentation links | Consumer, contract, schema, validator, and owner links resolve or are labeled `NEEDS VERIFICATION`. | **REQUIRED** |
| Diff review | Review changes to defaults as behavior-significant even when code is unchanged. | **REQUIRED** |

### Minimum manual review

- [ ] File is a configuration example, not a template, fixture, test corpus, or operational config.
- [ ] Intended consumer and configuration scope are named.
- [ ] Format is valid and expected by the consumer.
- [ ] Every deployment-specific value is an obvious placeholder or reference-by-name.
- [ ] No secret-like, private, sensitive, or production-bound value appears.
- [ ] Schema/contract authority is linked or explicitly unresolved.
- [ ] Example does not grant policy, source activation, release, or publication permission.
- [ ] Validation command is verified or labeled `PROPOSED`.
- [ ] Example does not rely on network access or side effects merely to prove syntax.
- [ ] Rollback is restoring the prior blob or reverting the scoped commit.

### Validation is not activation

A passing syntax or schema check proves only that the example matches a shape. It does not prove:

- the consumer loads it;
- the values are appropriate for a deployment;
- upstream services are reachable;
- policy gates pass;
- lifecycle transitions are allowed;
- a release is approved;
- public exposure is safe.

[Back to top](#top)

---

## Review burden

| Change type | Required review posture |
|---|---|
| README-only clarification | Config steward or docs steward; security review when secret handling changes. |
| New example for an app/package/pipeline/runtime/tool | Config steward plus the named consumer owner. |
| New or changed placeholder/secret reference | Security steward plus consumer owner. |
| New default that could alter processing, access, visibility, resource use, retention, or public behavior | Consumer owner plus relevant policy/security/domain/release reviewer. |
| Schema or contract mismatch discovered | Schema/contract steward; fix the authority surface or label the example drift—do not silently redefine it here. |
| Deprecated key or compatibility example | Consumer owner plus migration reviewer; include sunset and rollback. |
| Sensitive-domain configuration | Relevant domain and sensitivity/geoprivacy reviewer even when values are synthetic. |

`CODEOWNERS` coverage for this exact lane is `NEEDS VERIFICATION`. `OWNER_TBD` must not be interpreted as approval by the repository-wide placeholder team.

[Back to top](#top)

---

## Related folders

| Surface | Relationship to `configs/examples/` |
|---|---|
| [`../README.md`](../README.md) | Parent configuration-root contract. |
| [`../templates/`](../templates/README.md) | Reusable placeholder structures; templates are less concrete than examples. |
| [`../local/`](../local/README.md) | Commit-safe local setup defaults and notes. |
| `../dev/` | Development configuration defaults/templates, if verified. |
| `../test/` | Test-oriented configuration defaults, not general examples. |
| [`../domains/`](../domains/README.md) | Domain-scoped configuration defaults and guardrails. |
| `../maplibre/` | MapLibre-specific configuration lane, if verified. |
| [`../../examples/`](../../examples/README.md) | Worked examples, walkthroughs, synthetic flows, and assemblies—not config examples. |
| `../../fixtures/` | Deterministic test inputs and expected outputs. |
| `../../tests/` | Executable validation and behavior proof. |
| `../../schemas/contracts/v1/` | Machine shape authority. |
| `../../contracts/` | Semantic meaning. |
| `../../policy/` | Admissibility and allow/deny/restrict/abstain rules. |
| `../../apps/`, `../../packages/`, `../../pipelines/`, `../../runtime/`, `../../tools/` | Possible consumers; consumption must be proven individually. |
| `../../pipeline_specs/` | Durable declarative pipeline definitions. |
| `../../infra/` | Deployment and exposure controls. |
| `../../data/` | Lifecycle, registry, receipt, proof, catalog, and published object homes. |
| `../../release/` | Release decisions, correction, withdrawal, and rollback. |
| [`../../docs/security/SECRETS.md`](../../docs/security/SECRETS.md) | No-secrets doctrine and reference-by-name guidance. |

[Back to top](#top)

---

## ADRs

No accepted ADR was verified in this update that specifically assigns a machine contract, loader, precedence rule, or validation workflow to `configs/examples/`.

Potential ADR or per-root decision triggers include:

- making this lane auto-discovered or runtime-loaded;
- defining a repository-wide config merge/precedence algorithm;
- declaring one universal config schema or cross-consumer envelope;
- moving examples into or out of another canonical responsibility root;
- allowing environment-specific live bindings in committed files;
- standardizing a cross-repository placeholder vocabulary with machine enforcement;
- promoting examples into fixtures or operational defaults by reference rather than explicit copy/migration.

This README does not enact any of those decisions.

[Back to top](#top)

---

## Last reviewed

**2026-07-13**

Review basis:

- current target README and its v0.1 introduction commit;
- parent `configs/` README;
- sibling `configs/local/`, `configs/templates/`, and `configs/domains/` READMEs;
- root `examples/` README;
- Directory Rules placement posture;
- secrets doctrine;
- path-scoped search and named conventional file probes.

No consumer code, loader, schema validator, secret scanner, CI enforcement, deployment runtime, or production config was established by this documentation review.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---:|---|---|
| `configs/examples/README.md` prior blob `c1308ae4518ad3a8b852ecf0bafcc74eb4e926f3` | **CONFIRMED** | Existing v0.1 lane boundary and exact rollback target. | Does not prove example files or consumers. |
| Introduction commit `df73db648805f5bbbe885d334cfbf492e6592404` | **CONFIRMED** | v0.1 expanded a three-line greenfield stub into the first governed README. | Historical lineage, not current runtime evidence. |
| Path-scoped search for `configs/examples` | **CONFIRMED SEARCH RESULT** | Returned this README and no other file in the lane. | Search is not an exhaustive recursive tree listing. |
| Named probes for common example filenames | **CONFIRMED ABSENT AT PROBES** | `default.example.yaml`, `config.example.yaml`, `.env.example`, and `validation.md` were absent. | Differently named files remain unknown. |
| `configs/README.md` | **CONFIRMED** | `configs/` is the safe non-secret defaults/templates root and forbids deployment-only confidential values. | Parent doctrine does not prove child consumers or enforcement. |
| `configs/local/README.md` and `configs/templates/README.md` | **CONFIRMED** | Neighboring sublane distinctions and non-authoritative posture. | Their current inventories and consumers also remain uncertain. |
| `configs/domains/README.md` | **CONFIRMED** | Stronger v0.2 config guardrails, no-secrets rule, consumer/validator posture, and authority separation. | Domain-specific concerns do not automatically bind this lane. |
| `examples/README.md` | **CONFIRMED** | Root `examples/` owns worked examples and walkthroughs; examples are non-authoritative. | Does not define config loader behavior. |
| `docs/security/SECRETS.md` | **CONFIRMED DOCUMENT / IMPLEMENTATION MIXED** | No real secrets in the repository; references-by-name and obvious mock values are acceptable. | Secret-store choice, automated enforcement, and owner cadence remain uncertain. |
| Actual config consumers and validators | **UNKNOWN** | None established in this pass. | Requires code, tests, workflows, and runtime evidence. |

### Evidence conflicts and drift signals

- The parent `configs/` README lists several suggested sublanes but marks inventory unverified; the repository does contain multiple config sublane READMEs. Parent inventory should eventually be refreshed from a real tree receipt.
- `configs/examples/` and `configs/templates/` overlap semantically unless maintainers preserve a concrete distinction: examples show safe illustrative values; templates emphasize replacement placeholders.
- Documentation repeatedly requires secret-safe config, but no dedicated lane-specific secret-scan or config-validation workflow was established in the inspected evidence.
- A folder can be README-only while documentation presents candidate filenames. Candidate filenames are examples, not repo facts.

[Back to top](#top)

---

## Configuration lane distinctions

| Lane | Primary question | Appropriate content | Must not become |
|---|---|---|---|
| `configs/examples/` | “What does a safe illustrative configuration look like for this named consumer?” | Concrete but mock/non-operational values. | Runtime or deployment binding. |
| `configs/templates/` | “Which fields must an operator replace?” | Reusable placeholder structure. | Schema authority or live config. |
| `configs/local/` | “What safe local-development defaults/notes are appropriate?” | Commit-safe local setup templates. | Personal machine override store. |
| `configs/dev/` | “What development defaults are shared?” | Verified development-only defaults/templates. | Production settings. |
| `configs/test/` | “What test configuration is shared?” | Test-specific safe defaults. | General examples or fixture payloads. |
| `configs/domains/` | “Which safe domain-scoped knobs and review defaults exist?” | Domain config defaults with sensitivity guardrails. | Domain truth, policy, or release authority. |
| `examples/` | “How does a governed scenario or walkthrough look?” | Multi-step examples and synthetic assemblies. | Config authority, proof, or public path. |
| `fixtures/` | “Which deterministic input/output cases prove behavior?” | Valid/invalid test corpora. | Documentation-only examples. |
| `infra/` | “How is an environment actually deployed and exposed?” | Deployment/network/access controls. | Generic config-example lane. |
| External secret/deployment store | “What are the real environment values?” | Protected operational values. | Repository content. |

### Example versus template

Use an **example** when safe illustrative values help understanding:

```yaml
# Illustrative only; not consumed unless explicitly copied and reviewed.
service:
  mode: "mock"
  endpoint: "https://example.invalid"
```

Use a **template** when every deployment must supply replacements:

```yaml
service:
  mode: "<REQUIRED_MODE>"
  endpoint: "${SERVICE_ENDPOINT}"
```

Both remain non-authoritative. Neither belongs in the repository with real secret or production values.

[Back to top](#top)

---

## Proposed example-file contract

The following header is a **PROPOSED documentation convention**, not an implemented schema:

```yaml
kfm_example:
  example: true
  authority: non_authoritative_config_example
  do_not_use_in_production: true
  consumer_ref: "<repo path or package/app identifier>"
  consumer_version: "<commit, release, or NEEDS_VERIFICATION>"
  config_scope: "<bounded purpose>"
  schema_ref: "<schema path or NEEDS_VERIFICATION>"
  contract_ref: "<contract path or NEEDS_VERIFICATION>"
  validation_ref: "<test/tool/command or NEEDS_VERIFICATION>"
  secret_posture: references_by_name_or_obvious_mock_values_only
  network_posture: no_network_by_default
  lifecycle_effect: none
  release_effect: none
  owner: "<OWNER_TBD>"
```

A consumer that cannot tolerate an in-band metadata object should receive the same information in adjacent Markdown or comments supported by the format.

### Required semantic fields

Whether in-band or documented beside the file, every consequential example should identify:

- **consumer** — the exact component intended to read the operational equivalent;
- **scope** — the behavior or subsystem illustrated;
- **version** — consumer version, commit, or explicit uncertainty;
- **authority references** — schema, contract, policy, or accepted config docs;
- **replacement fields** — which values must be supplied elsewhere;
- **secret posture** — how secret references are injected without storing values;
- **validation** — parse/schema/consumer test path;
- **side effects** — expected none for example validation;
- **owner** — reviewer responsible for freshness;
- **sunset** — when a migration example can be removed.

[Back to top](#top)

---

## Placeholder and secret handling

### Acceptable values

- `${VARIABLE_NAME}` references that resolve outside the repository;
- `<REQUIRED_VALUE>` or `REPLACE_ME_NON_SECRET` markers;
- `example.invalid` hostnames;
- RFC-reserved documentation IP ranges only when an IP is unavoidable;
- obvious mock IDs such as `mock-source-id`;
- temporary paths rooted in a symbolic variable or test directory;
- public verifier material that is intentionally non-secret and documented as such.

### Forbidden values

- bearer tokens, PATs, API keys, OAuth secrets, refresh tokens;
- private keys, password hashes intended for real use, session secrets;
- live cookies or authorization headers;
- pre-signed or signed download URLs;
- real database connection strings containing credentials;
- private/internal hostnames, VPN addresses, operator IPs;
- production buckets, account IDs, tenant IDs, or project IDs when disclosure is sensitive;
- real email addresses, usernames, home directories, device names;
- source credentials embedded in query parameters;
- exact restricted geometry or identifiers disguised as config;
- copied `.env`, kubeconfig, cloud credential, service-account, or SSH material.

### Reference-by-name rule

An example may show **where** a secret reference goes:

```yaml
credentials:
  token_env: "UPSTREAM_TOKEN"
```

It must not show the secret value:

```yaml
credentials:
  token: "actual-secret-value"  # forbidden
```

### Leak response

When a real secret is discovered:

1. stop treating the file as documentation;
2. revoke or rotate the credential;
3. preserve an auditable incident path without repeating the secret;
4. remove the value through reviewed history-safe remediation;
5. follow the secret-leak runbook;
6. inspect logs, artifacts, caches, PR comments, and forks for propagation;
7. add prevention tests or scanning where practical.

A normal revert does not make an exposed secret safe again.

[Back to top](#top)

---

## Consumer binding and precedence

This README does not establish any config loader or precedence algorithm.

Until implementation evidence proves otherwise:

- files under `configs/examples/` are **not auto-loaded**;
- placing a file here does not activate a feature;
- copying a file does not prove the target consumer accepts it;
- environment-variable expansion behavior is consumer-specific;
- merge order between default, file, environment, CLI, policy, and deployment values is `UNKNOWN`;
- unknown-key handling is `UNKNOWN`;
- deprecated-key behavior is `UNKNOWN`;
- reload/hot-reload behavior is `UNKNOWN`;
- secret resolution is external and consumer-specific;
- public clients must not receive internal or secret-bearing configuration.

### Required precedence documentation

A future consumer-bound example should link to verified behavior resembling:

```text
compiled safe default
  < reviewed config file
  < environment-specific non-secret override
  < external secret reference resolution
  < explicit operator/CLI override, if allowed
```

This ordering is illustrative only. The real order must come from code, tests, and accepted documentation.

### Fail-closed posture

If the example and consumer disagree:

- do not silently ignore the mismatch;
- do not guess renamed keys;
- do not substitute unsafe defaults;
- do not expose unresolved values;
- return a deterministic parse/validation/configuration error;
- record the mismatch for correction;
- keep publication and sensitive operations disabled.

[Back to top](#top)

---

## File format and naming posture

### Proposed names

| Format | Preferred example form | Notes |
|---|---|---|
| YAML | `<consumer>.<scope>.example.yaml` | Human-readable; avoid ambiguous YAML typing. |
| JSON | `<consumer>.<scope>.example.json` | Strict parse; no comments. |
| TOML | `<consumer>.<scope>.example.toml` | Good for typed local tooling where supported. |
| Environment | `.env.example` or `<consumer>.env.example` | Names and obvious mock/reference values only. |
| INI/CFG | `<consumer>.<scope>.example.ini` | Use only for a verified consumer. |

Naming is `PROPOSED` until a `configs/` per-root convention or ADR freezes it.

### File-level requirements

- UTF-8 text;
- final newline;
- stable key order where the format permits;
- comments only where valid for the format;
- no duplicate keys;
- no anchors/aliases or advanced parser-specific behavior unless the consumer requires and tests them;
- explicit units in keys or documentation;
- explicit time zones and duration units;
- explicit path relativity;
- no machine-specific absolute paths;
- no hidden defaults that weaken policy or review;
- deterministic values where practical.

### Unsafe ambiguity examples

Avoid:

```yaml
enabled: yes
timeout: 10
date: 2026-07-13
```

Prefer consumer-verified, explicit forms:

```yaml
enabled: true
timeout_seconds: 10
effective_date: "2026-07-13"
```

Exact typing still depends on the consumer schema and parser.

[Back to top](#top)

---

## Negative examples and fixtures

Invalid configurations used to test deterministic rejection should normally live under `fixtures/` with consuming tests under `tests/`.

`configs/examples/` may describe a negative state in Markdown, but should not become an unowned invalid-fixture corpus.

| Need | Correct posture |
|---|---|
| Show a maintainer why a field is unsafe | Small README snippet with `INVALID — DO NOT COPY`. |
| Prove a parser rejects a missing field | Invalid fixture plus executable test. |
| Prove secrets are detected | Synthetic secret-pattern fixture plus scanner test; never use a real credential. |
| Prove unknown keys fail | Invalid config fixture tied to consumer/schema test. |
| Prove policy-sensitive values deny | Policy fixture/test under policy/test responsibility roots. |
| Show a complete governed workflow | Root `examples/`, not this lane. |

Negative examples must not leak the forbidden value they are intended to guard against.

[Back to top](#top)

---

## Safe change pattern

1. **Identify the consumer.** Do not add an orphan example.
2. **Inspect authority.** Read the relevant contract, schema, policy, consumer code, and config docs.
3. **Choose the correct lane.** Example, template, local/dev/test config, fixture, pipeline spec, or worked example.
4. **Author from shape, not production copies.**
5. **Use obvious non-secret values and references-by-name.**
6. **Validate syntax.**
7. **Validate schema and known keys where available.**
8. **Exercise the consumer in no-side-effect/no-network mode where available.**
9. **Run secret scanning and manual sensitive-value review.**
10. **Document unresolved behavior with truth labels.**
11. **Keep the change small and reversible.**
12. **Update this README inventory only after the file is actually present.**

### Anti-patterns

- “It is under examples, so any value is safe.”
- “The filename says `.example`, so the consumer will not load it.”
- “It passed YAML parsing, so it is deployment-ready.”
- “This template defines the schema.”
- “The config enables the policy.”
- “A fake token that resembles a real token is harmless.”
- “We can copy production config and redact only the password.”
- “An ignored unknown key is close enough.”
- “A config example is a fixture.”
- “A walkthrough belongs beside a config because it mentions config.”

[Back to top](#top)

---

## Rollback and correction posture

### Exact rollback target

Restore prior blob:

```text
c1308ae4518ad3a8b852ecf0bafcc74eb4e926f3
```

or revert the scoped commit that introduces this v0.2 revision.

### Rollback triggers

Rollback or correct this README if it is used to justify:

- committing real secrets or live bindings;
- automatic consumer loading without code/test evidence;
- production deployment from example files;
- bypassing schemas, contracts, policy, review, or release;
- treating example values as approved defaults;
- moving fixtures, pipeline specs, infra definitions, or worked examples into this lane;
- claiming validation or CI enforcement not supported by executable evidence;
- hiding inventory or ownership uncertainty.

### Correction discipline

Documentation errors should be fixed by transparent commits. If an example value escaped into logs, caches, artifacts, or releases, use the relevant security, correction, withdrawal, and rollback processes rather than editing history silently.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Produce a recursive `configs/examples/` inventory | **NEEDS VERIFICATION** | Tree receipt pinned to commit. |
| Confirm whether the lane should remain README-only | **OPEN** | Maintainer/config-steward decision. |
| Assign owners and CODEOWNERS coverage | **NEEDS VERIFICATION** | Accepted ownership mapping. |
| Freeze example-versus-template distinction | **PROPOSED** | `configs/` per-root decision or ADR if cross-cutting. |
| Freeze file naming convention | **PROPOSED** | Per-root convention and migration plan. |
| Identify real consumers | **UNKNOWN** | Code/config-loader references and tests. |
| Document config precedence per consumer | **UNKNOWN** | Code, tests, and accepted docs. |
| Bind examples to schemas/contracts | **NEEDS VERIFICATION** | Accepted paths and validators. |
| Add syntax validation | **PROPOSED** | Parser-based tests/tooling. |
| Add known-key/deprecation validation | **PROPOSED** | Consumer/schema-aware validator. |
| Verify secret scanning | **NEEDS VERIFICATION** | Workflow/tool configuration and passing/failing fixtures. |
| Verify no-network/no-side-effect validation | **NEEDS VERIFICATION** | Test harness and logs. |
| Verify docs/link validation | **NEEDS VERIFICATION** | Substantive workflow, not placeholder echo. |
| Review `.env.example` policy | **OPEN** | Security/config-steward decision. |
| Define migration/sunset rules for old examples | **PROPOSED** | Maintainer policy and tests. |
| Reconcile parent `configs/` suggested tree with current repository | **NEEDS VERIFICATION** | Current tree inventory and README refresh. |
| Confirm secret-leak runbook path and operational readiness | **NEEDS VERIFICATION** | Runbook inspection and drill evidence. |

[Back to top](#top)

---

## Definition of done

This lane may advance beyond README-only draft when:

- [ ] a commit-pinned recursive inventory exists;
- [ ] owners and CODEOWNERS coverage are assigned;
- [ ] example-versus-template/local/dev/test/fixture/worked-example boundaries are accepted;
- [ ] every example names a verified consumer and scope;
- [ ] every example records consumer version or commit;
- [ ] every example links the accepted schema/contract or explicitly records why none applies;
- [ ] every example uses only obvious mock values, placeholders, or references-by-name;
- [ ] no real secret, private endpoint, operator path, sensitive identifier, or production binding is present;
- [ ] syntax parsing is automated for every supported format;
- [ ] known-key and deprecation behavior is tested where consumers support it;
- [ ] secret scanning is configured and has safe positive/negative test coverage;
- [ ] validation is no-network and no-side-effect by default;
- [ ] consumer compatibility tests exist where practical;
- [ ] config precedence and override rules are documented per consumer;
- [ ] examples cannot activate sources, weaken policy, promote lifecycle state, release artifacts, or expose public/internal routes;
- [ ] stale examples have owners, review dates, and removal/migration paths;
- [ ] documentation/link checks are substantive and passing;
- [ ] rollback and secret-leak response are documented and tested;
- [ ] this README is refreshed from resulting evidence.

A parseable example is useful documentation. It is not runtime readiness, deployment approval, policy approval, release approval, or truth.

[Back to top](#top)
