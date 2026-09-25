# Docker review-image boundary

`infra/docker/` contains a payload-free Governed API review image. It checks a
pinned base image, hash-locked build tooling, bounded OS package repairs, and a
non-root final user. It does not package or start the API or the Explorer Site.

| Path | Role |
|---|---|
| [`Dockerfile.governed-api`](Dockerfile.governed-api) | Digest-pinned Python 3.11 review image with a non-root final user |
| [`governed-api-requirements.lock`](governed-api-requirements.lock) | Hash-locked build dependencies |
| [`.dockerignore`](.dockerignore) | Allowlist for the Docker build context |

The former Explorer Web placeholder Dockerfile and npm overlay were retired with
the old monorepo app. The current Site source is maintained on the separate
[Site v71 branch](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/codex/live-site-v71-source-20260925).

## Validation

From the repository root:

```bash
python -m unittest discover --start-directory tests/infra --pattern 'test_*.py' --verbose
docker build --file infra/docker/Dockerfile.governed-api --tag kfm/governed-api:security-scan infra/docker
```

The [`infra-compose-smoke`](../../.github/workflows/infra-compose-smoke.yml)
workflow tests the static Compose boundary and builds the placeholder image.
The [`security`](../../.github/workflows/security.yml) workflow scans that image.
Those checks provide bounded input and image evidence; they do not establish a
running service, deployment, release, or publication.
