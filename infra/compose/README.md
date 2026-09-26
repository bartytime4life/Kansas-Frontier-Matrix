# Compose review-stack boundary

`infra/compose/docker-compose.yml` builds one payload-free Governed API review
image. Its `127.0.0.1:8080:8080` mapping is loopback-only; the image does not
contain the application or define an application startup command. The retired
Explorer Web placeholder service was removed with the old monorepo app.

| Path | Role |
|---|---|
| [`docker-compose.yml`](docker-compose.yml) | One Governed API review-image build and loopback mapping |
| [`README.md`](README.md) | Current scope and validation boundary |

No tracked Compose override, volume, secret, health check, application command,
or deployment target is defined here. A successful render or build is not a
service startup or reachability test. The current Explorer source and local-host
instructions are in the [Site v74-derived source mirror](../../apps/site/README.md).

## Validation

Run from the repository root:

```bash
python -m unittest discover --start-directory tests/infra --pattern 'test_*.py' --verbose
docker compose -f infra/compose/docker-compose.yml config --quiet
docker compose -f infra/compose/docker-compose.yml build
```

The static test checks the declared Dockerfile, non-root final user, loopback
port, and absence of privileged, host-network, Docker-socket, sensitive-data,
release, or secret markers. The
[`infra-compose-smoke`](../../.github/workflows/infra-compose-smoke.yml)
workflow runs those checks and builds the review image without starting a
service. This lane grants no source, evidence, policy, release, deployment, or
publication authority.
