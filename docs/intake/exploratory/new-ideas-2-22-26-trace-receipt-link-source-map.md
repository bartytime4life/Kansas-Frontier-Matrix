# New ideas 2-22-26 - repository assay and selected trace-link slice

**Status:** CONFIRMED source assay at `main@9960a2e22fb78cd6d6cf9bedb2379c09c8d5239c` / PROPOSED implementation  
**Source:** `New ideas 2-22-26.pdf`  
**Selected pages:** 7-12  
**Public-release effect:** none

## Goal

Mine the attached packet for one high-value, dependency-closed increment that fits current repository authority and can be validated with deterministic, no-network fixtures.

## Source candidates

| Candidate | Packet pressure | Current repository assay | Disposition |
|---|---|---|---|
| PR-first automation and branch evidence bundle | Every automated change opens a branch/PR with `spec_hash`, run manifest, AI receipt, checksums, policy gates, and rollback evidence. | KFM already delivers feature branches, generated authoring receipts, pinned actions, and extensive PR CI. The packet's writable automation and `/evidence/` root would broaden permissions and create a parallel authority unless separately designed. | DEFERRED as a larger repository-control change. |
| RFC 8785 JCS `spec_hash` helper | Canonical JSON plus SHA-256 anchors each run. | `tools/spec_hash/README.md` and hashing doctrine exist, but the executable package remains incomplete and true RFC 8785 behavior needs a dedicated standards/compatibility slice. | DEFERRED; do not ship a subset canonicalizer as if it were RFC 8785. |
| Trace-to-receipt-to-evidence linkage | `trace_id` joins run manifests, receipts, attestations, logs, and evidence; linkage missing or later than a bounded window fails closed. | `contracts/telemetry/README.md` and `docs/dashboards/observability/ingest-run-trace-coverage.md` already describe this boundary, but no telemetry schema, validator, fixture family, or linkage probe was found. | **SELECTED.** |
| Automatic revert PR | Post-merge monitor opens a revert PR preserving the original evidence and incident tags. | No implementation was found, but this requires accepted release, incident, monitor, authoring, and rollback authority plus write permissions. | DEFERRED to a release-control PR. |
| Feed card and UI drill-down | Compact update card links dataset, evidence digest, run receipt, and trace. | Depends on released payload contracts, public-safe resolver behavior, and UI integration. | DEFERRED until the underlying linkage object is proven. |
| Live OTel collector / Tempo / Grafana / OCI / Cosign | Operational trace export and clickable evidence. | Existing docs are primarily specifications; live sink, retention, access, sensitivity, and signing posture are not established by this source assay. | OUT OF SCOPE for the no-network slice. |

## Selected dependency-closed slice

Add one `TraceReceiptLink` profile that:

- binds the same `run_id`, accepted-format `spec_hash`, and W3C `trace_id` across run, receipt, and evidence-bundle sections;
- verifies a deterministic link identifier;
- recomputes receipt/evidence linkage delays from canonical UTC-second timestamps and fails over the declared maximum;
- binds OCI subject digests and attestation subjects;
- returns only stable finding codes and JSON pointers;
- refuses telemetry, evidence-truth, promotion, release, publication, or public-route authority;
- uses synthetic fixtures and performs no network, signing, source activation, lifecycle write, or runtime export.

## Directory Rules basis

Accepted ADR-0029 controls placement. The change uses existing responsibility roots: meaning in `contracts/`, shape in `schemas/`, synthetic vectors in `fixtures/`, enforcement in `tools/validators/` and `tests/validators/`, CI in `.github/workflows/`, source assay in `docs/intake/exploratory/`, and AI provenance in `data/receipts/generated/`.

No new root, `/evidence/` store, `releases/` evidence index, telemetry sink, dashboard implementation, policy bundle, or public API is created.

## Acceptance

```bash
python -m unittest discover   --start-directory tests/validators   --pattern 'test_validate_trace_receipt_link.py'   --verbose

python tools/validators/validate_trace_receipt_link.py --fixtures
```

Expected fixture polarity: every valid linked record passes; missing, mismatched, late, contradictory, placeholder, or governance-overreaching records fail with reviewed stable codes.

## Follow-on cursor

After human review of this slice, the next safe increment is an adapter-neutral receipt writer that emits this profile from existing fixture-only pipeline outputs. Live OpenTelemetry, OCI lookup, Cosign/Rekor verification, OPA promotion policy, dashboards, and auto-revert authoring remain separate authority-bearing changes.
