# Infrastructure tests

`tests/infra/`

Status: bounded static test lane.

The current test verifies only that the checked-in Compose contexts and Dockerfiles resolve, published ports are loopback-bound, and the placeholder does not add sensitive mounts or privileged escape settings.

A passing test is not proof that images build, services start, applications function, health checks pass, data is safe, or deployment is authorized. Hosted CI separately runs Compose rendering and image builds without starting services.
