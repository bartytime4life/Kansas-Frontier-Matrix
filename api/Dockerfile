# 🐳 `api/Dockerfile` (KFM API)

According to a document from **2026-01-02**, KFM’s **Main REST API Service** is a **Python-based web service** using frameworks like **FastAPI** (chosen for OpenAPI docs + async support), and the system is designed to be **containerized with Docker** (Dockerfiles for backend + microservices). [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

This Dockerfile follows the same document’s approach of using Python **virtual environments** and pinned dependencies in **`requirements.txt`** for reproducible builds. [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 📁 Target Path

```text
📦 repo/
└── 🧠 api/
    └── 🐳 Dockerfile
```

---

## 🐳 `api/Dockerfile`

```dockerfile
# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11

############################
# Builder: install deps into a venv
############################
FROM python:${PYTHON_VERSION}-slim-bookworm AS builder

ARG INSTALL_GEOSPATIAL_DEPS=true

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    VIRTUAL_ENV=/opt/venv

WORKDIR /app

# System deps:
# - build-essential/gcc: for packages with native extensions
# - libpq-dev: for PostgreSQL drivers (psycopg/psycopg2) if used
# - optional geospatial libs (GDAL/PROJ/GEOS) for GIS workflows
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
      gcc \
      libpq-dev \
    && if [ "${INSTALL_GEOSPATIAL_DEPS}" = "true" ]; then \
         apt-get install -y --no-install-recommends \
           gdal-bin \
           libgdal-dev \
           libgeos-dev \
           proj-bin \
           libproj-dev \
       ; fi \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv "${VIRTUAL_ENV}"
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

# Install python dependencies first (best cache behavior)
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt \
    # Ensure the default CMD works even if these aren't pinned yet
    && pip install --no-cache-dir "uvicorn[standard]" "gunicorn"

# Copy the rest of the API source
COPY . .

############################
# Runtime: smaller image + non-root
############################
FROM python:${PYTHON_VERSION}-slim-bookworm AS runtime

ARG INSTALL_GEOSPATIAL_DEPS=true

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH" \
    # Override these in compose/k8s as needed
    APP_MODULE="main:app" \
    PORT="8000" \
    WEB_CONCURRENCY="2" \
    HEALTHCHECK_PATH="/health"

WORKDIR /app

# Runtime OS deps (no compilers)
RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates \
      curl \
      tini \
      libpq5 \
    && if [ "${INSTALL_GEOSPATIAL_DEPS}" = "true" ]; then \
         apt-get install -y --no-install-recommends \
           gdal-bin \
           libgdal-dev \
           libgeos-dev \
           proj-bin \
           libproj-dev \
       ; fi \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd --create-home --shell /usr/sbin/nologin --uid 10001 appuser

# Bring in venv from builder (contains all Python deps)
COPY --from=builder /opt/venv /opt/venv

# Copy app code (owned by non-root)
COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 8000

# Healthcheck expects the API to expose HEALTHCHECK_PATH (default: /health)
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -fsS "http://localhost:${PORT}${HEALTHCHECK_PATH}" || exit 1

# Proper signal handling (K8s/Docker stop)
ENTRYPOINT ["/usr/bin/tini","--"]

# Default: production-ish gunicorn + uvicorn worker (override for dev/reload)
CMD ["sh","-c","gunicorn -k uvicorn.workers.UvicornWorker -w ${WEB_CONCURRENCY} -b 0.0.0.0:${PORT} ${APP_MODULE}"]
```

---

## 🔧 Runtime knobs (quick reference)

| Env Var | Default | What it controls |
|---|---:|---|
| `APP_MODULE` | `main:app` | Import path to your ASGI app (FastAPI) |
| `PORT` | `8000` | Container listen port |
| `WEB_CONCURRENCY` | `2` | Worker processes (gunicorn) |
| `HEALTHCHECK_PATH` | `/health` | HTTP path used by Docker HEALTHCHECK |
| `INSTALL_GEOSPATIAL_DEPS` | `true` (build arg) | Toggles GDAL/PROJ/GEOS OS packages |

✅ Example builds (assuming build context is `./api`):
```bash
docker build -t kfm-api:local ./api
docker run --rm -p 8000:8000 kfm-api:local
```