# Docker — Kansas Frontier Matrix / Kansas Geo Timeline

Mission-grade, repeatable containers for building terrain COGs, validating STAC, and previewing the web viewer — without polluting your host.

> Base image: `ghcr.io/osgeo/gdal:ubuntu-small-latest` (see `Dockerfile`)

---

## Quickstart (one-liners)

```bash
# Build local image (tag chosen for clarity)
docker build -t kfm:dev .

# Drop into an interactive shell with the repo mounted read-write
docker run --rm -it \
  -v "$PWD":/workspace \
  -w /workspace \
  kfm:dev bash

Inside the container:

# Optional: install dev deps for tests/lint
make install-dev

# Build terrain derivatives (hillshade/slope/aspect) and mirror to data/derivatives
make terrain

# Create/patch STAC + validate + write simple site manifest
make stac stac-validate site

# Items-only fast validation pass
make stac-validate-items

# Clean generated rasters (keeps ./stac)
make clean


⸻

Why containers for this project?
	•	GDAL stability: Pin a known-good GDAL across Linux/macOS/WSL.
	•	Reproducible builds: Same Makefile + Python toolchain for CI and local.
	•	Zero host deps: Avoid installing GDAL, Proj, or Python libs on your workstation.

⸻

Host ↔ Container volume layout

The image is stateless. Everything lands in your mounted repo:

/workspace
├── data/               # raw/ cogs/ derivatives/ processed/
├── stac/               # items/ collections/
├── scripts/            # helper CLIs (make_*; validate_*; etc.)
├── web/                # layers.json; app assets
└── Makefile

Mount with:

docker run --rm -it \
  -v "$PWD":/workspace \
  -w /workspace \
  kfm:dev bash

Tip: Add -u $(id -u):$(id -g) on Linux to avoid root-owned files (see “UID/GID & permissions”).

⸻

Common run patterns

1) Fire-and-forget target

Run a single Make target without an interactive shell:

docker run --rm \
  -v "$PWD":/workspace -w /workspace \
  kfm:dev make terrain

Chain targets:

docker run --rm \
  -v "$PWD":/workspace -w /workspace \
  kfm:dev bash -lc "make stac && make stac-validate && make site"

2) Override DEM path

docker run --rm \
  -v "$PWD":/workspace -w /workspace \
  kfm:dev make terrain DEM=data/cogs/dem/ks_1m_dem_2018_2020.tif

3) Hydrology export (optional)

Provide layer URLs at runtime:

docker run --rm \
  -v "$PWD":/workspace -w /workspace \
  -e KSRIV_CHANNELS="https://.../FeatureServer/0" \
  -e KSRIV_FLOODPLAIN="https://.../FeatureServer/1" \
  -e KSRIV_GAUGES="https://.../FeatureServer/2" \
  kfm:dev make hydrology-fetch hydrology-stac


⸻

Image build options

The Dockerfile supports a GDAL base override:

docker build \
  --build-arg GDAL_IMAGE=ghcr.io/osgeo/gdal:ubuntu-small-3.9.0 \
  -t kfm:dev .

Recommended labels/tags:

docker build -t ghcr.io/<you>/kfm:dev -t kfm:dev .


⸻

Makefile integration inside the container

Your Make targets are designed to auto-detect:
	•	GDAL tools: gdaldem, gdal_translate, gdaladdo, ogr2ogr
	•	Python helpers: scripts/make_cog.py, scripts/make_hillshade.py, etc.
	•	Validators:
	•	scripts/validate_stac.py if present
	•	fallback to kgt validate-stac if kgt is installed
	•	Checksums: sha256sum/gsha256sum/shasum auto-detected

Helpful targets:
	•	make env — prints detected tools + paths
	•	make prebuild — stac-validate + site (CI-friendly)
	•	make stac-validate-items — fast pass over ./stac/items only
	•	make clean — removes generated rasters but keeps ./stac

⸻

GPU & heavy processing

This stack is CPU-oriented. If you add CUDA/GPU GDAL workflows later:
	•	Use --gpus all and a CUDA-enabled base.
	•	Keep current Makefile logic; only the image changes.

⸻

Docker Compose (optional convenience)

Create docker/compose.yml:

services:
  kfm:
    build:
      context: ..
      dockerfile: Dockerfile
    image: kfm:dev
    working_dir: /workspace
    volumes:
      - ../:/workspace
    tty: true

Then:

# Interactive shell
docker compose -f docker/compose.yml run --rm kfm bash

# One-shot target
docker compose -f docker/compose.yml run --rm kfm make terrain


⸻

UID/GID & permissions (Linux)

Avoid root-owned files by matching host UID/GID:

docker run --rm -it \
  -u $(id -u):$(id -g) \
  -v "$PWD":/workspace -w /workspace \
  kfm:dev bash

To bake this into the image, you can pass USER_ID/GROUP_ID as build args and add a user in the Dockerfile. For now, the runtime flag is simplest.

⸻

Caching tips
	•	Build cache: Keep the base image up-to-date with docker pull ghcr.io/osgeo/gdal:ubuntu-small-latest.
	•	Data cache: The data/ directory is mounted from host; repeated runs reuse downloads & COGs.

⸻

Troubleshooting
	•	“gdaldem not found”: Ensure your image built from the GDAL base and you’re using this image: docker run kfm:dev gdaldem --version.
	•	“No validators found”: Add scripts/validate_stac.py or pip install kgt inside the container.
	•	“Permission denied” writing to data/: Use -u $(id -u):$(id -g) on Linux.
	•	“KSRIV_ not set”*: Provide the three environment variables or edit Makefile defaults.

⸻

CI usage (GitHub Actions)

Example step leveraging this image:

- name: Build image
  run: docker build -t kfm:ci .

- name: Validate STAC + write site
  run: |
    docker run --rm \
      -v "$PWD":/workspace -w /workspace \
      kfm:ci bash -lc "make stac && make stac-validate-items && make site"


⸻

Security / provenance
	•	Pin base images for releases (e.g., :3.9.0) and generate SBOMs with Syft if needed.
	•	Keep LICENSE/NOTICE in repo; the image copies none of your data by default.

⸻

See also
	•	Dockerfile (root)
	•	Makefile — targets referenced above
	•	scripts/ — helper CLIs (optional, auto-detected)
