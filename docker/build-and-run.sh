#!/usr/bin/env bash
# One-shot helper: build the image and run a Make target inside it.
# Usage:
#   ./docker/build-and-run.sh            # opens a shell
#   ./docker/build-and-run.sh terrain    # runs 'make terrain'
#   ./docker/build-and-run.sh stac stac-validate-items site

set -euo pipefail

IMG="${IMG:-kfm:dev}"
CTX="${CTX:-.}"
DOCKERFILE="${DOCKERFILE:-Dockerfile}"
GDAL_IMAGE_ARG="${GDAL_IMAGE_ARG:-ghcr.io/osgeo/gdal:ubuntu-small-latest}"

echo ">> Building image: ${IMG}"
docker build \
  --build-arg "GDAL_IMAGE=${GDAL_IMAGE_ARG}" \
  -t "${IMG}" \
  -f "${DOCKERFILE}" \
  "${CTX}"

if [ "$#" -eq 0 ]; then
  echo ">> No target provided; starting interactive shell"
  exec docker run --rm -it \
    -u "$(id -u):$(id -g)" \
    -v "$PWD":/workspace -w /workspace \
    "${IMG}" bash
else
  echo ">> Running make $*"
  exec docker run --rm \
    -u "$(id -u):$(id -g)" \
    -v "$PWD":/workspace -w /workspace \
    "${IMG}" bash -lc "make $*"
fi
