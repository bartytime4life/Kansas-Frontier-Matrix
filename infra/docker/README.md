# Docker review-image boundary

`infra/docker/` contains a payload-free Governed API review image. It checks a
pinned base image, hash-locked build tooling, bounded OS package repairs, and a
non-root final user. It does not package or start the API or the Explorer Site.

| Path | Role |
|---|---|
| [`Dockerfile.governed-api`](Dockerfile.governed-api) | Digest-pinned Python 3.14 review image with a non-root final user |
| [`governed-api-requirements.lock`](governed-api-requirements.lock) | Hash-locked build dependencies |
| [`.dockerignore`](.dockerignore) | Allowlist for the Docker build context |

The former Explorer Web placeholder Dockerfile and npm overlay were retired with
the old monorepo app. The historical local Site source mirror is documented in the
[v74-derived mirror record](../../apps/site/README.md).

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

The pip and ensurepip bootstrap installers are removed after the hash-locked build tools are
installed. Pip's bundled libraries have their own versions; upgrading a
top-level package does not replace those copies. Ensurepip carries another pip
wheel, so uninstalling pip alone does not remove the bootstrap surface. The build asserts that both are
absent and that the retained setuptools, wheel and packaging versions match
the lock. This final image has no installation or application entrypoint.
The build still uses pip for the bounded, hash-verified installation; removing
it afterward does not assert that every build-time dependency is remediated.
The unchanged security workflow scans the resulting image for vulnerabilities
and secrets, with fixed HIGH/CRITICAL findings failing the job.

Rollback reverts the image change and rebuilds the prior pinned review image.
It does not alter an API deployment, the Site or its stored data. Retained
historical scanner results must not be represented as a scan of a newer image.
