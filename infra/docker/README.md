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
- Preserve digest-pinned base-image identity, checksum- or hash-locked dependency inputs, and explicit build context.
- When a pinned base contains a fixed vulnerability with an available distribution package, use the smallest reviewed package-family refresh, assert the required fixed-version floor, and remove package-manager metadata afterward.
- Do not weaken severity thresholds, ignore findings, add an exemption, or suppress scanner failure merely to restore a green workflow.
- Document exposed ports, intended runtime user, expected entrypoint, and whether the image is internal-only or public-facing.
- Keep internal stores, raw data paths, and direct model runtimes behind governed services.
- Treat image tags as build identifiers, not release approval or publication state.
- Treat every vulnerability scan as point-in-time evidence bound to the image bytes, scanner version, and vulnerability database used for that run.
- Do not treat a successful image build or scan as validation of KFM truth, evidence, policy, release, publication, or governance behavior.

## Confirmed review-image security posture

The two checked-in Dockerfiles are payload-free security-review placeholders. They are built and scanned by [`security.yml`](../../.github/workflows/security.yml) from the `infra/docker` context with Trivy configured for OS and library vulnerabilities at `HIGH,CRITICAL`, `ignore-unfixed: true`, and fail-closed exit code `1`.

Both digest-pinned Debian 13 base images previously carried `CVE-2026-53615` in the installed `util-linux` package family at version `2.41-5`. The bounded repair in PR #2986 preserved both base-image digests and all application dependency locks, upgraded only the nine already-installed affected packages, asserted `libblkid1 >= 2.41.5-0+deb13u1`, and removed apt metadata. It did not change the scanner policy, build context, runtime users, dependency manifests, or repository settings.

The exact-head security run for PR #3419 later found `CVE-2026-73566` in npm's bundled `tar@7.5.19` inside the Explorer review image. The bounded successor overlay keeps checksum-bound npm `11.19.0`, adds `tar@7.5.22` and its dependency graph to the committed integrity lock, replaces only npm's bundled `tar` directory, and asserts the exact resolved runtime dependency versions plus the loadable extraction API during image construction. It does not weaken scanner policy, suppress the finding, change the base-image digest, add an application payload, or change runtime exposure.

This confirms a repository-owned final-image assembly correction for the affected OS package layer. It does not establish that future base images or vulnerability databases will remain finding-free, that these placeholders are production images, or that any image is released, deployed, published, or approved for public use.

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

- Update this README when Dockerfiles, build templates, `.dockerignore` files, base images, build args, exposed ports, health checks, entrypoints, runtime users, package refreshes, scan requirements, SBOM steps, or image consumers are added.
- Every checked-in Dockerfile should document intended environment, base image posture, build context, exposed ports, runtime user, secret handling, data-copy posture, package refresh rationale, and validation command.
- Keep local-only convenience images visibly separate from production-like images.
- Re-run the focused image scans after base-image, OS-package, lockfile, dependency, build-context, scanner-version, or vulnerability-database changes.
- If a Dockerfile changes exposure, raw-data access, secret handling, model access, release behavior, or public-client routing, require maintainer review and steward review before relying on it.
- If a Docker build accidentally includes raw data, secrets, direct model runtime, canonical stores, proof/receipt material, release material, or generated CI output as source content, revert or disable the image path and record the correction path.

## Verification status

- Evidence snapshot: **CONFIRMED** against `main@101f9ca6983ffb8427855db60b9b4b30c82cb164`, the merged PR #2986 repair, and merged PR #3419 exact-head security run `32607461812`.
- Target README: same-path evidence refresh; no placement, authority, runtime, release, deployment, publication, or repository-setting change.
- Docker payload inventory: **CONFIRMED** tracked `Dockerfile.governed-api` and `Dockerfile.explorer-web`; both remain payload-free security-review placeholders. Both preserve their digest-pinned Debian 13 base images, upgrade only the affected installed `util-linux` package family to the fixed Debian security level, assert the `libblkid1` fixed-version floor, remove apt metadata, and end as non-root users.
- Explorer dependency posture: **CONFIRMED review-worktree bytes** keep npm `11.19.0` checksum-bound and install `brace-expansion` `5.0.9`, `ip-address` `10.3.1`, and `tar` `7.5.22` from the committed integrity lock; exact-head image scan remains pending.
- Governed API dependency posture: **CONFIRMED** `packaging` `26.3`, `wheel` `0.46.3`, and `setuptools` `82.0.1` remain installed from the hash-locked requirements file.
- Exact child-lane inventory under `infra/docker/`: **CONFIRMED** `README.md`, both Dockerfiles, `governed-api-requirements.lock`, and the `explorer-web/` npm manifest and lockfile at the inspected revision. No `.dockerignore` was verified in this lane.
- Security workflow: **CONFIRMED FAIL at the inspected predecessor head** because Explorer npm bundled `tar@7.5.19`; repository scan, dependency review, and governed-api image scan passed. The proposed `tar@7.5.22` overlay requires a fresh exact-head image build and Trivy scan before any corrected-green claim.
- Tests and validators: **CONFIRMED** the no-network Compose static suite checks context and Dockerfile resolution, loopback-only published ports, forbidden mount/privilege markers, and a final non-root `USER` in both Dockerfiles. The hosted `security` workflow independently supplies the current image-build and container-scan evidence.
- Parent infrastructure alignment: PARTIALLY VERIFIED against `infra/README.md`.
- Compose sibling alignment: PARTIALLY VERIFIED against `infra/compose/README.md`.
- Directory Rules alignment: PARTIALLY VERIFIED against `docs/doctrine/directory-rules.md`.
- Runtime/service alignment: NEEDS VERIFICATION against application startup, runtime adapters, configs, secret handling, SBOM generation, deployment targets, image tags, registry targets, release integration, and operational rollback.
- Security non-effects: a passing scan is point-in-time review evidence only; it does not prove permanent vulnerability absence, runtime behavior, release eligibility, deployment approval, publication safety, or public availability.
