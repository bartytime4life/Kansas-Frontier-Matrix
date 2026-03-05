<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/9f0cb56f-8984-434f-b9c7-ea988e703f67
title: KFM Root Governance Charter
type: standard
version: v1
status: draft
owners: ["KFM Governance Council", "KFM Platform Governance"]
created: 2026-03-05
updated: 2026-03-05
policy_label: public
related:
  - ./ROOT_GOVERNANCE.md
  - ../quality/GATES_DEFINITION_OF_DONE.md
  - ../quality/SECURITY_BASELINE.md
  - ../standards/README.md
tags: [kfm, governance, charter, policy, promotion]
notes:
  - Normative charter for trust membrane and promotion gating.
  - This file is designed to be linked by agent contracts and policy docs.
[/KFM_META_BLOCK_V2] -->

# KFM Root Governance Charter

This charter defines the non-negotiable governance posture for Kansas Frontier Matrix (KFM): **fail-closed**, **evidence-first**, and **policy-enforced**.

## Charter principles

1. **Trust membrane is mandatory.** All reads/writes affecting governed outputs MUST pass through approved policy enforcement points.
2. **Promotion is contractual.** No artifact becomes publishable unless required gates pass with auditable evidence.
3. **Evidence over assertion.** Claims in UI, APIs, and generated narrative MUST resolve to source artifacts and provenance.
4. **Least privilege by default.** Human and machine actors receive minimum permissions required for their role.
5. **Determinism is an operational requirement.** Equivalent inputs must produce equivalent identities and receipts.

## Governance decision model

- **Council-owned invariants:** membrane boundaries, policy-label semantics, release gates.
- **Steward-owned controls:** domain QA thresholds, approved upstream sources, redaction policies.
- **Operator-owned execution:** pipeline runtime, incident response, rollback mechanisms.

Conflicts resolve in this order:

1. Charter requirements
2. Published standards in `docs/standards/`
3. Schema/API contracts
4. Guides and runbooks

## Mandatory release gates

A release request MUST include machine-verifiable artifacts for the following checks:

| Gate | Required evidence | Fail condition |
|---|---|---|
| Identity | Stable `dataset_id`, `dataset_version_id`, digest set | Missing or non-deterministic IDs |
| Rights | License + rights + terms snapshot | Unspecified or non-compliant rights |
| Sensitivity | Policy label + obligations | Missing label/obligation data |
| Catalog | DCAT/STAC/PROV linkage validation | Broken links or schema violations |
| QA | Threshold report + exception log | Threshold breach without approved waiver |
| Receipt | Run receipt + toolchain metadata | Missing receipt or unverifiable digests |

### Example gate contract payload

```json
{
  "dataset_id": "kfm.hydrology.stream-network",
  "dataset_version_id": "kfm.hydrology.stream-network@2026.03.05",
  "spec_hash": "jcs:sha256:3fe2c6b48f8d16f2f2b4f8ab5ecf2209b6a2e4e96fbb4d4d84cece92a53f5f9f",
  "policy_label": "public_generalized",
  "gates": {
    "identity": {"status": "pass"},
    "rights": {"status": "pass"},
    "sensitivity": {"status": "pass", "obligations": ["geom-generalize-h3-r8"]},
    "catalog": {"status": "pass"},
    "qa": {"status": "pass"},
    "receipt": {"status": "pass"}
  }
}
```

## Policy enforcement reference (Rego)

```rego
package kfm.gates

default allow := false

required_gates := {"identity", "rights", "sensitivity", "catalog", "qa", "receipt"}

missing_gate[g] {
  g := required_gates[_]
  not input.gates[g]
}

failed_gate[g] {
  g := required_gates[_]
  input.gates[g].status != "pass"
}

allow {
  count(missing_gate) == 0
  count(failed_gate) == 0
  input.policy_label != ""
}
```

## Roles and accountability

- **Governance Council (Accountable):** approves invariant changes and emergency waivers.
- **Domain Stewards (Responsible):** maintain domain policy labels and QA rules.
- **Platform Operators (Responsible):** enforce CI/runtime policy parity and maintain audit trails.
- **Contributors (Consulted):** propose changes through governed pull requests with evidence.

## Change control

Any charter update MUST include:

1. A rationale section with risk tradeoffs.
2. A migration plan (if behavior changes).
3. Contract test updates proving the new rule.
4. Review from governance + platform owners.

## Minimum audit record

Each governance-impacting run MUST emit an immutable receipt that includes:

- `run_id`, `actor`, `time_window`
- policy bundle digest
- gate outputs and evidence URIs
- approved waiver IDs (if applicable)
- final decision (`promote`, `quarantine`, `deny`)

