<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-telemetry-readme
title: contracts/telemetry — Telemetry Contract Semantics README
type: readme
version: v0.1
status: draft; PROPOSED; semantic-contract-lane; observability-carrier; redaction-required; no-sovereign-truth
owners: OWNER_TBD — Observability steward · Runtime steward · Security/Privacy reviewer · Contracts steward · Schema steward · Policy steward · Release steward · Docs steward
created: NEEDS VERIFICATION — stub existed before v0.1 expansion
updated: 2026-06-24
policy_label: public; contracts; telemetry; observability; semantic-contracts; redaction; sensitivity; rights; receipts; release-gated; no-truth-authority
tags: [kfm, contracts, telemetry, observability, traces, metrics, logs, events, receipts, opentelemetry, openlineage, redaction, sensitivity, rights, trust-membrane, release-gates]
related:
  - ../README.md
  - ../runtime/run_receipt.md
  - ../runtime/ai_receipt.md
  - ../runtime/runtime_response_envelope.md
  - ../release/release_manifest.md
  - ../../docs/standards/TELEMETRY_MINIMUMS.md
  - ../../docs/adr/ADR-0016-telemetry-redaction-posture.md
  - ../../docs/dashboards/README.md
  - ../../docs/dashboards/INDICATOR_CATALOG.md
  - ../../schemas/contracts/v1/telemetry/
  - ../../schemas/contracts/v1/receipts/
  - ../../policy/runtime/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../policy/promotion/
  - ../../docs/architecture/contract-schema-policy-split.md
notes:
  - "Expanded from the short stub at `contracts/telemetry/README.md`."
  - "Repo search in this session found telemetry standards, dashboard docs, and a telemetry-redaction ADR, but did not verify a mature telemetry contract family or paired telemetry schema."
  - "Telemetry Minimums says telemetry is a carrier, not truth, and earns release evidence rather than establishing it."
  - "ADR-0016 says telemetry that leaves a KFM process is a governed emission subject to sensitivity, rights, and policy gates."
  - "This lane defines semantic meaning only; telemetry collection, sinks, dashboards, alerts, policy, schemas, receipts, release gates, and implementation remain in separate roots."
  - "Rollback target for this expansion is previous stub blob SHA `02327328e50c1bcb0435a9c8f03d3e2b0c0d740b`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/telemetry

> Proposed semantic-contract lane for telemetry and observability objects. Telemetry may carry operational and governance signals about what ran, when, under which source/policy/release context, and with what outcome. Telemetry is a carrier, not truth; it must not become a side channel around the trust membrane.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts/telemetry" src="https://img.shields.io/badge/root-contracts%2Ftelemetry-blue">
  <img alt="Purpose: semantic meaning" src="https://img.shields.io/badge/purpose-semantic__meaning-blueviolet">
  <img alt="Posture: redaction required" src="https://img.shields.io/badge/posture-redaction__required-critical">
  <img alt="Boundary: carrier not truth" src="https://img.shields.io/badge/boundary-carrier__not__truth-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/telemetry/README.md`  
**Owning root:** `contracts/` — semantic meaning only  
**Schema home:** `schemas/contracts/v1/telemetry/` or `schemas/contracts/v1/receipts/` — PROPOSED / NEEDS VERIFICATION  
**Policy homes:** `policy/runtime/`, `policy/sensitivity/`, `policy/rights/`, `policy/promotion/`  
**Operational docs:** `docs/standards/TELEMETRY_MINIMUMS.md`, dashboards docs, runbooks, ADRs  
**Truth posture:** CONFIRMED target was a short stub · CONFIRMED telemetry standards and telemetry redaction ADR exist · CONFIRMED telemetry is treated as carrier/process memory rather than truth · CONFIRMED telemetry emissions are subject to sensitivity, rights, and policy posture · NEEDS VERIFICATION for telemetry schema family, validators, fixtures, policy enforcement, sink implementation, dashboards, runtime probes, retention, and release-gate wiring

## Quick jumps

[Purpose](#purpose) · [Telemetry object meaning](#telemetry-object-meaning) · [Authority split](#authority-split) · [Candidate object families](#candidate-object-families) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Redaction posture](#redaction-posture) · [Invariants](#invariants) · [Validation expectations](#validation-expectations) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`contracts/telemetry/` is a proposed semantic-contract lane for telemetry objects that need governed meaning beyond generic observability terms.

It may define what KFM means by telemetry records such as:

- operational traces, metrics, logs, and events;
- lineage events and run-linked facets;
- runtime probe summaries;
- telemetry redaction receipts;
- promotion-gate observability evidence;
- public-safe telemetry summaries shown to stewards, release managers, or Evidence Drawer surfaces.

This lane does not define dashboard layout, alert routing, on-call process, telemetry backend selection, exporter code, collector configuration, raw log storage, or release approval.

---

## Telemetry object meaning

Telemetry in KFM answers operational and governance questions such as:

- what ran;
- when it ran;
- which run, source, artifact, layer, route, or release candidate it touched;
- which outcome, error class, latency, byte count, or SLO signal occurred;
- which lineage, receipt, policy, validation, or release references were attached;
- whether the emitted telemetry was public-safe, redacted, generalized, or restricted.

Telemetry does not answer:

- whether an underlying claim is true;
- whether a release is approved;
- whether evidence is sufficient;
- whether rights or sensitivity policy allows public exposure;
- whether RAW/WORK/QUARANTINE/canonical data can be exposed;
- whether a model-generated answer is correct;
- whether source material may bypass SourceDescriptor and EvidenceBundle checks.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| Telemetry object meaning | `contracts/telemetry/` | Proposed semantic contract lane only. |
| Runtime receipts | `contracts/runtime/` and receipt contract roots | Runtime objects like RunReceipt/AIReceipt have their own contracts. |
| Machine shape | `schemas/contracts/v1/telemetry/` or accepted schema roots | JSON Schema owns field shape. |
| Redaction/admissibility policy | `policy/runtime/`, `policy/sensitivity/`, `policy/rights/`, `policy/promotion/` | Policy decides allow/deny/redact/restrict. |
| Telemetry standards | `docs/standards/TELEMETRY_MINIMUMS.md` | Operational minimums and governance expectations. |
| ADRs | `docs/adr/` | Governance decisions such as telemetry redaction posture. |
| Dashboards | `docs/dashboards/` and dashboard/runtime roots | Display and operational views. |
| Collector/sink implementation | `infra/`, `runtime/`, apps, packages, pipelines, or accepted implementation roots | Executable telemetry plumbing stays outside contracts. |
| Fixtures/tests/validators | `fixtures/`, `tests/`, `tools/validators/` | Enforceability stays outside contracts. |
| Release gates | `contracts/release/`, `release/`, policy/promotion roots | Telemetry informs gates; it does not publish. |

---

## Candidate object families

These candidate contracts are PROPOSED until schemas, policy, fixtures, validators, and owners are accepted.

| Candidate | Purpose | Status |
|---|---|---|
| `telemetry_event.md` | Common semantics for structured telemetry events. | PROPOSED |
| `telemetry_redaction_receipt.md` | Records source-side telemetry redaction before sink/export. | PROPOSED |
| `runtime_probe_result.md` | Public-safe result of a runtime/health/probe check. | PROPOSED |
| `slo_measurement.md` | SLO/error-budget measurement semantics. | PROPOSED |
| `lineage_event_ref.md` | Reference semantics for OpenLineage or lineage backend event ids. | PROPOSED |
| `telemetry_release_evidence.md` | Telemetry evidence summary for promotion/release gate review. | PROPOSED |
| `telemetry_caveat.md` | Required caveats for sampled, partial, redacted, or degraded telemetry. | PROPOSED |

Do not create these as canonical contracts without checking Directory Rules, schema homes, policy homes, fixtures, tests, release behavior, and ADR status.

---

## Accepted contents

| Accepted content | Purpose | Guardrail |
|---|---|---|
| `README.md` | Defines telemetry contract-lane boundary. | Must preserve carrier-not-truth posture. |
| Telemetry semantic contracts | Define meaning for accepted telemetry object families. | Must identify schema/policy/fixture/test posture. |
| `INDEX.md` | Optional inventory after accepted telemetry contracts exist. | Must not present proposed objects as implemented facts. |
| `MIGRATION.md` | Optional migration/backlink plan. | Must identify rollback and stale-reference handling. |
| `BACKLINKS.md` | Optional stale-reference audit. | Must stay factual. |

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| Raw logs, traces, metrics, events, dumps, crash reports | telemetry/runtime/storage roots | Contracts do not store telemetry payloads. |
| Collector/exporter/backend configuration | infra/runtime/app roots | Implementation belongs outside contracts. |
| Dashboard definitions or screenshots | `docs/dashboards/` and dashboard roots | Display belongs outside contracts. |
| Alert routing/on-call runbooks | `docs/runbooks/` or ops roots | Operational response is not semantic contract meaning. |
| JSON Schema | `schemas/contracts/v1/telemetry/` or accepted schema roots | Schemas own shape. |
| Policy rules | `policy/` roots | Policy owns redaction, rights, sensitivity, promotion gates. |
| Fixtures/tests/validators | `fixtures/`, `tests/`, `tools/validators/` | Proof and validation stay outside contracts. |
| RAW/WORK/QUARANTINE/canonical data | lifecycle/canonical roots | Telemetry must not expose internal data. |
| Secrets, credentials, tokens, private URLs, exact restricted coordinates, raw prompts, chain-of-thought | nowhere public; restricted vault/audit paths if necessary | Telemetry must not become a leak path. |

---

## Redaction posture

Telemetry that leaves a process, crosses a trust boundary, reaches a sink, persists to a store, appears on a dashboard, or enters a release gate must be treated as governed emission.

Default posture:

- redact at source before export;
- fail closed for unknown sensitivity or rights posture;
- avoid exact restricted coordinates, living-person identifiers, DNA/genomic inference, rare-species locations, archaeological/sacred/cultural-sensitive details, infrastructure-sensitive details, credentials, tokens, private URLs, raw prompts, chain-of-thought, and payload fragments;
- emit receipt-safe references rather than protected values;
- record redaction/generalization/suppression when consequential;
- do not rely on sink-only filtering as the only protection.

---

## Invariants

PROPOSED semantic invariants:

- Telemetry is carrier/process memory, not sovereign truth.
- A telemetry value alone cannot promote, publish, validate, or prove a claim.
- Telemetry leaving a process is a governed emission subject to sensitivity, rights, and policy checks.
- Public or semi-public telemetry must be redacted, generalized, suppressed, or denied when policy requires it.
- Telemetry must preserve run/source/evidence/release references where needed for auditability without leaking restricted payloads.
- Under-instrumented services should fail release/promotion gates where telemetry minimums are accepted and enforced.
- Workers/watchers may emit telemetry and receipts; they are not publishers.
- Public clients must not read telemetry sinks as a bypass around governed APIs, released artifacts, or EvidenceBundle-backed surfaces.

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- accepted telemetry schema home and object names;
- validators for telemetry object contracts;
- fixtures for public-safe, restricted, redacted, sampled, partial, failed, degraded, and sink-export cases;
- policy enforcement for telemetry redaction, rights, sensitivity, and promotion gates;
- collector/exporter implementation and sink redaction guarantees;
- dashboard catalog integration;
- retention and access-control posture;
- linkage to RunReceipt, AIReceipt, RuntimeResponseEnvelope, PromotionDecision, and ReleaseManifest where applicable;
- CI/release gates for under-instrumented services.

---

## Open questions

- Should telemetry semantic contracts live under `contracts/telemetry/`, `contracts/runtime/`, `contracts/receipts/`, or a split by object type?
- Should `runtime_probe_result.md` be telemetry, runtime, release, or dashboard contract family?
- Which telemetry events require signed receipts versus ordinary observability signals?
- Which telemetry attributes are safe for public dashboards?
- Which telemetry minimums are ratified by ADR versus still proposed?

---

## Rollback

Rollback is required if this lane is used as log storage, telemetry backend configuration, dashboard implementation, policy authority, schema authority, release approval, evidence truth, source truth, AI truth, raw-data access, secret storage, or a bypass around the trust membrane.

Rollback target for this expansion: previous stub blob SHA `02327328e50c1bcb0435a9c8f03d3e2b0c0d740b`.

<p align="right"><a href="#top">Back to top</a></p>
