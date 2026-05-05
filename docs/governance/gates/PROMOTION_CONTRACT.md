# Promotion Contract

## Scope

Promotion is a governed transition from candidate artifacts to a publishable release. This contract binds each gate to artifacts, policy checks, integrity checks, and fail-closed semantics.

## Gate map

| Gate | Purpose | Policy pack | Required artifacts | Integrity check |
|---|---|---|---|---|
| A | Evidence integrity | `policy/evidence` | `EvidenceBundle.json`, `spec_hash.txt` | canonical `spec_hash` |
| B | Run provenance | `policy/provenance` | `run_receipt.json`, evidence Sigstore bundle | `cosign verify-blob` |
| C | Rights and sensitivity | `policy/rights` | `EvidenceBundle.json`, `LICENSE` | policy only |
| D | Obligations applied | `policy/obligations` | `redaction_receipt.json` | post-process hash alignment |
| E | Stewardship | `policy/approvals` | `decision_log.json` | policy only |
| F | Deploy preflight | `policy/preflight` | `preflight_report.json` | policy only |
| G | Final publish/archive | `policy/release` | `release_manifest.json`, release Sigstore bundle, `attestations/` | artifact hash verification and `cosign verify-blob` |

The machine-readable version is `promotion-contract.json`.

## Fail-closed semantics

Promotion stops on any of the following:

- missing required artifact
- malformed JSON artifact
- policy `deny`
- canonical `spec_hash` mismatch
- signature verification failure
- release manifest hash mismatch
- missing release approval

## Truth path

```text
EvidenceBundle.json + spec_hash.txt
        ↓
Conftest gate policies + validator receipts
        ↓
decision_log.json + preflight_report.json
        ↓
release_manifest.json + attestations
        ↓
public release / archive
```

## Required commands

```bash
tools/validators/run_gate.sh A
tools/validators/run_gate.sh B
tools/validators/run_gate.sh C
tools/validators/run_gate.sh D
tools/validators/run_gate.sh E
tools/validators/run_gate.sh F
tools/validators/run_gate.sh G
```

The workflow in `.github/workflows/promotion.yml` wires these commands to GitHub Actions jobs.
