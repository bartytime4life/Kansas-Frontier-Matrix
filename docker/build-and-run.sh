#!/usr/bin/env bash
# Kansas-Frontier-Matrix — Docker Helper
# -------------------------------------------------------------------
# One-shot helper to build the image and run tasks inside it.
#
# Quick start:
#   ./docker/build-and-run.sh                 # opens a shell
#   ./docker/build-and-run.sh make terrain    # runs 'make terrain'
#   ./docker/build-and-run.sh make stac stac-validate-items site
#
# With Compose service (recommended when using db/storage/web profiles):
#   ./docker/build-and-run.sh --compose shell
#   ./docker/build-and-run.sh --compose make terrain
#
# Options:
#   --compose           Use docker compose service "kfm" to build/run
#   --gpu               Request NVIDIA GPU (if available)
#   --no-cache          Build image without cache
#   --plain             Plain build logs (no fancy TTY progress)
#   --platform <p>      Target platform (e.g., linux/amd64,linux/arm64)
#   --progress <mode>   build progress=auto|plain|tty (default auto)
#   --context <path>    Build context (default repo root)
#   --dockerfile <file> Dockerfile path (default repo root/Dockerfile)
#   --image <name>      Image tag (default kfm:dev)
#   --gdal-image <ref>  Base GDAL image ARG (matches Dockerfile)
#   --envfile <file>    Load env vars from file (e.g., .env)
#   --workdir <path>    Workdir inside container (default /workspace)
#   --                 Everything after -- is executed as a raw command
#
# Examples:
#   ./docker/build-and-run.sh --gpu -- make nlcd
#   ./docker/build-and-run.sh -- platform linux/arm64 -- make site
#   ./docker/build-and-run.sh -- bash -lc 'python -V && make preview'
#
# Notes:
# - Passes through common KFM/DB/S3 env vars if present.
# - Uses buildx local cache at ./.cache/buildx when available (faster CI/dev).
# - Creates pip/npm caches under ./.cache/{pip,npm} (speedy installs).
# - On macOS/WSL, UID/GID fallback keeps file ownership sane.

set -euo pipefail
IFS=$'\n\t'

# ------------- utilities ------------------------------------------------------
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/.." && pwd)"

die() { echo "ERROR: $*" >&2; exit 1; }
info() { echo ">> $*"; }
have() { command -v "$1" >/dev/null 2>&1; }

# ------------- defaults -------------------------------------------------------
IMG="${IMG:-kfm:dev}"
CTX="${CTX:-${repo_root}}"
DOCKERFILE="${DOCKERFILE:-${repo_root}/Dockerfile}"
GDAL_IMAGE_ARG_DEFAULT="ghcr.io/osgeo/gdal:ubuntu-small-latest"
GDAL_IMAGE_ARG="${GDAL_IMAGE_ARG:-${GDAL_IMAGE_ARG_DEFAULT}}"
WORKDIR="${WORKDIR:-/workspace}"
USE_COMPOSE="0"
USE_GPU="0"
NO_CACHE="0"
PROGRESS="${PROGRESS:-auto}"
PLATFORM="${PLATFORM:-}"
ENVFILE="${ENVFILE:-}"
PLAIN="0"

# ------------- arg parsing ----------------------------------------------------
RAW_CMD=()
RUN_MODE="shell"   # "shell" | "make" | "raw"

while (( "$#" )); do
  case "$1" in
    --compose)        USE_COMPOSE="1"; shift ;;
    --gpu)            USE_GPU="1"; shift ;;
    --no-cache)       NO_CACHE="1"; shift ;;
    --plain)          PLAIN="1"; PROGRESS="plain"; shift ;;
    --progress)       PROGRESS="${2:-}"; shift 2 ;;
    --platform)       PLATFORM="${2:-}"; shift 2 ;;
    --context)        CTX="$(cd "${2:-}" && pwd)"; shift 2 ;;
    --dockerfile)     DOCKERFILE="${2:-}"; shift 2 ;;
    --image)          IMG="${2:-}"; shift 2 ;;
    --gdal-image)     GDAL_IMAGE_ARG="${2:-}"; shift 2 ;;
    --envfile)        ENVFILE="${2:-}"; shift 2 ;;
    --workdir)        WORKDIR="${2:-}"; shift 2 ;;
    make)             RUN_MODE="make"; shift; RAW_CMD+=("$@"); break ;;
    shell)            RUN_MODE="shell"; shift; break ;;
    --)               shift; RUN_MODE="raw"; RAW_CMD+=("$@"); break ;;
    *)                # If first free arg is 'make', catch above; otherwise treat as make
                      RUN_MODE="make"; RAW_CMD+=("$@"); break ;;
  esac
done

# ------------- sanity checks --------------------------------------------------
have docker || die "Docker is required."
if [[ "${USE_COMPOSE}" == "1" ]]; then
  have docker || die "Docker is required."
  have docker || die "Docker is required." # (double-check intentional; keep error clear)
  have docker && docker compose version >/dev/null 2>&1 || die "Docker Compose V2 is required."
fi

# OSX/WSL friendly UID/GID (fallback if unknown)
HOST_UID="$(id -u || echo 1000)"
HOST_GID="$(id -g || echo 1000)"

# ------------- env handling ---------------------------------------------------
if [[ -n "${ENVFILE}" ]]; then
  [[ -f "${ENVFILE}" ]] || die "Env file not found: ${ENVFILE}"
  set -o allexport
  # shellcheck disable=SC1090
  source "${ENVFILE}"
  set +o allexport
fi

# Common env passthroughs (only if set in the shell/.env)
passthrough_env=()
for v in \
  KFM_ENV KFM_DATA_ROOT KFM_STAC_ROOT \
  KSRIV_CHANNELS KSRIV_FLOODPLAIN KSRIV_GAUGES \
  PGHOST PGPORT PGDATABASE PGUSER PGPASSWORD \
  S3_ENDPOINT_URL AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_DEFAULT_REGION \
  NODE_OPTIONS PIP_CACHE_DIR PYTHONDONTWRITEBYTECODE PIP_DISABLE_PIP_VERSION_CHECK
do
  if [[ -n "${!v-}" ]]; then
    passthrough_env+=("-e" "${v}=${!v}")
  fi
done

# ------------- build (docker or compose) --------------------------------------
use_buildx="0"
if have docker && docker buildx version >/dev/null 2>&1; then
  use_buildx="1"
fi

BUILD_DATE="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
VCS_REF="$(git -C "${repo_root}" rev-parse --short HEAD 2>/dev/null || echo 'unknown')"

build_args=( "--build-arg" "GDAL_IMAGE=${GDAL_IMAGE_ARG}"
             "--build-arg" "BUILD_DATE=${BUILD_DATE}"
             "--build-arg" "VCS_REF=${VCS_REF}" )

if [[ "${USE_COMPOSE}" == "1" ]]; then
  info "Building via docker compose (service: kfm)"
  # Compose file lives under docker/compose.yml
  compose_file="${repo_root}/docker/compose.yml"
  [[ -f "${compose_file}" ]] || die "Missing compose file: ${compose_file}"

  # Let compose handle build args through environment expansion
  DOCKER_BUILDKIT=1 docker compose -f "${compose_file}" build \
    ${NO_CACHE:+--no-cache} \
    --build-arg "GDAL_IMAGE=${GDAL_IMAGE_ARG}"
else
  info "Building image: ${IMG}"
  if [[ "${use_buildx}" == "1" ]]; then
    cache_dir="${repo_root}/.cache/buildx"
    mkdir -p "${cache_dir}"
    DOCKER_BUILDKIT=1 docker buildx build \
      --load \
      --tag "${IMG}" \
      --file "${DOCKERFILE}" \
      --progress="${PROGRESS}" \
      ${NO_CACHE:+--no-cache} \
      ${PLATFORM:+--platform "${PLATFORM}"} \
      --cache-from "type=local,src=${cache_dir}" \
      --cache-to   "type=local,dest=${cache_dir},mode=max" \
      "${build_args[@]}" \
      "${CTX}"
  else
    DOCKER_BUILDKIT=1 docker build \
      --tag "${IMG}" \
      --file "${DOCKERFILE}" \
      ${NO_CACHE:+--no-cache} \
      "${build_args[@]}" \
      "${CTX}"
  fi
fi

# ------------- run helpers ----------------------------------------------------
# Volume caches to speed up Python/Node deps
mkdir -p "${repo_root}/.cache/pip" "${repo_root}/.cache/npm"

docker_run_common=(
  -u "${HOST_UID}:${HOST_GID}"
  -v "${repo_root}:${WORKDIR}"
  -v "${repo_root}/.cache/pip:/home/dev/.cache/pip"
  -v "${repo_root}/.cache/npm:/home/dev/.npm"
  -w "${WORKDIR}"
)

# GPU support
if [[ "${USE_GPU}" == "1" ]]; then
  if docker info 2>/dev/null | grep -qi nvidia; then
    docker_run_common+=( --gpus all )
  else
    info "GPU flag set, but NVIDIA runtime not detected; continuing CPU-only."
  fi
fi

# TTY detection
if [ -t 1 ]; then
  docker_run_common+=( -it )
fi

# ------------- execute (compose or plain docker) ------------------------------
if [[ "${USE_COMPOSE}" == "1" ]]; then
  compose_file="${repo_root}/docker/compose.yml"
  # Compose already built the "kfm" service; we can run/exec it
  case "${RUN_MODE}" in
    shell)
      info "Starting interactive shell via compose (kfm)"
      exec docker compose -f "${compose_file}" run --rm \
        "${passthrough_env[@]}" \
        kfm bash
      ;;
    make)
      : "${RAW_CMD:?No make target provided}"
      info "Running make via compose (kfm): ${RAW_CMD[*]}"
      exec docker compose -f "${compose_file}" run --rm \
        "${passthrough_env[@]}" \
        kfm bash -lc "make ${RAW_CMD[*]}"
      ;;
    raw)
      : "${RAW_CMD:?No command provided after --}"
      info "Running raw command via compose (kfm): ${RAW_CMD[*]}"
      exec docker compose -f "${compose_file}" run --rm \
        "${passthrough_env[@]}" \
        kfm bash -lc "${RAW_CMD[*]}"
      ;;
  esac
else
  case "${RUN_MODE}" in
    shell)
      info "Opening interactive shell in ${IMG}"
      exec docker run --rm \
        "${docker_run_common[@]}" \
        "${passthrough_env[@]}" \
        "${IMG}" bash
      ;;
    make)
      : "${RAW_CMD:?No make target provided}"
      info "Running make in ${IMG}: ${RAW_CMD[*]}"
      exec docker run --rm \
        "${docker_run_common[@]}" \
        "${passthrough_env[@]}" \
        "${IMG}" bash -lc "make ${RAW_CMD[*]}"
      ;;
    raw)
      : "${RAW_CMD:?No command provided after --}"
      info "Running raw command in ${IMG}: ${RAW_CMD[*]}"
      exec docker run --rm \
        "${docker_run_common[@]}" \
        "${passthrough_env[@]}" \
        "${IMG}" bash -lc "${RAW_CMD[*]}"
      ;;
  esac
fi
