<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-VERIFY-UUID
title: configs/
type: standard
version: v1
status: review
owners: TODO(verify platform/config owners)
created: TODO(verify YYYY-MM-DD)
updated: TODO(verify YYYY-MM-DD)
policy_label: TODO(verify directory classification)
related: [TODO(verify related paths: ../README.md, ../contracts/, ../policy/, ../infra/, ../apps/, ../packages/, ../tests/, ../scripts/, ../migrations/, ../examples/)]
tags: [kfm, configs, runtime, orchestration, observability, deployment]
notes: [Source-bounded draft. The March 2026 KFM manuals clearly establish configuration/package boundary discipline and continuity docs describe a root-level configs/ lane, but owners, UUID, dates, policy label, live subpaths, and exact validation commands still require direct repo verification before merge.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# configs/

_Repo-visible configuration templates and non-secret value surfaces for KFM runtime wiring, orchestration, shell defaults, observability, and deployment._

> **Status:** experimental  
> **Owners:** TODO(verify platform / config owners)  
> **Path:** `configs/README.md`  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![owners](https://img.shields.io/badge/owners-TODO-lightgrey) ![path](https://img.shields.io/badge/path-configs%2FREADME.md-blue) ![scope](https://img.shields.io/badge/scope-non--secret%20config-informational) ![truth](https://img.shields.io/badge/truth-source--bounded-lightgrey) ![posture](https://img.shields.io/badge/posture-fail--closed-red)  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree-working-shape-not-mounted-fact) · [Quickstart](#quickstart) · [Usage rules](#usage-rules) · [Diagram](#diagram) · [Reference tables](#reference-tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> This README is **source-grounded but repo-constrained**. The current session exposed March 2026 KFM manuals and continuity materials, but **not a mounted repository checkout**. Treat literal subpaths, owners, validation commands, and subdirectory names below as **review-ready after live repo verification**, not as already-confirmed filesystem fact.

## Scope

In KFM, configuration is not treated as a cosmetic settings bucket. It is a **trust-bearing operational surface**: it influences how governed services bind, which released scope they may read, where workers run, how shell defaults behave, and whether fail-closed behavior is preserved.

This `configs/` README covers the **repo-visible subset** of that broader configuration domain:

- non-secret templates
- reviewed defaults
- environment schemas and examples
- deployment and runtime value surfaces
- orchestration and observability settings that benefit from diffable review

It does **not** collapse the rest of KFM’s governing surfaces into one folder. Contracts, executable policy bundles, host-local secrets, release evidence, and canonical data remain separate on purpose.

### Truth posture for this README

| Label | How it applies here |
| --- | --- |
| **CONFIRMED** | March 2026 KFM design material explicitly treats configuration/package boundaries as trust-bearing, separates configuration from business and governance logic, and documents `configs/` as a root-level repo lane in continuity inventory. |
| **INFERRED** | The README path, sibling relationships, and several likely config families align with the attached corpus, but were not rechecked against a mounted checkout in this session. |
| **PROPOSED** | Working subdirectory names, example file shapes, validation commands, and note-backed config lanes such as orchestration, observability, or security thresholds. |
| **UNKNOWN** | Exact owners, exact live tree contents, exact CI wiring, exact package manifests, exact loader paths, and exact review/publish commands in the mounted repo. |
| **NEEDS VERIFICATION** | Any literal filename, subdirectory, badge target, owner assignment, or validation command that depends on the live repo rather than the directly visible source corpus. |

## Repo fit

| Field | Value |
| --- | --- |
| Path | `configs/README.md` |
| Directory role | Repo-visible home for non-secret configuration templates, reviewed defaults, environment schemas, and runtime/deployment value surfaces |
| Doctrinal baseline | March 2026 KFM configuration/package architecture material in the master design manual, Components Pass 5, repo-inventory compendium, and local-runtime/Ollama guide |
| Continuity repo signal | The current continuity corpus documents `configs/` as a root-level repo lane alongside `apps/`, `packages/`, `contracts/`, `policy/`, `infra/`, `tests/`, `scripts/`, `migrations/`, and `examples/` |
| Main consumers | governed API, workers, projection jobs, local/private host runtime, deployment overlays, shell defaults, observability surfaces |
| Review posture | Treat config edits as architecture-significant when they alter exposure, publication, policy behavior, citation enforcement, release scope, or negative-state handling |

### Upstream / downstream links

| Relationship | Paths | Status |
| --- | --- | --- |
| Governance / law sources | [`../contracts/`](../contracts/) · [`../policy/`](../policy/) · [`../docs/`](../docs/) · [`../infra/`](../infra/) | continuity-documented, **NEEDS VERIFICATION** against live checkout |
| Main runtime consumers | [`../apps/`](../apps/) · [`../packages/`](../packages/) · [`../tests/`](../tests/) · [`../scripts/`](../scripts/) | continuity-documented, **NEEDS VERIFICATION** against live checkout |
| Neighboring operational lanes | [`../migrations/`](../migrations/) · [`../examples/`](../examples/) | continuity-documented, **NEEDS VERIFICATION** against live checkout |
| Host-side companions | `/etc/kfm/*.env` · systemd unit/drop-ins · secret manager / host secret surface | documented host pattern; **not** evidence that these are versioned repo paths |

## Accepted inputs

| Category | Typical contents | Why it belongs here |
| --- | --- | --- |
| Environment schemas and examples | `env.schema.json`, `.env.example`-style templates, bind/path examples, non-secret defaults | Makes runtime wiring reviewable without committing secrets |
| Deployment/runtime values | ConfigMap-style values, service parameters, host/runtime examples, rollout-facing settings | Parameterizes deployment without redefining project law |
| Orchestration bindings | worker cadence defaults, scheduler values, platform bindings, queue/profile settings | Keeps operational behavior explicit and diffable |
| Shell / renderer defaults | non-secret UI flags, portrayal defaults, trust-visible shell settings | Lets shell behavior vary without hiding governance in frontend code |
| Observability defaults | collector/exporter config, log field maps, trace/join-key surfaces, alert thresholds without secrets | Supports operational evidence without turning logs into tribal knowledge |
| Security thresholds and waivers | vulnerability/license thresholds, scan configuration, audit policy values that are **not** executable governance bundles | Useful as operational config when kept clearly separate from `policy/` |

### What belongs here in practice

- non-secret env examples
- environment schema files
- deploy/runtime value files
- scheduler/orchestrator bindings
- observability config without secrets
- shell or renderer defaults that do not encode authoritative business meaning
- reviewed thresholds or waivers for operational tooling

## Exclusions

| Do **not** keep here | Put it instead | Why |
| --- | --- | --- |
| Real credentials, tokens, private keys, live connection secrets | secret manager or host-local protected files such as `/etc/kfm/*.env` | Versioned `configs/` must stay non-secret |
| JSON Schemas, OpenAPI contracts, controlled vocabularies treated as machine law | [`../contracts/`](../contracts/) | Contracts need first-class review, validation, and versioning |
| Executable Rego / Conftest bundles, reason codes, obligation codes, release policy | [`../policy/`](../policy/) | Governance should remain explicit, testable, and separately reviewable |
| Release manifests, proof packs, attestations, correction notices | release/proof location *(verify exact path)* | Trust-bearing publication evidence is not ordinary config |
| Database migrations | [`../migrations/`](../migrations/) | Schema evolution needs replay discipline and release handling |
| Generated local state, caches, temp files, build outputs | ignored runtime/cache/build directories | Reviewable config should remain stable and intentional |
| RAW / WORK / PROCESSED / CATALOG / PUBLISHED data or canonical business records | canonical data/store lanes | Config may point at these layers, but it does not replace them |

> [!WARNING]
> The broader KFM doctrine is clear that **configuration is not the same thing as law**. If a file defines schema rules, policy semantics, release criteria, or evidence resolution behavior, it probably belongs outside `configs/`.

## Directory tree (working shape, not mounted fact)

```text
configs/
├── README.md
├── env.schema.json
├── env/
├── deployment/
├── orchestration/
├── ui/
├── observability/
└── security/
```

How to read this tree:

- `env.schema.json` is a **documented proposed artifact** in the March 2026 design material.
- `env/` and `deployment/` are **inferred working lanes** for non-secret examples and runtime value surfaces.
- `orchestration/`, `ui/`, `observability/`, and `security/` are **doctrine-consistent proposed lanes**, not mounted-fact claims.
- `security/` here means **non-secret operational settings** such as thresholds or waivers, **not** executable policy bundles.

## Quickstart

1. Inspect the live `configs/` tree before editing anything.
2. Decide whether the change is truly configuration, or whether it belongs in `contracts/`, `policy/`, migrations, or host-local secret surfaces.
3. Make the smallest useful non-secret change.
4. Run the repo’s actual validation path before merge.

```bash
# Inspect the visible config surface.
find configs -maxdepth 3 -type f | sort

# Search for KFM-specific config keys and nearby consumers.
git grep -nE "KFM_(ARTIFACT_ROOT|POLICY_DIR|DB_DSN|MODEL_ADAPTER_URL|PUBLISHED_ONLY|CITATIONS_REQUIRED|BIND)" . || true

# Look for config validation or route-family checks.
git grep -nE "(env\.schema|config schema|forbidden import|route-family|dependency graph)" . || true
```

Illustrative runtime key surface:

```dotenv
# Example only — review against the live repo and host runtime before use.

KFM_ARTIFACT_ROOT=/srv/kfm
KFM_POLICY_DIR=/etc/kfm/policy
KFM_DB_DSN=unix:///var/run/postgresql/.s.PGSQL.5432
KFM_MODEL_ADAPTER_URL=http://127.0.0.1:11434
KFM_PUBLISHED_ONLY=true
KFM_CITATIONS_REQUIRED=true
KFM_BIND=127.0.0.1:8080
```

> [!NOTE]
> Real secret-bearing environment files belong **outside** versioned `configs/`. The current host-runtime guidance proposes root-owned files such as `/etc/kfm/kfm-api.env`, `/etc/kfm/kfm-worker.env`, `/etc/kfm/kfm-publish.env`, and an Ollama override or systemd drop-in.

## Usage rules

### 1) Keep `configs/` non-secret and reviewable

Commit examples, schemas, defaults, and reviewed value surfaces.  
Do **not** commit live credentials, one-machine hacks, or anything whose only safe home is a protected host file.

### 2) Keep configuration subordinate to law

Configuration expresses wiring, defaults, thresholds, and runtime shape. It must not quietly become the place where schema law, evidence law, or publication governance actually lives.

### 3) Review trust-affecting config like code

A “small config change” can widen network exposure, loosen release scope, weaken citation behavior, or change visible failure semantics. In KFM, those are architecture changes, not housekeeping.

### 4) Preserve explicit package and runtime boundaries

Keep renderer, shell, server, workers, contracts, policy, and evidence resolution separated. Config should reinforce those boundaries, not blur them.

### 5) Keep one canonical home per concern

Avoid duplicating the same rule across `configs/`, `contracts/`, `policy/`, application code, and deployment overlays. One concern should have one primary owner.

### 6) Make config dependence visible in outputs that need it

If a release artifact, projection build, or bounded synthesis path materially depends on configuration, the surrounding manifest, receipt, or provenance should be able to point back to the relevant config version or snapshot.

> [!CAUTION]
> A convenient config toggle that weakens citation, publication, scope handling, or trust visibility is not a convenience. It is a governance change.

## Diagram

```mermaid
flowchart TD
    A[configs/] --> B[env.schema.json + env examples]
    A --> C[deployment values]
    A --> D[orchestration bindings]
    A --> E[ui / renderer defaults]
    A --> F[observability defaults]
    A --> G[security thresholds / waivers]

    B --> H[API + workers + local runtime]
    C --> I[infra / deploy surfaces]
    D --> J[jobs, schedulers, rebuild flows]
    E --> K[governed shell behavior]
    F --> L[logs, traces, collector joins]
    G --> M[audit / scan tooling]

    N[contracts/] -. machine law .-> A
    O[policy/] -. executable governance .-> A
    P[/etc/kfm/*.env] -. secrets / host-local only .-> A
    Q[RAW → WORK/Quarantine → PROCESSED → CATALOG → PUBLISHED] -. referenced, not replaced .-> A
```

## Reference tables

### Config lanes at a glance

| Lane | Typical contents | Primary consumers | Status |
| --- | --- | --- | --- |
| `env.schema.json` | machine-checkable environment schema | API, workers, local runtime, tests | **PROPOSED artifact explicitly named in March 2026 docs** |
| `env/` | non-secret env examples and defaults | API, workers, CLI, local bring-up | **INFERRED** |
| `deployment/` | runtime parameters, deploy values, host examples | infra / deploy surfaces | **INFERRED** |
| `orchestration/` | scheduler or queue bindings, worker profiles | jobs, rebuild flows, ETL/orchestration | **PROPOSED** |
| `ui/` | shell/renderer defaults without secrets | web shell / portrayal layers | **PROPOSED** |
| `observability/` | collector, logging, join-key config | services, dashboards, audit flows | **PROPOSED** |
| `security/` | non-secret thresholds or waivers | audit / CI / scan tooling | **PROPOSED** |

### Placement rules at a glance

| Concern | Preferred home | Rule |
| --- | --- | --- |
| Non-secret runtime defaults | `configs/` | Keep them explicit, reviewable, and diffable |
| Outward contract law | `contracts/` | Version, validate, and test it as machine law |
| Executable governance | `policy/` | Keep deny/allow/generalize logic separate and testable |
| Secret-bearing values | host-local secret surfaces | Never commit them into repo-visible config |
| Release proof and correction artifacts | release/proof location | Treat trust-bearing publication evidence separately |
| Canonical write logic | worker / canonical-model packages | Do not hide it in frontend config or ad hoc scripts |
| Evidence resolution | governed API and resolver packages | Renderer components should not own it |

### Review triggers

| Change trigger | Treat as | Why |
| --- | --- | --- |
| Bind address, port, or proxy change | security + architecture review | Alters exposure posture |
| Publication, citation, or release-scope toggle | governance-significant change | Can weaken public trust behavior |
| New worker/job config | runtime + provenance review | Can alter rebuild, correction, or freshness semantics |
| UI default that affects trust cues | shell / UX review | Users must still see evidence and state honestly |
| New threshold / waiver config | operational risk review | Silent tolerance drift can undermine gates |

## Task list / definition of done

- [ ] No secrets, tokens, or private credentials are committed
- [ ] Every new config file names its primary consumer
- [ ] Configuration does not encode contract law or policy logic that belongs elsewhere
- [ ] Host-local secret-bearing files stay outside versioned `configs/`
- [ ] Validation hooks for schemas, dependency boundaries, or route-family checks are documented or linked
- [ ] Any config that materially shapes outputs can be tied back to manifests, receipts, or release evidence
- [ ] Working-shape paths in this README are verified against the live repo before merge
- [ ] Meta block placeholders are replaced or intentionally kept with review notes
- [ ] The README remains aligned with the repo’s actual build, deploy, and verification path

## FAQ

### Why is this README so strict about `configs/` versus `contracts/` and `policy/`?

Because KFM’s trust model depends on visible separation between value surfaces, machine-readable law, and executable governance. Folding them together makes review, rollback, and correction harder.

### Is all KFM configuration supposed to live under `configs/`?

No. This README covers the **repo-visible, non-secret subset** only. Host-local secrets, executable policy bundles, and release evidence belong elsewhere.

### Can `configs/` change user-visible behavior?

Yes. Bind scope, published-only behavior, shell defaults, stale-state handling, and observability can all change user-visible behavior. That is why config deserves review discipline.

### Are the subdirectories in this README confirmed?

No. The root `configs/` lane is continuity-documented, but this session did not include a mounted checkout. The tree shown here is a **working shape**, not a mounted-fact claim.

### Can security-related YAML live here?

Non-secret thresholds, waivers, or scan parameters can. Executable governance bundles, reason codes, and obligation codes should stay under `policy/`.

### Why include an `env.schema.json` file at the root?

Because the March 2026 design material explicitly names it as a proposed artifact. Even if the live repo uses a different exact shape, the concept of a validated environment schema is source-grounded.

## Appendix

<details>
<summary><strong>Documented examples visible in the current corpus</strong></summary>

| Example | What it shows | Status |
| --- | --- | --- |
| `configs/env.schema.json` | Explicitly named environment schema surface for validated config loading | **PROPOSED artifact explicitly named in March 2026 design material** |
| `configs/security/vuln_policy.yaml`, `configs/security/license_policy.yaml` | Example non-secret operational security config | **PROPOSED notebook-grade example** |
| `configs/orchestration/**` | Example orchestrator/platform bindings | **PROPOSED notebook-grade example** |
| `configs/remote_sensing/**` | Example mission-specific pipeline config family | **PROPOSED notebook-grade example** |
| `/etc/kfm/kfm-api.env`, `/etc/kfm/kfm-worker.env`, `/etc/kfm/kfm-publish.env`, `/etc/kfm/ollama.override.env` | Host-local secret-bearing environment file pattern | **Documented host pattern; excluded from repo-visible config** |
| `KFM_ARTIFACT_ROOT`, `KFM_POLICY_DIR`, `KFM_DB_DSN`, `KFM_MODEL_ADAPTER_URL`, `KFM_PUBLISHED_ONLY`, `KFM_CITATIONS_REQUIRED`, `KFM_BIND` | Illustrative runtime key family | **PROPOSED key set from runtime guidance** |

</details>

<details>
<summary><strong>Verification checklist before merge</strong></summary>

Verify at least the following against the live checkout:

1. Whether `configs/README.md` already exists and has local style conventions to preserve.
2. Whether `configs/` currently contains `env.schema.json` or an equivalent file.
3. Which of the working-shape lanes actually exist.
4. Whether validation scripts or CI checks already reference config schemas, route-family checks, or package-boundary rules.
5. Whether neighboring docs already link to `configs/`.
6. Whether owners, dates, and policy label can be confirmed for the meta block.

</details>

[Back to top](#top)
