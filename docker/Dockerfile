# =============================================
# Kansas-Frontier-Matrix — Dockerfile (dev+CI)
# Base: GDAL (Ubuntu) + Python wheels-first + Node + tiles tooling
# ---------------------------------------------
# Build args (override in CI or via build-and-run.sh):
#   GDAL_IMAGE=ghcr.io/osgeo/gdal:ubuntu-small-latest
#   BUILD_NATIVE=0|1          # allow source builds for Python deps
#   ENABLE_NODE=1|0           # install Node.js + corepack (for web)
#   ENABLE_TILES=1|0          # install tippecanoe + pmtiles CLIs
#   ENABLE_AWSCLI=1|0         # install awscli (S3, MinIO, STAC pushes)
#   USER_ID / GROUP_ID        # map to host (safe defaults below)
#   VCS_REF / BUILD_DATE      # injected by CI or helper script
# =============================================

ARG GDAL_IMAGE=ghcr.io/osgeo/gdal:ubuntu-small-latest
FROM ${GDAL_IMAGE} AS base

# ---- Meta / labels ----------------------------------------------------------
ARG VCS_REF=unknown
ARG BUILD_DATE=unknown
LABEL org.opencontainers.image.title="Kansas-Frontier-Matrix" \
      org.opencontainers.image.description="GDAL + Python wheels-first env for STAC/COG/PMTiles pipelines and web build" \
      org.opencontainers.image.source="https://github.com/bartytime4life/Kansas-Frontier-Matrix" \
      org.opencontainers.image.revision="${VCS_REF}" \
      org.opencontainers.image.created="${BUILD_DATE}"

# ---- Defaults / feature flags ----------------------------------------------
ARG BUILD_NATIVE=0
ARG ENABLE_NODE=1
ARG ENABLE_TILES=1
ARG ENABLE_AWSCLI=1

# ---- OS base deps (lean) ----------------------------------------------------
# Notes:
# - git-lfs helps with large rasters (COGs) under LFS.
# - node via distro is fine for dev; use ENABLE_NODE=0 to skip.
# - keep image slim; no recommends.
RUN set -eux; \
    apt-get update; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      python3-pip python-is-python3 \
      ca-certificates curl wget unzip xz-utils \
      make git git-lfs bash tini \
      gdal-bin proj-bin \
      pkg-config \
      # Node (optional; disable with ENABLE_NODE=0)
      ${ENABLE_NODE:+nodejs npm}; \
    git lfs install --system; \
    rm -rf /var/lib/apt/lists/*

# ---- Python / pip hygiene ---------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_ROOT_USER_ACTION=ignore

# ---- GDAL/PROJ runtime hints -----------------------------------------------
ENV GDAL_DISABLE_READDIR_ON_OPEN=YES \
    VSI_CACHE=TRUE \
    VSI_CACHE_SIZE=1000000 \
    CPL_TMPDIR=/tmp \
    PROJ_NETWORK=ON \
    GDAL_DATA=/usr/share/gdal \
    PROJ_DATA=/usr/share/proj

# ---- Optional native toolchain for source builds ---------------------------
# Only used if BUILD_NATIVE=1 (e.g., missing wheels on your arch).
RUN if [ "${BUILD_NATIVE}" = "1" ]; then \
      set -eux; \
      apt-get update; \
      DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential \
        libgdal-dev libproj-dev; \
      rm -rf /var/lib/apt/lists/*; \
    fi

# ---- Tile tooling (optional) -----------------------------------------------
# tippecanoe: static release tarball
# pmtiles: single static binary
ARG TIPPECANOE_VER=1.36.0
ARG PMTILES_VER=3.11.0
RUN if [ "${ENABLE_TILES}" = "1" ]; then \
      set -eux; \
      arch="$(uname -m)"; \
      # tippecanoe
      case "${arch}" in \
        x86_64) tarch="linux-x86_64";; \
        aarch64) tarch="linux-arm64";; \
        arm64) tarch="linux-arm64";; \
        *) echo "Unsupported arch for tippecanoe: ${arch}"; exit 1;; \
      esac; \
      curl -fsSL -o /tmp/tippecanoe.tar.gz \
        "https://github.com/mapbox/tippecanoe/releases/download/${TIPPECANOE_VER}/tippecanoe-${TIPPECANOE_VER}-${tarch}.tar.gz"; \
      mkdir -p /opt/tippecanoe && tar -xzf /tmp/tippecanoe.tar.gz -C /opt/tippecanoe --strip-components=1; \
      ln -s /opt/tippecanoe/tippecanoe /usr/local/bin/tippecanoe; \
      ln -s /opt/tippecanoe/tile-join /usr/local/bin/tile-join; \
      # pmtiles
      case "${arch}" in \
        x86_64) parch="x86_64";; \
        aarch64|arm64) parch="aarch64";; \
      esac; \
      curl -fsSL -o /usr/local/bin/pmtiles \
        "https://github.com/protomaps/PMTiles/releases/download/v${PMTILES_VER}/pmtiles-${PMTILES_VER}-linux-${parch}"; \
      chmod +x /usr/local/bin/pmtiles; \
    fi

# ---- AWS / S3 tooling (optional) -------------------------------------------
RUN if [ "${ENABLE_AWSCLI}" = "1" ]; then \
      python -m pip install --upgrade pip wheel && \
      python -m pip install --no-cache-dir awscli && \
      aws --version || true; \
    fi

# ---- Working directories ----------------------------------------------------
# /opt/app     → baked snapshot (for CI or non-mounted use)
# /workspace   → bind mount target in dev (compose/run scripts use this)
WORKDIR /opt/app

# ---- Dependency layer (cache-friendly) -------------------------------------
# Only copy manifests first to maximize caching across source changes.
COPY requirements.txt /tmp/requirements.txt
COPY constraints.txt  /tmp/constraints.txt
RUN set -eux; \
    python -m pip install --upgrade pip wheel; \
    if [ -s /tmp/constraints.txt ]; then \
      python -m pip install --only-binary=:all: --prefer-binary \
        -r /tmp/requirements.txt --constraint /tmp/constraints.txt \
      || { echo "Wheels missing; retry with source (BUILD_NATIVE=1 required)"; \
           [ "${BUILD_NATIVE}" = "1" ] && python -m pip install -r /tmp/requirements.txt --constraint /tmp/constraints.txt; }; \
    else \
      python -m pip install --only-binary=:all: --prefer-binary \
        -r /tmp/requirements.txt \
      || { echo "Wheels missing; retry with source (BUILD_NATIVE=1 required)"; \
           [ "${BUILD_NATIVE}" = "1" ] && python -m pip install -r /tmp/requirements.txt; }; \
    fi

# ---- App snapshot (optional baseline) --------------------------------------
# This lets the image run even without a bind mount (e.g., CI smoke tests).
COPY . /opt/app
RUN python -m pip install -e /opt/app || true

# ---- Non-root user ----------------------------------------------------------
ARG USER_ID=10001
ARG GROUP_ID=10001
RUN groupadd -g "${GROUP_ID}" appgroup && \
    useradd -m -u "${USER_ID}" -g appgroup -s /bin/bash appuser && \
    mkdir -p /workspace /home/appuser/.cache/pip /home/appuser/.npm && \
    chown -R appuser:appgroup /opt/app /workspace /home/appuser
USER appuser
WORKDIR /workspace

# ---- Node niceties (when enabled) ------------------------------------------
# Corepack makes yarn/pnpm available if project uses them.
RUN if [ "${ENABLE_NODE}" = "1" ]; then \
      npm --version >/dev/null 2>&1 && npx --yes corepack enable || true; \
    fi

# ---- Healthcheck (fast & meaningful) ---------------------------------------
# Verifies GDAL + core Python libs; also check pmtiles when enabled.
HEALTHCHECK --interval=60s --timeout=5s --retries=3 \
  CMD bash -lc '\
    gdalinfo --version >/dev/null 2>&1 || exit 1; \
    python - <<PY >/dev/null 2>&1 || exit 1 \
import importlib, sys; \
for m in ("rasterio","fiona"): \
  importlib.import_module(m) \
PY \
    ; \
    if [ "${ENABLE_TILES}" = "1" ]; then pmtiles --help >/dev/null 2>&1 || exit 1; fi; \
    exit 0'

# ---- Entrypoint -------------------------------------------------------------
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/bin/bash"]
