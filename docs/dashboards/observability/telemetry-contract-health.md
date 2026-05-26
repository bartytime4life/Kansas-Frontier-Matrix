<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-observability-telemetry-contract-health
title: Telemetry Contract Health (PROPOSED system-health spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: observability steward + infra owner + sensitivity reviewer
created: 2026-05-26
updated: 2026-05-26
policy_label: internal
related:
  - kfm://doc/dashboards-observability-readme
  - kfm://doc/standard-opentelemetry           # PROPOSED: docs/standards/OPENTELEMETRY.md (OPEN-DASH-OBS-08)
  - kfm://doc/standard-openlineage             # PROPOSED: docs/standards/OPENLINEAGE.md (OPEN-DR-05)
  - kfm://card/p20-feat-0007                   # PROPOSED card: telemetry contract health
tags: [kfm, dashboards, observability, telemetry, contract, conformance]
notes:
  - Source card KFM-P20-FEAT-0007 is PROPOSED in the corpus.
  - Sensitive-content posture defaults to T1 internal; T2+ spans MUST be redacted at emission.
  - Specification only; implementation lives in apps/admin/observability/ and runtime/observability/.
[/KFM_META_BLOCK_V2] -->

# Telemetry Contract Health

<!-- [doc: kfm://doc/dashboards-observability-telemetry-contract-health] -->
<a id="top"></a>

> Surfaces whether every CI run / pipeline run emitted OTel traces that conform to the KFM telemetry contract — required keys present, energy/carbon fields populated, missing-field counts at zero across the last 24h.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Audience: SRE / infra" src="https://img.shields.io/badge/audience-SRE%20%2F%20infra-blue">
  <img alt="Sensitivity: T1" src="https://img.shields.io/badge/sensitivity-T1-yellow">
  <img alt="Public-exposure: INTERNAL" src="https://img.shields.io/badge/public--exposure-INTERNAL-critical">
  <img alt="Source: KFM-P20-FEAT-0007" src="https://img.shields.io/badge/source-KFM--P20--FEAT--0007-purple">
</p>

> [!CAUTION]
> **Sensitive-content posture:** default **T1 internal**. Trace bodies originating from T2+ packages MUST be redacted at emission; this dashboard surfaces *conformance counts*, never raw span attributes. Sampling rate: 100% of conformance metrics; 0% of raw payloads.

---

## 1. Scope

- **Source anchor:** KFM-P20-FEAT-0007 *(PROPOSED card)* — daily OTel traces, energy/carbon, required keys, missing fields for last-24h CI runs.
- **Audience:** Observability steward, infra owner, SRE on-call.
- **Aggregation scope:** Whole-stack rollup of conformance per package and per CI runner; **not** per-domain.

[↑ back to top](#top)

---

## 2. Signals

| Signal | What it carries | Healthy posture | Emitting adapter / path |
|:---|:---|:---|:---|
| `telemetry.contract.required_keys_present` | Boolean per span: all required keys (`run_id`, `trace_id`, `spec_hash`, `policy_label`) present | 100% over 24h window | `runtime/observability/contract-validator/` *(PROPOSED)* |
| `telemetry.contract.missing_fields_count` | Counter of spans missing one or more required fields | 0 over 24h window | same |
| `telemetry.contract.energy_joules` | Per-run energy estimate | Populated on every CI run; non-null | `runtime/observability/energy-adapter/` *(PROPOSED)* |
| `telemetry.contract.carbon_grams` | Per-run carbon estimate | Populated on every CI run; non-null | same |
| `telemetry.contract.violations_by_package` | Histogram of violations bucketed by emitting package | 0 across all packages | `runtime/observability/contract-validator/` |

[↑ back to top](#top)

---

## 3. Sensitive-content posture

- **Sensitivity tier of signals:** T1 internal (conformance counts only).
- **Redaction-at-emission rules:** Source spans from T2+ packages (archaeology, fauna/flora rare species, settlements-infrastructure critical) MUST have body redacted before reaching the OTel Collector. This dashboard never reads raw span bodies.
- **Sampling policy:** 100% of conformance signals; 0% sampling of raw payloads (they never reach storage).
- **Trace-body retention window:** N/A — only conformance metrics are surfaced.
- **Access control on dashboard:** Internal-only (SRE + observability steward groups).

[↑ back to top](#top)

---

## 4. Public-exposure policy

- **Default:** INTERNAL. Not linked from any public KFM page.
- **Documented exceptions:** None.
- **Aggregation/redaction if surfaced publicly:** Not applicable; do not surface publicly without sensitivity-reviewer sign-off and explicit aggregation declaration.

[↑ back to top](#top)

---

## 5. Ownership

- **Observability steward:** OWNER_TBD
- **Infra owner:** OWNER_TBD
- **Sensitivity reviewer:** OWNER_TBD *(required because upstream packages may emit T2+ payloads even though this dashboard surfaces only T1 counts).*
- **Implementation owner:** OWNER_TBD *(SRE team)*

[↑ back to top](#top)

---

## 6. Implementation pointer

- **Dashboard UI:** `apps/admin/observability/telemetry-contract/` *(PROPOSED; NEEDS VERIFICATION)*
- **Telemetry source:** `runtime/observability/contract-validator/` *(PROPOSED)*
- **Standards:** `docs/standards/OPENTELEMETRY.md` *(PROPOSED; OPEN-DASH-OBS-08)*
- **Policy bundles:** `policy/observability/telemetry-minimums/` *(PROPOSED; Pass 10 C5-06)*

[↑ back to top](#top)

---

## 7. Cross-links

- **Governance dashboards consuming this signal:** `docs/dashboards/governance/evidence-and-source.md` *(consumes `required_keys_present` to confirm receipts carry trace IDs)*
- **Per-domain breakdown:** N/A — this dashboard is whole-stack only.
- **Release-lifecycle view:** `docs/dashboards/release/telemetry-conformance-by-release.md` *(PROPOSED sibling)*
- **Related observability spec:** `opentelemetry-stack.md` (stack health), `energy-carbon-footprint.md` (energy/carbon detail; OPEN-DASH-OBS-07 may merge).

[↑ back to top](#top)

---

## 8. Review cadence

- Reviewed quarterly.
- Trigger events: OTel SDK version bump, new required field added to the telemetry contract, sensitivity-tier reclassification of any upstream package, Pass 10 C5-06 policy bundle change.

[↑ back to top](#top)

---

## 9. Open questions

- **OPEN-DASH-OBS-CONTRACT-01** — Where does the telemetry contract schema-of-record live? (Relates to OPEN-DASH-OBS-06 in the parent README.)
- **OPEN-DASH-OBS-CONTRACT-02** — Should energy/carbon be a sub-panel of this dashboard or a separate spec (`energy-carbon-footprint.md`)? Relates to OPEN-DASH-OBS-07.

[↑ back to top](#top)

---

## 10. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| KFM-P20-FEAT-0007 | PROPOSED in corpus | §1, §2, §5.1 of parent README. |
| Pass 10 C5-06 (Observability as Code via OPA) | CONFIRMED in corpus | §6 policy-bundle pointer; §7 conflict rule. |
| Atlas v1.1 §24.5 (Sensitivity Tiers) | CONFIRMED | §3 default-deny posture. |
| `docs/dashboards/observability/README.md` | CONFIRMED (this folder) | §6 template alignment. |

<sub>Specification only. Implementation in `apps/admin/observability/`; emission in `runtime/observability/`. Behind the trust membrane; sensitivity rules tighten — they do not relax — for observability surfaces.</sub>
