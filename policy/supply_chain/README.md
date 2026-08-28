<a id="top"></a>

# Supply-chain policy lane

> **One-line purpose.** `policy/supply_chain/` is the current local source
> boundary for KFM's proposed static dependency-origin configuration. It
> inherits policy authority from [`policy/`](../README.md); it does not hold
> credentials, package bytes, installed environments, vulnerability findings,
> attestations, SBOMs, release decisions, deployment state, or publication
> authority.

> [!IMPORTANT]
> **Safe current conclusion:** at
> `main@97e124e67320c811fe6528b4828747ff81c22d26`, this directory contains
> this 661-byte README and one 1,303-byte JSON policy. The policy is explicitly
> `PROPOSED_STATIC_GUARD` with `authority: NONE`. Its dedicated validator
> can inspect a bounded set of repository declarations and return
> `PASS`, `DENY`, or `ERROR`; it does not install or resolve project
> dependencies.

> [!CAUTION]
> A passing static scan is a repository-hygiene signal only. It is not evidence
> of registry or publisher identity, package authenticity, signature or
> attestation verification, vulnerability absence, SBOM or provenance closure,
> lifecycle-script safety, compatibility, rights clearance, human approval,
> release readiness, deployment, publication, or public-use authority.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Child map](#current-direct-child-map) · [Profile](#current-policy-profile) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Scan surface](#repository-scan-surface) · [Outcomes](#finite-outcomes-and-finding-codes) · [Package manager](#package-manager-and-lockfile-boundary) · [npm](#npm-manifest-boundary) · [pnpm](#pnpm-lockfile-boundary) · [Python](#python-dependency-boundary) · [Adjacent controls](#relationship-to-adjacent-supply-chain-controls) · [Execution](#validator-and-workflow-execution-boundary) · [Validation](#validation-coverage-and-limits) · [Receipts](#generated-receipt-and-provenance-boundary) · [Security](#security-exposure-and-retention) · [Related evidence](#related-contracts-schemas-fixtures-tests-and-workflows) · [Authoring](#authoring-and-review-contract) · [Correction](#correction-and-rollback) · [Review](#review-triggers-and-evidence-snapshot) · [Open verification](#open-verification-register)

## Purpose

This lane records a machine-readable, repository-local proposal for detecting a
small set of dependency-origin declaration defects before they are normalized
into ordinary repository state. The current profile covers:

- an exact root package-manager declaration;
- one required root lockfile and a finite competing-lockfile deny list;
- one-level `apps/*` and `packages/*` npm manifests;
- local `@kfm/` package binding through `workspace:` or `link:`;
- configured direct npm source prefixes;
- integrity fields on the pnpm package-resolution entries the parser observes;
- allowlisted hosts on explicit pnpm tarball or URL fields; and
- configured direct references in root PEP 621 Python dependencies.

The policy is intentionally narrower than KFM's complete supply-chain posture.
It is one proposed declaration guard among separate update, audit, dependency
review, secret, filesystem, container, Scorecard, release, and provenance
controls. This README documents the tracked bytes, executable interpretation,
evidence relationships, and limitations without promoting the profile to
accepted or complete status.

[Back to top](#top)

## Inherited authority, owner, and scope

| Field | Current evidence |
|---|---|
| Parent | [`policy/`](../README.md), KFM's canonical repository root for normative allow, deny, hold, restrict, and abstain rule source. |
| README profile | `BOUNDARY_COMPACT`: this child introduces a dependency-declaration trust boundary while inheriting the parent root contract. |
| Placement | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). The rules place policy source under singular `policy/` and require local boundary documentation for material child lanes. |
| Machine projection | [`root_registry.yaml`](../../control_plane/root_registry.yaml) projects `policy/` as an internal, versioned, durable policy-rule root. The projection does not create policy authority or approve this profile. |
| Review route | [CODEOWNERS](../../.github/CODEOWNERS) routes `/policy/` to `@bartytime4life`. Routing does not prove stewardship, independent review, approval, required-check configuration, or effective branch protection. |
| Local owner | **NEEDS VERIFICATION.** No accepted supply-chain policy steward or independent approver was established by the reviewed repository evidence. |
| Profile identity | `kfm.governance.dependency-origin-policy.v1`, schema version `1.0.0`, status `PROPOSED_STATIC_GUARD`. |
| Validator scope | `governance.dependency_origin_policy`; deterministic repository declaration inspection only. |
| Policy authority | `NONE`, as required by the current policy schema and emitted result. |
| Release authority | None. [`release/`](../../release/README.md) separately owns governed release, correction, withdrawal, and rollback decisions. |
| Publication authority | None. A policy file, scan, receipt, workflow, commit, or merge cannot publish KFM knowledge or authorize public use. |

[Back to top](#top)

## Current status

| Surface | Confirmed state at the evidence base | Safe interpretation |
|---|---|---|
| Target README before this update | 661 bytes, blob `00b7f768444911123191b001aa18079d02ea1423` | The existing file stated the broad non-authority boundary but did not document the executable scan surface, findings, adjacent controls, review path, or open gaps. |
| Direct-child inventory | This README plus [`dependency_origin_policy.v1.json`](./dependency_origin_policy.v1.json) | Two tracked files only; no credential, package, SBOM, attestation, audit result, release, or deployment object is stored here. |
| Policy projection | Closed JSON object, schema `1.0.0`, profile `kfm.governance.dependency-origin-policy.v1`, status `PROPOSED_STATIC_GUARD`, authority `NONE` | Machine-readable configuration for the bounded validator; not a registry, installer, resolver, firewall, release decision, or runtime authorization. |
| Semantic contract | [`dependency_origin_policy.md`](../../contracts/governance/dependency_origin_policy.md) | Describes the proposed static guard and explicitly excludes install-time identity, publishers, signatures, attestations, vulnerabilities, lifecycle scripts, release, deployment, and publication. |
| Machine schema | [`dependency_origin_policy.schema.json`](../../schemas/contracts/v1/governance/dependency_origin_policy.schema.json) | Draft 2020-12 shape for the configuration. It is not a schema for live registry state, package metadata, a repository snapshot, or scan output. |
| Validator | [`validate_dependency_origin_policy.py`](../../tools/validators/governance/validate_dependency_origin_policy.py) | Deterministic Python parser and evaluator for fixtures or one repository root; prints a bounded result and exits zero only for `PASS`. |
| Focused tests | [`test_dependency_origin_policy.py`](../../tests/validators/governance/test_dependency_origin_policy.py) | Seven unit tests cover schema validity, policy ordering, nine fixture cases, two temporary repositories, static no-network/no-write shape, and deterministic CLI output. |
| Fixture suite | [README](../../fixtures/contracts/v1/governance/dependency_origin_policy/README.md) and [nine cases](../../fixtures/contracts/v1/governance/dependency_origin_policy/cases.json) | Synthetic positive, deny, and error examples; they do not contact a registry, install packages, reserve names, or verify publishers. |
| Dedicated workflow | [`dependency-origin-policy`](../../.github/workflows/dependency-origin-policy.yml) | Read-only hosted validation for this profile and its exact authoring receipt. Workflow presence or success does not prove the check is required or independently reviewed. |
| Current root declarations | [`package.json`](../../package.json) declares `pnpm@11.17.0`; [`pnpm-lock.yaml`](../../pnpm-lock.yaml) declares lockfile version `9.0`; [`pyproject.toml`](../../pyproject.toml) carries root PEP 621 dependencies | Confirmed source bytes at the evidence base. This README does not substitute for the exact-head repository scan. |
| Existing generated receipt | [`genrec-pass8-dependency-origin-policy-20260808.json`](../../data/receipts/generated/genrec-pass8-dependency-origin-policy-20260808.json) | Binds the original nine-file profile slice by SHA-256 and remains pending human review. It is provenance/process memory, not approval or technical proof. |
| Runtime or public behavior | No installer, resolver, runtime service, deployment, release, or public consumer is defined in this directory | Documentation and proposed static configuration only. |

All current-state claims are pinned to
`main@97e124e67320c811fe6528b4828747ff81c22d26`. Later repository or
platform changes require a fresh inventory and claim review.

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from the pinned tree, exact tracked bytes, tests, workflows, or an accepted repository decision. |
| **PROPOSED** | Candidate policy, profile, behavior, integration, or authority not accepted as current operation. |
| **NEEDS VERIFICATION** | A bounded check, assignment, configuration, or review remains before reliance. |
| **UNKNOWN** | The inspected evidence cannot support a stronger statement. |

[Back to top](#top)

## Current direct-child map

This is the complete tracked directory at the evidence base:

```text
policy/supply_chain/
├── README.md
└── dependency_origin_policy.v1.json  # PROPOSED_STATIC_GUARD; authority NONE
```

Neither file is marked as generated, mirrored, localized, or converted in its
own tracked bytes. The generated receipt for the broader implementation slice
lives under [`data/receipts/generated/`](../../data/receipts/generated/README.md),
where accountability records belong.

[Back to top](#top)

## Current policy profile

The JSON policy is closed by schema. The following table distinguishes stored
configuration from its present validator effect.

| Setting | Current value | Current executable interpretation |
|---|---|---|
| `authority` | `NONE` | Emitted results also declare `authority: NONE`; no decision or release authority is created. |
| `expected_package_manager` | `pnpm@11.17.0` | Requires exact equality with root `package.json.packageManager`; it does not execute or authenticate that binary. |
| `required_lockfile` | `pnpm-lock.yaml` | Requires one root, regular, non-symlink file at this name. |
| `forbidden_lockfiles` | `bun.lock`, `bun.lockb`, `npm-shrinkwrap.json`, `package-lock.json`, `yarn.lock` | Any matching root path that exists produces `ALTERNATIVE_LOCKFILE_PRESENT`. |
| npm allowed host | `registry.npmjs.org` | Applied only when a parsed lock entry exposes an explicit `resolution.tarball` or `resolution.url`. |
| npm direct-source prefixes | `file:`, `git+`, `http:`, `https:` | Applied by case-insensitive prefix comparison to non-`@kfm/` manifest specifiers. |
| internal npm scope | `@kfm/` | Matching dependency names must use `link:` or `workspace:` specifiers. |
| pnpm lockfile version | `9.0` | Compared as text with the root lockfile's `lockfileVersion`; mismatch is a repository scan error. |
| lock integrity | `true` | Requires a truthy `resolution.integrity` on package entries whose `resolution` is an object. |
| Python forbidden schemes | `file:`, `git+`, `http:`, `https:` | Applied to recognized direct-reference text in root PEP 621 dependencies. |
| Python editable-local flag | `allow_editable_local: true` | Schema-valid configuration, but the current validator does not read this field when scanning or deciding. It is not an implemented editable-install rule. |
| Outcomes | `PASS`, `DENY`, `ERROR` | Finite vocabulary declared by policy and used by the validator. |

The configuration also records explicit non-effects: it does not install or
resolve dependencies; prove registry, package, or publisher identity; verify
signatures, attestations, or vulnerabilities; authorize source or evidence;
approve policy or release; deploy; publish; or create public-use authority.

[Back to top](#top)

## What belongs here

Subject to accepted contracts, schemas, review, and versioning, this boundary
may contain:

- repository-level dependency-origin allow, deny, and error configuration;
- exact package-manager and lockfile ownership declarations;
- internal namespace and local-workspace binding rules;
- configured direct-source and explicit registry-host restrictions;
- stable profile, schema, outcome, finding-code, and compatibility metadata;
- policy-local non-effects and failure posture; and
- supersession or migration metadata for a future versioned profile.

A file belongs here because its primary responsibility is **dependency-origin
admissibility policy**. Mentioning a package, registry, lockfile, audit, SBOM,
workflow, container, or release does not make this directory its correct owner.

[Back to top](#top)

## What is prohibited

| Prohibited material | Owning surface or required action |
|---|---|
| Credentials, tokens, registry auth, signing keys, private registry URLs, or secret-bearing configuration | Do not commit here; use an approved secret-management and least-privilege path. |
| Package archives, wheels, tarballs, vendored dependency bytes, installed environments, caches, or `node_modules` | Approved package/cache/build infrastructure outside policy source; generated installations remain untracked. |
| Lockfiles or dependency manifests themselves | Their owning repository, application, package, pipeline, connector, or infrastructure roots. |
| Dependency contract or schema source | [`contracts/`](../../contracts/README.md) and [`schemas/`](../../schemas/README.md). |
| Validators, fixtures, and tests | [`tools/validators/`](../../tools/validators/README.md), [`fixtures/`](../../fixtures/README.md), and [`tests/`](../../tests/README.md). |
| Vulnerability reports, dependency-review findings, Scorecard SARIF, Trivy output, SBOMs, attestations, proofs, or run receipts | Their governed diagnostics, artifact, proof, or receipt families with explicit retention and sensitivity rules. |
| Source, evidence, review, policy-decision, release, correction, withdrawal, rollback, deployment, or publication instances | Their owning lifecycle, accountability, policy, or [`release/`](../../release/README.md) surfaces. |
| Runtime registry proxy, installer, resolver, firewall, worker, API, or update bot implementation | Application, package, infrastructure, workflow, or tool roots by primary responsibility. |
| A second independently writable copy of this policy | Version or supersede the canonical source and update its consumers; do not fork authority silently. |

Use minimal synthetic values for tests and examples. Do not paste real
credentials, private endpoints, proprietary package payloads, sensitive source
material, personal data, or harmful-precision locations into policy fixtures.

[Back to top](#top)

## Repository scan surface

The validator constructs a repository snapshot from a caller-supplied root.
Its current scan topology is exact and intentionally bounded:

| Surface | Included now | Not included now |
|---|---|---|
| Root npm manifest | Root `package.json`, including exact `packageManager` and four dependency fields | Other manifest fields, package provenance, scripts, overrides, engines, repository identity, signatures, and publish configuration |
| Workspace npm manifests | Existing one-level `apps/*/package.json` and `packages/*/package.json` | Recursive/nested packages, other responsibility roots, dynamically declared workspace patterns, and manifests outside those two globs |
| npm dependency fields | `dependencies`, `devDependencies`, `optionalDependencies`, `peerDependencies` | Bundled dependency declarations, overrides/resolutions semantics, importer parity, lifecycle scripts, and transitive manifest metadata |
| pnpm lockfile | Root configured lockfile; top-level `lockfileVersion`; `packages` entries with object-valued `resolution` | Importer completeness, snapshot graph closure, peer resolution, signature/attestation data, and entries without an object-valued `resolution` |
| Python project | Root `pyproject.toml` `project.dependencies` and every `project.optional-dependencies` array | `build-system.requires`, dependency groups, tool-specific dependencies, nested `pyproject.toml` files, requirements files, constraints, lockfiles, and installed distributions |
| Filesystem topology | Required root lockfile must be a regular non-symlink; unreadable or malformed required inputs become scan errors | Full path containment/supply-chain sandboxing, repository history, submodules, external package stores, or runtime filesystem state |

Missing or unreadable root `package.json` or `pyproject.toml`, and malformed
or unreadable content in an existing required lockfile, contributes
`REPOSITORY_SCAN_ERROR`. A missing required lockfile contributes
`LOCKFILE_MISSING` and therefore `DENY`; absence alone does not create a
repository scan error.

The profile does not discover the workspace from
[`pnpm-workspace.yaml`](../../pnpm-workspace.yaml). Its manifest globs are
hard-coded in the validator. Similarity between those paths and the current
workspace file does not make them a single source of truth.

[Back to top](#top)

## Finite outcomes and finding codes

### Outcomes

| Outcome | Current meaning | Exit behavior |
|---|---|---|
| `PASS` | The bounded snapshot produced no configured finding | CLI exits `0` |
| `DENY` | A policy-shape, collection-order, or declaration rule produced one or more findings without a repository scan error | CLI exits `1` |
| `ERROR` | Policy input could not be read or the repository snapshot could not be made safely and completely within the current parser | CLI exits `1` |

`DENY` and `ERROR` are deliberately distinct. A caller must not coerce an
error into permission, an empty result, or a weaker warning. The serialized
repository result includes only `authority`, sorted `findings`, `outcome`,
and `scope`.

### Finding-code inventory

| Family | Finding code | Trigger |
|---|---|---|
| Policy input | `POLICY_INPUT_INVALID` | Policy file is missing, unsafe, unreadable, or invalid JSON at CLI load time |
| Policy shape | `POLICY_SCHEMA_INVALID` | Policy does not conform to the closed Draft 2020-12 schema |
| Policy determinism | `POLICY_COLLECTION_NOT_SORTED_UNIQUE` | A configured collection is not sorted and unique |
| Repository read | `REPOSITORY_SCAN_ERROR` | Scan root resolution fails; a required package/TOML input is missing or unsafe; or parsed JSON, YAML, TOML, dependency-field, or lockfile structure is malformed, unreadable, or unsupported |
| Package manager | `PACKAGE_MANAGER_PIN_MISMATCH` | Root `packageManager` is not exactly `pnpm@11.17.0` |
| Lockfile ownership | `LOCKFILE_MISSING` | Configured root `pnpm-lock.yaml` is not a regular non-symlink file |
| Lockfile ownership | `ALTERNATIVE_LOCKFILE_PRESENT` | Any configured competing root lockfile path exists |
| Internal packages | `INTERNAL_PACKAGE_NOT_WORKSPACE_BOUND` | An `@kfm/` dependency does not start with `workspace:` or `link:` |
| Direct npm sources | `DIRECT_DEPENDENCY_SOURCE_FORBIDDEN` | A non-internal npm specifier begins with a configured forbidden prefix |
| Lock integrity | `LOCK_INTEGRITY_MISSING` | A parsed package-resolution entry lacks a truthy integrity value |
| Registry host | `REGISTRY_HOST_NOT_ALLOWED` | An explicit lock tarball/URL hostname is not in the allowlist |
| Python direct source | `PYTHON_DIRECT_REFERENCE_FORBIDDEN` | A recognized direct reference begins with a configured forbidden scheme |

Finding paths identify the bounded snapshot or policy location, not an
authenticated package, publisher, registry transaction, or root-cause proof.

[Back to top](#top)

## Package-manager and lockfile boundary

The profile requires the literal root declaration `pnpm@11.17.0` and the
literal root lockfile `pnpm-lock.yaml`. It denies the five configured
competing lockfile names.

This establishes neither package-manager binary identity nor execution:

- the validator does not invoke Corepack, pnpm, npm, Yarn, or Bun;
- it does not compare the installed pnpm binary with the declaration;
- it does not resolve or download a package;
- it does not prove that every workspace/importer is represented in the lock;
- it does not prove the lock was produced by trusted tooling; and
- it does not make the lockfile tamper-proof or signed.

The separate [pnpm audit-readiness validator](../../tools/validators/dependencies/pnpm_audit_readiness.py)
checks additional manager, engine, workspace-pattern, importer, and lock
readiness concerns for the audit workflow. That is a companion implementation,
not an extension silently owned by this policy profile.

[Back to top](#top)

## npm manifest boundary

For each included manifest, the validator reads the four ordinary dependency
maps and applies two rules:

1. dependency names beginning with `@kfm/` must use a specifier beginning
   with `workspace:` or `link:`; and
2. other dependency specifiers must not begin with `file:`, `git+`,
   `http:`, or `https:`.

The comparison is case-insensitive and prefix-based. The current profile does
not:

- reserve the `@kfm/` namespace or prove ownership of a registry scope;
- verify package or publisher identity;
- detect dependency confusion outside the configured internal prefix;
- constrain every npm-supported alias, VCS shorthand, local form, or protocol;
- require exact dependency versions;
- compare manifest dependencies with pnpm importers or resolved packages;
- inspect package lifecycle scripts or post-install behavior; or
- determine compatibility, licensing, maintenance, or release fitness.

An internal-looking name is not proof that its code is local or trusted.
Workspace binding is one repository-shape check, not an identity attestation.

[Back to top](#top)

## pnpm lockfile boundary

The lock parser loads YAML, compares `lockfileVersion` with `9.0`, then
iterates the top-level `packages` mapping. For entries with an object-valued
`resolution`, it records:

- the package key;
- `resolution.integrity`; and
- an explicit `resolution.tarball`, falling back to `resolution.url`.

When `require_integrity` is true, those recorded entries need a truthy
integrity field. If an explicit URL is present, its parsed hostname must equal
`registry.npmjs.org`.

Important limits remain:

- entries without an object-valued `resolution` are skipped by this check;
- implicit registry resolution carries no URL for host comparison;
- integrity is presence-checked, not cryptographically recomputed here;
- URL scheme, port, path, redirects, DNS, TLS, registry authentication, and
  mirror behavior are not validated;
- importers, snapshots, overrides, and full graph closure are not reconciled;
- signatures, attestations, SBOMs, and publisher identity are not checked; and
- a lockfile can pass this parser without being installed, audited, or proven
  reproducible.

[Back to top](#top)

## Python dependency boundary

The Python scan reads only root PEP 621 `project.dependencies` and every array
under `project.optional-dependencies`. It recognizes PEP 508 direct references
and several bare direct-reference prefixes, then denies only the four schemes
configured by policy: `file:`, `git+`, `http:`, and `https:`.

The parser can recognize bare `git:`, `github:`, `gitlab:`, and
`bitbucket:` prefixes, but the current decision logic does not deny them
unless a configured prefix also matches. Do not describe the present profile as
a complete VCS-reference deny rule.

The profile also does not inspect:

- `build-system.requires`—including the current root `hatchling` entry;
- dependency groups or tool-specific dependency tables;
- nested application, package, pipeline, or connector `pyproject.toml` files;
- requirements, constraints, or Python lock files;
- index URLs, hashes, wheels, sdists, editable-install syntax, installed
  distributions, or transitive dependencies; or
- package ownership, signatures, provenance, vulnerabilities, licenses, or
  compatibility.

`allow_editable_local: true` is stored and schema-valid but currently
unconsumed. It must not be treated as permission, denial, or implemented
editable-install handling.

[Back to top](#top)

## Relationship to adjacent supply-chain controls

These repository surfaces are related but remain separate in authority,
execution, network posture, inputs, outputs, and retention:

| Surface | Current bounded role | Not supplied by this lane |
|---|---|---|
| [Dependency-origin workflow](../../.github/workflows/dependency-origin-policy.yml) | Runs focused tests, fixtures, the current static repository scan, and exact generated-receipt integrity | Install-time registry identity, audit, signatures, SBOM, release, or publication |
| [Dependency scan](../../.github/workflows/dependency-scan.yml) | Installs a pinned Python audit tool, audits a hash-locked Python CI set, validates pnpm audit readiness, and queries pnpm advisory data | Vulnerability absence, provenance, compatibility, source integrity, or release approval |
| [Security workflow](../../.github/workflows/security.yml) | PR dependency review, Trivy repository/secret/misconfiguration scan, container builds/scans, and a default-branch Scorecard lane | Complete security proof or policy acceptance |
| [Scorecard workflow](../../.github/workflows/scorecard.yml) | Separate default-branch/scheduled OpenSSF Scorecard analysis, SARIF upload, and currently `publish_results: true` | Dependency-origin policy enforcement; its external publication behavior is not controlled here |
| [Dependabot](../../.github/dependabot.yml) | Proposes bounded ecosystem updates through pull requests with schedules, groups, cooldowns, labels, and assignees | Compatibility, security, review, merge, release, or publication approval |
| [pnpm audit readiness](../../tools/validators/dependencies/pnpm_audit_readiness.py) | No-network readiness checks for the locked pnpm audit command, including workspace/importer expectations | Advisory query results or this profile's policy authority |
| [Security policy](../../SECURITY.md) | Private-first vulnerability reporting and broad KFM security posture | A verified private contact, platform enforcement, or dependency-origin decision |
| [Generated receipts](../../data/receipts/generated/README.md) | AI-authoring provenance and exact artifact hashes | Technical proof, human approval, policy decision, release, or publication |
| [Release root](../../release/README.md) | Governed release, correction, withdrawal, and rollback boundary | Permission derived from a green dependency scan |

Registry authentication, package signing, SLSA-style provenance, attestations,
SBOM production and reconciliation, license policy, lifecycle-script admission,
artifact quarantine, and production registry egress require explicit owners and
controls. They are not silently implied by this directory.

[Back to top](#top)

## Validator and workflow execution boundary

### Local validator

The Python validator has two mutually exclusive modes:

```bash
python tools/validators/governance/validate_dependency_origin_policy.py --fixtures
python tools/validators/governance/validate_dependency_origin_policy.py --scan-root .
```

It reads local text files, produces deterministic JSON on standard output, and
returns zero only for a successful fixture suite or `PASS` repository result.
The focused test statically rejects network and write surfaces in the validator
source. This is a source-shape and test assertion, not an operating-system
network sandbox.

### Hosted workflow

The dedicated workflow:

- triggers on pull requests and main pushes touching the bounded policy slice,
  root dependency files, one-level npm manifests, or the original generated
  receipt, and also supports manual dispatch;
- grants `contents: read`, checks out without persisted credentials, and uses
  immutable action SHAs;
- declares `KFM_NO_NETWORK=1` and deterministic Python environment variables;
- installs the repository's declared Python test environment before validation;
- runs the seven focused tests, nine fixtures, and current repository scan;
- verifies the exact original generated receipt; and
- writes a trust-boundary summary to the GitHub job summary.

The Python dependency installation step may contact configured package
infrastructure and use runner caches. The subsequent validator does not install
or resolve project dependencies and does not run pnpm. A hosted runner, green
job, branch rule, or summary is not a package-origin attestation.

The workflow has no repository write permission and no release/deployment step.
Its summary is diagnostic process output, not a durable policy decision or
public artifact.

[Back to top](#top)

## Validation coverage and limits

### Current focused coverage

The seven unit tests establish:

1. the dependency-origin schema is a valid Draft 2020-12 schema;
2. the committed policy is closed and its configured collections are sorted
   and unique;
3. all nine synthetic fixture cases produce the exact expected outcome and
   finding-code set;
4. a minimal temporary repository passes;
5. an `@kfm/` registry escape is denied;
6. the validator source exposes no statically forbidden network or write
   surface; and
7. repeated CLI fixture runs are byte-deterministic.

The fixture suite includes one `PASS`, seven `DENY`, and one `ERROR`
case. Fixture polarity proves only the evaluator's behavior for those synthetic
snapshots.

### Repository-native commands

```bash
python -m unittest discover \
  --start-directory tests/validators/governance \
  --pattern 'test_dependency_origin_policy.py' \
  --verbose

python tools/validators/governance/validate_dependency_origin_policy.py \
  --fixtures

python tools/validators/governance/validate_dependency_origin_policy.py \
  --scan-root .

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-pass8-dependency-origin-policy-20260808.json \
  --repo-root .
```

Run these from the repository root in the declared Python environment. A local
subset cannot establish hosted required-check status, branch protection,
reviewer independence, external registry behavior, or production reliance.

### Coverage gaps

No current test closes the recursive workspace, additional Python manifest,
broader npm/VCS protocol, lock importer, explicit URL scheme/redirect,
cryptographic integrity recomputation, namespace ownership, signature,
attestation, SBOM, vulnerability, lifecycle-script, install sandbox, or
external-consumer gaps documented above.

[Back to top](#top)

## Generated receipt and provenance boundary

The dedicated workflow validates
[`genrec-pass8-dependency-origin-policy-20260808.json`](../../data/receipts/generated/genrec-pass8-dependency-origin-policy-20260808.json)
against the current [GENERATED_RECEIPT schema](../../schemas/contracts/v1/receipts/generated_receipt.schema.json)
and the exact bytes of nine profile artifacts.

Because that receipt binds this README by SHA-256, a substantive README change
requires dependency closure:

1. update the bound README hash in the existing receipt;
2. preserve the original receipt identity, emitter, timestamp, inputs, truth
   labels, and validation history rather than pretending the whole profile was
   regenerated; and
3. record the rebind transparently in the receipt notes and in a new
   provenance receipt for the documentation amendment.

This is an integrity maintenance action, not retroactive authorship, human
approval, policy acceptance, or evidence that the original nine-file slice is
correct. The original receipt remains `human_review.state: pending` until an
authorized reviewer acts.

Generated receipts belong in the generated-receipt lane. Do not place them
beside policy source, mutate their historical identity silently, or treat their
hash closure as release or public-use authority.

[Back to top](#top)

## Security, exposure, and retention

This directory is intended to contain public-safe repository policy source
only. It must never contain:

- registry, package-manager, GitHub, cloud, signing, or deployment credentials;
- private registry endpoints or authentication material;
- package contents, install logs with secrets, proprietary SBOM payloads, or
  restricted vulnerability details;
- personal data, protected cultural records, private-land details, or
  harmful-precision locations; or
- production access decisions, release keys, deployment state, or public data.

The static validator reads repository declarations and prints finding codes and
paths. Finding text should remain bounded and must not echo dependency payloads,
tokens, URLs with credentials, or other sensitive values.

This lane defines no retention, telemetry, network, cache, or deletion system.
Hosted runner logs, summaries, caches, SARIF, advisory queries, Scorecard
publication, and Dependabot pull requests belong to their respective workflows
and platform settings. Their actual retention and exposure remain separate
review concerns.

If a supply-chain weakness or credential exposure is discovered, follow
[`SECURITY.md`](../../SECURITY.md), minimize public detail, rotate affected
credentials through their owner, preserve necessary audit evidence, and use the
owning correction or release process. Editing this policy does not revoke an
already published package or deployed artifact.

[Back to top](#top)

## Related contracts, schemas, fixtures, tests, and workflows

| Evidence | Relationship and boundary |
|---|---|
| [Parent policy README](../README.md) | Inherited admissibility authority and non-authority boundaries |
| [Dependency-origin contract](../../contracts/governance/dependency_origin_policy.md) | Proposed human-readable semantic contract for this static guard |
| [Dependency-origin schema](../../schemas/contracts/v1/governance/dependency_origin_policy.schema.json) | Closed machine shape for the JSON configuration |
| [Policy JSON](./dependency_origin_policy.v1.json) | Current proposed machine projection consumed by the validator |
| [Validator](../../tools/validators/governance/validate_dependency_origin_policy.py) | Deterministic fixture and repository evaluator |
| [Focused tests](../../tests/validators/governance/test_dependency_origin_policy.py) | Seven bounded schema, policy, fixture, temporary-repository, source-shape, and determinism tests |
| [Fixture README](../../fixtures/contracts/v1/governance/dependency_origin_policy/README.md) and [cases](../../fixtures/contracts/v1/governance/dependency_origin_policy/cases.json) | Synthetic no-network inputs with finite expected outcomes |
| [Dedicated workflow](../../.github/workflows/dependency-origin-policy.yml) | Hosted exact-slice orchestration and original-receipt verification |
| [Original generated receipt](../../data/receipts/generated/genrec-pass8-dependency-origin-policy-20260808.json) | Exact authoring-provenance binding for the nine original profile artifacts |
| [GENERATED_RECEIPT schema](../../schemas/contracts/v1/receipts/generated_receipt.schema.json) and [validator](../../tools/validators/validate_generated_receipt.py) | Machine shape, cross-field rules, and exact artifact-hash checks for authoring receipts |
| [Directory Rules](../../docs/doctrine/directory-rules.md) and [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted placement and README-boundary governance |
| [Root registry](../../control_plane/root_registry.yaml) | Machine projection of root responsibilities; not an authority grant |
| [CODEOWNERS](../../.github/CODEOWNERS) | Review routing only |
| [Dependency scan](../../.github/workflows/dependency-scan.yml), [security](../../.github/workflows/security.yml), [Scorecard](../../.github/workflows/scorecard.yml), and [Dependabot](../../.github/dependabot.yml) | Separate update, audit, review, scan, analysis, artifact, and external-service lanes |

Together these files form a bounded proposed implementation slice. They do not
form a complete software-supply-chain assurance system.

[Back to top](#top)

## Authoring and review contract

A material policy or validator change should identify and validate:

- the threat model, bounded operation, actors, repository roots, dependency
  ecosystems, and protected boundaries;
- the canonical profile identity, semantic contract, schema, policy source,
  validator, fixture family, tests, workflow, and consumer;
- exact included and excluded manifests, fields, lockfile structures,
  protocols, registries, namespaces, package managers, and Python sources;
- finite outcomes, stable finding codes, error precedence, exit behavior, and
  public-safe diagnostics;
- deterministic no-network validation and separately declared networked
  installation, audit, or registry behavior;
- credentials, least privilege, egress, cache, log, artifact, SARIF, retention,
  and external-publication posture;
- publisher identity, signatures, attestations, SBOMs, vulnerabilities,
  licenses, lifecycle scripts, compatibility, and release concerns that remain
  outside the profile;
- positive, negative, malformed, missing, symlink, nested-workspace, alternate
  protocol, redirect, lock drift, and error fixtures as applicable;
- exact artifact-hash receipt closure and transparent provenance amendments;
  and
- compatibility, migration, supersession, correction, withdrawal, and rollback
  for every bound workflow or consumer.

README-only clarification requires policy, supply-chain/security, validation,
and documentation review. Policy, schema, validator, test, workflow, registry,
credential, package-manager, audit, artifact, release, or production-consumer
changes require the corresponding owners and independent review.

The author, validator, workflow, generated receipt, package manager, registry,
or update bot cannot be its own sole approver for a policy-significant
transition.

[Back to top](#top)

## Correction and rollback

This README revision and its provenance closure change documentation and
generated authoring receipts only. They do not change the JSON policy,
contract, schema, fixtures, validator, tests, workflow behavior, dependency
manifests, lockfiles, installed packages, audit configuration, runtime, release,
deployment, publication, or public behavior.

- **Before merge:** close or abandon the draft pull request. The target at the
  evidence base remains blob
  `00b7f768444911123191b001aa18079d02ea1423`.
- **After an authorized merge:** revert the documentation/provenance commit or
  apply a transparent forward correction that preserves corrected evidence and
  Git history.
- **Receipt correction:** rebind exact changed artifact hashes, retain the
  original receipt's historical identity, and document the amendment. Do not
  fabricate an earlier emitter, prompt, validation, or approval.
- **Policy correction:** version or supersede the policy, schema, fixtures,
  validator, tests, workflow, receipts, and consumers together. Do not edit the
  README to conceal incompatible behavior.
- **Unsafe dependency or release discovered:** stop affected installation,
  build, deployment, or publication paths; preserve bounded audit evidence;
  rotate credentials if needed; reassess packages and outputs; then use the
  owning security, correction, withdrawal, release, and rollback processes.

A Git revert can restore repository bytes. It cannot by itself uninstall a
package, invalidate a cache, revoke credentials, withdraw an artifact, correct
an external Scorecard result, or roll back a deployment.

[Back to top](#top)

## Review triggers and evidence snapshot

### Evidence snapshot

| Evidence | Reviewed identity |
|---|---|
| Repository base | `main@97e124e67320c811fe6528b4828747ff81c22d26` |
| Prior target README | `00b7f768444911123191b001aa18079d02ea1423` |
| Policy JSON | `3e087c69a5ee38a1988c1aad097a94c60e6fb950` |
| Parent policy README | `6c5021f9d92778581a4e9331a9dd6ddb7efc5e35` |
| Contract / schema | `a5949ac0f802c5213d9c8bc12be505caed011e6e` / `5b03f791dfc7710a065574b323964fbf571de272` |
| Validator / focused tests | `2a79c09213b24e855ff2e8a4a16086755bc3736f` / `ba2a7f4dc39fc62032ca2ea572d0bc9e8918ca8f` |
| Fixture README / cases | `c1c4aab4ea7d53f65735ad2c90266945a773a471` / `e57c563697a10e7b9c143f10fb884e4b41b33198` |
| Dedicated workflow | `3eeb78d3088fdd7e9b3602024d22968ef972cbc1` |
| Original generated receipt | `24b17beedc2b1f906c2c1dc232f176f1f9ca4a38` |
| GENERATED_RECEIPT schema | `fba21ed27ebccf1362fe397fe0c3ebd85e072685` |
| Directory Rules / ADR-0029 | `fd49a0b83e55cef52c1124281f093e263526898d` / `b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62` |
| Root registry / CODEOWNERS | `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` / `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` |
| Dependency scan / security / Scorecard | `127da480605f25f7be4987a73ab70c7072fe25a8` / `d4bab2d2092f91afb99c0f0c3d769c163e9f1a45` / `5fb47ecb50ac3be2be0b535bcb0e1ec423f7e4c2` |
| Dependabot / pnpm audit readiness | `b5c798807b973dba6145db0822ab88071479ab93` / `6b1a96ee1748867b45029d97fb4c584bdf466638` |
| Open-PR overlap | No open pull request was returned for the exact target immediately before authoring |
| Review date | 2026-08-12 |

Re-review this boundary when any of the following changes:

- a direct child, profile field, schema constant, status, authority,
  non-effect, generation relationship, or receipt hash;
- a manifest glob, dependency field, direct-reference parser, lockfile parser,
  registry-host rule, Python table, finding code, outcome, exit code, or error
  precedence;
- the root package-manager pin, lockfile, Python project, workspace topology,
  internal scope, allowed registry, or alternate lockfile set;
- fixtures, tests, deterministic/no-write/no-network assertions, workflow
  triggers, permissions, action pins, install steps, or exact receipt path;
- dependency scan, security, Scorecard, Dependabot, audit readiness, registry,
  package signing, attestation, SBOM, lifecycle-script, or release integration;
- Directory Rules, ADR-0029, parent policy authority, root-registry projection,
  CODEOWNERS, required checks, branch protection, or reviewer independence; or
- external installation, build, registry, release, deployment, or public
  reliance.

[Back to top](#top)

## Open verification register

| ID | Open item | State | Evidence needed to close |
|---|---|---|---|
| `SUP-001` | Accepted supply-chain policy owner and independent review route | **NEEDS VERIFICATION** | Approved steward assignments plus effective policy/security/validation review controls |
| `SUP-002` | Required-check and branch-protection enforcement | **NEEDS VERIFICATION** | Current platform settings and exact-head check evidence |
| `SUP-003` | Recursive and dynamically declared npm workspace coverage | **CONFIRMED absent from current scan** | Accepted discovery contract, safe path handling, nested fixtures, and migration plan |
| `SUP-004` | Complete npm direct-source and alias protocol coverage | **NOT ESTABLISHED** | Explicit protocol vocabulary, fixtures for every supported form, and compatibility review |
| `SUP-005` | Complete Python direct-reference coverage | **NOT ESTABLISHED** | Decision for bare VCS shorthands plus tests for all accepted/denied forms |
| `SUP-006` | Executable meaning of `allow_editable_local` | **CONFIRMED unconsumed** | Defined syntax, path containment, symlink behavior, fixtures, and validator implementation—or removal in a versioned profile |
| `SUP-007` | Python build-system, dependency-group, nested-project, requirements, constraints, and lock coverage | **CONFIRMED outside current scan** | Accepted scope and one canonical validator/lock strategy |
| `SUP-008` | pnpm importer, snapshot, override, and graph reconciliation | **NOT ESTABLISHED in this profile** | Cross-check contract, deterministic implementation, and drift fixtures |
| `SUP-009` | Cryptographic verification of integrity fields and lock provenance | **NOT ESTABLISHED** | Trusted package bytes, recomputation, signing/attestation trust roots, and replayable evidence |
| `SUP-010` | Registry, scope, package, and publisher identity | **NOT ESTABLISHED** | Authenticated registry configuration, namespace ownership, provenance, and fail-closed verification |
| `SUP-011` | Redirect, DNS, TLS, mirror, proxy, and credential-safe registry egress | **NOT ESTABLISHED** | Network policy, proxy/registry architecture, hostile redirect tests, secret controls, and run evidence |
| `SUP-012` | SBOM, vulnerability, license, lifecycle-script, compatibility, and artifact-quarantine closure | **SEPARATE / INCOMPLETE** | Owned controls with bound artifacts, finite outcomes, retention, receipts, and release gates |
| `SUP-013` | Hosted current-repository scan at the proposed exact head | **PENDING** | Dedicated workflow result for the final pull-request commit |
| `SUP-014` | Original generated-receipt rebind and amendment provenance | **PENDING in this draft** | Schema-valid exact hashes, transparent amendment note, and hosted receipt-integrity result |
| `SUP-015` | Production or external reliance on this profile | **UNKNOWN** | Repository plus external consumer inventory with owner confirmation |
| `SUP-016` | Release, deployment, and publication integration | **CONFIRMED unauthorized by this lane** | Separate governed gates and release evidence; this profile remains insufficient |

Until these items close through their owning authorities, this lane remains a
proposed, static, repository-declaration guard—not a complete supply-chain
security system.

[Back to top](#top)

## No-loss and change ledger

| Baseline element | Disposition |
|---|---|
| Stable path and H1 | Preserved |
| Existing statement that this directory holds proposed allow/deny configuration | Preserved and expanded with exact profile, scan, and authority boundaries |
| Existing prohibition on credentials, package bytes, installed environments, attestations, SBOMs, release decisions, and deployment state | Preserved and expanded into placement and security tables |
| Existing statement that the JSON is consumed by a no-network static validator | Preserved with exact inputs, outputs, commands, tests, and workflow caveat |
| Existing separation from registry authentication, signing, vulnerabilities, lifecycle scripts, and release attestations | Preserved and reconciled with adjacent repository controls |
| Existing warning that a pass is only repository hygiene | Preserved prominently and expanded through every trust boundary |
| Direct-child navigation and ownership | Added from the verified tree and accepted directory governance |
| Finding codes and finite outcomes | Added from exact validator behavior |
| Manifest, lockfile, and Python scan limitations | Added without upgrading intent into implementation |
| Generated-receipt dependency closure | Added because the hosted workflow binds this README's exact hash |
| Correction, rollback, review triggers, evidence identities, and open gaps | Added with reversible documentation-only posture |

This README does not upgrade `PROPOSED_STATIC_GUARD`, `authority: NONE`, a
green fixture, a static scan, a generated receipt, or a workflow result into an
accepted or operational supply-chain authority.

<p align="right"><a href="#top">Back to top</a></p>
