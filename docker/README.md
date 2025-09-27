# Docker — Kansas Frontier Matrix / Kansas Geo Timeline

Mission-grade, repeatable containers for building terrain COGs, validating STAC, and previewing the web viewer — **without polluting your host**.

> **Base image:** `ghcr.io/osgeo/gdal:ubuntu-small-latest` (configurable via `--build-arg`)

---

## Quickstart

```bash
# Build local image (tag chosen for clarity)
docker build -t kfm:dev .

# Drop into an interactive shell with the repo mounted read-write
docker run --rm -it \
  -v "$PWD":/workspace \
  -w /workspace \
  kfm:dev bash
````

Inside the container:

```bash
# Optional: install dev deps for tests/lint
make install-dev

# Build terrain derivatives (hillshade/slope/aspect)
make terrain

# Create/patch STAC + validate + write simple site manifest
make stac stac-validate site

# Items-only fast validation pass
make stac-validate-items

# Clean generated rasters (keeps ./stac)
make clean
```

---

## Why containers for this project?

* **GDAL stability** — Pin a known-good GDAL across Linux/macOS/WSL.
* **Reproducible builds** — Same Makefile + Python toolchain in CI and local.
* **Zero host deps** — Avoid installing GDAL, PROJ, or Python libs on your workstation.

---

## Host ↔ Container volume layout

The image is stateless. Everything lands in your mounted repo:

```
/workspace
├── data/               # raw/ cogs/ derivatives/ processed/
├── stac/               # items/ collections/
├── scripts/            # helper CLIs (convert, validate, etc.)
├── web/                # viewer config + assets
└── Makefile
```

Run with:

```bash
docker run --rm -it \
  -v "$PWD":/workspace \
  -w /workspace \
  kfm:dev bash
```

**Linux tip:** add `-u $(id -u):$(id -g)` to avoid root-owned files (see “UID/GID & permissions”).

---

## Common run patterns

### 1) Fire-and-forget target

```bash
# Run a single Make target
docker run --rm \
  -v "$PWD":/workspace -w /workspace \
  kfm:dev make terrain
```

Chain targets:

```bash
docker run --rm \
  -v "$PWD":/workspace -w /workspace \
  kfm:dev bash -lc "make stac && make stac-validate && make site"
```

### 2) Override DEM path

```bash
docker run --rm \
  -v "$PWD":/workspace -w /workspace \
  kfm:dev make terrain DEM=data/cogs/dem/ks_1m_dem_2018_2020.tif
```

### 3) Hydrology export (optional)

Provide layer URLs at runtime:

```bash
docker run --rm \
  -v "$PWD":/workspace -w /workspace \
  -e KSRIV_CHANNELS="https://.../FeatureServer/0" \
  -e KSRIV_FLOODPLAIN="https://.../FeatureServer/1" \
  -e KSRIV_GAUGES="https://.../FeatureServer/2" \
  kfm:dev make hydrology-fetch hydrology-stac
```

---

## Image build options

Override the GDAL base:

```bash
docker build \
  --build-arg GDAL_IMAGE=ghcr.io/osgeo/gdal:ubuntu-small-3.9.0 \
  -t kfm:dev .
```

Recommended tagging:

```bash
docker build -t ghcr.io/<you>/kfm:dev -t kfm:dev .
```

---

## Makefile integration (inside the container)

Targets auto-detect:

* **GDAL tools:** `gdaldem`, `gdal_translate`, `gdaladdo`, `ogr2ogr`
* **Python helpers:** `scripts/convert.py`, etc.
* **Validators:** `scripts/validate_stac.py` (if present) or `kgt validate-stac` (if installed)
* **Checksums:** `sha256sum` / `gsha256sum` / `shasum` (auto-detected)

Helpful targets:

* `make env` — prints detected tools + paths
* `make prebuild` — STAC validate + site (CI-friendly)
* `make stac-validate-items` — fast pass over `./stac/items`
* `make clean` — removes generated rasters but keeps `./stac`

---

## GPU & heavy processing

This stack is CPU-oriented. If you add CUDA/GPU workflows later:

* Run with `--gpus all` and use a CUDA-enabled base image.
* Keep Makefile logic; only the image changes.

---

## Docker Compose (optional)

Create `docker/compose.yml`:

```yaml
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
```

Run:

```bash
# Interactive shell
docker compose -f docker/compose.yml run --rm kfm bash

# One-shot target
docker compose -f docker/compose.yml run --rm kfm make terrain
```

---

## UID/GID & permissions (Linux)

Avoid root-owned files by matching host UID/GID:

```bash
docker run --rm -it \
  -u $(id -u):$(id -g) \
  -v "$PWD":/workspace -w /workspace \
  kfm:dev bash
```

You can also bake a user into the image via `--build-arg USER_ID/GROUP_ID`, but the runtime flag is simplest.

---

## Caching tips

* **Build cache:** keep the base image fresh

  ```bash
  docker pull ghcr.io/osgeo/gdal:ubuntu-small-latest
  ```
* **Data cache:** `data/` is host-mounted; repeated runs reuse downloads & COGs.

---

## Troubleshooting

* **“gdaldem not found”** — Ensure you built from the GDAL base and are using the right image:
  `docker run kfm:dev gdaldem --version`
* **“No validators found”** — Add `scripts/validate_stac.py` or `pip install kgt` inside the container.
* **“Permission denied” writing to `data/`** — Use `-u $(id -u):$(id -g)` on Linux.
* **“KSRIV_… not set”** — Provide the three env vars or edit Makefile defaults.

---

## CI usage (GitHub Actions)

Example job step:

```yaml
- name: Build image
  run: docker build -t kfm:ci .

- name: Validate STAC + write site
  run: |
    docker run --rm \
      -v "$PWD":/workspace -w /workspace \
      kfm:ci bash -lc "make stac && make stac-validate-items && make site"
```

---

## Security & provenance

* **Pin base images** for releases (e.g., `:3.9.0`), and generate SBOMs with Syft if needed.
* The image copies none of your data by default; all artifacts remain in the mounted repo.
* Keep `LICENSE`/`NOTICE` in the repo; reference in release notes.

---

## See also

* `Dockerfile` (root)
* `Makefile` — targets referenced above
* `scripts/` — helper CLIs (`convert.py`, validators, etc.)

```
```
