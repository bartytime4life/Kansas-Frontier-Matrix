<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-consent-revocation
title: Consent and Revocation Control Plane
type: standard
version: v1
status: draft
owners: TODO
created: TODO
updated: TODO
policy_label: public
related: [kfm://doc/control-plane-index, kfm://doc/policy-core, TODO]
tags: [kfm, consent, governance, privacy]
notes: [Placeholders require verification; aligns with EvidenceBundle + policy gate doctrine]
[/KFM_META_BLOCK_V2] -->

# Consent and Revocation Control Plane
*Governed consent attachment, verification, and revocation lineage for KFM EvidenceBundles*

---

## ⛳ Purpose

This document defines how **consent is encoded, enforced, audited, and revoked** across the Kansas Frontier Matrix (KFM) control plane.

It ensures:

- Every EvidenceBundle carries **explicit, inspectable consent**
- Consent is **verifiable, time-bound, and policy-enforced**
- Revocation is **deterministic, auditable, and fail-closed**
- Downstream artifacts reflect **correct lineage after revocation**

---

## 🔗 Quick Navigation

- [Consent Model](#consent-model)
- [Revocation Model](#revocation-model)
- [Policy Gates](#policy-gates)
- [Run Receipts](#run-receipts)
- [CI / Conftest Enforcement](#ci--conftest-enforcement)
- [Evidence Drawer Requirements](#evidence-drawer-requirements)
- [File Map](#file-map)
- [Test Fixtures](#test-fixtures)

---

## 🧭 Scope

### Included

- EvidenceBundle consent attachment
- Consent schema structure
- Revocation lifecycle and lineage
- Policy enforcement gates
- CI / validation integration
- UI visibility requirements

### Excluded

- Identity verification systems (handled elsewhere)
- Credential issuance systems (e.g., VC issuance)
- External consent capture UX (out of scope here)

---

## 🧱 Consent Model

Every EvidenceBundle MUST include a `consent` block.

### Structure

```json
{
  "consent": {
    "consent_standard": "ISO-TS-27560 | Kantara",
    "consent_scope": "kfm://scope/<uri>",
    "consent_issued_iso": "YYYY-MM-DDThh:mm:ssZ",
    "consent_expiry_iso": "YYYY-MM-DDThh:mm:ssZ",
    "revocation_token": "urn:uuid:<opaque>",
    "consent_vc_ref": "kfm://vc/<optional>",
    "minimum_count_policy": {
      "min_count": 5,
      "mode": "suppress"
    },
    "differential_privacy": {
      "epsilon": 0.5,
      "mechanism": "laplace",
      "seed_hash": "sha256:<seed>"
    },
    "audit_run_receipt_url": "https://audit.example/run/<id>",
    "spec_hash": "sha256:<canonical-hash>"
  }
}
```

### Invariants

| Rule | Description |
|------|-------------|
| REQUIRED | Consent block must exist on all EvidenceBundles |
| SIGNED | Included in bundle envelope signature |
| CANONICAL | `spec_hash` computed via canonical JSON |
| STABLE | Hash must not change due to retrieval metadata |
| VALIDATED | CI must reject missing or malformed consent |

---

## 🔁 Revocation Model

Revocation is modeled as an immutable **delta event**.

### Deterministic ID

```text
sha256("revoke" || revocation_token || prior_spec_hash || timestamp)
```

### Revocation Manifest

```json
{
  "revoke_delta": {
    "id": "sha256:<computed>",
    "artifact_ids": ["kfm://artifact/<id>"],
    "change_type": "suppress | recompute",
    "prior_digest": "sha256:<previous>",
    "suppression_policy": { "minimum_count": 5 },
    "dp_params": {
      "epsilon": 0.5,
      "mechanism": "laplace",
      "seed_hash": "sha256:<seed>"
    },
    "timestamp": "YYYY-MM-DDThh:mm:ssZ",
    "signer": "cosign://<identity>"
  }
}
```

---

## ⚙️ Revocation Behavior

### Suppress Mode

- Applies minimum-count thresholds
- Removes identifying contribution
- Marks artifacts as **REVOKED**
- Fail-closed for downstream queries

### Recompute Mode

- Rebuilds aggregates excluding revoked subject
- Applies DP if required
- Emits new signed artifacts + run receipts
- Marks previous artifacts as **SUPERSEDED**

---

## 🚦 Policy Gates

Promotion and public release MUST enforce:

| Condition | Action |
|----------|--------|
| Missing consent | DENY |
| Expired consent | DENY |
| Active revoke_delta | DENY until recompute/suppress complete |
| Small-n exposure | DENY |
| Missing DP where required | DENY |

---

## 🧾 Run Receipts

Each pipeline step MUST emit:

```json
{
  "run_receipt": {
    "id": "kfm://run/<uuid>",
    "artifact_ids": ["kfm://artifact/<id>"],
    "inputs_spec_hash": "sha256:<spec>",
    "consent_spec_hash": "sha256:<consent>",
    "policy_eval_ref": "kfm://policy_eval/<id>",
    "timestamp": "YYYY-MM-DDThh:mm:ssZ",
    "signer": "cosign://<identity>",
    "audit_ledger_entry": "https://audit.example/entry/<id>"
  }
}
```

### Invariants

- Every transformation step MUST emit a receipt
- Consent hash MUST be carried forward
- Receipts MUST link to audit ledger

---

## 🧪 CI / Conftest Enforcement

### Example Rego Gate

```rego
package kfm.consent

default allow = false

required_keys := {
  "consent_standard",
  "consent_scope",
  "consent_issued_iso",
  "consent_expiry_iso",
  "revocation_token",
  "minimum_count_policy",
  "differential_privacy",
  "audit_run_receipt_url",
  "spec_hash"
}

allow {
  input.kind == "EvidenceBundle"
  consent := input.consent
  every k in required_keys { consent[k] }
  time.parse_rfc3339(consent.consent_issued_iso)
  time.parse_rfc3339(consent.consent_expiry_iso)
  consent.minimum_count_policy.min_count >= 2
}
```

---

## 🧭 Evidence Drawer Requirements

Public UI MUST expose:

- Consent standard + scope
- Issue + expiry timestamps
- Spec hash
- Revocation state (ACTIVE / REVOKED / SUPERSEDED)
- Privacy posture:
  - Minimum count threshold
  - DP epsilon (if applied)
- Links:
  - Run receipts
  - Revocation ledger entries

---

## 🗂️ File Map

```
policy/core/consent.rego
policy/core/revocation.rego
schemas/contracts/v1/core/consent.schema.json
schemas/contracts/v1/core/revoke_delta.schema.json
tools/validators/core/validate_consent.py
tools/validators/core/validate_revoke_delta.py
data/receipts/runs/**/run_receipt.json
data/receipts/revocations/**/revoke_delta.json
docs/control-plane/CONSENT_AND_REVOCATION.md
```

---

## 🧪 Test Fixtures

```
tests/fixtures/consent/valid_bundle.json
tests/fixtures/consent/missing_keys.json
tests/fixtures/revoke/revoke_delta_valid.json
tests/policy/consent_test.rego
```

---

## ⚠️ Open Questions

| Area | Status |
|------|--------|
| Canonical JSON standard (JCS vs alternative) | NEEDS VERIFICATION |
| DP enforcement threshold rules | NEEDS VERIFICATION |
| Ledger implementation details | UNKNOWN |
| Consent VC integration depth | INFERRED |

---

## ✅ Definition of Done

- Consent block required + validated in CI
- Revocation produces signed delta
- Downstream artifacts reflect lineage
- Public outputs fail closed when revoked
- Evidence Drawer exposes full consent + revoke chain

---

## 🔙 Back to top
