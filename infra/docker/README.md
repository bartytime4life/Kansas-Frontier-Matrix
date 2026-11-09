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

The bounded OS upgrade includes `apt` and `libapt-pkg7.0`, with a build-time
minimum of 3.0.4 for each. Debian's [DSA-6607-1](https://lists.debian.org/debian-security-announce/2026/msg00526.html)
fixes CVE-2026-109518 in that trixie version. Both APT acquisition commands use
`Acquire::Retries=0` while the pinned base still contains the older package:
the [Debian tracker](https://security-tracker.debian.org/tracker/CVE-2026-109518)
identifies nonzero retries as a prerequisite. Signature verification remains
enabled; no unauthenticated-package, insecure-repository or scan exception is
introduced. A transient acquisition failure fails the build instead of retrying.
These package floors are build assertions, not substitutes for the image scan.

The bounded upgrade also includes `zlib1g`, with a build-time minimum of
`1:1.3.dfsg+really1.3.1-1+deb13u1`. Debian's
[DSA-6613-1](https://lists.debian.org/debian-security-announce/2026/msg00532.html)
fixes CVE-2026-76844 and CVE-2026-85091 in that trixie security update. The floor
uses Debian package ordering, including its epoch and security revision; the
upstream zlib version string alone does not identify a backported fix. A stale
package or unavailable security update fails the build. The Python base digest,
APT signature checks, bootstrap retry restriction, and scan thresholds remain
unchanged.

Trivy's displayed title is not package-attribution evidence by itself. For the
2026-11-09 findings, its JSON identifies the Debian `zlib1g` package and Debian
Security Tracker source; CVE-2026-76844 has an unrelated webpack title but a zlib
description. Debian lists both CVEs against the old trixie source package and
backports the same upstream fix. CVE-2026-85091's published upstream range starts
at 1.3.1.2, so that narrower non-blocking trigger must not be asserted for 1.3.1
without qualification. These package findings do not establish an attacker path,
application exposure, or exploitation of this payload-free review image.

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
