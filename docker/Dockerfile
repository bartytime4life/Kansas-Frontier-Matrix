# ============================================
# Kansas-Frontier-Matrix / MCP — Dockerfile
# GDAL base (Ubuntu) + Python tooling (wheels-first)
# --------------------------------------------
# Build args you can override from CI:
#   GDAL_IMAGE=ghcr.io/osgeo/gdal:ubuntu-small-latest
#   USER_ID / GROUP_ID to match host UID/GID (optional)
# ============================================

ARG GDAL_IMAGE=ghcr.io/osgeo/gdal:ubuntu-small-latest
FROM ${GDAL_IMAGE} AS runtime

# ---- OS deps (lean) ----------------------------------------------------------
# - python3-pip + python-is-python3: pip + 'python' shim
# - curl/ca-certificates: HTTPS fetch
# - make/git/bash: make targets & repo ops
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      python3-pip python-is-python3 \
      curl ca-certificates \
      make git bash && \
    rm -rf /var/lib/apt/lists/*

# ---- Python/pip hygiene ------------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_ROOT_USER_ACTION=ignore

# ---- GDAL/PROJ runtime hints (safe defaults) --------------------------------
ENV GDAL_DISABLE_READDIR_ON_OPEN=YES \
    VSI_CACHE=TRUE \
    VSI_CACHE_SIZE=1000000 \
    CPL_TMPDIR=/tmp \
    PROJ_NETWORK=ON

WORKDIR /app

# ---- Dependency layer (cache-friendly) --------------------------------------
# Copy manifests first to leverage Docker layer caching
COPY requirements.txt /tmp/requirements.txt
# Optional constraints; if missing/empty we ignore gracefully
COPY constraints.txt /tmp/constraints.txt

RUN python -m pip install --upgrade pip wheel && \
    if [ -s /tmp/constraints.txt ]; then \
      python -m pip install --prefer-binary -r /tmp/requirements.txt --constraint /tmp/constraints.txt ; \
    else \
      python -m pip install --prefer-binary -r /tmp/requirements.txt ; \
    fi

# ---- App layer ---------------------------------------------------------------
# Copy the repo after deps to keep the cache hot for frequent code changes
COPY . /app

# If this is a Python package, make CLI (kgt) available without reinstalling deps.
# Fails safely if pyproject.toml/setup.cfg isn't present.
RUN python -m pip install -e . || true

# ---- Non-root user (optional UID/GID mapping) --------------------------------
ARG USER_ID=10001
ARG GROUP_ID=10001
RUN groupadd -g "${GROUP_ID}" appgroup && \
    useradd -m -u "${USER_ID}" -g appgroup appuser && \
    chown -R appuser:appgroup /app
USER appuser

# ---- Healthcheck (verifies GDAL is wired) -----------------------------------
HEALTHCHECK --interval=60s --timeout=3s --retries=3 CMD gdalinfo --version || exit 1

# ---- Default shell -----------------------------------------------------------
CMD ["/bin/bash"]
