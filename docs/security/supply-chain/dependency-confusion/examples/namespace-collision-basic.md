<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-NEEDS-ASSIGNMENT>
title: Namespace Collision (Basic)
type: standard
version: v1
status: draft
owners: <owners-NEEDS-VERIFICATION>
created: <YYYY-MM-DD-NEEDS-SET>
updated: <YYYY-MM-DD-NEEDS-SET>
policy_label: <policy_label-NEEDS-VERIFICATION>
related: [<docs/security/supply-chain/dependency-confusion/examples/README.md-NEEDS-REPO-VERIFICATION>]
tags: [kfm]
notes: [illustrative npm-focused dependency-confusion example; current-session workspace evidence was PDF-only; mounted manifests, lockfiles, .npmrc, and CI workflow YAML were not directly inspected]
[/KFM_META_BLOCK_V2] -->

# Namespace Collision (Basic)

Minimal, non-live example of how ambiguous package naming and ambiguous registry routing can cross a software trust boundary.

> [!IMPORTANT]
> This file documents the **shape of the failure**, not a verified live KFM incident. In this session, the directly accessible workspace evidence was PDF-only. No mounted repo checkout, `package.json`, lockfiles, `.npmrc`, or CI workflow YAML were directly inspected. Package names, scopes, registry hosts, and paths below are therefore illustrative unless later reverified.

| Aspect | Status | Notes |
|---|---|---|
| Threat class | CONFIRMED | Namespace collision / dependency confusion is a real package-resolution risk. |
| KFM doctrinal fit | CONFIRMED | KFM doctrine favors explicit contracts, fail-closed gates, and visible proof before promotion. |
| Example ecosystem | PROPOSED | npm is used here because scope and registry behavior are easy to show compactly. |
| Current KFM package manager / registry posture | UNKNOWN | No manifests, lockfiles, or registry config were directly inspected in this session. |
| Example names and hosts | PROPOSED | `widget-utils`, `@kfm/widget-utils`, and the registry hosts below are placeholders. |

## Background

A namespace collision happens when a build intends to use an internal package such as `widget-utils`, but the dependency is referenced in a way that still allows the package manager to resolve a public package with the same name instead.

> [!NOTE]
> The core failure is **resolution ambiguity**. This example deliberately avoids payload mechanics and focuses on the boundary mistake that lets the wrong package source enter a build.

## Failure shape

```mermaid
flowchart LR
    A[Manifest requests widget-utils] --> B{Owned scope<br/>and registry-bound?}
    B -- No --> C[Default registry lookup]
    C --> D[Public package with same name exists]
    D --> E[Wrong trust boundary enters build]
    E --> F[Build may still appear green]
    B -- Yes --> G[Scoped package lookup]
    G --> H[Private registry only]
    H --> I[Source intent stays reviewable]
```

## Vulnerable shape

### Manifest

```json
{
  "name": "kfm-example-app",
  "private": true,
  "dependencies": {
    "widget-utils": "^1.4.2"
  }
}
```

### Ambiguous registry config

```ini
registry=https://registry.npmjs.org/
# No scope-to-registry mapping.
# No rule that forces internal packages into an owned namespace.
```

### Why this fails

1. The dependency name is unscoped.
2. The installer falls back to the default registry.
3. A public package with the same name can satisfy the request.
4. The build receives code from the wrong trust boundary.

## Tell-tale lockfile clue

If a reviewer believes `widget-utils` is internal-only, a lockfile entry like the following is already a failure signal:

```text
"node_modules/widget-utils": {
  "version": "1.4.2",
  "resolved": "https://registry.npmjs.org/widget-utils/-/widget-utils-1.4.2.tgz"
}
```

The exact lockfile format varies by tool and version, but the review question does not: **did the dependency resolve from the intended trust boundary?**

## Simulated detection output

> [!NOTE]
> The output below is illustrative. It shows the kind of failure a governed review path should emit; it is **not** a current-session KFM CI log.

```text
FAIL validation.schema_failed
detail: internal-looking dependency is unscoped

FAIL policy.denied
detail: resolved package source crossed the intended trust boundary
package: widget-utils
resolved: https://registry.npmjs.org/widget-utils/-/widget-utils-1.4.2.tgz
obligation: withhold
```

## Safer shape

### Scoped dependency

```json
{
  "name": "kfm-example-app",
  "private": true,
  "dependencies": {
    "@kfm/widget-utils": "1.4.2"
  }
}
```

### Scope-bound registry config

```ini
registry=https://registry.npmjs.org/
@kfm:registry=https://packages.example.internal/npm/
```

### Why this is materially better

- `@kfm/widget-utils` is namespaced.
- The `@kfm` scope is bound to one registry.
- Public and private trust zones are no longer competing for the same dependency name.
- Reviewers can reason about intended source directly from the manifest and config.

## Signals reviewers should look for

| Signal | Why it matters | Expected response |
|---|---|---|
| Unscoped internal-looking package names | Highest namespace-collision risk | Reject or rename into an owned scope |
| Missing scope-to-registry mapping | Resolution can drift to the default registry | Add explicit `@scope:registry=` rule |
| Lockfile resolves an internal-only dependency from a public host | Trust boundary has already been crossed | Fail review and regenerate from the intended source |
| Mixed public/private naming without a declared source policy | Human review becomes guesswork | Add an allowlist, registry policy, or equivalent contract surface |
| Installs succeed without source assertions | Build can pass for the wrong reason | Add merge-blocking verification |

## KFM-aligned governed posture

In KFM terms, this is not just a package-manager hygiene issue. It is a publication-trust issue: the build must prove where code came from before later surfaces can trust what they are serving.

| Governed artifact family | What it should carry for this failure mode |
|---|---|
| SourceDescriptor or equivalent source contract | Owned namespace, approved registry family, access model, and validation intent for internal package sources |
| ValidationReport | Manifest, registry-config, and lockfile source checks with machine-readable failures |
| DecisionEnvelope | Allow/deny result plus reason and obligation codes when the wrong registry resolves |
| ReleaseManifest / proof pack | Exact resolved package sources that entered the release candidate |
| CorrectionNotice | Supersession path if a build or release consumed the wrong source and must be replaced |

### Minimal control expectations

1. Internal packages use an owned scope.
2. Scope-to-registry mapping is explicit.
3. Dependency-source checks are merge-blocking, not advisory.
4. Lockfiles are reviewed as trust-boundary evidence, not just install artifacts.
5. A bad resolution path has a correction path: lockfile rotation, rebuild, and visible supersession where needed.

## Reviewer guidance

- Never infer “internal” solely from a package’s name.
- Treat a public-host resolution for an internal-only dependency as a hard failure, not a warning.
- Keep source intent visible in the manifest, registry config, and lockfile together.
- Do not claim current KFM enforcement details until manifests, lockfiles, and workflow YAML are directly reverified.

## Minimal review checklist

- [ ] Internal packages use an owned scope.
- [ ] Scope-to-registry mapping is explicit.
- [ ] Lockfile does not resolve internal packages from a public host.
- [ ] Validation fails closed when source-boundary expectations are violated.
- [ ] Release notes or proof artifacts capture the dependency-source decision when it matters.

## What remains to verify in the mounted repo

<details>
<summary>Open verification items</summary>

The current session did not directly expose a mounted repo checkout, so the following remain unverified:

- actual package manager in use (`npm`, `pnpm`, `yarn`, or other)
- presence or absence of `.npmrc` files
- current internal package naming conventions
- lockfile host patterns
- whether any workflow YAML currently enforces dependency-source checks
- whether this example already exists at `docs/security/supply-chain/dependency-confusion/examples/namespace-collision-basic.md` or nearby paths suggested by earlier attached idea material

</details>

## Takeaway

Use this example to document the **shape of the failure**: ambiguous names plus ambiguous registry routing. In KFM terms, the fix is not only “use scopes.” The fix is to make package-source intent explicit, reviewable, testable, and fail-closed before promotion.
