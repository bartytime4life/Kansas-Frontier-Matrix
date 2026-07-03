# Compose infrastructure

`infra/compose/`

Status: draft / infrastructure configuration lane / Docker Compose and local stack orchestration.

This directory is for Docker Compose and Compose-adjacent infrastructure files that describe local or deployable service wiring, network posture, volume posture, profile wiring, health checks, and exposure boundaries for KFM services.

These files are operational configuration examples and deployment helpers. They are not application source code, lifecycle data, source records, SourceDescriptors, EvidenceBundles, RunReceipts, proof packs, policy decisions, release manifests, public API authority, public map authority, tile authority, source authority, evidence authority, policy authority, release authority, AI authority, or published artifacts.

## Compose lane posture

Use this lane for Compose files and README documentation that support controlled local/runtime operation. Compose configuration must preserve the KFM trust membrane: public clients should go through governed interfaces, internal stores should not be exposed directly, and raw data or direct model runtime surfaces should not be made available as normal public paths.

The parent `infra/` root is for deployment, host, network, and exposure posture. Its current README states deny-by-default, least privilege, no direct model exposure, and no raw data exposure. Compose files in this lane must follow that posture.

A Compose file can document intended service wiring before every service, health check, secret source, policy bundle, validator, CI job, or deployment target exists. Configuration presence is not proof that the runtime works.

## Placement basis

This lane belongs under `infra/` because Docker Compose primarily describes deployment, host, network, volume, and exposure posture. It does not belong under `apps/`, `packages/`, `data/`, `release/`, `policy/`, `schemas/`, `contracts/`, `fixtures/`, or `artifacts/` unless those roots own the primary responsibility of a different file.

Directory Rules says file location encodes ownership, governance, and lifecycle. It also assigns deployment, host, network, and exposure posture to `infra/`. This README therefore treats `infra/compose/` as an infrastructure lane, not a convenience topic folder.

## Accepted material

This lane may contain:

- `compose.yaml`, `compose.yml`, `docker-compose.yaml`, or `docker-compose.yml` files;
- Compose override files for local, dev, test, demo, or CI-like operation when clearly named;
- service profile notes, port exposure notes, volume notes, network notes, health-check notes, and dependency notes;
- `.env.example` or template references that contain placeholders only;
- documentation for running a bounded local stack;
- documentation for validating that exposed surfaces remain governed and deny-by-default.

## Exclusions

Do not use this lane for secrets, credentials, tokens, private keys, production certificates, real `.env` files, raw data dumps, source exports, lifecycle data, generated CI outputs, release artifacts, proof material, receipt material, implementation code, schema definitions, semantic contracts, policy decisions, direct model runtime exposure, direct canonical-store exposure, direct raw-data exposure, public API bypasses, public tile publication, or published artifacts.

## Compose safety rules

- Default to no public exposure unless a service is intentionally exposed.
- Prefer binding development services to localhost where practical.
- Keep internal stores, raw data paths, and direct model runtimes behind governed services.
- Do not mount RAW, WORK, QUARANTINE, proof, receipt, release, or secret material into containers unless a reviewed operational need exists.
- Use named volumes or clearly documented local volumes; avoid silently binding sensitive host paths.
- Keep secret handling external to checked-in Compose files; checked-in examples should use placeholders only.
- Document exposed ports, intended consumers, and whether the service is internal-only or public-facing.
- Keep local convenience profiles separate from production-like profiles.
- Do not treat a successful `docker compose up` as validation of KFM truth, evidence, policy, release, publication, or governance behavior.

## Expected Compose file families

| File family | Expected posture | Notes |
|---|---|---|
| Local development Compose | Developer-only or localhost-bound | Should not expose raw data or model runtimes directly. |
| Governed API stack Compose | Internal plus governed public interface | Public path should route through governed API behavior. |
| Map/runtime support Compose | Internal service wiring | Tiles, maps, or assets should not become published output by Compose alone. |
| Database/cache/search support Compose | Internal-only by default | Avoid direct public exposure and sensitive host mounts. |
| CI-like Compose | Reproducible check harness | Does not replace tests or validators. |
| Demo Compose | Public-safe demo only | Use synthetic or public-safe data and document limits. |

## Relationship to adjacent roots

| Root or lane | Relationship |
|---|---|
| `../README.md` | Parent infrastructure boundary: deployment, host, network, exposure posture. |
| `../../apps/` | Deployable applications that Compose may run; Compose does not own app code. |
| `../../packages/` | Shared libraries used by applications; Compose does not own package code. |
| `../../configs/` | Non-secret defaults or templates; Compose may reference them but should not replace them. |
| `../../runtime/` | Local runtime adapters or harnesses; Compose may wire them but should not redefine them. |
| `../../data/` | Governed lifecycle data; Compose must not bypass lifecycle boundaries. |
| `../../policy/` | Policy authority; Compose may mount policy bundles only through reviewed paths. |
| `../../release/` | Release authority; Compose does not promote, publish, correct, or roll back releases. |
| `../../tests/` | Tests and validation harnesses; Compose can support tests but is not a test result. |
| `../../artifacts/` | Generated outputs; Compose files should not treat generated outputs as authority. |

## Maintenance notes

- Update this README when Compose files, override files, service profiles, exposed ports, volumes, networks, health checks, or runtime consumers are added.
- Every checked-in Compose file should document intended environment, exposed ports, internal-only services, volume posture, secret handling, data-mount posture, and validation command.
- Keep local-only convenience settings visibly separate from production-like settings.
- If a Compose file changes exposure, raw-data access, secret handling, model access, release behavior, or public-client routing, require maintainer review and steward review before relying on it.
- If a Compose file accidentally exposes raw data, secrets, direct model runtime, canonical stores, proof/receipt material, or release material, revert or disable the exposure and record the correction path.

## Verification status

- Target README: replaced greenfield stub content.
- Compose payload inventory: no Compose YAML files verified under `infra/compose/` during this update.
- Exact child-lane inventory under `infra/compose/`: NOT VERIFIED during this update.
- Parent infrastructure alignment: PARTIALLY VERIFIED against `infra/README.md`.
- Directory Rules alignment: PARTIALLY VERIFIED against `docs/doctrine/directory-rules.md`.
- Runtime/service alignment: NEEDS VERIFICATION against actual Compose files, app services, runtime adapters, configs, secrets handling, validators, tests, CI, deployment targets, network bindings, and volume mounts.
- Tests and validators: NOT RUN.
