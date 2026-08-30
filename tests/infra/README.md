# Infrastructure static-test boundary

`tests/infra/` contains repository-local, no-network assertions for the bounded
Docker and Compose review inputs under `infra/`. It is a test lane, not an
infrastructure definition, deployment runbook, security policy, or release
authority.

Status: `CONFIRMED STATIC TESTS / NO RUNTIME OR DEPLOYMENT PROOF`.

## Current inventory

| Path | Reads | Bounded assertion |
|---|---|---|
| `test_compose_static.py` | `infra/compose/docker-compose.yml` and its referenced Dockerfiles | The two exact build contexts and Dockerfiles resolve; each Dockerfile declares `FROM`, `WORKDIR`, and a final non-root `USER`; both published ports are loopback-bound; the Compose text omits the enumerated privileged, host-network, Docker-socket, sensitive-data, release, and secret markers |
| `test_docker_security_overrides.py` | Explorer review-image Dockerfile, manifest, and lockfile under `infra/docker/` | The three exact runtime overrides are pinned; the lock binds `tar` `7.5.22` and integrity metadata; its five checked runtime dependencies have `sha512` integrity values; the Dockerfile contains the expected npm checksum, replacement paths, exact dependency versions, and fail-closed extraction-API assertion |
| `README.md` | Repository and workflow evidence | Human-maintained routing, execution, interpretation, and maintenance boundary |

These checks inspect committed text and JSON. They do not invoke Docker, start a
service, open a socket, contact a registry, query a vulnerability database, or
load application data.

## Run locally

Run both modules from the repository root:

```bash
KFM_NO_NETWORK=1 \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONHASHSEED=0 \
python -m unittest discover \
  --start-directory tests/infra \
  --pattern 'test_*.py' \
  --verbose
```

Run only one boundary by replacing the pattern with
`test_compose_static.py` or `test_docker_security_overrides.py`.

`KFM_NO_NETWORK=1` records the intended test posture. These modules do not read
that variable or install a process-wide network guard; their current no-network
property follows from the inspected Python code, which performs only local file
reads and in-process assertions. A future subprocess, socket, HTTP client, or
plugin import requires a separate enforcement decision and test update.

## Hosted workflow binding

| Workflow | Trigger relationship | What it runs | Limit |
|---|---|---|---|
| [`infra-compose-smoke`](../../.github/workflows/infra-compose-smoke.yml) | Changes under `tests/infra/**`, `infra/compose/**`, `infra/docker/**`, or the workflow itself | Explicitly runs `test_compose_static.py`, renders the Compose file, and builds both review images | Does not run `test_docker_security_overrides.py` or start services |
| [`security`](../../.github/workflows/security.yml) | Runs on every pull request and on configured main/scheduled/manual events | Scans the repository and builds and scans both review images with the configured Trivy policy | Does not directly invoke either Python module; scan results are point-in-time signals, not permanent vulnerability absence |

At the pinned repository base for this document, the Makefile's `test` target
runs only `tests/schemas` and `tests/contracts`; it does not aggregate this lane.
The Explorer security-overlay module therefore needs the explicit local command
above unless another caller deliberately adds it to an accepted aggregate or
workflow. Do not report it as hosted test evidence merely because the related
image built or scanned.

## Result interpretation

| Result | Supported conclusion | Required handling |
|---|---|---|
| Compose static module passes | The enumerated file, user, port, and forbidden-token assertions held for the tested commit | Keep the result scoped to those assertions |
| Explorer overlay module passes | The exact manifest, lock, integrity, checksum, replacement, version, and API strings matched the tested commit | Keep the result scoped to repository inputs; run a separate build and scan when those claims matter |
| Static module fails | A checked invariant or expected input changed | Stop, inspect the diff, and reconcile the test and implementation together; do not weaken an assertion solely to restore green status |
| Module was not invoked | No test conclusion exists | Record `NOT_RUN`; do not infer a pass from a different job |
| Workflow, Docker build, or scan fails | The associated hosted or build boundary did not complete successfully | Preserve the failure and classify whether it was introduced, inherited, environmental, pending, or unknown |

A passing static test does not prove that images build, vulnerabilities are
absent, services start, inherited base-image commands are suitable, listeners
exist, applications function, health checks pass, governed data is safe, or any
release, deployment, promotion, or publication is authorized.

## Maintenance contract

Update the affected test and this README together when any of the following
changes materially:

- Compose service names, build contexts, Dockerfile paths, published ports,
  mounts, networks, privileges, secrets, or governed-data references;
- Dockerfile base, working directory, final user, Explorer override archive,
  checksum, replacement target, dependency version, or API assertion;
- Explorer overlay manifest or lockfile shape, version, dependency graph, or
  integrity metadata;
- local command, Make target, workflow path filters, direct test invocation,
  image build, or scan policy;
- test network behavior, dependencies, fixtures, expected failures, or
  diagnostics.

When adding a new invariant, include a negative assertion or fixture when it can
demonstrate that the check fails closed. When removing an invariant, record why
it is obsolete and identify any successor control; absence from this static lane
does not prove another layer enforces it.

## Unresolved boundaries

- `test_docker_security_overrides.py` is not directly invoked by the inspected
  hosted workflows or current Make targets.
- The tests use bounded text and JSON assertions rather than a Compose schema,
  container runtime, SBOM, signature, provenance, or deployed-environment
  inspection.
- No service-start, listener, health, reachability, secrets, filesystem,
  capability, ingress, egress, observability, restore, or operational rollback
  test is established here.
- Required-check status and accountable infrastructure ownership are outside
  this README and remain `UNKNOWN` unless separately evidenced.

## Related boundaries

- [Root test authority and routing](../README.md)
- [Compose review-stack boundary](../../infra/compose/README.md)
- [Docker review-image boundary](../../infra/docker/README.md)
- [Infrastructure boundary](../../infra/README.md)
- [Directory Rules](../../docs/doctrine/directory-rules.md)

This README is hand-maintained documentation. Reverting it changes no test,
workflow, image, runtime, release, deployment, promotion, or publication state.
