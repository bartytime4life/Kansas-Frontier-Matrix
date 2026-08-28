# Flora infrastructure

`infra/flora/`

Status: draft / domain-segmented infrastructure lane / Flora deployment and exposure posture only.

This directory is for Flora-specific infrastructure documentation and configuration that supports deployment, host, network, exposure, runtime wiring, and operational safety for Flora services or Flora-adjacent runtime components.

These files are infrastructure posture material only. They are not Flora domain source code, lifecycle data, botanical source records, rare-plant records, SourceDescriptors, EvidenceBundles, RunReceipts, proof packs, policy decisions, release manifests, public API authority, public map authority, tile authority, Flora truth, source authority, evidence authority, policy authority, release authority, AI authority, or published artifacts.

## Flora infrastructure posture

Use this lane only when the primary responsibility is infrastructure for Flora-related services: deployment wiring, host/network posture, firewall references, Compose/Docker references, service exposure notes, runtime environment assumptions, or operational guardrails.

Flora remains a sensitive domain. Infrastructure must not expose rare-plant locations, raw observations, raw source exports, internal stores, unpublished candidates, direct model runtimes, or unreviewed joins as normal public paths. Public clients should use governed interfaces and released, policy-safe outputs.

The parent `infra/` root is for deployment, host, network, and exposure posture. Its current README states deny-by-default, least privilege, no direct model exposure, and no raw data exposure. Flora infrastructure files in this lane must follow that posture.

## Placement basis

This lane belongs under `infra/` only when the file's primary responsibility is deployment, host, network, or exposure posture for Flora services. It does not own Flora domain meaning, machine shape, policy, lifecycle data, source registry records, source admission, package code, pipeline logic, fixtures, proofs, receipts, or release decisions.

Directory Rules says file location encodes ownership, governance, and lifecycle. It assigns deployment, host, network, and exposure posture to `infra/`, and says domain-specific files appear as segments inside responsibility roots. This README therefore treats `infra/flora/` as an infrastructure lane with a Flora domain segment, not as Flora domain authority.

## Relationship to Flora responsibility roots

| Root or lane | Relationship |
|---|---|
| `../README.md` | Parent infrastructure boundary: deployment, host, network, exposure posture. |
| `../compose/README.md` | Compose orchestration lane; Flora infrastructure may reference Compose files but should not duplicate orchestration rules. |
| `../docker/README.md` | Docker build lane; Flora infrastructure may reference image build posture but should not own Dockerfile contracts. |
| `../firewall/README.md` | Firewall exposure-control lane; Flora infrastructure may reference firewall posture for Flora services. |
| `../../docs/domains/flora/` | Flora domain documentation and placement plans. |
| `../../contracts/domains/flora/` | Flora semantic contracts if present; infrastructure does not define object meaning. |
| `../../schemas/contracts/v1/domains/flora/` | Flora machine schemas if present; infrastructure does not define schema shape. |
| `../../policy/domains/flora/` | Flora policy authority if present; infrastructure does not decide admissibility. |
| `../../packages/domains/flora/` | Flora implementation packages; infrastructure may deploy/package services but does not own package code. |
| `../../pipelines/domains/flora/` | Flora executable pipeline logic if present; infrastructure does not own pipeline behavior. |
| `../../data/` | Governed lifecycle data; Flora infrastructure must not bypass RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED. |
| `../../data/registry/sources/flora/` | Flora source registry if present; infrastructure does not admit sources. |
| `../../release/` | Release authority; infrastructure does not promote, publish, correct, or roll back releases. |
| `../../tests/` | Tests and validation harnesses; infrastructure checks can support tests but are not test results. |
| `../../artifacts/` | Generated outputs; infrastructure files should not treat generated outputs as authority. |

## Accepted material

This lane may contain:

- Flora-specific deployment notes and bounded local/runtime operation notes;
- Flora service exposure tables that identify public-facing, internal-only, and denied surfaces;
- Flora runtime dependency notes that reference Compose, Docker, firewall, apps, packages, configs, or runtime lanes without replacing them;
- non-secret environment variable templates or references when they are Flora-specific and placeholder-only;
- data-mount posture notes that explicitly prevent raw, sensitive, unpublished, proof, receipt, or release material from being exposed;
- operational checklists for confirming that Flora services remain governed, deny-by-default, and public-safe.

## Exclusions

Do not use this lane for Flora source records, rare-plant location records, observation exports, sensitive exact geometry, lifecycle data, SourceDescriptors, EvidenceBundles, RunReceipts, proof packs, release manifests, policy decisions, implementation source code, schemas, semantic contracts, generated CI outputs, public API material, public map material, public tiles, direct model runtime output, direct raw-data exposure, direct canonical-store exposure, source authority, evidence authority, policy authority, release authority, AI authority, or published artifacts.

## Flora infrastructure safety rules

- Default to deny-by-default and least privilege.
- Keep raw Flora data, sensitive locations, unpublished candidates, and direct source exports out of public and local-convenience exposure paths.
- Keep internal stores and direct model runtimes behind governed services.
- Public Flora surfaces should expose only released, policy-safe, generalized, or bounded outputs.
- Document every exposed port, service, profile, host binding, volume, and intended consumer.
- Do not mount RAW, WORK, QUARANTINE, proof, receipt, release, source-registry, or secret material into Flora containers unless a reviewed operational need exists.
- Keep local-only convenience exposure visibly separate from production-like exposure.
- Do not treat a successful deployment, health check, Compose run, image build, open port, or firewall pass as validation of Flora truth, evidence, policy, release, publication, or governance behavior.

## Expected Flora infrastructure file families

| File family | Expected posture | Notes |
|---|---|---|
| Flora local runtime note | Developer-only or localhost/private-network posture | No raw data or sensitive location exposure. |
| Flora governed API exposure note | Public route terminates at governed interface | Does not bypass policy, evidence, or release controls. |
| Flora internal service note | Internal-only by default | May reference stores, workers, queues, or caches without exposing them. |
| Flora data-mount note | Explicit deny-by-default data posture | Must not mount sensitive lifecycle material by default. |
| Flora demo posture note | Public-safe demo only | Use synthetic or generalized public-safe data and document limits. |
| Flora CI/runtime support note | Reproducible check harness | Does not replace tests, scans, receipts, or release gates. |

## Maintenance notes

- Update this README when Flora infrastructure files, service profiles, exposed ports, networks, volume mounts, Compose references, Docker references, firewall references, deployment targets, or validation commands are added.
- Every checked-in Flora infrastructure file should document intended environment, public/internal status, data exposure posture, model exposure posture, service owner, and validation command.
- If a Flora infrastructure file changes public exposure, raw-data access, secret handling, model access, release behavior, or public-client routing, require maintainer review and steward review before relying on it.
- If a file belongs to Flora domain docs, policy, schemas, contracts, data, source registry, packages, pipelines, tests, fixtures, or release lanes, move it to that responsibility root instead of keeping it here.
- If infrastructure accidentally exposes raw Flora data, sensitive locations, secrets, direct model runtime, canonical stores, proof/receipt material, release material, or internal-only service ports, revert or disable the exposure and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Flora infrastructure payload inventory: no infrastructure payload files verified under `infra/flora/` during this update.
- Exact child-lane inventory under `infra/flora/`: NOT VERIFIED during this update.
- Parent infrastructure alignment: PARTIALLY VERIFIED against `infra/README.md`.
- Directory Rules alignment: PARTIALLY VERIFIED against `docs/doctrine/directory-rules.md`.
- Flora domain placement alignment: PARTIALLY VERIFIED against `docs/domains/flora/FILE_SYSTEM_PLAN.md`.
- Runtime/service alignment: NEEDS VERIFICATION against actual Flora services, app routes, runtime adapters, configs, Compose files, Dockerfiles, firewall rules, data mounts, secret handling, validators, tests, CI, deployment targets, ingress routes, egress rules, port bindings, and network zones.
- Tests and validators: NOT RUN.
