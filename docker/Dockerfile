# ============================================
# Kansas-Frontier-Matrix / MCP — Dockerfile
# Debugged & Upgraded: GDAL + Python wheels
# ============================================

# ---- Base: GDAL with glibc (Ubuntu) -------------------------
# Alpine (musl) often breaks manylinux wheels for rasterio/pyproj.
# Use the Ubuntu-based image for reliable binary wheels.
ARG GDAL_IMAGE=ghcr.io/osgeo/gdal:ubuntu-small-latest
FROM ${GDAL_IMAGE} AS runtime

# Minimal OS deps (most wheels will "just work")
# - curl/ca-certificates: HTTPS fetch; make: for Makefile targets
# - python3-pip: pip; python-is-python3 for a 'python' shim
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      python3-pip python-is-python3 \
      curl ca-certificates \
      make git bash && \
    rm -rf /var/lib/apt/lists/*

# Python/pip sanity (fast & clean installs)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_ROOT_USER_ACTION=ignore

# GDAL/proj env hints (many libs look at these)
ENV GDAL_DISABLE_READDIR_ON_OPEN=YES \
    VSI_CACHE=TRUE \
    VSI_CACHE_SIZE=1000000 \
    CPL_TMPDIR=/tmp \
    PROJ_NETWORK=ON

WORKDIR /app

# ---- Dependency install (cached) ----------------------------
# Copy dependency manifests first to leverage Docker layer caching
COPY requirements.txt /tmp/requirements.txt
# If you maintain constraints for CI/reproducibility, copy them too
# (it’s okay if this file doesn’t exist—command below handles both)
COPY constraints.txt /tmp/constraints.txt

# Upgrade pip & install deps
# Prefer binary wheels to avoid source builds (especially on CI)
RUN python -m pip install --upgrade pip wheel && \
    if [ -s /tmp/constraints.txt ]; then \
      python -m pip install --no-cache-dir --prefer-binary \
        -r /tmp/requirements.txt --constraint /tmp/constraints.txt ; \
    else \
      python -m pip install --no-cache-dir --prefer-binary \
        -r /tmp/requirements.txt ; \
    fi

# ---- App code (late copy = faster rebuilds) -----------------
# Copy the rest of the repo after deps to keep docker layer cache hot
# If you use a src/ layout, this keeps editable code separate from deps
COPY . /app

# Optional: non-root user for safer runtime
RUN useradd -m -u 10001 appuser && chown -R appuser:appuser /app
USER appuser

# Expose a default working directory
WORKDIR /app

# Health check (optional): verify GDAL works
# (will just log a message in most local runs; useful in k8s/compose)
HEALTHCHECK --interval=60s --timeout=3s --retries=3 CMD gdalinfo --version || exit 1

# Default command: bash (override in docker-compose or CI)
CMD ["/bin/bash"]
