# Firewall infrastructure

`infra/firewall/`

Status: draft / infrastructure exposure-control lane / firewall and network access posture.

This directory is for firewall, ingress, egress, and network access-control documentation or configuration that supports KFM deployment and local/runtime exposure posture.

These files are defensive infrastructure configuration and documentation. They are not application source code, lifecycle data, source records, SourceDescriptors, EvidenceBundles, RunReceipts, proof packs, policy decisions, release manifests, public API authority, public map authority, tile authority, source authority, evidence authority, policy authority, release authority, AI authority, or published artifacts.

## Firewall lane posture

Use this lane for defensive network exposure rules and README documentation that support deny-by-default operation. Firewall configuration must preserve the KFM trust membrane: public clients should go through governed interfaces, internal stores should not be exposed directly, and raw data or direct model runtime surfaces should not be reachable as normal public paths.

The parent `infra/` root is for deployment, host, network, and exposure posture. Its current README states deny-by-default, least privilege, no direct model exposure, and no raw data exposure. Firewall files in this lane must follow that posture.

A firewall rule can describe intended exposure control before every service, port, network, health check, policy bundle, validator, CI job, or deployment target exists. Firewall configuration is not proof that the runtime is secure, policy-compliant, released, or publication-ready.

## Placement basis

This lane belongs under `infra/` because firewall rules primarily describe deployment, host, network, and exposure posture. It does not belong under `apps/`, `packages/`, `data/`, `release/`, `policy/`, `schemas/`, `contracts/`, `fixtures/`, or `artifacts/` unless those roots own the primary responsibility of a different file.

Directory Rules says file location encodes ownership, governance, and lifecycle. It also assigns deployment, host, network, and exposure posture to `infra/`. This README therefore treats `infra/firewall/` as an infrastructure lane, not a convenience topic folder.

## Accepted material

This lane may contain:

- firewall rule templates and README documentation for local, development, demo, staging-like, or production-like environments;
- UFW, nftables, iptables, cloud security-group, reverse-proxy allowlist, or equivalent exposure-control notes when clearly scoped;
- ingress and egress posture notes;
- port inventory tables for intended public-facing and internal-only services;
- service-to-port mapping notes that reference `infra/compose/`, `infra/docker/`, `apps/`, `runtime/`, or `configs/` without replacing them;
- validation notes for checking that raw data, internal stores, and direct model runtimes are not exposed.

## Exclusions

Do not use this lane for secrets, credentials, tokens, private keys, production certificates, real `.env` files, raw data dumps, source exports, lifecycle data, generated CI outputs, release artifacts, proof material, receipt material, implementation source code, schema definitions, semantic contracts, policy decisions, direct model runtime exposure, direct canonical-store exposure, direct raw-data exposure, public API bypasses, public tile publication, or published artifacts.

## Firewall safety rules

- Default to deny-by-default and least privilege.
- Document every intentionally exposed port, protocol, service owner, intended consumer, and review status.
- Prefer localhost-only or private-network bindings for development services unless public exposure is explicitly required.
- Keep databases, caches, object stores, raw data paths, proof/receipt stores, release stores, and direct model runtimes internal-only by default.
- Public routes should terminate at governed public interfaces, not internal stores or direct runtime surfaces.
- Keep egress needs explicit where services call external systems.
- Keep local convenience exposure separate from production-like exposure.
- Do not treat an open port, firewall pass, or successful connection as validation of KFM truth, evidence, policy, release, publication, or governance behavior.

## Expected firewall file families

| File family | Expected posture | Notes |
|---|---|---|
| Local development firewall note | Developer-only or localhost/private-network posture | Should not expose raw data or direct model runtimes publicly. |
| Governed API ingress note | Public route terminates at governed interface | Does not bypass policy or evidence controls. |
| Internal service allowlist | Internal-only by default | Use for databases, caches, search, queues, object stores, or workers. |
| Egress posture note | Explicit outbound need | Does not authorize source admission or external data use by itself. |
| Demo exposure note | Public-safe demo only | Use synthetic or public-safe data and document limits. |
| CI or ephemeral environment note | Reproducible check harness | Does not replace tests, scans, receipts, or release gates. |

## Relationship to adjacent roots

| Root or lane | Relationship |
|---|---|
| `../README.md` | Parent infrastructure boundary: deployment, host, network, exposure posture. |
| `../compose/README.md` | Compose orchestration lane; firewall docs may reference ports and networks exposed by Compose. |
| `../docker/README.md` | Docker build lane; firewall docs may reference image-exposed ports but do not own image builds. |
| `../../apps/` | Deployable applications that may expose governed interfaces; firewall does not own app code. |
| `../../configs/` | Non-secret defaults or templates; firewall may reference them but should not replace them. |
| `../../runtime/` | Local runtime adapters or harnesses; firewall may constrain exposure but should not redefine runtime behavior. |
| `../../data/` | Governed lifecycle data; firewall must not bypass lifecycle boundaries. |
| `../../policy/` | Policy authority; firewall does not decide admissibility. |
| `../../release/` | Release authority; firewall does not promote, publish, correct, or roll back releases. |
| `../../tests/` | Tests and validation harnesses; firewall checks can support tests but are not test results. |
| `../../artifacts/` | Generated outputs; firewall files should not treat generated outputs as authority. |

## Maintenance notes

- Update this README when firewall rule templates, allowlists, exposed ports, protocols, service mappings, network zones, ingress routes, egress rules, deployment targets, or validation commands are added.
- Every checked-in firewall or exposure-control file should document intended environment, default action, exposed ports, internal-only ports, service owner, data exposure posture, model exposure posture, and validation command.
- Keep local-only convenience exposure visibly separate from production-like exposure.
- If a firewall file changes public exposure, raw-data access, secret handling, model access, release behavior, or public-client routing, require maintainer review and steward review before relying on it.
- If firewall configuration accidentally exposes raw data, secrets, direct model runtime, canonical stores, proof/receipt material, release material, or internal-only service ports, revert or disable the exposure and record the correction path.

## Verification status

- Target README: replaced greenfield stub content.
- Firewall payload inventory: no firewall rule files verified under `infra/firewall/` during this update.
- Exact child-lane inventory under `infra/firewall/`: NOT VERIFIED during this update.
- Parent infrastructure alignment: PARTIALLY VERIFIED against `infra/README.md`.
- Compose sibling alignment: PARTIALLY VERIFIED against `infra/compose/README.md`.
- Docker sibling alignment: NEEDS VERIFICATION against `infra/docker/README.md` and actual Docker files.
- Directory Rules alignment: PARTIALLY VERIFIED against `docs/doctrine/directory-rules.md`.
- Runtime/service alignment: NEEDS VERIFICATION against actual firewall files, Compose files, Dockerfiles, app services, runtime adapters, configs, secrets handling, validators, tests, CI, deployment targets, ingress routes, egress rules, port bindings, and network zones.
- Tests and validators: NOT RUN.
