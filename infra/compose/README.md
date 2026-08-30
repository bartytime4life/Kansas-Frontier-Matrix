# Compose review-stack boundary

`infra/compose/` contains the checked-in Docker Compose review-stack placeholder
and the documentation that defines its bounded meaning.

**Status:** `CONFIRMED REPOSITORY INPUT / REVIEW IMAGES ONLY / NO SERVICE START`

This README is the same-path lane contract for Compose material. It is not a
generated document, deployment record, environment inventory, release approval,
or publication authority.

## Current inventory

| Path | Confirmed role |
|---|---|
| [`docker-compose.yml`](docker-compose.yml) | Builds two payload-free review images and assigns loopback-only host ports. |
| [`README.md`](README.md) | Documents this lane's scope, validation, limitations, and rollback. |

No override files, profiles, explicit networks, volumes, secrets, environment
files, health checks, service commands, restart policies, or deployment targets
are tracked in this directory.

## Current services

| Service key | Build input | Published port | Safe conclusion |
|---|---|---|---|
| `governed-api` | `infra/docker/Dockerfile.governed-api` | `127.0.0.1:8080:8080` | Builds a non-root Python review image with no application payload or startup command. |
| `explorer-web` | `infra/docker/Dockerfile.explorer-web` | `127.0.0.1:5173:5173` | Builds a non-root Node review image with no application payload or startup command. |

The service keys resemble application families, but the images do not contain
[`apps/governed-api/`](../../apps/governed-api/) or
[`apps/explorer-web/`](../../apps/explorer-web/) payloads. The port mappings do
not establish listeners, reachable applications, governed behavior, or public
routes.

See the [Docker review-image boundary](../docker/README.md) for the exact image
contents and security controls.

## Authority and placement

Accepted [Directory Rules](../../docs/doctrine/directory-rules.md), adopted by
[ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md),
place deployment, host, network, and exposure configuration under `infra/`.
Compose therefore belongs here when its primary responsibility is service
wiring or deployment posture.

This lane may configure how reviewed applications are packaged or connected. It
does not own:

- application behavior or API contracts;
- source admission, evidence, policy, or lifecycle state;
- rights, sensitivity, privacy, or sovereignty decisions;
- proof, receipt, release, correction, or publication decisions;
- secrets, credentials, private keys, production certificates, or real `.env`
  files;
- generated test results or deployed-environment observations.

The [parent infrastructure boundary](../README.md) remains authoritative for
the root posture. Public clients must use governed interfaces or released
public-safe artifacts; Compose must not create a path to RAW, WORK,
QUARANTINE, canonical internal stores, review surfaces, or direct model
runtimes.

## Focused validation

Run commands from the repository root.

### Static repository boundary

```bash
python -m unittest discover \
  --start-directory tests/infra \
  --pattern 'test_compose_static.py' \
  --verbose
```

[`test_compose_static.py`](../../tests/infra/test_compose_static.py) reads only
tracked files. It checks:

- the two build contexts and Dockerfiles resolve;
- each Dockerfile has a base image, work directory, and non-root final user;
- both published ports use the `127.0.0.1` host address; and
- the Compose file omits the selected privileged, host-network, Docker-socket,
  sensitive lifecycle-mount, release-mount, and Compose-secret tokens encoded
  by the test.

This is a bounded lexical/static check. It is not a general Compose policy
engine and does not inspect ignored, generated, external, or deployed state.

### Compose render and build

```bash
docker compose -f infra/compose/docker-compose.yml config --quiet
docker compose -f infra/compose/docker-compose.yml build
```

The tracked
[`infra-compose-smoke` workflow](../../.github/workflows/infra-compose-smoke.yml)
runs the static test, renders the Compose file, and builds both review images on
its supported runner. It does not run `docker compose up`, start containers, or
probe ports.

The build may contact configured image and package registries for pinned inputs;
it is not a no-network procedure. A successful build is runner- and
revision-specific evidence, not a guarantee that future registry bytes,
networks, or toolchains will remain available.

## Result interpretation

| Observation | What it supports | What it does not support |
|---|---|---|
| Static test passes | Checked-in paths, selected deny tokens, loopback port strings, and non-root Dockerfile users match the test. | Complete security, runtime behavior, or deployed enforcement. |
| `docker compose ... config --quiet` passes | The installed Compose implementation accepts the checked-in file. | Image availability, container startup, health, or application behavior. |
| `docker compose ... build` passes | Both review-image definitions build in that runner context. | Application payloads, service commands, listening ports, safe data access, or deployment readiness. |
| Hosted workflow passes | The bounded checks completed for the tested revision. | Human review, release, deployment, promotion, publication, or source activation. |

Do not report the stack as running, deployable, public, production-like, or
application-complete from these results.

## Failure handling

- **Static path or port failure:** inspect the exact Compose and Dockerfile diff;
  do not weaken an assertion merely to make the check green.
- **Render failure:** treat the configuration as unusable with the runner's
  recorded Compose version until the syntax or unsupported field is resolved.
- **Build failure:** distinguish an invalid Dockerfile or dependency-integrity
  failure from transient registry, runner, or network failure. Do not infer an
  application defect because no application payload is present.
- **Unexpected service-start claim:** stop and correct the documentation or
  workflow; the current workflow never starts services.
- **Exposure or sensitive-mount change:** hold reliance until the new route,
  identity, mount, rights/sensitivity consequences, denial evidence, and
  rollback are reviewed.

Failures do not authorize bypassing checks, adding secrets to Git, widening
ports, mounting non-public lifecycle stores, or publishing artifacts.

## Admission requirements

Before this placeholder becomes an operational stack, a reviewed change must
identify and verify at least:

1. intended environment and accountable operational stewardship;
2. real application payloads, commands, entrypoints, and supported versions;
3. service identities and least-privilege filesystem access;
4. explicit network, ingress, egress, port, and public/private route posture;
5. volumes and lifecycle phases, including denial of public access to
   non-public stores;
6. external secret references, custody, rotation, and revocation;
7. health, readiness, logging, redaction, and monitoring behavior;
8. deterministic positive and negative tests, including direct-runtime and
   sensitive-store denial;
9. release identity and the distinction between merge, release, deployment,
   and publication; and
10. an executable containment and rollback procedure tied to the environment.

Until those items are closed, the current file remains a buildable review-image
placeholder, not an adopted runtime topology.

## Maintenance and rollback

Update this README whenever the Compose inventory, service keys, build inputs,
ports, networks, volumes, profiles, secrets, health checks, commands, consumers,
workflow behavior, or maturity changes.

If the documentation gets ahead of implementation, narrow the claim to current
repository evidence or label the gap `UNKNOWN` or `NEEDS VERIFICATION`. Preserve
the distinction between repository configuration and externally managed state.

Before merge, close the unmerged documentation PR. After merge, revert the
scoped Markdown commit. Reverting this README changes no image, container,
route, environment, release, deployment, or publication state.

## Open verification

- Are these review-image builds intended to evolve into an application stack,
  or should a future runtime topology use a different deployment path?
- Which Compose and Docker versions are supported outside the hosted workflow?
- What service-start and health fixture can be added without inventing secrets,
  external dependencies, or deployment claims?
- Which environment, if any, consumes this Compose file?
- Who is accountable for runtime operation, exposure review, and rollback?
