# Egress (Outbound Connectivity) — Platform Guardrail

![KFM Governed](https://img.shields.io/badge/KFM-governed-2ea44f)
![Evidence-first](https://img.shields.io/badge/evidence--first-required-2ea44f)
![Default Deny](https://img.shields.io/badge/egress-default--deny-critical)
![Policy as Code](https://img.shields.io/badge/policy--as--code-OPA%2FRego-informational)
![GitOps](https://img.shields.io/badge/deploy-GitOps-blue)

> [!IMPORTANT]
> This directory defines **cluster/platform egress controls** (outbound networking).  
> It is part of KFM’s **trust membrane**: workloads must not “reach around” governance by talking directly to arbitrary external endpoints or by bypassing policy checks.

---

## Purpose

KFM is a governed geospatial + historical knowledge system with a canonical flow of:  
**data → pipeline → catalogs/provenance → governed APIs → UI/Focus Mode**.

Egress controls extend that same governance posture to **outbound connectivity**:

- **Default-deny outbound** traffic for governed namespaces.
- **Allow-by-exception** for approved destinations and ports.
- **Auditability** for who approved what, why, and for how long.
- **Operational safety**: reduce dependency drift and limit data exfiltration paths.

> [!NOTE]
> This README describes a **recommended** egress module design.  
> Some implementation details (proxy choice, CNI-specific CRDs, exact folder contents) may be **(not confirmed in repo)** and should be aligned to your cluster runtime and existing platform conventions.

---

## What this module does

### Primary KFM uses
- **Connectors / ingestion** reaching upstream data sources (APIs, bulk downloads) in a controlled way.
- **CI/build** pulling container images and dependencies from approved registries.
- **Telemetry** exporting metrics/logs to approved sinks (if enabled).
- **Defense-in-depth**: limit what a compromised pod can reach.

### Non-goals
- **Ingress** / north-south traffic to KFM (handled elsewhere).
- Replacing application-level authz/policy checks.
- Granting any direct path to storage (databases/object store) — those remain behind governed APIs.

---

## Architecture

```mermaid
flowchart LR
  subgraph Cluster["KFM Cluster"]
    W[Workload Pods] -->|Allowed by policy| NP[Namespace Egress Policy]
    NP -->|Allowed destination| EP[Egress Proxy/Gateway\n(optional; not confirmed in repo)]
    EP --> NET[(Internet / Partner APIs)]
    NP -.->|Denied| DROP[Drop/Reject]
    EP --> LOGS[Audit logs + metrics]
  end

  LOGS --> OBS[(Observability / SIEM sinks)]
```

### Design principles

| Principle | What it means in practice | Why it exists |
|---|---|---|
| **Default deny** | No namespace has outbound access unless explicitly allowed | Prevent exfiltration & surprise dependencies |
| **Narrow scope** | Prefer rules tied to namespace + workload + port | Least privilege |
| **Single chokepoint (optional)** | External traffic routes via egress proxy/gateway | Central allowlists, logging, and controls |
| **Policy-as-code** | Rules are PR-reviewed and CI-validated | Fail-closed posture; prevent drift |
| **Auditable exceptions** | Each allow has owner + reason + expiry | Evidence-first governance |

---

## Directory layout

```text
infra/platform/egress/
├── README.md
├── kustomize/                         # (recommended; not confirmed in repo)
│   ├── base/                          # baseline egress controls (default deny + essentials)
│   └── overlays/
│       ├── dev/
│       ├── stage/
│       └── prod/
├── policies/                          # (recommended; not confirmed in repo)
│   ├── networkpolicy/                 # Kubernetes NetworkPolicy resources
│   ├── allowlists/                    # domain/CIDR allowlists + metadata (owner/expiry)
│   └── opa/                           # Rego rules + conftest policy tests
├── components/                        # (recommended; not confirmed in repo)
│   ├── egress-proxy/                  # proxy Deployment/Service/config (if used)
│   └── dns/                           # DNS allowances / node-local DNS (optional)
└── tests/                             # (recommended; not confirmed in repo)
    ├── conftest/
    └── smoke/
```

---

## GitOps deployment

This module is designed to be deployed via GitOps (Argo CD / OpenShift GitOps) **(not confirmed in repo)**.

Recommended pattern:
1. `kustomize/base` defines baseline **default-deny** and “minimum required allows”.
2. Overlays add only environment-specific, reviewed exceptions (e.g., dev-only endpoints).

> [!TIP]
> A common GitOps pattern is to deploy platform modules as “core” cluster components, separate from application workloads, aligned to organizational boundaries.

---

## Baseline policy: default-deny egress

Baseline **namespace default-deny** egress NetworkPolicy:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-egress
  namespace: app
spec:
  podSelector: {}
  policyTypes:
  - Egress
  egress: []
```

> [!WARNING]
> **NetworkPolicy enforcement depends on the cluster networking implementation.**  
> Policies can exist but be non-enforced if the network plugin doesn’t implement them. Validate enforcement before treating egress policy as a security boundary.

### Minimum allowed traffic (typical)
Even in default-deny mode, most namespaces need limited outbound for:
- **Cluster DNS** (UDP/TCP 53 to CoreDNS/kube-dns Service)
- **In-cluster platform dependencies** (only what is required)
- **Egress proxy/gateway Service** (if using a chokepoint design)

---

## Requesting new outbound access

All egress exceptions are **governed changes**.

### Required PR metadata
| Field | Example | Notes |
|---|---|---|
| `owner` | `data-eng@…` | Accountable party |
| `reason` | “Chronicling America OCR ingest” | Tie to dataset/work item |
| `scope` | `namespace + workload` | Narrowest possible |
| `destinations` | domains/CIDRs/ports | Prefer domains via proxy |
| `data-classification` | `public / restricted / sensitive-location` | Drives review strictness |
| `expiry` | `2026-06-30` | Required for time-bounded access |
| `audit_ref` | ticket/issue link | Traceability requirement |

### Approval & CI gates (recommended)
- ✅ Platform/SRE review (operability + correctness)
- ✅ Security/governance review (least privilege; sensitivity)
- ✅ CI policy checks (OPA/Rego + schema validation)
- ✅ Smoke test evidence attached:
  - **ALLOW** works for intended destination(s)
  - **DENY** still holds for arbitrary endpoints

---

## Operations runbook

<details>
<summary><strong>Verify effective egress controls</strong></summary>

1. Confirm NetworkPolicies exist in the namespace.
2. Run a smoke pod/job to test:
   - Allowed: DNS + proxy + approved domains
   - Denied: arbitrary outbound IPs/domains
3. Capture evidence (command output + relevant logs) and attach to the PR.

</details>

<details>
<summary><strong>Troubleshoot “egress is blocked”</strong></summary>

1. Confirm the namespace/workload is supposed to have egress.
2. Validate that your cluster enforces NetworkPolicy egress.
3. If using an egress proxy:
   - Check proxy denies (host not allowlisted, port blocked, TLS handshake issues).
4. Confirm DNS is allowed (blocked DNS often looks like “everything is broken”).

</details>

<details>
<summary><strong>Emergency rollback</strong></summary>

- Roll back via GitOps (revert PR or roll back the Application revision).
- Avoid “hot fixes” in-cluster that drift from Git; if emergency changes occur, backport immediately.

</details>

---

## Observability and auditing

Egress is a governance surface; minimum signals:
- Proxy access logs (destination host/port, allow/deny, request size) **if proxy is used**
- Network policy denies (if exposed by your CNI / network plugin)
- Audit events for allowlist changes (who approved, when, what changed)

> [!IMPORTANT]
> Logs may contain sensitive URLs/parameters. Apply redaction rules before exporting logs off-cluster.

---

## Definition of Done

- [ ] Baseline default-deny egress applied to governed namespaces
- [ ] Allow rules are scoped (namespace + workload + port) and documented
- [ ] Policy-as-code checks exist and block unsafe broad rules
- [ ] Smoke tests prove deny-by-default and allow-by-exception
- [ ] Audit metadata is present for every exception
- [ ] Runbook validated (operator can troubleshoot + rollback)

---

## Security notes

- Prefer allowlisting **domains via proxy** instead of raw IP allowlists.
- Treat any “allow all egress” change as a **P0 security incident** unless explicitly approved and time-bounded.
- For restricted/sensitive-location datasets, avoid outbound transfers except to explicitly approved endpoints.

---

## Maintainers

This is a **platform guardrail** module.

Recommended:
- Add a `CODEOWNERS` rule requiring platform/security approval for:
  - `infra/platform/egress/**`
