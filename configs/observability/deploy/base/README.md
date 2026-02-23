<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/58a5746a-94d4-4885-9543-68d1eb3cb5ee
title: Observability Deploy Base
type: standard
version: v1
status: draft
owners: TODO: Observability maintainers
created: 2026-02-23
updated: 2026-02-23
policy_label: restricted
related:
  - ../overlays/
  - ../../README.md
tags: [kfm, observability, deploy, kustomize, kubernetes]
notes:
  - Environment-agnostic Kustomize base for the KFM observability plane.
  - Treat as infrastructure documentation; avoid secrets and cluster-specific endpoints here.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Observability Deploy Base
Environment-agnostic Kubernetes manifests for the KFM observability plane, intended to be composed by overlays.

![Status](https://img.shields.io/badge/status-draft-yellow)
![Scope](https://img.shields.io/badge/scope-k8s%20kustomize-blue)
![Telemetry](https://img.shields.io/badge/telemetry-OTel%20to%20Prometheus%2FMimir%20to%20Tempo-9cf)
![Policy](https://img.shields.io/badge/policy-restricted-red)
![CI](https://img.shields.io/badge/ci-TODO-lightgrey)

---

## Navigate
- [Intent](#intent)
- [Directory contract](#directory-contract)
- [Deploy](#deploy)
- [Telemetry traceability contract](#telemetry-traceability-contract)
- [Catalog linkage](#catalog-linkage)
- [Operational checklist](#operational-checklist)
- [Troubleshooting](#troubleshooting)
- [Change management](#change-management)
- [Appendix](#appendix)

---

## Intent
This directory is the **base** deployment package for KFM observability. It should be:

- **Environment-agnostic**: no cluster-specific endpoints, storage classes, or hostnames.
- **Composable**: overlays (by environment, cluster, or tenancy) apply patches and add deltas.
- **Traceable**: the telemetry it enables must carry KFM identity keys so metrics and traces can be linked back to catalogs and provenance receipts.

If you are deploying KFM observability into a real cluster, you should almost always deploy an **overlay** (for example, `../overlays/dev`) rather than this base directly.

[Back to top](#top)

---

## Directory contract

### Where it fits
`configs/observability/deploy/base/` is the lowest-level Kustomize package for observability.

Expected relationship in the repo:

- `deploy/base` provides shared resources
- `deploy/overlays/<env-or-cluster>` composes the base and applies environment-specific patches

### Acceptable inputs
This directory may contain:

- Kubernetes manifests and Kustomize config used by the observability plane
- ConfigMaps for OTel Collector pipelines and processors
- Non-secret dashboard JSON and alert rules (if your org stores them as code)

### Exclusions
Do **not** put these in `base/`:

- Secrets, tokens, private keys, cloud credentials
- Cluster-specific endpoints (Ingress hostnames, external LB IPs, public URLs)
- Environment-specific storage classes, node selectors, tolerations
- Any hard-coded policy decisions that vary by environment (move to overlays)

> WARNING  
> Base should remain safe to render in any environment. Treat it as reusable infrastructure code.

### Expected layout
Actual files may vary; keep the intent and boundaries stable.

```text
configs/observability/deploy/
└── base/
    ├── README.md
    ├── kustomization.yaml                 # base entry point
    ├── namespaces/                        # optional
    ├── otel-collector/                    # optional
    ├── metrics/                           # optional (Prometheus or Mimir integration)
    ├── traces/                            # optional (Tempo integration)
    ├── dashboards/                        # optional (Grafana dashboards as code)
    └── alerts/                            # optional (rules, alert routing)
```

[Back to top](#top)

---

## Deploy

### Render manifests
Render without applying, to inspect output:

```sh
kubectl kustomize configs/observability/deploy/base
```

### Apply base directly
This is typically for quick sandboxes only:

```sh
kubectl apply -k configs/observability/deploy/base
```

### Recommended: apply an overlay
If overlays exist, prefer:

```sh
kubectl apply -k configs/observability/deploy/overlays/<env-or-cluster>
```

> NOTE  
> Namespaces are often created/managed by platform administration. If this base omits namespaces, that is intentional and overlays or cluster bootstrap may be responsible.

[Back to top](#top)

---

## Telemetry traceability contract
KFM observability is only useful if telemetry can be **joined** to:

- pipeline run receipts
- dataset version identifiers
- catalog entries (STAC and DCAT)
- provenance bundles (PROV)

This base deployment is expected to enforce or support that join via a **canonical set of identity keys**.

### Canonical identity keys
At minimum, telemetry should carry these canonical keys (as OTel resource attributes), and the metrics pipeline should map them into stable Prometheus label names.

| Canonical key | Meaning | Typical source |
|---|---|---|
| `kfm.pipeline.name` | Stable pipeline slug | pipeline runner / orchestrator |
| `kfm.job.run_id` | Unique run identifier | pipeline runner |
| `kfm.artifact.dataset_version_id` | Dataset version id for produced artifacts | pipeline output promotion step |
| `kfm.git.commit_sha` | Code commit that produced the run | CI system / build metadata |
| `kfm.gov.policy_label` | Policy label for data & narrative constraints | governance policy decision |
| `kfm.env` | Environment identifier | deployment environment |

### Mapping guidance
If you run Prometheus-compatible metrics, labels should be mapped to predictable names:

| OTel resource attribute | Prometheus label | Notes |
|---|---|---|
| `kfm.pipeline.name` | `pipeline` | Prefer stable, low-cardinality pipeline identifiers |
| `kfm.job.run_id` | `job_run_id` | Can be high-cardinality; see note below |
| `kfm.artifact.dataset_version_id` | `dataset_version_id` | Required to join telemetry to cataloged artifacts |
| `kfm.git.commit_sha` | `commit` | Helpful for deploy regression correlation |
| `kfm.gov.policy_label` | `policy_label` | Enables policy-aware filtering of telemetry |
| `kfm.env` | `env` | Should match cluster/environment naming standard |

> WARNING  
> `job_run_id` is inherently high-cardinality. If your metrics backend has strict cardinality limits, consider restricting `job_run_id` to:
> - traces and logs only, **or**
> - a small set of “run summary” metrics, **or**
> - exemplars (if supported)
>
> Do not silently drop the key everywhere; it is required for deterministic linkage.

### Responsibilities of this base deployment
This base should, as applicable in your stack:

- Deploy an **OTel Collector** pipeline that:
  - accepts OTLP from pipelines and services
  - ensures the canonical attributes exist (or rejects/flags missing identity keys)
  - maps attributes into metrics labels for the Prometheus-compatible exporter path
- Provide a default set of dashboards/alerts oriented around:
  - pipeline runs
  - dataset versions
  - policy label filtering (where permitted)

[Back to top](#top)

---

## Catalog linkage
Telemetry must be joinable back to catalog and provenance artifacts without guesswork.

Minimum expectation:

- The same run and dataset identifiers used in telemetry are written into:
  - STAC Item `properties`
  - PROV activity records
  - run receipts and audit records

If you can’t join these objects by key, treat it as a broken traceability chain.

[Back to top](#top)

---

## Operational checklist

### Pre-merge checks
- [ ] `kustomize build` succeeds for `base/`
- [ ] No secrets in `base/` (ConfigMaps ok; Secrets belong elsewhere)
- [ ] Canonical identity keys are documented and enforced
- [ ] Any added labels are reviewed for cardinality risk

### Post-deploy checks
- [ ] OTel Collector is healthy and receiving OTLP
- [ ] Metrics are present in the backend and include required labels
- [ ] Traces are present and searchable by `kfm.job.run_id` and `kfm.artifact.dataset_version_id`
- [ ] Dashboards load without manual steps
- [ ] Alerts route to the correct on-call targets in the overlay

[Back to top](#top)

---

## Troubleshooting

### No metrics arriving
- Confirm workloads are exporting OTLP to the collector service.
- Confirm the collector pipeline has an exporter configured for your metrics backend.
- Check that required canonical keys are not being dropped by processors.

### Labels missing or renamed
- Ensure the mapping from OTel attributes to Prometheus labels is defined in the collector pipeline.
- Ensure you aren’t overwriting resource attributes in overlays.

### High-cardinality warnings
- Identify which labels exploded cardinality.
- Reduce label set on high-volume metrics first.
- Preserve linkage keys on traces and low-volume summary metrics.

[Back to top](#top)

---

## Change management
Treat changes here as **infrastructure API changes**:

- Small diffs, reversible
- Overlays remain compatible or are updated in the same change
- Maintain backward compatibility for canonical identity keys whenever possible

Recommended practice:

- Document every change that affects exported telemetry fields or label names.
- Add a migration note in overlays if a mapping changes.

[Back to top](#top)

---

## Appendix

<details>
  <summary><strong>Example: setting canonical attributes from a pipeline runner</strong></summary>

This is a generic example of what a pipeline runner might set for OTel resource attributes.

```sh
export KFM_ENV="dev"
export OTEL_RESOURCE_ATTRIBUTES="kfm.env=${KFM_ENV},kfm.pipeline.name=etl_air_quality,kfm.job.run_id=run_2026_02_23_001,kfm.artifact.dataset_version_id=dv_abc123,kfm.git.commit_sha=deadbeef,kfm.gov.policy_label=restricted"
```

</details>

<details>
  <summary><strong>Example: overlay patch pattern</strong></summary>

Example only — do not assume file names match.

```yaml
# overlays/dev/kustomization.yaml
resources:
  - ../../base

patches:
  - target:
      kind: Deployment
      name: otel-collector
    patch: |-
      - op: replace
        path: /spec/template/spec/containers/0/resources
        value:
          requests:
            cpu: "250m"
            memory: "256Mi"
          limits:
            cpu: "1000m"
            memory: "1Gi"
```

</details>
