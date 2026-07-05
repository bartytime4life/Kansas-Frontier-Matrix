# `runtime/service_configs/` — Runtime Service Configuration Lane

Runtime service configuration templates and handoff notes for KFM local/runtime services. This lane may document non-secret service settings, adapter wiring, ports, health checks, and environment expectations, but it must not store secrets, provider credentials, policy rules, deployable service authority, lifecycle data, or release records.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-service-configs-readme
title: runtime/service_configs/README.md — Runtime Service Configuration Lane
type: readme; directory-readme; runtime-service-config-guardrail; configuration-index
version: v0.1
status: draft; greenfield-stub-expanded; no-service-config-files-confirmed; NEEDS VERIFICATION
owners: OWNER_TBD — Runtime steward · Security steward · DevOps steward · Policy steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-07-05
policy_label: public; runtime; service-configs; templates; no-secrets
tags: [kfm, runtime, service-configs, configuration, templates, adapters, local-runtime, no-secrets]
related:
  - ../README.md
  - ../AI/README.md
  - ../model_adapters/README.md
  - ../model_adapters/AdapterContract.md
  - ../mock/README.md
  - ../ollama/README.md
  - ../envelopes/README.md
  - ../local/
  - ../../configs/
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
  - ../../fixtures/
  - ../../tests/
  - ../../tools/validators/
  - ../../data/
  - ../../release/
notes:
  - "Expanded from a greenfield stub containing only '# runtime/service_configs' and 'Greenfield stub.'."
  - "Current-session search found no direct runtime/service_configs files beyond this README."
  - "runtime/ is confirmed as local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release."
  - "runtime/AI notes identify service_configs as a canonical runtime sublane for service configuration."
  - "runtime/ollama notes point local service configuration notes here when templates are needed."
  - "This README does not prove service configuration implementation, service deployment, dependency availability, CI wiring, security review, policy enforcement, receipt emission, or public-client behavior."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: runtime" src="https://img.shields.io/badge/root-runtime%2F-blue">
  <img alt="Lane: service configs" src="https://img.shields.io/badge/lane-service__configs-purple">
  <img alt="Maturity: no configs confirmed" src="https://img.shields.io/badge/maturity-no__configs__confirmed-orange">
  <img alt="Boundary: no secrets" src="https://img.shields.io/badge/boundary-no__secrets-critical">
</p>

**Status:** draft / runtime service-configuration guardrail
**Path:** `runtime/service_configs/`
**Current role:** README-only configuration/template lane
**Truth posture:** CONFIRMED greenfield stub before this update; CONFIRMED no direct service config files found in current search; CONFIRMED adjacent runtime, governed-AI, model-adapter, Ollama, and envelope README boundaries; NEEDS VERIFICATION for actual config files, service runners, deployment targets, tests, validation, CI, security review, and owner assignments.

## Purpose

`runtime/service_configs/` is the runtime lane for non-secret service configuration templates and configuration handoff notes.

Use it to document local/runtime service setup that supports KFM runtime components, including model adapters, mock runtimes, local model runtimes, runtime envelopes, service harnesses, health checks, and development-only runtime wiring.

This lane should help operators understand **how runtime services are configured** without making configuration files into policy, evidence, release, lifecycle, or public-client authority.

## Boundary

This path is not a secret store, not a deployable service by itself, not runtime implementation code, not policy authority, not schema or contract authority, not validator code, not lifecycle data storage, not proof/receipt storage, not release authority, and not a public runtime endpoint.

Configuration templates may describe non-secret names, ports, paths, feature flags, mode labels, and handoff expectations. They must not contain credentials, tokens, API keys, private URLs, private model paths, private datasets, local `.env` values, signing keys, or production-only configuration.

> [!IMPORTANT]
> A service configuration can enable a runtime path, but it does not authorize that path. Runtime behavior still needs governed evidence, policy, finite outcomes, validation, receipts where applicable, review, release, correction, and rollback controls.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `runtime/service_configs/README.md` | present | Greenfield stub expanded by this README. |
| `runtime/service_configs/*` | no files found in current search | No service templates, environment examples, service profiles, tests, or configs confirmed under this path. |
| `runtime/README.md` | present | Runtime root for local runtime wiring, model adapters, and service harnesses subordinate to evidence, policy, and release. |
| `runtime/AI/README.md` | present | Governed AI runtime lane; identifies service configs as a runtime sublane. |
| `runtime/model_adapters/README.md` | present | Provider-neutral model adapter lane. |
| `runtime/model_adapters/AdapterContract.md` | present | Runtime adapter boundary note. |
| `runtime/ollama/README.md` | present | Local Ollama lane; points service configuration templates here when needed. |
| `runtime/envelopes/README.md` | present | Finite-outcome runtime envelope helper lane. |

## Repo fit

```text
runtime/
├── README.md
├── service_configs/
│   └── README.md                     # this file; non-secret service config lane
├── AI/
├── model_adapters/
├── mock/
├── ollama/
├── envelopes/
├── local/
├── pipelines/
├── people/
└── release/

contracts/                            # semantic meaning
schemas/                              # machine-checkable shape
policy/                               # allow / deny / restrict / abstain posture
fixtures/                             # deterministic examples
tests/                                # executable proof of behavior
tools/validators/                     # validator implementation
data/                                 # lifecycle records, receipts, proofs, catalogs, emitted data
release/                              # release, correction, rollback authority
```

## Service configuration responsibilities

| Responsibility | Requirement |
|---|---|
| Non-secret posture | Store templates and documentation only; keep secrets and private config out of the repo. |
| Runtime-mode clarity | Mark config mode explicitly: mock, local, dev, test, review, CI, or production-candidate. |
| Adapter linkage | Link model adapter, mock, Ollama, envelope, or local runtime notes when config supports them. |
| Policy posture | Do not encode policy decisions as hidden config defaults; reference policy roots when behavior is gated. |
| Evidence posture | Do not point public runtime config directly at RAW, WORK, QUARANTINE, or internal stores. |
| Outcome posture | Preserve finite runtime outcomes through envelope/adaptor boundaries. |
| Receipt posture | Link AIReceipt, RunReceipt, validation receipt, or RuntimeResponseEnvelope requirements where relevant. |
| Security posture | Prefer deny-by-default binding, least privilege, local-only defaults, and explicit review before public exposure. |
| Test posture | Config behavior claims require fixtures, tests, validators, or runtime evidence. |

## What belongs here

- This README.
- Non-secret service configuration templates.
- Example `.env.example`-style documentation with placeholders only, if accepted by repo policy.
- Local/dev/test service-profile notes.
- Runtime adapter service binding notes.
- Mock, Ollama, envelope, or local runtime service handoff notes.
- Health-check, port, timeout, queue, cache, and feature-flag documentation when values are non-secret and reviewable.
- Pointers to tests, fixtures, validators, policy, contracts, schemas, runtime envelopes, and receipts.

## What does not belong here

| Do not put this in `runtime/service_configs/` | Correct home |
|---|---|
| Secrets, API keys, provider tokens, signing keys, passwords, private URLs, local `.env`, or credentials | never in repo |
| Production-only private configuration | secret manager / deployment platform, not repo |
| Runtime implementation code | accepted runtime, app, package, or service root |
| Provider-neutral adapter cards | `runtime/model_adapters/` |
| Mock runtime notes | `runtime/mock/` or `runtime/model_adapters/mock/` |
| Ollama runtime notes | `runtime/ollama/` unless this lane only hosts linked config templates |
| Canonical semantic contracts | `contracts/` |
| JSON Schema definitions | `schemas/` |
| Policy rules or policy decisions | `policy/` and governed review/release roots |
| Fixture payloads or golden outputs | `fixtures/` |
| Executable tests | `tests/` |
| Validator source code | `tools/validators/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | `data/` lifecycle roots |
| EvidenceBundles, SourceDescriptors, receipts, proofs, catalogs, release manifests | accepted `data/`, registry, proof, receipt, catalog, or release roots |
| Public API routes or UI components | accepted app, UI, or web roots |
| Generated text treated as evidence, policy, review, release, correction, rollback, or publication authority | nowhere |

## Configuration note template

```markdown
# <service-config-note-id>

## Status
DRAFT / READY_FOR_REVIEW / LOCAL_ONLY / TEST_ONLY / ACTIVE_TEMPLATE / VALIDATION_REQUIRED / HELD / SUPERSEDED / RETIRED

## Runtime scope
<model adapter / mock / ollama / envelope / local service / other / N/A>

## Configuration mode
mock / local / dev / test / review / ci / production-candidate / N/A

## Public exposure
none / local-only / internal-only / review-only / public-candidate / N/A

## Governed support pointers
- Runtime lane: <path or N/A>
- Adapter: <path or N/A>
- Contract: <path or N/A>
- Schema: <path or N/A>
- Policy: <path or N/A>
- Fixture: <path or N/A>
- Test: <path or N/A>
- Validator: <path or N/A>
- Receipt or envelope: <path or N/A>

## Non-secret values
<ports, mode labels, placeholder variable names, timeout classes, or N/A>

## Secret handling
<which values must be supplied outside repo; never include actual secret values>

## Boundary notes
<what this config may enable and what it must not authorize>

## Reviewer
<steward or maintainer>

## Review date
<YYYY-MM-DD>

## Follow-up
<open items or none>
```

## Validation

```bash
find runtime/service_configs -maxdepth 4 -type f | sort
find runtime contracts schemas policy fixtures tests tools/validators -maxdepth 5 -type f 2>/dev/null | sort
grep -RInE '(api[_-]?key|token|secret|password|PRIVATE|BEGIN .*KEY)' runtime/service_configs || true
pytest tests/runtime tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once accepted service-config validation commands are confirmed.

## Review checklist

- [ ] Config note or template contains no secrets or private environment values.
- [ ] Runtime mode and public exposure posture are explicit.
- [ ] Adapter, envelope, local runtime, or mock runtime linkage is explicit where applicable.
- [ ] Policy is referenced rather than encoded as hidden defaults.
- [ ] Config does not point public paths at RAW, WORK, QUARANTINE, unpublished candidates, internal stores, or direct model output.
- [ ] Finite runtime outcome posture is preserved where applicable.
- [ ] Tests, fixtures, validators, or runtime evidence support behavior claims.
- [ ] Public or production-candidate exposure requires security, policy, runtime, and release review.

## Open questions

| Question | Status |
|---|---|
| Which service configuration formats are accepted here: Markdown notes, YAML templates, JSON templates, `.env.example`, or another format? | NEEDS VERIFICATION |
| Should `runtime/service_configs/` contain templates directly, or only point to deployment-platform configuration outside the repo? | NEEDS VERIFICATION |
| Which runtime services currently consume this lane, if any? | NEEDS VERIFICATION |
| Which CI workflow validates service configs and scans for secrets? | NEEDS VERIFICATION |
| Who approves public or production-candidate service configuration changes? | NEEDS VERIFICATION |
