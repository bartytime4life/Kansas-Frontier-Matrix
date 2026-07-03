# Docker infrastructure

`infra/docker/`

Status: draft / infrastructure build lane / Docker image and container build posture.

This directory is for Dockerfile and container-image-adjacent infrastructure files that describe how KFM services are packaged for local, CI-like, demo, or deployable container runtime use.

These files are operational build configuration and deployment helpers. They are not application source code, lifecycle data, source records, SourceDescriptors, EvidenceBundles, RunReceipts, proof packs, policy decisions, release manifests, public API authority, public map authority, tile authority, source authority, evidence authority, policy authority, release authority, AI authority, or published artifacts.

## Docker lane posture

Use this lane for Docker build files and README documentation that support controlled image construction. Docker configuration must preserve the KFM trust membrane: public clients should go through governed interfaces, internal stores should not be exposed directly, and raw data or direct model runtime surfaces should not be baked into normal public images.

The parent `infra/` root is for deployment, host, network, and exposure posture. Its current README states deny-by-default, least privilege, no direct model exposure, and no raw data exposure. Docker files in this lane must follow that posture.

A Dockerfile can describe intended packaging before every service, dependency lock, security scan, SBOM, CI job, registry target, runtime profile, or deployment target exists. Image-build configuration is not proof that the runtime works, that a release is approved, or that an image is safe for publication.

## Placement basis

This lane belongs under `infra/` because Docker build files primarily describe deployment packaging, host/runtime posture, image construction, and exposure defaults. It does not belong under `apps/`, `packages/`, `data/`, `release/`, `policy/`, `schemas/`, `contracts/`, `fixtures/`, or `artifacts/` unless those roots own the primary responsibility of a different file.

Directory Rules says file location encodes ownership, governance, and lifecycle. It also assigns deployment, host, network, and exposure posture to `infra/`. This README therefore treats `infra/docker/` as an infrastructure lane, not a convenience topic folder.

## Accepted material

This lane may contain:

- `Dockerfile`, `Dockerfile.*`, or image build templates;
- `.dockerignore` files that prevent accidental inclusion of secrets, raw data, generated outputs, and local caches;
- image build notes for local, dev, test, demo, or CI-like operation;
- non-secret build argument documentation and placeholder examples;
- base-image, runtime-user, exposed-port, health-check, volume, and entrypoint notes;
- SBOM, scan, provenance, and image-tagging documentation when implementation exists;
- documentation for validating that built images preserve governed access and deny-by-default exposure.

## Exclusions

Do not use this lane for secrets, credentials, tokens, private keys, production certificates, real `.env` files, raw data dumps, source exports, lifecycle data, generated CI outputs, release artifacts, proof material, receipt material, implementation source code, schema definitions, semantic contracts, policy decisions, direct model runtime exposure, direct canonical-store exposure, direct raw-data exposure, public API bypasses, public tile publication, or published artifacts.

## Docker safety rules

- Do not bake secrets, tokens, credentials, private keys, local `.env` files, raw data, proof material, receipt material, or release artifacts into images.
- Use `.dockerignore` to exclude local caches, raw data, generated outputs, credentials, and other non-image material.
- Prefer non-root runtime users where practical.
- Keep build-time dependencies separate from runtime image contents when practical.
- Document exposed ports, intended runtime user, expected entrypoint, and whether the image is internal-only or public-facing.
- Keep internal stores, raw data paths, and direct model runtimes behind governed services.
- Treat image tags as build identifiers, not release approval or publication state.
- Do not treat a successful image build as validation of KFM truth, evidence, policy, release, publication, or governance behavior.

## Expected Docker file families

| File family | Expected posture | Notes |
|---|---|---|
| Local development image | Developer-only or local stack support | Should not include secrets, raw data, or release material. |
| Governed API image | Packaged service behind governed interface | Public path should route through governed API behavior. |
| Map/runtime support image | Internal service support | Tiles, maps, or assets do not become published output by image build alone. |
| Worker or validator image | Reproducible check/runtime helper | Does not replace test results, policy decisions, or receipts. |
| Demo image | Public-safe demo only | Use synthetic or public-safe data and document limits. |
| CI build image | Reproducible CI helper | Does not replace CI evidence, scans, or release gates. |

## Relationship to adjacent roots

| Root or lane | Relationship |
|---|---|
| `../README.md` | Parent infrastructure boundary: deployment, host, network, exposure posture. |
| `../compose/README.md` | Compose orchestration lane; Compose may run Docker-built images but does not own image build contracts. |
| `../../apps/` | Deployable applications that Docker images may package; Docker does not own app code. |
| `../../packages/` | Shared libraries included by applications; Docker does not own package code. |
| `../../configs/` | Non-secret defaults or templates; Docker may reference them but should not replace them. |
| `../../runtime/` | Local runtime adapters or harnesses; Docker may package them but should not redefine them. |
| `../../data/` | Governed lifecycle data; Docker must not bake lifecycle data into images. |
| `../../policy/` | Policy authority; Docker may package policy bundles only through reviewed paths. |
| `../../release/` | Release authority; Docker image builds do not promote, publish, correct, or roll back releases. |
| `../../tests/` | Tests and validation harnesses; Docker can support tests but is not a test result. |
| `../../artifacts/` | Generated outputs; Docker build outputs and CI artifacts should not become source authority. |

## Maintenance notes

- Update this README when Dockerfiles, build templates, `.dockerignore` files, base images, build args, exposed ports, health checks, entrypoints, runtime users, scan requirements, SBOM steps, or image consumers are added.
- Every checked-in Dockerfile should document intended environment, base image posture, build context, exposed ports, runtime user, secret handling, data-copy posture, and validation command.
- Keep local-only convenience images visibly separate from production-like images.
- If a Dockerfile changes exposure, raw-data access, secret handling, model access, release behavior, or public-client routing, require maintainer review and steward review before relying on it.
- If a Docker build accidentally includes raw data, secrets, direct model runtime, canonical stores, proof/receipt material, release material, or generated CI output as source content, revert or disable the image path and record the correction path.

## Verification status

- Target README: replaced greenfield stub content.
- Docker payload inventory: no Dockerfile or `.dockerignore` files verified under `infra/docker/` during this update.
- Exact child-lane inventory under `infra/docker/`: NOT VERIFIED during this update.
- Parent infrastructure alignment: PARTIALLY VERIFIED against `infra/README.md`.
- Compose sibling alignment: PARTIALLY VERIFIED against `infra/compose/README.md`.
- Directory Rules alignment: PARTIALLY VERIFIED against `docs/doctrine/directory-rules.md`.
- Runtime/service alignment: NEEDS VERIFICATION against actual Dockerfiles, app services, runtime adapters, configs, secrets handling, scanners, SBOM tooling, validators, tests, CI, deployment targets, image tags, and registry targets.
- Tests and validators: NOT RUN.
