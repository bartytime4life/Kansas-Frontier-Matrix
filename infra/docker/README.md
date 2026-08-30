# Docker review-image boundary

`infra/docker/` owns the repository inputs used to assemble KFM container review
images. The two current Dockerfiles are payload-free security placeholders: they
exercise base-image, dependency, and non-root-user controls, but they do not
package an application or define a runnable service.

This lane is infrastructure configuration. It is not source, evidence, policy,
release, publication, or deployment authority. A successful build or scan is
point-in-time review evidence for particular bytes; it does not approve an image
for release, prove runtime behavior, or make an image public-safe.

## Current inventory

| Path | Repository evidence | Boundary |
|---|---|---|
| `Dockerfile.explorer-web` | Digest-pinned Node 22 / Debian 13 review image | Contains dependency repairs and ends as `USER node`; no Explorer application payload |
| `Dockerfile.governed-api` | Digest-pinned Python 3.11 / Debian 13 review image | Installs hash-locked build tooling and ends as `USER 10001:10001`; no API application payload |
| `explorer-web/package.json` | Exact security-overlay versions | Declares `brace-expansion` `5.0.9`, `ip-address` `10.3.1`, and `tar` `7.5.22` only |
| `explorer-web/package-lock.json` | npm lockfile for the Explorer overlay | Supplies integrity-locked transitive inputs used during the image build |
| `governed-api-requirements.lock` | Hash-locked Python requirements | Pins `packaging` `26.3`, `wheel` `0.46.3`, and `setuptools` `82.0.1` |
| `README.md` | Human-maintained lane contract | Describes current repository evidence and its limits |

No `.dockerignore` is present in this directory. Neither Dockerfile currently
declares an application copy step, `CMD`, `ENTRYPOINT`, `EXPOSE`, or
`HEALTHCHECK`. Those absences are evidence that these are review images, not
complete service or deployment definitions.

## Image assembly controls

| Control | Explorer review image | Governed API review image |
|---|---|---|
| Base identity | `node:22.23.2-trixie-slim` with a committed digest | `python:3.11.15-slim-trixie` with a committed digest |
| OS package repair | Refreshes the installed `util-linux` and OpenSSL package families | Same bounded package-family refresh |
| Version floors | Asserts `libblkid1 >= 2.41.5-0+deb13u1` and `libssl3t64 >= 3.5.7-1~deb13u2` | Same assertions |
| Dependency integrity | Checksum-bound npm `11.19.0` archive plus the committed npm lock | `pip --require-hashes` against the committed requirements lock |
| Build-time assertions | Verifies exact `tar` runtime dependencies and a loadable extraction API | Fails if the hash-locked Python requirements cannot install |
| Final identity | `node` | UID/GID `10001:10001` |
| Application content | None | None |

The package refreshes and dependency overlays are repository implementation,
not a general instruction to mutate arbitrary images. Keep the base digest,
package scope, fixed-version floors, integrity inputs, cleanup, and final user
reviewable together when changing either Dockerfile.

## Validation contract

### Static checks

Run the focused repository tests from the repository root:

```bash
python -m unittest discover \
  --start-directory tests/infra \
  --pattern 'test_docker_security_overrides.py' \
  --verbose

python -m unittest discover \
  --start-directory tests/infra \
  --pattern 'test_compose_static.py' \
  --verbose
```

[`test_docker_security_overrides.py`](../../tests/infra/test_docker_security_overrides.py)
checks the exact Explorer overlay manifest and lock, integrity metadata, the
checksum-bound npm archive, replacement targets, runtime dependency versions,
and the extraction API assertion.

[`test_compose_static.py`](../../tests/infra/test_compose_static.py) checks that
the Compose build contexts and Dockerfiles resolve, published ports are bound to
loopback, enumerated privileged or sensitive-mount markers are absent, and both
Dockerfiles end with a non-root `USER`.

These are static repository checks. They do not build an image, inspect a
running container, or establish deployed network, filesystem, secret,
capability, or process controls.

### Image build and scan

The hosted [`security` workflow](../../.github/workflows/security.yml) builds
both Dockerfiles from the `infra/docker` context. Its container matrix runs
Trivy `0.73.0` for OS and library vulnerabilities and secrets, filters to
`HIGH,CRITICAL`, uses `ignore-unfixed: true`, and exits with code `1` when a
configured finding remains. The repository job separately scans tracked files
for vulnerabilities, misconfigurations, and secrets under its configured
policy.

The latest successful image-scan evidence inspected for the current Docker bytes is
[security run `33270285794`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/33270285794)
at commit `977cd78c127e297317ca0806b2e95b69458b256e`, completed on
2026-08-29. The Explorer and governed API image jobs succeeded, and their Trivy
reports listed zero findings at the workflow's configured threshold. Later
commits through the current base changed other repository files but not the
Dockerfiles or their lane-specific dependency inputs.

That result is bounded to the referenced commit, image inputs, scanner version,
vulnerability database, severity filter, and `ignore-unfixed` setting. It does
not claim permanent vulnerability absence. The current documentation-only base
commit does not change the Docker inputs, but any later Docker, lockfile,
workflow, scanner, or vulnerability-database change requires fresh evidence.

### Build commands

The workflow's image builds can be reproduced locally when Docker and network
access to the pinned inputs are available:

```bash
docker build \
  --file infra/docker/Dockerfile.explorer-web \
  --tag kfm/explorer-web:security-scan \
  infra/docker

docker build \
  --file infra/docker/Dockerfile.governed-api \
  --tag kfm/governed-api:security-scan \
  infra/docker
```

These tags are local review identifiers. They are not registry coordinates,
release names, publication state, or deployment authorization.

## Failure interpretation

| Signal | What it establishes | Required response |
|---|---|---|
| Static test failure | A checked repository invariant no longer holds | Stop and reconcile the Dockerfile, lock, manifest, or Compose reference; do not waive the assertion for a green result |
| Image build failure | The declared image cannot be assembled under the observed build conditions | Preserve logs, classify dependency or environment causes, and leave the image unverified |
| Configured scan finding | The scanner found an in-scope issue in the built bytes | Keep the lane failed until a bounded repair is reviewed and a fresh scan succeeds |
| Scan unavailable or incomplete | No current scan conclusion exists | Record `NOT_RUN`, `UNKNOWN`, or `NEEDS VERIFICATION`; do not infer a pass from static tests |
| Successful build and scan | The referenced bytes passed the configured checks at that time | Retain the evidence link and continue separate runtime, release, and deployment review |

Do not lower severity thresholds, add suppressions, broaden
`ignore-unfixed`, or change exit behavior merely to restore a passing check.
Any exception requires its own reviewed policy basis; this README cannot create
one.

## Trust and exposure rules

- Do not copy secrets, credentials, private keys, real environment files, raw or
  restricted data, proof material, receipts, release material, or local caches
  into an image.
- Public clients must use governed interfaces or released public-safe artifacts;
  an image must not expose canonical stores, RAW/WORK/QUARANTINE data, or direct
  model runtimes.
- A Docker tag identifies build output. It does not imply review, release,
  deployment, promotion, publication, or rollback authority.
- Rights, sensitivity, privacy, sovereignty, harmful precision, provenance,
  correction, and rollback remain separate controls when an eventual service
  packages or serves governed material.
- If sensitive or authority-bearing content enters a build context, stop the
  path, preserve evidence, remove the material from the context, and require a
  fresh build and scan before reuse.

## Maintenance triggers

Refresh this document and the focused evidence when any of the following
changes:

- base image name or digest;
- OS package-family scope or fixed-version floor;
- npm archive checksum, overlay manifest, or lockfile;
- Python requirements or hashes;
- build context, copied content, runtime user, port, health check, entrypoint, or
  command;
- scanner version, scan categories, severity threshold, ignore policy, or exit
  behavior;
- image consumer, registry target, signing, provenance, SBOM, release, or
  deployment integration.

## Unresolved before operational use

The repository does not yet establish the following for this lane:

- application payloads, startup commands, health checks, or runtime behavior;
- a `.dockerignore` boundary for the `infra/docker` build context;
- production image identities, registry custody, tagging, retention, signing,
  provenance, or SBOM generation;
- runtime secrets, capabilities, mounts, filesystems, networks, ingress, egress,
  or observability;
- environment-specific deployment, release approval, rollback procedure, or
  accountable operational stewardship.

Until those gaps are resolved with current evidence, treat these files only as
review-image inputs.

## Related boundaries

- [Infrastructure boundary](../README.md)
- [Compose orchestration boundary](../compose/README.md)
- [Security workflow](../../.github/workflows/security.yml)
- [Directory Rules](../../docs/doctrine/directory-rules.md)
- [CODEOWNERS review-routing boundary](../../.github/CODEOWNERS)

CODEOWNERS routes GitHub review requests. It does not prove that review
occurred or grant release, deployment, publication, or operational authority.
