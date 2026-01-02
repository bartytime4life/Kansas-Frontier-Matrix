# 🧰 `.github/workflows` — CI/CD for Kansas Frontier Matrix (KFM)

![CI](https://github.com/<ORG>/<REPO>/actions/workflows/ci.yml/badge.svg)
![Security](https://github.com/<ORG>/<REPO>/actions/workflows/security.yml/badge.svg)
![Docker](https://github.com/<ORG>/<REPO>/actions/workflows/docker.yml/badge.svg)

> This folder contains GitHub Actions workflows that keep KFM **buildable, testable, secure, and shippable**—from geospatial pipelines to web UI.

---

## 🌐 Why our workflows look “layered”

KFM is intentionally modular (domain logic separated from infrastructure details), so our CI mirrors that separation: we validate **core logic**, then adapters, then deployment packaging. This lines up with KFM’s stated architectural principles (layer separation, dependency direction, interface-based integration, testability, replaceability).  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

KFM also spans multiple system surfaces (data ingestion → repositories → AI/analysis → visualization UI), so CI needs multiple “lanes” to avoid coupling everything into one mega-job.  [oai_citation:1‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

---

## 🗂️ Workflow catalog (recommended baseline)

> Filenames below are the **intended** baseline. If a file isn’t present yet, treat this README as the spec for creating it.

| Workflow 📄 | What it protects ✅ | Typical triggers ⏱️ | Outputs 📦 |
|---|---|---|---|
| `ci.yml` | Fast PR checks (lint + unit tests) | `pull_request`, `push` | Test results, coverage |
| `integration.yml` | PostGIS + service integration tests | `pull_request` (optional), nightly | Logs, reports |
| `docker.yml` | Build/push images + cache | `push` to `main`, tags | OCI images to GHCR |
| `security.yml` | Dependency + container scanning | `pull_request`, nightly | SARIF, scan reports |
| `docs.yml` | Docs build/link checks | `pull_request` | Built docs artifact |
| `deploy.yml` | Promote to envs (dev/stage/prod) | tags / manual dispatch | Deployment logs |

---

## ✅ Quality gates (what must pass)

### 1) Code health 🧼
- Formatting + linting (fast fail)
- Unit tests (core logic first)
- Type checks (if applicable)

### 2) Geo + data correctness 🗺️
Geospatial work tends to fail from data mismatch and unclear requirements, so CI should enforce:
- schema validation
- reproducible pipelines
- deterministic outputs where possible (pin versions & seeds)

(As a reminder: defining requirements early pays dividends in data-heavy GIS workflows.)  [oai_citation:2‡Geographic Information System Basics - geographic-information-system-basics.pdf](file-service://file-Kjn2enYFqXQtK3J4zN2DWz)

### 3) Infra parity 🐳
Use containers to keep build/test environments consistent across dev + CI, which is a core CI/CD advantage of Dockerized workflows.  [oai_citation:3‡Introduction-to-Docker.pdf](file-service://file-5SALje8G4GDUXHUM3P3LuU)

---

## 🧪 Integration tests with PostGIS (KFM-specific)

KFM’s infra explicitly calls out PostgreSQL + PostGIS for geospatial storage.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)  
So integration tests should run against a real PostGIS container (Docker Compose is fine).

Example `docker-compose.ci.yml` snippet:

```yaml
version: "3.9"
services:
  db:
    image: postgis/postgis:15-3.4
    environment:
      POSTGRES_DB: kfm_test
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
```

And your CI can run tests via Compose (pattern commonly used in CI/CD).  [oai_citation:5‡Introduction-to-Docker.pdf](file-service://file-5SALje8G4GDUXHUM3P3LuU)

---

## 🐳 Docker builds: caching + multi-arch

### Layer caching (BuildKit/buildx)
Caching Buildx layers can dramatically speed up CI builds.  [oai_citation:6‡Introduction-to-Docker.pdf](file-service://file-5SALje8G4GDUXHUM3P3LuU)

Example (conceptual):

```yaml
- name: Cache Docker layers
  uses: actions/cache@v2
  with:
    path: /tmp/.buildx-cache
    key: ${{ runner.os }}-buildx-${{ github.sha }}
    restore-keys: |
      ${{ runner.os }}-buildx-
```

### Matrix builds/tests
Matrix strategies can validate multiple runtime versions in parallel (useful for Node services).  [oai_citation:7‡Introduction-to-Docker.pdf](file-service://file-5SALje8G4GDUXHUM3P3LuU)

---

## 🔐 Security scanning (containers + deps)

Integrate image scanning into the pipeline (example tool: Trivy).  [oai_citation:8‡Introduction-to-Docker.pdf](file-service://file-5SALje8G4GDUXHUM3P3LuU)

Also: governance & assurance matter—AI/data systems need lifecycle thinking (design → deployment → decommissioning) and data governance.  [oai_citation:9‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  
In practice: scan in PRs, enforce policy on `main`, and keep reports.

---

## 🧠 Data/AI workflows (Earth Engine, analytics, reproducibility)

KFM’s research surface includes remote sensing workflows (image collections, large catalogs, time series, etc.). CI shouldn’t try to run **all** of that on every PR—prefer:
- lightweight unit tests + static checks on PR
- scheduled “heavy” pipelines nightly/weekly

Earth Engine work often revolves around image collections as an organizing structure (and learning outcomes revolve around accessing, filtering, and visualizing those collections).  [oai_citation:10‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-CXGLTw8wpR4uKWWqjrGkyk)

---

## 📦 Artifacts & reporting

Recommended artifacts:
- ✅ `unit-test-results.xml` / `pytest.xml`
- ✅ coverage report (`coverage.xml`, HTML)
- ✅ integration logs (zipped)
- ✅ security reports (SARIF)
- ✅ built images digests (for deploy traceability)

---

## 🧭 Secrets & environments (keep it boring)

Common secrets you’ll likely need:
- `GHCR_TOKEN` (push container images)
- `DEPLOY_SSH_KEY` / `CLOUD_CREDENTIALS` (deployment)
- `POSTGRES_PASSWORD` (CI integration DB, or use ephemeral defaults)

Tip: keep “outer layer” concerns (networking, cloud provider details) in the workflow/env layer—don’t leak them into domain tests. This mirrors KFM’s stated separation where networking details stay at the edges.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🧰 Debugging workflows locally

Options:
- Run the same commands as CI (recommended)
- Use `act` to simulate GitHub Actions locally (best effort; not perfect parity)
- Use Docker Compose profiles when you want targeted service subsets (handy for front/back splits).  [oai_citation:12‡Introduction-to-Docker.pdf](file-service://file-5SALje8G4GDUXHUM3P3LuU)

---

## 🧾 Adding a new workflow (checklist)

- [ ] Name jobs after outcomes (e.g., `lint`, `unit-tests`, `integration-tests`, `build-image`)
- [ ] Keep PR checks fast (≤ ~10 minutes target)
- [ ] Put slow jobs behind schedules or manual dispatch
- [ ] Cache dependencies and Docker layers
- [ ] Upload artifacts on failure (logs are gold)
- [ ] Pin action versions (avoid surprise breakage)
- [ ] Avoid secrets on `pull_request` from forks

---

## 📚 Internal references used for this folder

- KFM architecture principles + layering rationale  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)  
- KFM infrastructure note (PostgreSQL + PostGIS)  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)  
- KFM mapping hub architecture (data→AI→UI)  [oai_citation:15‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)  
- Docker in CI/CD (compose, scanning, caching, matrices)  [oai_citation:16‡Introduction-to-Docker.pdf](file-service://file-5SALje8G4GDUXHUM3P3LuU)  [oai_citation:17‡Introduction-to-Docker.pdf](file-service://file-5SALje8G4GDUXHUM3P3LuU)  
- Governance + assurance framing (why we enforce security & lifecycle checks)  [oai_citation:18‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  

KFM master doc (link marker):  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)