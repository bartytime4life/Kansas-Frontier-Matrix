<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<TODO-VERIFY-UUID>
title: configs/security/
type: standard
version: v1
status: draft
owners: @bartytime4life
created: TODO-VERIFY
updated: TODO-VERIFY-LIVE-GIT-DATE
policy_label: public
related: [../README.md, ../../policy/README.md, ../../contracts/README.md, ../../.github/workflows/README.md, ../../.github/SECURITY.md, ../../SECURITY.md, ../../tools/README.md, ../../tests/README.md, ../../scripts/README.md]
tags: [kfm, configs, security, supply-chain, thresholds, waivers]
notes: [Current public main shows this directory as README-only; both .github/SECURITY.md and root SECURITY.md exist and should stay aligned; exact UUID and git-tracked dates still need verification.]
[/KFM_META_BLOCK_V2] -->

# configs/security/

_Repo-visible, non-secret security thresholds, waivers, and scan-facing configuration surfaces for Kansas Frontier Matrix._

> **Status:** `experimental`  
> **Owners:** `@bartytime4life` *(inherited from `/configs/` in `.github/CODEOWNERS`; verify if a narrower owner is later added)*  
> **Path:** `configs/security/README.md`  
> **Repo fit:** security-config lane inside [`../README.md`](../README.md); upstream from [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS), [`../../.github/SECURITY.md`](../../.github/SECURITY.md), [`../../SECURITY.md`](../../SECURITY.md), [`../../policy/README.md`](../../policy/README.md), and [`../../contracts/README.md`](../../contracts/README.md); downstream into [`../../.github/workflows/README.md`](../../.github/workflows/README.md), [`../../tools/README.md`](../../tools/README.md), [`../../scripts/README.md`](../../scripts/README.md), and [`../../tests/README.md`](../../tests/README.md)  
> ![status](https://img.shields.io/badge/status-experimental-orange)
> ![owner](https://img.shields.io/badge/owner-%40bartytime4life-blue)
> ![path](https://img.shields.io/badge/path-configs%2Fsecurity%2FREADME.md-1f6feb)
> ![public main](https://img.shields.io/badge/public_main-README--only-lightgrey)
> ![scope](https://img.shields.io/badge/scope-non--secret%20security%20config-informational)
> ![posture](https://img.shields.io/badge/posture-config%20not%20policy-red)
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current snapshot](#current-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> Treat this lane as **config, not policy**.
> `configs/security/` is for repo-visible, non-secret operational settings.
> Executable deny/allow logic, policy bundles, and policy tests belong in [`../../policy/README.md`](../../policy/README.md).
> Secrets, tokens, private keys, and vault-managed material do **not** belong here.

---

## Scope

In KFM, security configuration is not a miscellaneous dump for “security-ish” files, and it is not a second policy engine.

This lane is for the narrow, reviewable subset of security settings that should remain:
- non-secret
- diffable in Git
- clearly consumed by workflows, tools, scripts, or runtime wiring
- subordinate to stronger trust surfaces such as contracts, executable policy, release proof, and governed correction

Typical examples include threshold files, allow/review/deny posture maps, short-lived waiver metadata, scanner profiles, and non-secret hardening defaults.

### Truth posture used in this README

| Label | Meaning here |
| --- | --- |
| **CONFIRMED** | Visible in the current public tree or directly supported by adjacent repo docs |
| **INFERRED** | Conservative implication drawn from those visible repo surfaces plus KFM doctrine |
| **PROPOSED** | Recommended working shape that fits KFM but is not proven as current-tree reality |
| **UNKNOWN** | Not verified strongly enough to present as settled current implementation |
| **NEEDS VERIFICATION** | Placeholder detail that should be checked against a live checkout before merge |

[Back to top](#configssecurity)

## Repo fit

| Aspect | Value |
| --- | --- |
| **Path** | `configs/security/README.md` |
| **Role** | Directory README for the security-specific slice of the repo-visible `configs/` lane |
| **Upstream** | [`../README.md`](../README.md) · [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) · [`../../.github/SECURITY.md`](../../.github/SECURITY.md) · [`../../SECURITY.md`](../../SECURITY.md) · [`../../policy/README.md`](../../policy/README.md) · [`../../contracts/README.md`](../../contracts/README.md) |
| **Downstream** | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) · [`../../tools/README.md`](../../tools/README.md) · [`../../scripts/README.md`](../../scripts/README.md) · [`../../tests/README.md`](../../tests/README.md) |
| **Why it exists** | To keep non-secret security behavior explicit without collapsing policy, contracts, workflows, tooling, disclosure posture, and secrets into one blurry surface |
| **Handoff rule** | If a file starts expressing executable allow/deny logic, schema authority, disclosure policy, or secret-bearing host values, it belongs somewhere else |

## Accepted inputs

These are the kinds of things that belong here.

| Input family | What fits | Typical examples |
| --- | --- | --- |
| **Threshold configs** | Reviewable knobs that determine fail / warn / review posture | vulnerability severity cutoffs, secrets-scan thresholds, allowed exception TTLs |
| **License / dependency posture maps** | Non-secret policy-adjacent value files consumed by checks | allow / review / deny license classes, approved dependency source rules |
| **Waiver metadata** | Short-lived exception records that stay human-reviewable | waiver ID, reason, scope, owner, expiry, linked issue / ADR |
| **Non-secret hardening defaults** | Safe operational defaults that do not reveal credentials | TLS minimums, header toggles, exposure flags, rate-limit defaults |
| **Scanner / check profiles** | Tool-facing selectors and ignore scopes that are safe to commit | path excludes, file globs, package selectors, scan profile names |
| **Illustrative examples** | Starter files that make review concrete without claiming live use | example YAML, profile templates, review notes |

## Exclusions

These do **not** belong here.

| Does not belong here | Why | Put it in / near |
| --- | --- | --- |
| **Secrets, tokens, private keys, local certs** | Secret-bearing material should not be committed into a repo-visible config lane | Host-local secret manager, vault, ignored local files, deployment secret surfaces |
| **Executable policy bundles or `.rego` rules** | KFM keeps config separate from executable deny/allow logic | [`../../policy/README.md`](../../policy/README.md) |
| **Machine-readable contracts and schemas** | Contracts are a stronger trust surface than runtime knobs | [`../../contracts/README.md`](../../contracts/README.md) |
| **Workflow orchestration YAML** | Workflow files are the automation lane, not the config lane | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) |
| **Disclosure instructions, reporting contacts, or coordination timelines** | Public reporting posture is a security-policy surface, not an operational threshold file | [`../../.github/SECURITY.md`](../../.github/SECURITY.md) and [`../../SECURITY.md`](../../SECURITY.md) |
| **Generated reports, SBOMs, attestations, telemetry outputs** | Emitted artifacts are outputs, not source config | Workflow-managed report / release / evidence surfaces |
| **Security tool implementation code** | Code belongs with tooling or script entrypoints | [`../../tools/README.md`](../../tools/README.md) or [`../../scripts/README.md`](../../scripts/README.md) |
| **Business or domain law hiding as “settings”** | Slow-moving truth-bearing rules should not disappear into mutable config | Promote to contracts, policy, or package-level code after review |

## Current snapshot

The safest current statement is deliberately narrow.

### Confirmed current public `main` state

```text
configs/security/
└── README.md
```

That means this README must do two jobs at once:
1. document what the lane is for, and
2. avoid pretending that a richer internal subtree is already proven in the visible branch.

### Confirmed adjacent security-doc context

| Path | Current public signal | Why it matters here |
| --- | --- | --- |
| `.github/SECURITY.md` | GitHub-facing security policy says this is the intended canonical path | Disclosure posture stays separate from operational config |
| `SECURITY.md` | Secondary public path also exists | It should delegate or remain text-aligned instead of being redefined here |

### Confirmed parent-lane context

```text
configs/
├── deployment/
├── env/
├── observability/
├── security/
├── ui/
├── README.md
└── env.schema.json
```

> [!WARNING]
> Do not treat the working shape below as a claim that those files already exist.
> They are **PROPOSED** until a live checkout proves otherwise.

## Directory tree

### Working shape for this lane (PROPOSED)

```text
configs/security/
├── README.md
├── vuln_policy.yaml          # vulnerability thresholds / fail-warn posture
├── license_policy.yaml       # license review / allow / deny posture
├── waivers.yaml              # short-lived, reviewable exceptions
└── profiles/
    └── README.md             # optional per-scanner or per-check notes
```

### Interpretation rules

- `vuln_policy.yaml` and `license_policy.yaml` are useful starter names for a KFM security-config lane, but they are **not** treated here as confirmed current-tree files.
- `waivers.yaml` is a **PROPOSED** consolidation pattern. A live tree may instead split waivers by tool, environment, or release class.
- `profiles/` is optional. Add it only if multiple tools actually consume distinct profiles.

## Quickstart

Use this section to inspect reality before expanding the lane.

```bash
# 1) See what is actually present
find configs/security -maxdepth 3 -type f | sort

# 2) Find current consumers or references
git grep -nE 'configs/security|vuln_policy|license_policy|waiver|sbom|secrets_scan|cosign|attest' -- .

# 3) Re-read adjacent boundary docs before adding files
sed -n '1,200p' configs/README.md
sed -n '1,200p' policy/README.md
sed -n '1,200p' .github/workflows/README.md
sed -n '1,200p' contracts/README.md

# 3b) Keep disclosure policy separate from config
sed -n '1,200p' .github/SECURITY.md
sed -n '1,200p' SECURITY.md

# 4) Keep review focused on this lane
git diff -- configs/security/
```

## Usage

### Operating rules

1. **Keep it non-secret.**  
   If a value would be unsafe to publish in a public branch, it does not belong here.

2. **Keep it finite and reviewable.**  
   Thresholds should converge on clear outcomes such as `fail`, `warn`, or `review`, not hand-wavy prose.

3. **Keep waivers explicit and short-lived.**  
   KFM should prefer bounded exceptions with owner, reason, and expiry over permanent silent ignores.

4. **Keep config subordinate to policy.**  
   Config may feed policy-aware checks, but it should not become the hidden place where governance law drifts.

5. **Make consumers obvious.**  
   Every committed config file should name its primary consumer: workflow, tool, script, or runtime surface.

6. **Prefer deterministic behavior.**  
   The same commit plus the same config should produce the same check posture and the same class of findings.

### Waiver minimum fields

| Field | Why it matters |
| --- | --- |
| `id` | Stable reference for audit, review, and later removal |
| `reason` | Human-readable justification |
| `scope` | Exact package, path, image, dependency, or check being waived |
| `owner` | Who is responsible for the exception |
| `approved_by` | Review trail |
| `expires_at` | Forces revisit instead of permanent drift |
| `ticket` | Link to remediation or architecture discussion |
| `notes` | Short supporting context, kept concise |

> [!NOTE]
> If a waiver needs cryptographic proof, token validation, or executable allow/deny branching, the stronger enforcement logic belongs in policy or workflow code, not in this directory alone.

[Back to top](#configssecurity)

## Diagram

```mermaid
flowchart LR
    A[policy/] -->|normative law| B[configs/security/]
    C[contracts/] -->|schema / contract boundaries| B
    D[.github/SECURITY.md + SECURITY.md] -->|reporting / disclosure posture| B

    B --> E[.github/workflows/]
    B --> F[tools/]
    B --> G[scripts/]
    B --> H[tests/]

    E --> I[security checks]
    F --> I
    G --> I
    H --> I

    I --> J[reports / evidence / release artifacts]

    S[(Secrets / vault / host-local)] -. never committed .-> B
```

A useful mental model is simple: `configs/security/` tunes **non-secret security behavior**, but it should not replace policy, contracts, disclosure policy, or secret management.

## Tables

### Security config family matrix

| Family | Belongs here? | Typical contents | Status in this README |
| --- | --- | --- | --- |
| Vulnerability posture | Yes | fail / warn severities, approved waiver model, review windows | **PROPOSED** |
| License posture | Yes | allow / review / deny classes, escalation paths | **PROPOSED** |
| Secrets-scan posture | Yes | thresholds, ignore scopes, path filters | **PROPOSED** |
| Attestation / provenance posture | Maybe | require signatures, checksum presence, telemetry toggles | **PROPOSED** |
| Runtime hardening defaults | Maybe | non-secret exposure flags, TLS minima, header toggles | **NEEDS VERIFICATION** |
| Rego bundles / executable allow-deny logic | No | policy rules, tests, decision grammar | **EXCLUDED** |
| Disclosure / reporting policy | No | reporting channels, coordination rules, public security policy | **EXCLUDED** |
| Secret material | No | tokens, passwords, private certs | **EXCLUDED** |

### Review triggers

| Change type | Review expectation | Minimum proof |
| --- | --- | --- |
| Severity threshold changes | Re-check workflows and tools that consume the file | diff + consumer confirmation |
| New waiver | Verify owner, reason, scope, and expiry | issue / ADR / remediation link |
| New ignore / allowlist entry | Prove it suppresses a false positive, not a real risk | sample finding or test evidence |
| New attestation toggle | Verify downstream workflow and artifact expectations still align | workflow / tool review |
| New hardening default | Verify it is non-secret and environment-safe | consumer + rollout note |
| Any file that starts encoding business law | Stop and move it to a stronger surface | contract / policy design review |

## Task list — Definition of done

- [ ] The file is **non-secret** and safe for a repo-visible lane.
- [ ] The primary consumer is named in a comment, README note, or adjacent doc.
- [ ] Any waiver entry is short-lived, owned, and reviewable.
- [ ] Threshold changes are paired with test or consumer validation.
- [ ] The change does not smuggle executable policy into config.
- [ ] The change does not create a parallel schema or contract authority.
- [ ] The change does not create a second disclosure-policy surface inside `configs/security/`.
- [ ] Proposed file names and paths were checked against the live tree before merge.
- [ ] This README stays honest about **CONFIRMED** versus **PROPOSED** structure.

## FAQ

### Why not put Rego or policy bundles here?

Because KFM benefits from keeping **config surfaces** and **executable policy surfaces** separate. This directory can feed checks; it should not silently become the only place where allow/deny law lives.

### Can this directory contain secrets?

No. If the value would be unsafe to expose in a repo-visible branch, move it out of this lane.

### Are `vuln_policy.yaml` and `license_policy.yaml` current repo files?

Not confirmed from the current public tree. They are useful **PROPOSED** starter names, not asserted current facts.

### Can a config here block CI?

Yes, but only through a consuming workflow, tool, script, or runtime. Config alone is not enforcement.

### Should disclosure policy or vulnerability reporting contacts live here?

No. Keep public reporting and coordinated disclosure rules in [`../../.github/SECURITY.md`](../../.github/SECURITY.md). The root [`../../SECURITY.md`](../../SECURITY.md) should delegate or remain text-aligned; this directory is for non-secret operational settings, not public reporting policy.

### When should a file leave this directory?

When it becomes one of the following:
- executable policy
- machine-readable contract authority
- generated evidence / report output
- secret-bearing host or deployment material
- substantial implementation code

## Appendix

<details>
<summary>Illustrative starter YAML (PROPOSED, not current-tree fact)</summary>

### `vuln_policy.yaml`

```yaml
version: 1
consumer: security-supply-chain
severity:
  fail_on:
    - critical
    - high
  warn_on:
    - medium
    - low
waivers:
  require_id: true
  require_reason: true
  require_owner: true
  require_expires_at: true
  default_max_ttl_days: 14
dependency_rules:
  require_lockfiles: true
  require_pinned_sources: true
notes:
  - "Illustrative only; verify exact consumer and key names before merge."
```

### `license_policy.yaml`

```yaml
version: 1
consumer: security-supply-chain
licenses:
  allow:
    - MIT
    - BSD-2-Clause
    - BSD-3-Clause
    - Apache-2.0
  review:
    - MPL-2.0
    - LGPL-3.0-only
  deny:
    - GPL-3.0-only
    - AGPL-3.0-only
actions:
  on_allow: continue
  on_review: require_manual_review
  on_deny: fail
notes:
  - "Illustrative only; policy meaning remains subordinate to reviewed repo doctrine."
```

### `waivers.yaml`

```yaml
version: 1
waivers:
  - id: kfm-sec-0001
    scope: dependency:example-package
    reason: "False positive under current scanner rule"
    owner: "@owner"
    approved_by: "@reviewer"
    ticket: "ADR-OR-ISSUE-ID"
    expires_at: "2026-04-30T00:00:00Z"
    notes: "Remove after upstream fix is adopted"
```

</details>

[Back to top](#configssecurity)
