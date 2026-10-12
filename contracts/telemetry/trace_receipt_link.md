<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-telemetry-trace-receipt-link
title: TraceReceiptLink Contract
type: semantic-contract; telemetry; observability; receipt-linkage; promotion-input
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-live-telemetry-or-release-authority
owners: OWNER_TBD — Observability steward · Runtime steward · Contracts steward · Schema steward · Validation steward · Release steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; contracts; telemetry; observability; receipts; evidence-linkage; no-truth-authority
related:
  - ./README.md
  - ../../schemas/contracts/v1/telemetry/trace_receipt_link.schema.json
  - ../../fixtures/contracts/v1/telemetry/trace_receipt_link/
  - ../../tools/validators/validate_trace_receipt_link.py
  - ../../tests/validators/test_validate_trace_receipt_link.py
  - ../../docs/dashboards/observability/ingest-run-trace-coverage.md
  - ../../docs/intake/exploratory/new-ideas-2-22-26-trace-receipt-link-source-map.md
notes:
  - "Implements the bounded trace_id -> run receipt -> evidence-bundle digest linkage gate mined from New ideas 2-22-26.pdf, pages 7-12."
  - "The contract validates a positive linkage assertion only. Missing, mismatched, late, or unsafe records fail closed through validator findings."
  - "No OpenTelemetry collector, Tempo/Jaeger backend, Grafana dashboard, OCI push, Cosign invocation, OPA decision, promotion, release, or publication is created."
[/KFM_META_BLOCK_V2] -->

# TraceReceiptLink

`TraceReceiptLink` is a fixture-first positive assertion that one pipeline run's W3C trace identity is bound to the matching run receipt, immutable evidence-bundle digest, and attestation subjects within a declared maximum delay.

The object exists to make the question below deterministic and reviewable:

> Do the run anchor, run receipt, evidence bundle, and attestation subjects all identify the same run, specification, and trace within the allowed linkage window?

A valid object answers only that linkage question. It does not prove that the underlying evidence is true, rights-cleared, policy-allowed, reviewed, released, or published.

## Source-derived pattern

The source packet proposes making every pipeline observable by default, using `trace_id` as the join key across CI, receipts, logs, attestations, and evidence bundles. It further proposes a fail-closed probe that blocks promotion when trace-to-receipt-to-evidence linkage is missing or later than a bounded interval such as five minutes.

This repository slice adapts that idea to current KFM responsibility roots and existing telemetry doctrine. It does not create the packet's illustrative `/evidence/` root, direct `releases/` evidence store, live collector configuration, or broad promotion workflow.

## Directory Rules basis

Accepted ADR-0029 and the adopted Directory Rules v2 responsibility model assign each artifact to one existing owner:

| Responsibility | Home |
|---|---|
| Telemetry object meaning | `contracts/telemetry/` |
| Machine shape | `schemas/contracts/v1/telemetry/` |
| Synthetic examples | `fixtures/contracts/v1/telemetry/trace_receipt_link/` |
| Deterministic validation | `tools/validators/` |
| Enforceability | `tests/validators/` |
| Focused CI orchestration | `.github/workflows/` |
| Exploratory source mapping | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No new root, parallel receipt store, policy home, release home, evidence store, telemetry sink, or public path is created.

## Required anchors

| Anchor | Required fields | Purpose |
|---|---|---|
| Run | `run_id`, `spec_hash`, `trace_id`, `root_span_id`, time interval, service, Git SHA, dataset, sensitivity | Fixes the run and trace context. |
| Run receipt | receipt reference/digest plus repeated `run_id`, `spec_hash`, `trace_id`, and emission time | Proves the receipt claims the same anchor. |
| Evidence bundle | bundle reference, OCI content-addressed reference/digest, repeated anchors, record time, attestations | Binds the immutable evidence carrier and its attestations. |
| Assessment | evaluation time, delay budget, measured delays, `LINKED/PASS`, stable reason code | Makes the bounded linkage decision explicit. |
| Governance | all authority-creation and unsafe-payload flags `false` | Prevents observability from becoming truth or release authority. |

## Deterministic identity

`link_id` uses the local profile `kfm-trace-link-id-v1`:

```text
UTF8(run_id + "\\n" + trace_id + "\\n" + run_receipt.digest + "\\n" + evidence_bundle.digest)
  -> SHA-256
  -> urn:kfm:trace-receipt-link:sha256:<64 lowercase hex>
```

This profile identifies the linkage assertion. It does not replace the repository's accepted RFC 8785 JCS plus SHA-256 `spec_hash` policy, and it does not recompute `spec_hash` without the governed source specification bytes.

## Required semantic invariants

A `TraceReceiptLink` passes only when:

- `run_id`, `spec_hash`, and `trace_id` are identical across the run, receipt, and evidence sections;
- the W3C trace ID and root span ID are non-zero lowercase hexadecimal identifiers;
- `link_id` recomputes exactly under `kfm-trace-link-id-v1`;
- run, receipt, evidence, and evaluation timestamps are canonical UTC seconds and temporally ordered;
- declared receipt/evidence delays equal the timestamp-derived delays and are no greater than `max_link_delay_seconds`;
- the evidence OCI reference's subject digest matches `evidence_bundle.digest`;
- every attestation reference digest is content-addressed and every `subject_digest` equals the evidence-bundle digest;
- assessment state is exactly `LINKED`, `PASS`, and `TRACE_RECEIPT_EVIDENCE_LINKED`;
- telemetry creates no evidence, policy, promotion, release, publication, or public-route authority;
- restricted or sensitive-location runs include no protected payload values in this linkage record.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape and every linkage invariant passed. |
| `FAIL` | The candidate is readable but linkage is missing, mismatched, late, contradictory, or governance-unsafe. |
| `ERROR` | The validator could not safely read or evaluate the candidate. |

Findings contain stable codes and JSON pointers only. Candidate values, private URLs, source payloads, and sensitive details are not echoed.

## Trust boundary

A green result proves bounded local shape, anchor equality, deterministic link identity, timestamp-derived delay checks, OCI/attestation digest linkage, and no-authority flags. It does **not**:

- start or verify a real OpenTelemetry trace;
- configure an OTLP collector, exporter, Tempo, Jaeger, Grafana, or alerting route;
- verify a live run receipt, OCI object, Cosign signature, Rekor inclusion, SLSA statement, or policy decision;
- activate a source, move lifecycle state, write RAW, close an EvidenceBundle, promote, release, deploy, publish, or create a public route.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_trace_receipt_link.py' \
  --verbose

python tools/validators/validate_trace_receipt_link.py --fixtures
```

## Rollback

Before merge, close the draft pull request and delete its feature branch. After an authorized merge, revert the dependency-closed contract, schema lane, fixtures, validator, tests, workflow, exploratory source map, and generated authoring receipt. No live trace, sink, evidence object, registry object, release, deployment, or published state is created by this slice.
