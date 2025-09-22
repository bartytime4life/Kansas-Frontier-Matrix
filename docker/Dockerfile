# ============================================
# Kansas-Frontier-Matrix / MCP — Dockerfile
# GDAL base (Ubuntu) + Python tooling (wheels-first)
# --------------------------------------------
# Build args (override from CI if needed):
#   GDAL_IMAGE=ghcr.io/osgeo/gdal:ubuntu-small-latest
#   USER_ID / GROUP_ID  -> match host UID/GID (optional)
#   BUILD_NATIVE=0|1    -> install native build deps (only if you must compile)
# ============================================

ARG GDAL_IMAGE=ghcr.io/osgeo/gdal:ubuntu-small-latest
FROM ${GDAL_IMAGE} AS base

# ---- Labels ---------------------------------------------------------------
LABEL org.opencontainers.image.title="Kansas-Frontier-Matrix" \
      org.opencontainers.image.description="GDAL + Python wheels-first env for STAC/COG pipelines" \
      org.opencontainers.image.source="https://github.com/bartytime4life/Kansas-Frontier-Matrix"

# ---- OS deps (lean) -------------------------------------------------------
# Keep super minimal; add BUILD_NATIVE block below only on demand.
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      python3-pip python-is-python3 \
      ca-certificates curl \
      make git bash tini && \
    rm -rf /var/lib/apt/lists/*

# ---- Python/pip hygiene ---------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_ROOT_USER_ACTION=ignore

# ---- GDAL/PROJ runtime hints ---------------------------------------------
# These avoid excessive directory listings over VSI and enable remote grids.
ENV GDAL_DISABLE_READDIR_ON_OPEN=YES \
    VSI_CACHE=TRUE \
    VSI_CACHE_SIZE=1000000 \
    CPL_TMPDIR=/tmp \
    PROJ_NETWORK=ON

# Try to set GDAL/PROJ data paths (image-dependent but safe defaults)
ENV GDAL_DATA=/usr/share/gdal \
    PROJ_DATA=/usr/share/proj

WORKDIR /app

# ---- Optional native toolchain (off by default) --------------------------
# Enable only when you *must* compile wheels (no manylinux available).
# E.g., docker build --build-arg BUILD_NATIVE=1 .
ARG BUILD_NATIVE=0
RUN if [ "$BUILD_NATIVE" = "1" ]; then \
      set -eux; \
      apt-get update; \
      DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential pkg-config \
        libgdal-dev gdal-bin \
        libproj-dev; \
      rm -rf /var/lib/apt/lists/*; \
    fi

# ---- Dependency layer (cache-friendly) -----------------------------------
# Copy only manifests first to leverage Docker layer caching.
COPY requirements.txt /tmp/requirements.txt
# Optional pin file (if present). Build does not fail if absent/empty.
COPY constraints.txt /tmp/constraints.txt

RUN python -m pip install --upgrade pip wheel && \
    if [ -s /tmp/constraints.txt ]; then \
      # Wheels-first; failover to source only when native toolchain enabled.
      python -m pip install --only-binary=:all: --prefer-binary \
        -r /tmp/requirements.txt --constraint /tmp/constraints.txt \
        || { echo "Wheels missing; retry with source builds (requires BUILD_NATIVE=1)"; \
             [ "$BUILD_NATIVE" = "1" ] && python -m pip install -r /tmp/requirements.txt --constraint /tmp/constraints.txt; }; \
    else \
      python -m pip install --only-binary=:all: --prefer-binary \
        -r /tmp/requirements.txt \
        || { echo "Wheels missing; retry with source builds (requires BUILD_NATIVE=1)"; \
             [ "$BUILD_NATIVE" = "1" ] && python -m pip install -r /tmp/requirements.txt; }; \
    fi

# ---- App layer ------------------------------------------------------------
# Copy after deps to keep cache stable for frequent code changes.
COPY . /app

# Install project in editable mode to expose CLI (e.g., `kgt`) without
# re-resolving third-party deps.
RUN python -m pip install -e . || true

# ---- Non-root user (optional UID/GID mapping) -----------------------------
ARG USER_ID=10001
ARG GROUP_ID=10001
RUN groupadd -g "${GROUP_ID}" appgroup && \
    useradd -m -u "${USER_ID}" -g appgroup appuser && \
    chown -R appuser:appgroup /app
USER appuser

# ---- Healthcheck (fast & meaningful) -------------------------------------
# gdalinfo verifies GDAL wiring; a tiny Python probe verifies wheels load.
HEALTHCHECK --interval=60s --timeout=5s --retries=3 \
  CMD sh -lc 'gdalinfo --version >/dev/null 2>&1 && python - <<PY >/dev/null 2>&1 || exit 1
import importlib, sys
for m in ("rasterio", "fiona"):
    try: importlib.import_module(m)
    except Exception as e: sys.exit(1)
print("ok")
PY'

# ---- Runtime niceties -----------------------------------------------------
# Tini handles proper signal forwarding if you later add long-running cmds.
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/bin/bash"]