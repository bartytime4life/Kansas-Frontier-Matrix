<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-observability-validator-orchestrator-health
title: Validator Orchestrator Health (system-health spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: observability steward + validation owner
created: 2026-05-26
updated: 2026-05-26
policy_label: internal
related:
  - kfm://doc/dashboards-observability-readme
  - kfm://doc/directory-rules                  # CONFIRMED — tools/validate_all.py per §7.5.a
tags: [kfm, dashboards, observability, validators, orchestrator, ci]
notes:
  - tools/validate_all.py is CONFIRMED live per docs/doctrine/directory-rules.md §7.5.a.
  - Exit-code semantics: 0=pass, 1=validation-failure, 2=system-error.
[/KFM_META_BLOCK_V2] -->

# Validator Orchestrator Health

<!-- [doc: kfm://doc/dashboards-observability-validator-orchestrator-health] -->
<a id="top"></a>

> Surfaces the operational health of the `tools/validate_all.py` orchestrator — run frequency, exit-code distribution (0 / 1 / 2), p95 wallclock per-validator and overall, and validator-coverage drift.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Audience: SRE / validation owner" src="https://img.shields.io/badge/audience-SRE%20%2F%20validation%20owner-blue">
  <img alt="Sensitivity: T0" src="https://img.shields.io/badge/sensitivity-T0-green">
  <img alt="Public-exposure: INTERNAL" src="https://img.shields.io/badge/public--exposure-INTERNAL-critical">
  <img alt="Source: validate_all.py (CONFIRMED)" src="https://img.shields.io/badge/source-validate__all.py-success">
</p>

> [!CAUTION]
> **Sensitive-content posture:** T0. Validator output is structured pass/fail/exit; this dashboard surfaces counts and durations only. If a validator log entry would name a T2+ artifact (e.g., a failing archaeology dataset), the log line is redacted at emission — this dashboard never reads validator stderr.

---

## 1. Scope

- **Source anchor:** `tools/validate_all.py` *(CONFIRMED live per `docs/doctrine/directory-rules.md` §7.5.a)*.
- **Audience:** Validation owner, SRE on-call, observability steward.
- **Aggregation scope:** Orchestrator-wide; per-validator; per-CI-runner.

[↑ back to top](#top)

---

## 2. Signals

| Signal | What it carries | Healthy posture | Emitting adapter / path |
|:---|:---|:---|:---|
| `validator.orchestrator.runs_per_day` | Count of orchestrator invocations | ≥ baseline (set per CI cadence; PROPOSED) | CI runner telemetry |
| `validator.orchestrator.exit_0_rate` | % runs exiting 0 (all pass) | Tracking metric; no threshold *(infra-health, not doctrine)* | orchestrator self-telemetry |
| `validator.orchestrator.exit_1_rate` | % runs exiting 1 (one or more validators reported fail) | Tracking metric | same |
| `validator.orchestrator.exit_2_rate` | % runs exiting 2 (system error in the orchestrator itself) | < 0.5% | same |
| `validator.orchestrator.p95_wallclock_seconds` | p95 end-to-end orchestrator wallclock | < 300s *(PROPOSED)* | same |
| `validator.per_validator.p95_wallclock_seconds` | p95 per individual validator | per-validator budget *(PROPOSED)* | per-validator instrumentation |
| `validator.coverage.registered_vs_run` | Δ between registered validators and validators actually executed on a run | 0 | orchestrator manifest |

[↑ back to top](#top)

---

## 3. Sensitive-content posture

- **Sensitivity tier of signals:** T0.
- **Redaction-at-emission rules:** Validator stderr / artifact-naming output redacted at the orchestrator boundary; this dashboard never reads raw validator output.
- **Sampling policy:** 100% of orchestrator-level metrics.
- **Trace-body retention window:** Not applicable — this dashboard surfaces metrics, not trace bodies.
- **Access control on dashboard:** Internal-only.

[↑ back to top](#top)

---

## 4. Public-exposure policy

- **Default:** INTERNAL.
- **Documented exceptions:** None.
- **Aggregation/redaction if surfaced publicly:** Forbidden. Validator pass/fail rates can be inferred to suggest data-quality drift in particular domains, which is itself signal that should not be public.

[↑ back to top](#top)

---

## 5. Ownership

- **Observability steward:** OWNER_TBD
- **Validation owner:** OWNER_TBD *(owns the orchestrator and the validator registry)*
- **Sensitivity reviewer:** Not required *(T0 only)*.
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 6. Implementation pointer

- **Dashboard UI:** `apps/admin/observability/validator-orchestrator/` *(PROPOSED; NEEDS VERIFICATION)*.
- **Telemetry source:** `tools/validate_all.py` *(CONFIRMED live)*; per-validator instrumentation in `tools/validators/`.
- **Standards:** `docs/standards/OPENTELEMETRY.md` *(PROPOSED)*.
- **Policy bundles:** `policy/observability/validator-coverage/` *(PROPOSED; Pass 10 C5-06; enforces that every registered validator runs)*.

[↑ back to top](#top)

---

## 7. Cross-links

- **Governance dashboards consuming this signal:** `docs/dashboards/governance/validation-and-conformance.md` *(governance reads the exit-1-rate as a doctrine indicator;* **same signal, different rendering**, per parent README §9).
- **Per-domain breakdown:** `docs/dashboards/domain/<domain>.md` *(per-domain validators are sub-rolled-up there).*
- **Release-lifecycle view:** `docs/dashboards/release/validation-by-release.md` *(PROPOSED sibling).*
- **Related observability specs:** `build-ci-health.md`, `ingest-run-trace-coverage.md`.

[↑ back to top](#top)

---

## 8. Review cadence

- Reviewed quarterly.
- Trigger events: Addition or removal of a validator from the orchestrator registry, change in exit-code semantics, CI runner-fleet topology change.

[↑ back to top](#top)

---

## 9. Open questions

- **OPEN-DASH-OBS-VAL-01** — What is the per-validator wallclock budget set to? Listed PROPOSED; needs ratification.
- **OPEN-DASH-OBS-VAL-02** — Should exit-1 spikes auto-page or are they always pull-only signals? Doctrine vs infra answer differs (governance side may want paging; infra side may not).

[↑ back to top](#top)

---

## 10. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| `docs/doctrine/directory-rules.md` §7.5.a (validate_all.py CONFIRMED live) | CONFIRMED (prior-session authored) | §1 source anchor. |
| Pass 10 C5-06 (Observability as Code via OPA) | CONFIRMED in corpus | §6 policy-bundle pointer. |
| `docs/dashboards/observability/README.md` | CONFIRMED (this folder) | §6 template; §9 same-signal-different-rendering rule. |

<sub>Specification only. Behind the trust membrane.</sub>
