# KFM Network Layer (infra/platform/network)

![Governed](https://img.shields.io/badge/KFM-governed-2955C0)
![Evidence-first](https://img.shields.io/badge/evidence--first-yes-0B3D91)
![Trust membrane](https://img.shields.io/badge/trust%20membrane-enforced-FF6A13)
![Platform](https://img.shields.io/badge/platform-Kubernetes%20%2F%20OpenShift-EE0000)

Network is not “plumbing” in KFM — it is part of the **governance surface**.

This directory is where we define and enforce **network boundaries** that make the KFM trust membrane real:
- what is reachable from outside the cluster,
- what can talk to what inside the cluster,
- what can leave the cluster (egress),
- and what *must never* be exposed (datastores, admin ports, internal-only services).

> [!IMPORTANT]
> **KFM trust membrane invariant (non-negotiable):**
> UI and external clients never access databases directly. All access is via the governed API + policy boundary.  
> This README documents how the network layer enforces that invariant.

---

## Contents

- [Scope](#scope)
- [Non-negotiables](#non-negotiables)
- [Architecture at a glance](#architecture-at-a-glance)
- [Repository layout](#repository-layout)
- [Ingress](#ingress)
- [East–west traffic](#eastwest-traffic)
- [Egress controls](#egress-controls)
- [DNS and naming](#dns-and-naming)
- [TLS and certificates](#tls-and-certificates)
- [Network policy baseline](#network-policy-baseline)
- [Observability and audit](#observability-and-audit)
- [Change workflow](#change-workflow)
- [Validation gates](#validation-gates)
- [Glossary](#glossary)

---

## Scope

This folder covers **platform networking** required to run KFM safely:

- **North–south traffic** (internet ↔ cluster): ingress controllers / routes / edge gateways
- **East–west traffic** (service ↔ service): service-to-service paths, service mesh (optional), mTLS (optional)
- **Datastore isolation**: PostGIS, graph DB, object storage, search indices must be **internal-only**
- **Egress governance**: connectors/pipelines can reach approved upstreams; everything else is blocked or brokered
- **DNS/TLS**: domains, wildcard routing (when applicable), certificate automation, and rotation

---

## Non-negotiables

> [!NOTE]
> These are **requirements**, not suggestions. If an environment cannot satisfy these, it is not a valid KFM deployment.

### 1) Trust membrane reachability rules

- The **only** externally reachable application endpoints are:
  - **Web UI** (static + API calls)
  - **Governed API Gateway** (FastAPI/GraphQL or equivalent)
- Datastores are **never** exposed publicly (no public LoadBalancer services, no public NodePorts, no public routes).
- Internal services that touch protected data must be **cluster-internal only**.

### 2) Default deny, explicit allow

- Cluster workloads run under **default-deny** network policies.
- Allow rules are added narrowly:
  - by namespace
  - by label selectors
  - by port/protocol
  - with **documented rationale** in PR

### 3) Every boundary crossing is governed

Traffic crossing the trust membrane must pass through:
- authentication,
- policy evaluation,
- query shaping/redaction,
- and audit/provenance logging.

Network ensures the gateway remains the only feasible path for these requirements to be met.

---

## Architecture at a glance

```mermaid
flowchart LR
  user[Users / Partners] -->|HTTPS| edge[Edge DNS/WAF/CDN (env-specific)]
  edge -->|HTTPS| ingress[Cluster Ingress (OpenShift Router / Ingress Controller)]

  ingress -->|HTTPS| ui[Web UI (React/Map UI)]
  ingress -->|HTTPS| api[Governed API Gateway]

  api --> opa[Policy-as-Code (OPA)]
  api --> audit[Audit + Provenance]

  api -->|DB| postgis[(PostGIS)]
  api -->|Graph| neo4j[(Graph DB)]
  api -->|Index| search[(Search/Vector)]
  api -->|Objects| obj[(Object Store)]

  api -->|Egress (restricted)| upstream[Approved upstream APIs/files]
```

Key idea: **UI does not and cannot reach databases directly.** The network policies and service exposure rules make the API gateway the only path.

---

## Repository layout

> [!TIP]
> If you are bootstrapping this directory, start with **NetworkPolicy baselines + ingress** first. Everything else layers on.

Proposed structure (adjust to your repo conventions):

```text
infra/
  platform/
    network/
      README.md

      # 01 - ingress / edge
      ingress/
        openshift-routes/          # Route + TLS termination definitions (if OpenShift)
        ingress-nginx/             # Ingress controller manifests (if not OpenShift)
        gateway/                   # API gateway definitions (if separated from app repo)

      # 02 - network policies
      policies/
        baseline/
          default-deny.yaml
          allow-dns.yaml
          allow-ingress-to-api.yaml
          allow-api-to-datastores.yaml
        namespaces/
          edge.yaml
          app.yaml
          data.yaml
          pipelines.yaml

      # 03 - egress governance
      egress/
        allowlists/                # approved domains/IPs (environment overlay references)
        egress-proxy/              # optional: proxy/broker for outbound traffic
        networkpolicy-egress.yaml  # baseline egress policy

      # 04 - dns + certs
      dns/
        external-dns/              # optional: ExternalDNS config
      tls/
        cert-manager/              # optional: cert-manager issuers + certificates

      # 05 - docs + runbooks
      docs/
        diagrams/
        runbooks/
```

> [!IMPORTANT]
> Any environment-specific values (domains, CIDRs, IPs, cloud resource IDs) should live in an overlay system (e.g., `infra/environments/<env>/...`).  
> **Do not commit secrets** and **do not hardcode production IPs** into shared manifests.

---

## Ingress

### Pattern

- External clients talk to the cluster via **HTTPS**.
- Ingress is terminated at:
  - OpenShift Router **Route** (if OpenShift), or
  - an Ingress Controller (nginx/HAProxy/etc.), or
  - a dedicated gateway (env-dependent)

### Allowed public endpoints

| Endpoint | Public? | Purpose | Notes |
|---|---:|---|---|
| Web UI | ✅ | human interface | static + API calls |
| Governed API Gateway | ✅ | policy + auth boundary | must be the only path to data |
| Datastores (PostGIS/Neo4j/etc.) | ❌ | internal only | **never** public |

---

## East–west traffic

### Recommended segmentation

| Zone | What lives there | Network stance |
|---|---|---|
| edge | ingress/router/gateway | allow inbound from edge + allow to app |
| app | API gateway + app services | deny by default; allow from edge + allow to data as needed |
| data | PostGIS/graph/search/object store | deny by default; allow only from API gateway (and ops tooling if required) |
| pipelines | ingestion/ETL jobs | deny by default; allow to data + controlled egress to upstreams |
| observability | logging/metrics/tracing | allow from cluster only; no public access |

> [!NOTE]
> Exact namespaces and labels are environment-dependent. The “zones” above are a governance tool: **make boundaries explicit and enforceable**.

---

## Egress controls

KFM ingests from many upstream providers. Egress must be **explicitly controlled** because it is a data exfiltration and supply-chain surface.

Baseline requirements:

- Default deny egress for most namespaces.
- Allow egress:
  - from `pipelines` namespace (or equivalent),
  - to approved domains/IPs,
  - via an egress proxy (recommended) for logging and throttling.
- Record:
  - why the destination is needed,
  - what dataset(s) it supports,
  - which connector uses it,
  - any rate-limiting rules.

---

## DNS and naming

### Domain strategy

- Use a consistent FQDN layout for stable routing and certificates, e.g.:

| Name | Example | Purpose |
|---|---|---|
| UI | `kfm.<env>.<domain>` | human access |
| API | `api.kfm.<env>.<domain>` | governed API |
| Internal-only | `*.svc.cluster.local` | cluster traffic |

> [!WARNING]
> Public DNS names should only exist for the UI and API gateway. Datastores must not have public DNS entries.

---

## TLS and certificates

Requirements:

- HTTPS everywhere for north–south traffic.
- TLS termination strategy must be explicit (edge vs router vs gateway).
- Certificates must support:
  - automated renewal,
  - rotation runbooks,
  - staging vs production issuers,
  - and auditability.

Recommended (if available): `cert-manager` + issuer per environment.

---

## Network policy baseline

### Baseline policies we expect to exist

- ✅ `default-deny` for every namespace (or a default template applied at namespace creation)
- ✅ `allow-dns` (cluster DNS resolution)
- ✅ `allow-ingress-to-ui` and `allow-ingress-to-api`
- ✅ `allow-api-to-datastores`
- ✅ `deny-all-to-datastores-except-api`
- ✅ `egress-deny` (plus allowlists where necessary)

### Minimal “trust membrane enforcement” policy set

> [!IMPORTANT]
> If you implement only one thing first, implement this.

- Deny all ingress to `data` namespace.
- Allow only from API gateway pod labels to datastore pod labels on required ports.
- Ensure datastores are ClusterIP only.

---

## Observability and audit

Network and edge logs are first-class evidence in KFM incident response:

- Ingress/gateway access logs must be captured (with redaction controls as needed).
- Audit logs from policy evaluation must be retained according to governance policy.
- (Optional but recommended) capture:
  - flow logs (north–south),
  - NetworkPolicy drops (east–west),
  - egress proxy logs (outbound).

---

## Change workflow

Network changes are **production changes**.

### PR checklist

- [ ] Change is scoped to one concern (ingress OR policy OR egress OR DNS/TLS)
- [ ] Default deny remains intact
- [ ] No datastore exposure
- [ ] Rationale included in the PR description (“why is this needed?”)
- [ ] Validation gates pass (see below)
- [ ] Rollback plan documented (how to revert safely)

---

## Validation gates

Expected CI gates for this directory:

### Static checks (fast)

- [ ] YAML lint / schema validation
- [ ] K8s/OpenShift manifest validation
- [ ] Policy-as-code checks (Conftest/OPA) ensuring:
  - no public services for datastores,
  - no Route/Ingress for internal-only services,
  - required NetworkPolicy objects exist.

### Runtime checks (integration)

- [ ] “Canary” environment smoke test:
  - UI and API reachable
  - API can reach datastores
  - UI cannot reach datastores directly
- [ ] Egress tests:
  - pipelines can reach approved upstreams
  - non-pipeline namespaces cannot egress by default

---

## Glossary

- **Trust membrane**: the governed boundary where auth + policy + redaction + audit must occur.
- **Governed API gateway**: the only supported path for external clients to access KFM data/services.
- **Default deny**: NetworkPolicy stance where nothing communicates unless explicitly allowed.
- **North–south traffic**: external ↔ cluster traffic.
- **East–west traffic**: service ↔ service traffic inside the cluster.
- **Egress**: outbound traffic from cluster workloads to the internet / upstream providers.
- **Route (OpenShift)**: OpenShift-native HTTP(S) exposure primitive (similar to Ingress, but OpenShift-specific).

---
