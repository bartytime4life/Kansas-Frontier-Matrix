# 🩺 Health (v1) — Response Examples

![Contract](https://img.shields.io/badge/contract-response_examples-blue)
![API](https://img.shields.io/badge/api-v1-informational)
![Endpoint](https://img.shields.io/badge/endpoint-GET_%2Fv1%2Fhealth-success)

This folder contains **canonical response examples** for the **KFM API** health endpoint.

> 📍 Path: `api/contracts/examples/responses/v1/health/`

---

## 🎯 What this endpoint is for

`GET /v1/health` is a **readiness-style** endpoint used by:

- ✅ Load balancers / uptime monitors
- ✅ Kubernetes readiness probes
- ✅ The UI (and tooling) to quickly validate the backend API surface
- ✅ Operators to see whether **core stores + governance signals + provenance stores** are “good enough to serve requests”

It returns **high-level status** plus a **structured breakdown** of subsystem checks.

---

## 🧱 Contract goals (design principles)

- **Fail-closed reporting**: if a dependency cannot be checked, treat it as **unhealthy** (or at least **degraded**) rather than “OK”.
- **No secrets**: never return credentials, connection strings, internal tokens, or sensitive paths.
- **Evidence-friendly**: include *build identifiers* + *governance/policy revision identifiers* so health snapshots can be tied back to a specific deploy.
- **Stable + extensible**: adding new checks should not break clients.

---

## 🔌 Endpoint

| Item | Value |
|---|---|
| Method | `GET` |
| Path | `/v1/health` |
| Response Content-Type | `application/json` |
| Cache | Recommended: `Cache-Control: no-store` |

---

## 🧾 Response shape (overview)

Top-level object:

```json
{
  "service": "kfm-api",
  "api_version": "v1",
  "status": "ok",
  "time_utc": "2026-01-24T18:09:30Z",
  "uptime_seconds": 18432,
  "build": {
    "version": "1.7.0",
    "git_sha": "bb86bf1",
    "build_time_utc": "2026-01-24T17:50:12Z"
  },
  "governance": {
    "mode": "fail_closed",
    "policy_pack_revision": "bb86bf1"
  },
  "checks": {
    "postgis": { "status": "ok", "latency_ms": 12 },
    "neo4j": { "status": "ok", "latency_ms": 18 },
    "catalogs": { "status": "ok", "stac": "ok", "dcat": "ok" },
    "prov_store": { "status": "ok" }
  },
  "graph_integrity": {
    "status": "ok",
    "last_run_utc": "2026-01-21T03:00:00Z",
    "orphaned_metadata_nodes": { "count": 0 }
  },
  "pipeline": {
    "last_run": {
      "run_id": "run_2026-01-23T02:14:55Z_7d2b",
      "run_time_utc": "2026-01-23T02:14:55Z",
      "idempotency_key": "ingest:usgs:nwis:2026-01-23",
      "canonical_digest": "sha256:9d9f2baf2c06d7c0b0c80dd3b2c24f5f0bb62da5f0b7d9d2bd60d4f7deadc0de"
    }
  },
  "links": {
    "openapi": "/openapi.json",
    "docs": "/docs"
  }
}
```

---

## ✅ Status semantics

### Top-level `status`

| Value | Meaning | Typical HTTP |
|---|---|---|
| `ok` | All **required** checks are healthy | `200` |
| `degraded` | Core checks pass, but at least one **non-critical** check failed | `200` |
| `down` | A **required** check failed (not safe to serve) | `503` |

### Per-check `status`

| Value | Meaning |
|---|---|
| `ok` | Healthy |
| `warn` | Responding, but impaired (latency, stale, partial availability) |
| `fail` | Not usable / unreachable |

> 🧠 Tip: If you’re unsure whether a dependency is “required”, treat it as required for **readiness** and optional for **liveness**.

---

## 🗂️ Recommended files in this folder

Even though this README is the contract “front door”, the folder is designed to hold **example JSON payloads** for tooling/tests:

```text
api/contracts/examples/responses/v1/health/
├── README.md
├── 200.ok.json
├── 200.degraded.json
└── 503.down.json
```

---

## 📦 Example responses

### ✅ `200 OK` — healthy (`200.ok.json`)

```json
{
  "service": "kfm-api",
  "api_version": "v1",
  "status": "ok",
  "time_utc": "2026-01-24T18:09:30Z",
  "uptime_seconds": 18432,
  "build": {
    "version": "1.7.0",
    "git_sha": "bb86bf1",
    "build_time_utc": "2026-01-24T17:50:12Z"
  },
  "governance": {
    "mode": "fail_closed",
    "policy_pack_revision": "bb86bf1"
  },
  "checks": {
    "postgis": {
      "status": "ok",
      "latency_ms": 12
    },
    "neo4j": {
      "status": "ok",
      "latency_ms": 18
    },
    "catalogs": {
      "status": "ok",
      "stac": "ok",
      "dcat": "ok"
    },
    "prov_store": {
      "status": "ok"
    },
    "search": {
      "status": "ok",
      "engine": "elasticsearch",
      "latency_ms": 24
    },
    "telemetry": {
      "status": "ok",
      "metrics": "enabled"
    }
  },
  "graph_integrity": {
    "status": "ok",
    "last_run_utc": "2026-01-21T03:00:00Z",
    "node_relationship_delta_pct": {
      "nodes": 0.4,
      "relationships": 0.8
    },
    "constraints": { "status": "ok" },
    "indexes": { "status": "ok" },
    "orphaned_metadata_nodes": { "count": 0 }
  },
  "pipeline": {
    "last_run": {
      "run_id": "run_2026-01-23T02:14:55Z_7d2b",
      "run_time_utc": "2026-01-23T02:14:55Z",
      "idempotency_key": "ingest:usgs:nwis:2026-01-23",
      "canonical_digest": "sha256:9d9f2baf2c06d7c0b0c80dd3b2c24f5f0bb62da5f0b7d9d2bd60d4f7deadc0de"
    }
  },
  "links": {
    "openapi": "/openapi.json",
    "docs": "/docs"
  }
}
```

---

### ⚠️ `200 OK` — degraded (`200.degraded.json`)

Example: core data stores are healthy, but a non-critical subsystem (search or telemetry) is impaired.

```json
{
  "service": "kfm-api",
  "api_version": "v1",
  "status": "degraded",
  "time_utc": "2026-01-24T18:12:11Z",
  "uptime_seconds": 18603,
  "build": {
    "version": "1.7.0",
    "git_sha": "bb86bf1",
    "build_time_utc": "2026-01-24T17:50:12Z"
  },
  "governance": {
    "mode": "fail_closed",
    "policy_pack_revision": "bb86bf1"
  },
  "checks": {
    "postgis": { "status": "ok", "latency_ms": 14 },
    "neo4j": { "status": "ok", "latency_ms": 21 },
    "catalogs": { "status": "ok", "stac": "ok", "dcat": "ok" },
    "prov_store": { "status": "ok" },
    "search": {
      "status": "warn",
      "engine": "elasticsearch",
      "latency_ms": 1800,
      "detail": "High latency; serving results may be slow."
    },
    "telemetry": {
      "status": "fail",
      "metrics": "unavailable",
      "detail": "Metrics exporter not responding."
    }
  },
  "graph_integrity": {
    "status": "warn",
    "last_run_utc": "2026-01-21T03:00:00Z",
    "orphaned_metadata_nodes": { "count": 3 },
    "detail": "Non-zero orphan count; investigate lineage links."
  },
  "pipeline": {
    "last_run": {
      "run_id": "run_2026-01-23T02:14:55Z_7d2b",
      "run_time_utc": "2026-01-23T02:14:55Z",
      "idempotency_key": "ingest:usgs:nwis:2026-01-23",
      "canonical_digest": "sha256:9d9f2baf2c06d7c0b0c80dd3b2c24f5f0bb62da5f0b7d9d2bd60d4f7deadc0de"
    }
  },
  "links": {
    "openapi": "/openapi.json",
    "docs": "/docs"
  }
}
```

---

### ❌ `503 Service Unavailable` — down (`503.down.json`)

Example: a required subsystem is unreachable (PostGIS or Neo4j).

```json
{
  "service": "kfm-api",
  "api_version": "v1",
  "status": "down",
  "time_utc": "2026-01-24T18:13:42Z",
  "uptime_seconds": 18694,
  "build": {
    "version": "1.7.0",
    "git_sha": "bb86bf1",
    "build_time_utc": "2026-01-24T17:50:12Z"
  },
  "governance": {
    "mode": "fail_closed",
    "policy_pack_revision": "bb86bf1"
  },
  "checks": {
    "postgis": {
      "status": "fail",
      "latency_ms": 0,
      "detail": "Connection failed."
    },
    "neo4j": {
      "status": "fail",
      "latency_ms": 0,
      "detail": "Skipped (dependency chain broken)."
    },
    "catalogs": {
      "status": "fail",
      "stac": "unknown",
      "dcat": "unknown",
      "detail": "Skipped (required stores unavailable)."
    },
    "prov_store": {
      "status": "fail",
      "detail": "Skipped (required stores unavailable)."
    }
  },
  "errors": [
    {
      "code": "DEPENDENCY_UNAVAILABLE",
      "message": "Required dependency check failed: postgis"
    }
  ],
  "links": {
    "openapi": "/openapi.json",
    "docs": "/docs"
  }
}
```

---

## 🧪 Graph integrity health (recommended sub-object)

If your deployment includes scheduled graph integrity checks, surface a compact summary here.

Suggested minimum fields:

- `last_run_utc`
- `status` (`ok|warn|fail`)
- One or more stable, count-based signals (e.g., orphan counts)
- Optional `detail` for operator context

> 🛠️ Keep this section **operator-friendly**, not “debug-dump” noisy.

---

## 🔐 Redaction rules (MUST)

To preserve security + privacy:

- ✅ OK to return **statuses**, **durations/latency**, and **non-sensitive build identifiers**
- ❌ Never return hostnames, IPs, credentials, tokens, internal connection strings, private bucket paths, or sensitive dataset names
- ❌ Avoid returning anything that makes targeted enumeration easier (e.g., full list of private indices)

---

## 🧩 Backward compatibility rules

✅ Safe changes (v1):
- Add new optional fields
- Add new optional checks under `checks`
- Add new links under `links`

⚠️ Breaking changes (require v2 folder + endpoint version bump):
- Renaming/removing existing fields
- Changing field types
- Changing enum values in a way that breaks existing clients

---

## 🛠️ Quick local test

```bash
curl -s http://localhost:8000/v1/health | jq
```

---

## 🧭 Related contract folders

- `api/contracts/examples/responses/v1/…`
- `api/contracts/examples/requests/v1/…` (if present)
- `api/contracts/schemas/v1/…` (if present)

✅ Keep responses + schemas in lockstep so tooling/tests don’t drift.
