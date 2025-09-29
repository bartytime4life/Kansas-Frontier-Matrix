# 1) Build (with wheels-first Python, GDAL preinstalled)
docker build -t kfm:dev -f docker/Dockerfile .

# 2) Open a shell with the repo mounted
docker run --rm -it -u $(id -u):$(id -g) -v "$PWD":/workspace -w /workspace kfm:dev bash

# 3) Do work inside the container
make terrain                # build hillshade/slope/aspect etc.
make stac stac-validate     # create & validate STAC
make site                   # build viewer/site artifacts

Prefer the helper script:

# Build with local buildx cache and open a shell
./docker/build-and-run.sh

# Run Make targets
./docker/build-and-run.sh make terrain
./docker/build-and-run.sh make stac stac-validate-items site

# Use Compose service (with optional db/storage/web profiles)
./docker/build-and-run.sh --compose shell
./docker/build-and-run.sh --compose make prebuild


⸻

What’s in the image
	•	GDAL/PROJ + common CLI tools (gdal_translate, gdaldem, ogr2ogr).
	•	Python (wheels-first) with your project installed in editable mode.
	•	Optional:
	•	Node.js + corepack for web viewer builds (ENABLE_NODE=1).
	•	tippecanoe + pmtiles CLIs for vector tiling & serving (ENABLE_TILES=1).
	•	AWS CLI for S3/MinIO sync and STAC pushes (ENABLE_AWSCLI=1).
	•	git-lfs for large rasters.
	•	Non-root default user; /workspace prepared for bind mount.
	•	Healthcheck validates GDAL + core geo libs (and pmtiles if enabled).

Build-time flags (override with --build-arg)

ARG	Default	Purpose
GDAL_IMAGE	ghcr.io/osgeo/gdal:ubuntu-small-latest	Base image / GDAL pin
BUILD_NATIVE	0	Allow source builds if wheels are missing
ENABLE_NODE	1	Install Node.js for web build
ENABLE_TILES	1	Install tippecanoe + pmtiles CLIs
ENABLE_AWSCLI	1	Install AWS CLI
USER_ID/GROUP_ID	10001	Image user mapping
VCS_REF/BUILD_DATE	injected by CI or helper script	Provenance labels

Example:

docker build \
  -t kfm:dev \
  -f docker/Dockerfile \
  --build-arg ENABLE_TILES=1 \
  --build-arg ENABLE_NODE=1 \
  --build-arg GDAL_IMAGE=ghcr.io/osgeo/gdal:ubuntu-small-3.9.0 \
  .


⸻

Compose stack (optional but recommended)

docker/compose.yml defines a profile-driven stack:
	•	kfm (dev toolbox)
	•	db profile: PostGIS + pgAdmin
	•	storage profile: MinIO + bootstrap (buckets for cogs/ and tiles/)
	•	web profile: Caddy (serves _site/) + pmtiles server

Examples:

# Shell in dev container (lean)
docker compose -f docker/compose.yml run --rm kfm bash

# Bring up PostGIS & pgAdmin too
docker compose -f docker/compose.yml --profile db up -d

# Bring up MinIO (S3-compatible) + pmtiles + Caddy
docker compose -f docker/compose.yml --profile storage --profile web up -d

Ports (defaults):
Postgres 5432, pgAdmin 8081, MinIO 9000/9001, Caddy 8080, PMTiles 8082.

⸻

Host ↔ Container layout

All artifacts stay on the host via bind mount:

/workspace
├── data/               # raw/, cogs/, processed/, derivatives/, tiles/
├── stac/               # items/, collections/
├── scripts/            # CLI helpers (convert, validate, etc.)
├── web/                # viewer config + assets
├── _site/              # built site (served by Caddy in 'web' profile)
└── Makefile

Run pattern:

docker run --rm -it \
  -u $(id -u):$(id -g) \
  -v "$PWD":/workspace -w /workspace \
  kfm:dev bash


⸻

Environment variables (pass-through)

These are respected by build-and-run.sh and compose.yml:

Variable	What it’s used for
KFM_ENV	environment tag (dev, ci, …)
KFM_DATA_ROOT	path to data/ (default /workspace/data)
KFM_STAC_ROOT	path to stac/ (default /workspace/stac)
KSRIV_CHANNELS	hydrology channels service/URL
KSRIV_FLOODPLAIN	floodplain service/URL
KSRIV_GAUGES	gauges service/URL
PGHOST/PGPORT/PGDATABASE/PGUSER/PGPASSWORD	PostGIS connectivity
S3_ENDPOINT_URL/AWS_*	MinIO/S3 connectivity

Example .env (optional)

KFM_ENV=dev
KFM_DATA_ROOT=/workspace/data
KFM_STAC_ROOT=/workspace/stac

# Hydrology (optional)
KSRIV_CHANNELS=
KSRIV_FLOODPLAIN=
KSRIV_GAUGES=

# Postgres (compose db profile)
PGHOST=db
PGPORT=5432
PGDATABASE=kfm
PGUSER=kfm
PGPASSWORD=kfm

# MinIO (compose storage profile)
S3_ENDPOINT_URL=http://minio:9000
AWS_ACCESS_KEY_ID=kfm
AWS_SECRET_ACCESS_KEY=kfm-secret
AWS_DEFAULT_REGION=us-east-1


⸻

Common workflows

Make targets (inside container)

make env                      # print detected tools & paths
make terrain                  # hillshade/slope/aspect/tri/tpi (as configured)
make stac stac-validate       # generate STAC & validate collections/items
make stac-validate-items      # fast pass over ./stac/items
make site                     # generate site manifest/config
make clean                    # remove generated rasters (keeps ./stac)

Vector tiling (if ENABLE_TILES=1)

# Tippecanoe → PMTiles
tippecanoe -o data/tiles/ks_roads.pmtiles -zg -pf -pk -ps -ai data/processed/roads.geojson
# Serve locally (compose 'web' profile also provides a pmtiles server)
pmtiles serve data/tiles

Hydrology fetch (with env URLs)

docker run --rm \
  -v "$PWD":/workspace -w /workspace \
  -e KSRIV_CHANNELS="https://…/FeatureServer/0" \
  -e KSRIV_FLOODPLAIN="https://…/FeatureServer/1" \
  -e KSRIV_GAUGES="https://…/FeatureServer/2" \
  kfm:dev make hydrology-fetch hydrology-stac


⸻

Performance & caching
	•	Buildx cache: ./docker/build-and-run.sh uses ./.cache/buildx for fast incremental builds.
	•	pip/npm caches: created under ./.cache/{pip,npm} and mounted in the container.
	•	Data reuse: data/ is host-mounted, so downloads/COGs/tiles persist.

Keep the base fresh:

docker pull ghcr.io/osgeo/gdal:ubuntu-small-latest


⸻

UID/GID & permissions (Linux)

Prevent root-owned files:

docker run --rm -it \
  -u $(id -u):$(id -g) \
  -v "$PWD":/workspace -w /workspace \
  kfm:dev bash

The image also supports --build-arg USER_ID/GROUP_ID to bake a matching user.

⸻

GPU / heavy runs (optional)

This stack is CPU-first. If you later add CUDA workflows:

# Requires NVIDIA runtime & CUDA-enabled base
docker run --rm --gpus all -v "$PWD":/workspace -w /workspace your-cuda-image make <target>

The helper supports --gpu to request GPUs when present.

⸻

CI usage (GitHub Actions)

- name: Build image (w/ provenance labels)
  run: |
    docker build \
      -t kfm:ci \
      -f docker/Dockerfile \
      --build-arg VCS_REF=${{ github.sha }} \
      --build-arg BUILD_DATE=$(date -u +%Y-%m-%dT%H:%M:%SZ) \
      .

- name: Validate STAC + build site
  run: |
    docker run --rm \
      -v "$PWD":/workspace -w /workspace \
      kfm:ci bash -lc "make stac && make stac-validate-items && make site"

To exercise the full stack in CI, use compose with selected profiles (db/storage/web) as needed.

⸻

Troubleshooting
	•	gdaldem: command not found
Confirm you built with the provided Dockerfile:
docker run --rm kfm:dev gdaldem --version
	•	Wheels missing / source build required
Rebuild with --build-arg BUILD_NATIVE=1 or add missing wheels to constraints.txt.
	•	Permission denied writing to data/
Run with -u $(id -u):$(id -g) or set USER_ID/GROUP_ID at build time.
	•	MinIO/pmtiles not reachable
Ensure compose profiles storage and/or web are up:
docker compose -f docker/compose.yml --profile storage --profile web up -d
	•	PostGIS not ready
Compose db profile includes healthchecks; wait for healthy status:
docker compose ps

⸻

Security & provenance
	•	Pin base images for releases (e.g., :ubuntu-small-3.9.0) and record VCS_REF, BUILD_DATE.
	•	Generate SBOMs (e.g., Syft) in release workflows if required.
	•	Image does not copy your data; all artifacts stay in the mounted repo.

⸻

See also
	•	docker/Dockerfile — feature-flagged GDAL + Python + tiling toolchain
	•	docker/compose.yml — dev stack with PostGIS, MinIO, Caddy, pmtiles
	•	docker/build-and-run.sh — buildx-cached helper with Compose & GPU options
	•	Makefile — canonical targets used in docs above
