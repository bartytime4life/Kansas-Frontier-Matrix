# Infrastructure tests

`tests/infra/`

Status: bounded static test lane.

The Compose test verifies that the checked-in contexts and Dockerfiles resolve, published ports are loopback-bound, and the placeholder does not add sensitive mounts or privileged escape settings. The Explorer image security-overlay test verifies the exact manifest and lock bindings, the integrity-locked `tar` runtime dependency graph, and the Dockerfile replacement and fail-closed version/API assertions.

A passing static test is not proof that images build, vulnerabilities are absent, services start, applications function, health checks pass, data is safe, or deployment is authorized. Hosted CI separately runs Compose rendering, image builds, and Trivy scans without starting services.
